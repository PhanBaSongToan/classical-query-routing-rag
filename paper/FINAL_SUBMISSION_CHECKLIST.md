# Final paper submission checklist

This checklist separates evidence that is already present in the repository from
the final checks that must be completed before sending the manuscript to a
supervisor, workshop, conference, or journal.

## Scientific claims

- [x] State that the work is an auditable reproduction and extension, not an
  exact reproduction of every reported number.
- [x] Separate the reference TF-IDF/SVM protocol from the extended benchmark
  protocol.
- [x] Report the selected ensemble's protocol with its accuracy, macro-F1,
  savings, and per-class recall.
- [x] Report source-order, grouped, and leave-one-domain-out stress results.
- [ ] Add the exact paired comparison of the paper baseline and the extension on
  identical folds, seeds, tokenization, and preprocessing.
- [ ] Add confidence intervals or a paired statistical comparison for the main
  baseline-versus-extension claim.
- [ ] Add an ablation table for word features, character features, structural
  features, NB-SVM, boosting, and stacking. Do not fill this table with values
  from a different protocol.

## Reproduction record

- [x] Record the ten repeated-CV seeds: `0, 1, 2, 3, 4, 13, 21, 42, 77, 100`.
- [x] Record screening seeds: `(0, 21, 42)` and expensive feature-screen seeds
  `(0, 42)`.
- [x] Record the dataset label mapping and the four domains.
- [x] Record the model artifact path and Git LFS requirement.
- [x] Record the 54-test result.
- [x] Add the final dataset fingerprint produced by the current checkout.
- [ ] Add the final repository commit hash to the manuscript.
- [x] Save the final generated CSV/JSON reports for the exact run used in the
  paper, outside the source tree if they are too large for Git.

## Leakage and robustness

- [x] Keep preprocessing and model selection inside training folds.
- [x] Keep answer text and supporting facts out of model inputs.
- [x] Train the stacking meta-model only from inner out-of-fold scores.
- [x] Report normalized-query and template-grouped evaluation.
- [x] Report source-order and leave-one-domain-out evaluation.
- [ ] Inspect the final run manifest and verify that no generated answer or
  test-label information entered feature construction.

## Writing and ethics

- [ ] Replace the placeholder author email and affiliation.
- [ ] Confirm all authors made a qualifying intellectual contribution and approve
  the submitted version.
- [ ] Cite the reference paper, RAGRouter-Bench, and reused software/data.
- [ ] Check that no credentials, private paths, or unnecessary personal data are
  included in the source ZIP.
- [ ] State that simulated cost is not measured billing, latency, or answer
  quality.
- [ ] State that the project does not run the complete RAG answer-generation
  pipeline.
- [ ] Have a supervisor or experienced researcher review the manuscript.

## Submission package

- [ ] Compile `main.tex` successfully on Overleaf with the same compiler as the
  selected venue.
- [ ] Confirm every citation appears in `references.bib` and every table/figure
  is referenced in the text.
- [ ] Check the venue's page limit, anonymization rules, template, and deadline.
- [ ] Upload the code repository link and reproducibility instructions as
  supplementary material when permitted.
- [ ] Upload to arXiv only after the author metadata and claims are final.
- [ ] Treat arXiv as a preprint; submit separately to the selected peer-reviewed
  venue.
