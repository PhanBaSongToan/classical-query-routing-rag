# arXiv readiness review

The manuscript is a credible technical preprint, but the following items should
be completed before submission.

## Required scientific cleanup

- Run the reference TF-IDF/SVM and the selected extension on exactly the same
  folds, seeds, tokenization, and selection protocol.
- Report paired confidence intervals or a paired permutation test; do not infer
  significance from independent means and standard deviations.
- Add a predeclared ablation for word, character, structural, NB-SVM,
  dimensionality-reduction/boosting, and stacking components.
- State clearly that the official reproduction is not numerically identical to
  the reported paper result (`0.807558/0.806758` versus `0.932/0.928`).
- Keep the shuffled, source-order, grouped, and leave-one-domain-out results as
  separate deployment assumptions.

## Reproducibility package

- Freeze the final Git commit and Python dependency versions.
- Preserve the dataset SHA-256 fingerprint and the exact command line for every
  headline table.
- Keep the model artifact, report manifest, fold indices, and generated tables
  together; do not commit downloaded raw data or secrets.
- Run the test suite from a clean environment and record the result.

## Writing and submission

- Replace the placeholder email and affiliation.
- Verify author order, acknowledgements, dataset/software citations, and license
  compatibility.
- Remove local Windows paths, credentials, and irrelevant historical files from
  the submission archive.
- Check the target venue template and page limit; arXiv accepts a preprint but
  does not peer-review or certify the claims.
- Have at least one independent reader check every number in the abstract,
  tables, figures, and conclusion against the saved reports.
