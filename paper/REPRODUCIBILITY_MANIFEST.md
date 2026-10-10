# Reproducibility manifest

This manifest records the environment used for the current working-tree paper
build. The working tree was intentionally not committed by the assistant.

| Item | Value |
|---|---|
| Base repository commit | `7ab8e4892dfa6d585d9a6163157a39686d5ec331` |
| Working tree | Dirty; final submission must record the commit after review |
| Python | 3.14.5 |
| Dataset records | 7,727 |
| Dataset SHA-256 | `c3566f9dca7c322861767df5b5384b97f25fac82344ef84615027cc67f77c7a9` |
| Official protocol | `StratifiedKFold(n_splits=5, shuffle=False)` |
| Extended seeds | `0, 1, 2, 3, 4, 13, 21, 42, 77, 100` |
| Tests | `54 passed` |
| Paper build | `pdflatex + bibtex + pdflatex + pdflatex`, exit code 0 |

The final author should replace the base commit with the final commit hash after
all files are reviewed and committed.
