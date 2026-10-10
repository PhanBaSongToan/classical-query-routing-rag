"""Paired bootstrap and permutation test for two OOF prediction files.

Each CSV must contain the same rows in the same order and columns
``y_true`` and ``y_pred``. This avoids comparing independent CV averages.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import f1_score


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("baseline", type=Path)
    parser.add_argument("extension", type=Path)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--resamples", type=int, default=10000)
    parser.add_argument("--output", type=Path, default=Path("paired_comparison.json"))
    args = parser.parse_args()

    base = pd.read_csv(args.baseline)
    ext = pd.read_csv(args.extension)
    if len(base) != len(ext) or not base["y_true"].equals(ext["y_true"]):
        raise ValueError("Prediction files must contain identical y_true rows in identical order.")

    rng = np.random.default_rng(args.seed)
    truth = base["y_true"].to_numpy()
    bpred = base["y_pred"].to_numpy()
    epred = ext["y_pred"].to_numpy()
    bcorrect = (bpred == truth).astype(float)
    ecorrect = (epred == truth).astype(float)
    difference = ecorrect - bcorrect

    boot_acc = np.empty(args.resamples)
    boot_f1 = np.empty(args.resamples)
    indices = np.arange(len(truth))
    for i in range(args.resamples):
        sample = rng.choice(indices, size=len(indices), replace=True)
        boot_acc[i] = ecorrect[sample].mean() - bcorrect[sample].mean()
        boot_f1[i] = f1_score(truth[sample], epred[sample], average="macro") - f1_score(
            truth[sample], bpred[sample], average="macro"
        )

    observed = float(difference.mean())
    signs = rng.choice(np.array([-1.0, 1.0]), size=(args.resamples, len(difference)))
    null = (signs * difference).mean(axis=1)
    p_value = float((np.abs(null) >= abs(observed)).mean())
    result = {
        "n": len(truth),
        "seed": args.seed,
        "resamples": args.resamples,
        "accuracy_difference_extension_minus_baseline": observed,
        "accuracy_difference_bootstrap_95ci": [float(np.quantile(boot_acc, .025)), float(np.quantile(boot_acc, .975))],
        "macro_f1_difference_bootstrap_95ci": [float(np.quantile(boot_f1, .025)), float(np.quantile(boot_f1, .975))],
        "paired_sign_flip_permutation_p": p_value,
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
