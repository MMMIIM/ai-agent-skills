# Evaluator Calibration

Use this reference when a model-based grader, classifier, rubric judge, or other learned evaluator contributes to an Eval score or release decision.

## Principle

An evaluator is part of the evaluated quality system. Its output is evidence, not automatic ground truth.

## Calibration set

Build a trusted labeled set that is separate from the examples used to author the evaluator prompt or tune thresholds.

Include:

- clear positives and negatives;
- borderline or partial cases;
- high-similarity false positives;
- invalid/missing inputs;
- policy/safety boundary cases when applicable;
- representative domain and difficulty slices.

Record label provenance and reviewer status. Distinguish system-drafted labels from trusted human labels.

## Minimum calibration analysis

For classification-style evaluators, report a confusion matrix and the error rates that matter to the product, such as precision/recall, true-positive rate, true-negative rate, or false-positive/false-negative rate.

For scalar/rubric graders, measure agreement with trusted labels, inspect disagreement slices, and verify that score thresholds map to the intended product meaning.

Do not hide asymmetric risk in one average agreement number.

## Human disagreement

Human labels can disagree. When the decision is consequential, record reviewer disagreement and an adjudication path instead of pretending the first label is infallible.

Use multiple reviewers selectively for ambiguous, high-risk, or evaluator-calibration examples; do not require redundant review for every ordinary case.

## Revalidation triggers

Recalibrate when any of the following materially changes:

- evaluator prompt or rubric;
- evaluator model/provider;
- output schema or label taxonomy;
- task distribution or product domain;
- safety/quality threshold meaning;
- evidence showing systematic disagreement with humans.

Do not rerun calibration merely because unrelated application code changed.

## Release use

A model-based evaluator may support automated regression and release gates only to the degree justified by its calibration evidence.

If calibration is incomplete, mark semantic metrics provisional. If disagreement is concentrated in a high-risk slice, use a hard gate or human review for that slice rather than averaging it away.

## Avoid

- using the same examples to tune and certify the grader;
- assuming a stronger model is automatically a reliable evaluator;
- changing thresholds after seeing candidate results;
- treating evaluator availability failures as model-quality failures;
- using one judge for every metric when deterministic checks are available.
