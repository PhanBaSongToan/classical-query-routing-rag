# Paper draft

This directory contains the first English draft of a paper based on the
repository implementation. It is intentionally separated from the model source
and does not change the benchmark, artifacts, or README.

## Compile with LaTeX

From PowerShell:

```powershell
Set-Location "C:\Users\ACER\Code\LLM-Semantic-Router\paper"
.\compile.ps1
```

On Windows, install MiKTeX if the commands are not found:

```powershell
winget install --id MiKTeX.MiKTeX -e
```

Restart Codex after installation so its terminal receives the updated PATH.
Verify with `pdflatex --version` and `bibtex --version`.

If `pdflatex` is not installed, open `main.tex` in Overleaf and upload
`main.tex` and `references.bib`.

## Before submission

- Replace the placeholder author email and affiliation.
- Add the exact repository commit hash and confirm the dataset fingerprint
  (`c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9`) in
  the final version.
- The full official reproduction sweep is already included in `main.tex` and
  `reports/official_reproduction/official_raw_labels/REPRODUCTION_REPORT.md`.
- Run a final numerical check against the current reports.
- Select a target venue and switch to its official template.
- Have the supervisor review authorship, claims, and venue requirements.
