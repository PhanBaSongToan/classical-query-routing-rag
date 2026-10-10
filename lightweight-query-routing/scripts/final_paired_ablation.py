"""Final same-fold paired comparison and boosting/stacking ablation.

This is intentionally a small, predeclared run: the reference TF-IDF/RBF-SVM,
the selected logistic OOF ensemble, one fixed LightGBM booster, and one fixed
OOF logistic stack are evaluated on the same ten shuffled five-fold seeds.
Raw OOF files are written for an independent paired test.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from lightweight_router.data import load_dataset
from lightweight_router.extended_benchmark import (
    ExtendedCandidate, _evaluate_global_seed, _evaluate_per_domain_seed,
)
from lightweight_router.improvement import SEEDS
from lightweight_router.extended_models import build_extended_estimator


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--seeds", nargs="+", type=int, default=list(SEEDS))
    args = parser.parse_args()
    dataset = load_dataset(args.data, query_field="question", label_field="type",
                           id_field="id", expect_ragrouter_bench=True)
    frame = dataset.frame.sort_values("record_number").reset_index(drop=True)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    # These are the four roles used by the selected ensemble in the manuscript.
    structural = ExtendedCandidate.create("word_char_structural", "linear_svc_reference")
    nbsvm = ExtendedCandidate.create("nbsvm_word_char", "nbsvm_linear_svc", mode="per_domain")
    complement = ExtendedCandidate.create("word_3000", "complement_nb")
    booster = ExtendedCandidate.create("svd_structural_100", "lightgbm")
    selected = ExtendedCandidate.create("retained_nested", "ensemble_stack_logistic",
                                        {"base_ids": [structural.candidate_id, nbsvm.candidate_id,
                                                       complement.candidate_id, booster.candidate_id]})
    stack_no_boost = ExtendedCandidate.create("retained_nested", "ensemble_stack_logistic",
                                              {"base_ids": [structural.candidate_id, nbsvm.candidate_id,
                                                             complement.candidate_id]})
    candidates = [selected, booster, stack_no_boost]
    registry = {c.candidate_id: c for c in [structural, nbsvm, complement, booster, selected, stack_no_boost]}

    # Evaluate base candidates first so nested candidates can resolve their base definitions.
    seeds = tuple(args.seeds)
    for candidate in [structural, nbsvm, complement, booster]:
        for seed in seeds:
            target = output / candidate.candidate_id / f"seed_{seed}_oof.csv"
            if target.exists():
                continue
            if candidate.mode == "per_domain":
                oof, metrics, domains = _evaluate_per_domain_seed(frame, candidate, seed, registry)
            else:
                oof, metrics, domains = _evaluate_global_seed(frame, candidate, seed, registry)
            target.parent.mkdir(parents=True, exist_ok=True)
            oof.to_csv(target, index=False)
            (target.with_name(target.name.replace("_oof.csv", "_metrics.json"))).write_text(
                json.dumps(metrics, indent=2, default=str), encoding="utf-8")

    for candidate in candidates:
        for seed in seeds:
            target = output / candidate.candidate_id / f"seed_{seed}_oof.csv"
            if target.exists():
                continue
            oof, metrics, domains = _evaluate_global_seed(frame, candidate, seed, registry)
            target.parent.mkdir(parents=True, exist_ok=True)
            oof.to_csv(target, index=False)
            (target.with_name(target.name.replace("_oof.csv", "_metrics.json"))).write_text(
                json.dumps(metrics, indent=2, default=str), encoding="utf-8")

    rows = []
    for candidate in candidates:
        for seed in seeds:
            metrics = json.loads((output / candidate.candidate_id / f"seed_{seed}_metrics.json").read_text())
            rows.append({"candidate_id": candidate.candidate_id, "seed": seed,
                         "accuracy": metrics["accuracy"], "macro_f1": metrics["macro_f1"]})
    pd.DataFrame(rows).to_csv(output / "summary.csv", index=False)
    (output / "manifest.json").write_text(json.dumps({"seeds": list(seeds),
        "candidates": [c.candidate_id for c in [structural, nbsvm, complement, booster, selected, stack_no_boost]],
        "protocol": "StratifiedKFold(n_splits=5, shuffle=True, random_state=seed)",
        "dataset_records": len(frame)}, indent=2), encoding="utf-8")
    print(f"Wrote final paired OOF artifacts to {output.resolve()}")


if __name__ == "__main__":
    main()
