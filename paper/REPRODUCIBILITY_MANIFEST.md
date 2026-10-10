# Reproducibility manifest

This manifest records the environment used for the current working-tree paper
build. The working tree was intentionally not committed by the assistant.

| Item | Value |
|---|---|
| Final artifact commit | `a682822efbb06dd0618eade2c4517009e5f225de` (paper, figures, paired-ablation code/report) |
| Working tree | LaTeX auxiliary/log files may change after compilation; source/artifact commit is recorded above |
| Python | 3.14.5 |
| Dataset records | 7,727 |
| Dataset SHA-256 | `c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9` |
| Official protocol | `StratifiedKFold(n_splits=5, shuffle=False)` |
| Extended seeds | `0, 1, 2, 3, 4, 13, 21, 42, 77, 100` |
| Tests | `54 passed` |
| Paper build | `pdflatex + bibtex + pdflatex + pdflatex`, exit code 0 |

The final author should rerun `git rev-parse HEAD` after any later manuscript
edit and update this row if the submitted source changes.
