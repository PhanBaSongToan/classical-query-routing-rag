"""Protocol-matched OOF comparison and feature ablation.

Runs the reference TF-IDF/SVM and a small predeclared extension family on the
same shuffled five-fold splits. Outputs aligned OOF files for paired tests.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import clone
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold

from lightweight_router.config import CANONICAL_LABELS
from lightweight_router.data import load_dataset
from lightweight_router.extended_benchmark import ExtendedCandidate, _candidate_builder
from lightweight_router.models import build_pipeline


SEEDS = (0, 1, 2, 3, 4, 13, 21, 42, 77, 100)
CANDIDATES = {
    "word": ExtendedCandidate.create("word_3000", "linear_svc_reference"),
    "character": ExtendedCandidate.create("char_15000", "linear_svc_reference"),
    "word_character": ExtendedCandidate.create("word_char", "linear_svc_reference"),
    "word_character_structural": ExtendedCandidate.create("word_char_structural", "linear_svc_reference"),
    "nbsvm": ExtendedCandidate.create("nbsvm_word_char", "nbsvm_word_char_linear_svc"),
}


def run_model(frame: pd.DataFrame, model_name: str, seed: int, extension: bool) -> pd.DataFrame:
    splitter = StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)
    predictions = np.empty(len(frame), dtype=object)
    registry = CANDIDATES
    for train, valid in splitter.split(frame["query"], frame["label"]):
        if extension:
            estimator = _candidate_builder(CANDIDATES[model_name], registry)
        else:
            estimator = clone(build_pipeline("tfidf_svm"))
        estimator.fit(frame.iloc[train]["query"], frame.iloc[train]["label"])
        predictions[valid] = estimator.predict(frame.iloc[valid]["query"])
    out = frame[["record_number", "id", "domain", "label", "query"]].copy()
    out["y_true"] = out["label"]
    out["y_pred"] = predictions
    out["seed"] = seed
    out["model"] = model_name if extension else "baseline_tfidf_svm"
    return out.drop(columns=["label", "query"])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", type=Path, default=Path("reports/paired_ablation"))
    args = parser.parse_args()
    dataset = load_dataset(args.data, query_field="question", label_field="type",
                           domain_field="domain", id_field="id", expect_ragrouter_bench=True)
    frame = dataset.frame.sort_values("record_number").reset_index(drop=True)
    args.output.mkdir(parents=True, exist_ok=True)
    summaries = []
    for seed in SEEDS:
        baseline = run_model(frame, "baseline_tfidf_svm", seed, False)
        baseline.to_csv(args.output / f"baseline_seed_{seed}.csv", index=False)
        for name in CANDIDATES:
            ext = run_model(frame, name, seed, True)
            ext.to_csv(args.output / f"{name}_seed_{seed}.csv", index=False)
            summaries.append({"seed": seed, "model": name,
                              "accuracy": accuracy_score(ext.y_true, ext.y_pred),
                              "macro_f1": f1_score(ext.y_true, ext.y_pred, labels=CANONICAL_LABELS, average="macro")})
    pd.DataFrame(summaries).to_csv(args.output / "ablation_summary.csv", index=False)
    (args.output / "manifest.json").write_text(json.dumps({"seeds": SEEDS,
        "baseline": "tfidf_svm", "candidates": list(CANDIDATES),
        "protocol": "identical shuffled stratified five-fold splits",
        "answers_used_as_features": False}, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote paired OOF and ablation outputs to {args.output.resolve()}")


if __name__ == "__main__":
    main()
