# Reproduction report

## Objective

Reproduction of the non-deep-learning subset of the paper.

Protocol: `official_raw_labels`.

## Exact scope

Eight classical combinations only: TF-IDF or `structural_documented_18` with Logistic Regression, SVM, Random Forest, or KNN. It is not a full reproduction of all paper configurations.

## Explicit deep-learning exclusion

No deep-learning components, embeddings, external embedding APIs, LLM APIs, or transformer pipelines are present. The static prohibition test scans imports and dependency declarations.

## Dataset audit

Source checksum: `c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9`. Valid records: 7727. Detected fields: query `question`, label `type`, domain `domain`, id `id`. See `dataset_audit.md`.

## Reproduction protocol

Primary evaluation is `StratifiedKFold(n_splits=5, shuffle=False)`. TF-IDF uses `(1,2)` n-grams, 3,000 max features, `min_df=2`, and sublinear TF. TF-IDF and scaling are fitted inside each pipeline fold.

## Feature definitions

The TF-IDF branch applies no stemming, lemmatization, stop-word removal, or custom text cleaning. The structural branch is `structural_documented_18`: token/character counts, average word length, seven question-word flags, negation, approximate capitalized-span entities, clause heuristic, and five documented pattern flags.

## Classifier definitions

Logistic Regression uses L2, C=1.0, `max_iter=5000`, and no class weights. SVM uses RBF with `gamma=scale`, default C, and disabled probability estimation. Random Forest uses 200 trees, `random_state=42`, and `n_jobs=-1`. KNN uses 7 neighbours, cosine distance, and brute-force search. Resolved estimator parameters and sklearn version are recorded in saved model metadata.

## Cross-validation protocol

Every valid record receives exactly one OOF prediction. The saved fold indices, metrics, confusion matrices, and fit/prediction times make fold behavior auditable. Unshuffled CV is a minimally assumed choice because the paper does not state shuffle behavior or a seed.

## Main results

| configuration | protocol | mean_accuracy | std_accuracy | mean_macro_f1 | std_macro_f1 | pooled_accuracy | pooled_macro_f1 | fit_time_seconds | prediction_time_seconds |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| tfidf_logistic_regression | official_raw_labels | 0.805005 | 0.144900 | 0.798170 | 0.161868 | 0.804970 | 0.803974 | 1.193429 | 0.127706 |
| tfidf_svm | official_raw_labels | 0.807595 | 0.148262 | 0.800431 | 0.168138 | 0.807558 | 0.806758 | 17.067696 | 3.600517 |
| tfidf_random_forest | official_raw_labels | 0.823254 | 0.144014 | 0.821765 | 0.154194 | 0.823217 | 0.824086 | 3.372474 | 0.312139 |
| tfidf_knn | official_raw_labels | 0.730072 | 0.133407 | 0.722003 | 0.170489 | 0.730038 | 0.739226 | 0.927775 | 0.831583 |
| structural_documented_18_logistic_regression | official_raw_labels | 0.738605 | 0.095999 | 0.729820 | 0.098101 | 0.738579 | 0.728839 | 1.480716 | 0.320259 |
| structural_documented_18_svm | official_raw_labels | 0.766038 | 0.091726 | 0.762300 | 0.099463 | 0.766015 | 0.762058 | 3.002295 | 1.339915 |
| structural_documented_18_random_forest | official_raw_labels | 0.738735 | 0.101616 | 0.727865 | 0.106985 | 0.738708 | 0.727939 | 2.609681 | 0.502343 |
| structural_documented_18_knn | official_raw_labels | 0.733426 | 0.094232 | 0.727203 | 0.099905 | 0.733402 | 0.728999 | 1.321174 | 1.033159 |

## Paper comparison

See `paper_comparison.md`; its GREEN/YELLOW/RED rubric reports numerical parity separately from protocol match.

A consistent class-name permutation does not necessarily alter accuracy or macro-F1. It does change per-class names, confusion-matrix interpretation, majority-class identity, and routing decisions when label names map to different RAG costs. It therefore changes simulated token savings. Matching macro-F1 does not prove semantic reproduction.

## Cost simulation

See `cost_accuracy_tradeoff.md`. All costs are post-hoc relative-cost simulations, not RAG or LLM measurements.

## Domain breakdown

See `domain_breakdown.md`; it uses pooled OOF predictions when a domain field is present.

## Robustness audit

See `robustness/` when the optional command is run. It is explicitly an additional audit and not part of the primary protocol.

## Reproduction gaps

See `REPRODUCTION_GAPS.md`.

## Conclusions

Protocol match does not by itself establish numerical parity; use the comparison and gaps reports together.

## Commands to reproduce

`python -m lightweight_router reproduce --data <labeled.json> --output reports`
