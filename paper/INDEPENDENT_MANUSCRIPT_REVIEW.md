# Manuscript review before submission

Review type: internal AI-assisted review. This is not a peer review and does
not replace review by a human researcher who is independent of the authors.

## Overall assessment

The manuscript is a useful reproducibility and robustness preprint with a clear
negative finding: the public dataset and minimally assumed order-preserving
protocol do not numerically reproduce the reference TF-IDF/SVM result. The
paper is suitable for an arXiv preprint after the author metadata and evidence
package are finalized, but it should not claim a controlled superiority result
until the paired comparison and ablation are run.

## Evidence audit performed

- The Git history currently attributes all five commits to Song Toan. It does
  not independently prove that the two named coauthors did not contribute, but
  it also provides no repository evidence for their contribution.
- No aligned baseline/extension OOF pair or final paired-test JSON is currently
  present, so a paired statistical claim cannot be verified.
- The current benchmark report contains selected-model and stress results, but
  not a same-protocol feature-family ablation table.
- The Hugging Face dataset card declares MIT; the upstream source-corpus terms
  still need to be checked separately.
- No raw dataset files are tracked by Git. Generated Markdown reports were
  sanitized, and remaining absolute paths are only user-facing local setup
  examples, not credentials or private data.

## Major issues to resolve

1. **Paired comparison.** Run the reference baseline and selected extension on
   exactly the same folds, seeds, preprocessing, and selection rule. Report
   paired bootstrap intervals and a paired permutation test.
2. **Ablation.** Add a table isolating word, character, structural, NB-SVM,
   boosting/dimensionality-reduction, and stacking contributions under one
   declared protocol.
3. **Dataset provenance.** Preserve the final dataset fingerprint, repository
   commit, lockfile, and exact commands used for every headline result.
4. **Authorship.** Obtain written confirmation from every listed author. If a
   person cannot confirm a qualifying contribution, remove the name or move it
   to acknowledgements.
5. **Claims.** Keep simulated savings explicitly separate from measured API
   billing, latency, retrieval quality, and answer quality.

## Minor issues

- Check the final PDF for table width, column balance, and bibliography style
  under the target venue template.
- Keep the full dataset hash in the machine-readable report and use only a short
  prefix in the two-column paper.
- Check that public archives contain no local paths, credentials, or downloaded
  raw data that the dataset license does not permit redistributing.
- Ask a human reader unfamiliar with the code to follow the README from a clean
  environment and record any setup failures.

## Recommendation

**Preprint after metadata and author confirmation; major revision before making a
strong baseline-versus-extension claim.**
