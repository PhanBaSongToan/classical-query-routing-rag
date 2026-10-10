# Auditable Classical Query Routing for Adaptive RAG

This repository contains an auditable, strictly non-deep-learning implementation
of query-type routing on RAGRouter-Bench. It is based on the reference study
**Lightweight Query Routing for Adaptive RAG: A Baseline Study on RAGRouter-Bench**
and adds an extended classical benchmark plus a forensic and robustness audit.

The project predicts one of three query types:

```text
single_hop  -> NaiveRAG      (1.4x simulated cost)
multi_hop   -> HybridRAG     (2.8x simulated cost)
summary     -> IterativeRAG  (3.5x simulated cost)
```

The mapping is a literature-motivated simulation. The classifier does not execute
retrieval or generate an answer.

The structural feature schema is versioned at
`configs/structural_patterns.json`. This file is part of the reproducibility
surface and is required by the structural feature extractor.

## Installation on Windows PowerShell

Run these commands from the directory containing `pyproject.toml`:

```powershell
Set-Location "C:\Users\ACER\Code\LLM-Semantic-Router\lightweight-query-routing"

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,extended-classical]"
git lfs install
git lfs pull
```

If PowerShell blocks activation, run this once in the same PowerShell window:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

The dataset is not committed to this repository. Download the four question
files from [Hugging Face](https://huggingface.co/datasets/Chaplain0908/RAGRouter)
with:

```powershell
python -m pip install huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Chaplain0908/RAGRouter', repo_type='dataset', allow_patterns='data/*/Question.json', local_dir=r'data\raw\ragrouter-dataset')"
```

This creates `data\raw\ragrouter-dataset\data\<domain>\Question.json` for the
four domains. Pass the `data` directory to `--data`; the loader expects the four
domains and 7,727 records when `--expect-ragrouter-bench` is used:

```powershell
$data = (Resolve-Path "data\raw\ragrouter-dataset\data").Path
```

## Run a prediction

The tracked demonstration model is managed with Git LFS:

```powershell
python -m lightweight_router predict `
  --model "demo_models\best_accuracy_model\model.joblib" `
  --query "What is the most common type of skin cancer?"
```

Expected fields include `predicted_label`, `recommended_paradigm`,
`simulated_cost_ratio`, and `uncalibrated_decision_score`. Decision scores are
raw classifier scores and must not be reported as calibrated confidence.

## Run the audit and benchmark

Set the dataset path once, then run:

```powershell
$data = "C:\path\to\RAGRouter\data"

python -m lightweight_router audit `
  --data $data `
  --expect-ragrouter-bench `
  --query-field question --label-field type `
  --domain-field domain --id-field id `
  --output reports

python -m lightweight_router reproduce `
  --data $data `
  --expect-ragrouter-bench `
  --query-field question --label-field type `
  --domain-field domain --id-field id `
  --protocol official_raw_labels `
  --output reports

python -m lightweight_router extended-benchmark `
  --data $data `
  --expect-ragrouter-bench `
  --query-field question --label-field type `
  --domain-field domain --id-field id `
  --output reports\extended_classical_benchmark `
  --artifact-output artifacts\extended_classical_benchmark
```

For the separate robustness and forensic tracks:

```powershell
python -m lightweight_router robustness `
  --data $data `
  --expect-ragrouter-bench `
  --query-field question --label-field type `
  --domain-field domain --id-field id `
  --output reports\robustness

python -m lightweight_router forensic `
  --data $data `
  --expect-ragrouter-bench `
  --query-field question --label-field type `
  --domain-field domain --id-field id `
  --dataset-repo "C:\path\to\ragrouter-dataset" `
  --output reports\forensic_reproduction
```

## Reproducibility record

### 1. Random seeds

The selectable extended-benchmark candidates use the same ten shuffled
stratified five-fold seeds:

```text
0, 1, 2, 3, 4, 13, 21, 42, 77, 100
```

Screening uses seeds `(0, 21, 42)` and expensive feature screens use `(0, 42)`.
Screen-only configurations are not eligible for final model selection. The
benchmark uses fold-local preprocessing, feature selection, dimensionality
reduction, NB ratios, and meta-model fitting.

### 2. Model artifact

The demonstration artifact is:

```text
demo_models/best_accuracy_model/model.joblib
```

It is approximately 40.7 MB and is stored with Git LFS. After cloning, run
`git lfs pull`. The selected model is a global out-of-fold logistic stacking
ensemble. Its base components are a word/character structural LinearSVC, a
per-domain NB-SVM LinearSVC, a word n-gram Complement Naive Bayes model, and a
structural SVD LightGBM model. This is an extended benchmark artifact, not the
paper's original RBF-SVM artifact.

### 3. Benchmark reports

The tracked summary report is:

```text
reports/extended_classical_benchmark/MODEL_BENCHMARK_REPORT.md
```

The benchmark command additionally writes detailed CSV/JSON outputs under the
requested report directory, including repeated-CV results, per-class metrics,
stress results, cost-quality results, model runtime/size, and the run manifest.
Large generated artifacts and datasets are intentionally not committed.

The selected extended ensemble reports 0.952103 accuracy and 0.947794 macro-F1
under repeated shuffled evaluation. The best single model reports 0.948104
accuracy and 0.943432 macro-F1. These numbers must be cited with their protocol;
they are not a direct same-fold replacement for the paper's TF-IDF/SVM result.

### 4. Test results

Run the existing test suite with:

```powershell
python -m pytest -q
```

The validated project state passed **54 tests**. Deprecation warnings from the
installed Python/scikit-learn versions may appear; they do not change the test
result. The tests cover data loading, label normalization, CLI smoke behavior,
reproducibility, leakage safeguards, structural features, cost simulation,
forensic protocols, and the extended benchmark.

### 5. Limitation of simulated cost

The cost ratios are illustrative relative token-cost ratios inherited from the
benchmark literature. They are not measured API prices, latency, GPU cost, or
answer-quality loss. The type-to-strategy mapping is also a simplification:
optimal RAG strategy can depend on query--corpus interaction. Consequently:

- simulated savings must be reported together with macro-F1 and per-class recall;
- higher savings alone is not evidence of a better router;
- a cheap wrong route may harm a multi-hop or summary query;
- the project does not claim end-to-end RAG quality or real billing savings.

### 6. Leakage and robustness audit

The benchmark keeps preprocessing and model selection inside training folds.
Answers and supporting facts are not model inputs. The extended stacking
meta-model is trained only from inner out-of-fold base scores, never from
in-sample base predictions. Dataset provenance, normalized-query grouping,
structural-template grouping, source-order evaluation, and leave-one-domain-out
evaluation are treated as separate audits.

The selected ensemble stress results are:

| Protocol | Accuracy | Macro-F1 | Under-routing |
| --- | ---: | ---: | ---: |
| Ten-seed shuffled CV | 0.9521 | 0.9478 | 0.0252 |
| Source-order 5-fold | 0.8455 | 0.8448 | 0.0958 |
| Normalized-query grouped | 0.9453 | 0.9413 | 0.0252 |
| Template grouped | 0.9436 | 0.9393 | 0.0263 |
| Leave-one-domain-out | 0.6406 | 0.6729 | 0.2579 |

Grouped evaluation causes only a modest reduction, so direct duplicate/template
overlap does not explain the entire shuffled-CV gain. The much larger
leave-one-domain-out drop indicates substantial domain-specific signal and
limits claims of out-of-domain generalization.

## CLI commands

Available commands are:

```text
audit
reproduce
robustness
train-final
predict
forensic
improve
extended-benchmark
```

The primary reproduction uses `official_raw_labels`. The optional
`paper_label_permutation_diagnostic` is explicitly diagnostic and must not be
treated as canonical dataset semantics.

The official order-preserving reproduction produced pooled TF-IDF/SVM accuracy
`0.807558` and macro-F1 `0.806758`, versus the paper's `0.932` and `0.928`.
The downloaded dataset fingerprint was
`c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9`.

## Streamlit demonstration

If the optional demo files are present, install and run:

```powershell
python -m pip install -r demo\requirements-demo.txt
python -m streamlit run demo\streamlit_app.py
```

The dashboard calls the existing prediction API and does not retrain or replace
the model.

## Scope and limitations

This repository is a query-side classical routing study. It does not implement
the complete answer-generation pipeline, does not use external LLM APIs, and
does not establish that query type alone is sufficient for optimal corpus-aware
RAG selection. Reproduction and extension results must be reported separately.
