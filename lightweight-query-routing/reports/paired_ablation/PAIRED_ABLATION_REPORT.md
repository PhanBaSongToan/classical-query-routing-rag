# Protocol-matched paired comparison and ablation

This report was generated with `scripts/paired_ablation.py` on the public
RAGRouter-Bench release. Every candidate used the identical ten shuffled
stratified five-fold seeds: `0, 1, 2, 3, 4, 13, 21, 42, 77, 100`.

## Feature ablation

| Feature family | Mean accuracy | Mean macro-F1 |
| --- | ---: | ---: |
| Word n-grams | 0.927553 | 0.924241 |
| Character n-grams | 0.928653 | 0.924778 |
| Word + character | 0.940909 | 0.936459 |
| Word + character + structural | 0.946732 | 0.942050 |
| NB-SVM (word + character) | 0.931099 | 0.925072 |

## Paired comparison

The reference TF-IDF/RBF-SVM and the fixed word-character-structural LinearSVC
were evaluated on the same folds. The extension's mean paired accuracy gain was
`0.018869`. Across the ten seeds, the bootstrap 95% interval endpoints ranged
from `[0.011000, 0.021483]` to `[0.016044, 0.026142]`. Each 1,000-resample
sign-flip permutation test returned `p < 0.001` (reported as zero by the finite
Monte Carlo estimate).

This is a comparison of two fixed candidates, not a significance claim for the
post-selection ensemble. Boosting and stacking are not included in this
isolated ablation because their complete fold-local OOF artifacts were not
available in the same run.

The raw OOF CSV/JSON files are intentionally ignored by Git because they are
large/generated outputs. Recreate them with:

```powershell
python scripts\paired_ablation.py `
  --data data\raw\ragrouter-dataset `
  --output reports\paired_ablation
```
