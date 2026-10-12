# Classical Query Routing for Adaptive RAG

**Classical Query Routing for Adaptive Retrieval-Augmented Generation: Reproducibility, Robustness, and Cost-Aware Evaluation**

This repository accompanies the Zenodo preprint and contains the auditable
implementation, experiment reports, figures, and paper sources:
[Zenodo preprint and DOI](https://doi.org/10.5281/zenodo.23276765).

**Abstract.** This work audits and extends a classical query-routing benchmark
for retrieval-augmented generation (RAG). It reproduces the query-side setting
under explicitly declared evaluation protocols, adds lexical, character, and
structural classical features, and evaluates leakage-aware robustness under
source-order, grouped, and leave-one-domain-out splits. The router predicts a
retrieval strategy; it does not execute retrieval or answer generation.

Auditable reproduction and non-deep-learning extension of the query-routing
baseline reported in [Lightweight Query Routing for Adaptive RAG](https://arxiv.org/abs/2604.03455).
The maintained implementation is in [`lightweight-query-routing/`](lightweight-query-routing/).

**Topics:** `rag` · `query-routing` · `retrieval-augmented-generation` ·
`classical-machine-learning` · `reproducibility` · `robustness-evaluation` ·
`data-leakage` · `ragrouter-bench`

## What this repository contains

- Query-only routing among `single_hop`, `multi_hop`, and `summary` labels.
- Fold-local TF-IDF, character, structural, NB-SVM, dimensionality-reduction,
  boosting, and out-of-fold stacking experiments.
- Reproduction, robustness, leakage-audit, and cost-simulation reports.
- The paper source and compiled PDF under [`paper/`](paper/).

The router predicts a route recommendation only. It does not execute retrieval,
generation, or external LLM API calls. Simulated costs are relative benchmark
weights, not measured billing, latency, or answer quality.

## Quick start

```powershell
Set-Location .\lightweight-query-routing
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,extended-classical]"
python -m pip install -r requirements-lock.txt
git lfs install
git lfs pull
```

Download the public dataset:

```powershell
python -m pip install huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Chaplain0908/RAGRouter', repo_type='dataset', allow_patterns='data/*/Question.json', local_dir=r'data\raw\ragrouter-dataset')"
$data = (Resolve-Path "data\raw\ragrouter-dataset\data").Path
```

Then follow [`lightweight-query-routing/README.md`](lightweight-query-routing/README.md)
for audit, reproduction, robustness, prediction, and benchmark commands.

## Main findings

The order-preserving reproduction obtains 0.807558 accuracy and 0.806758
macro-F1, below the reference paper's reported 0.932 and 0.928. Under the
declared ten-seed shuffled protocol, the selected extended ensemble obtains
0.9521 accuracy and 0.9478 macro-F1. These values use different evaluation
protocols and must not be presented as an exact same-fold superiority claim.

## Repository layout

```text
lightweight-query-routing/  package, scripts, tests, reports, and artifact
paper/                       LaTeX source, figures, PDF, and reproducibility docs
models/                      small tracked baseline artifacts
LICENSE                      project license
```

Raw benchmark files and large generated experiment outputs are intentionally not
committed. See the package README for dataset provenance, seeds, leakage audit,
and limitations.

## License and contact

The project source is released under the license in [`LICENSE`](LICENSE).
The downloaded benchmark remains subject to its dataset and upstream-corpus
licenses. Contact: Phan Ba Song Toan, FPT University, Da Nang, Vietnam.
