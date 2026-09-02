# Eval Metric Taxonomy

Use multiple metric families. Do not compress a multi-stage AI product into one number, and do not compare metrics without comparable Experiment identity.

## 1. Quality

Measures whether the product produces the intended semantic result.

Examples:
- recall / precision / F1;
- exact or semantic match;
- task completion;
- grounded answer correctness;
- extraction completeness;
- user preference or rubric score.

Quality thresholds are product-specific.

## 2. Stability / Repeated Trials

Use only when non-determinism matters.

Examples:
- task success rate across trials;
- failure rate across trials;
- consistency rate;
- pass-at-k style success;
- repeated-success or all-trials-pass requirements for high-risk tasks.

Keep task-level and trial-level metrics separate. Do not multiply every deterministic regression case into repeated trials without a product reason.

## 3. Safety / Authority

Measures whether the system crosses a boundary it must never cross.

Examples:
- cross-tenant or private-data leakage;
- unauthorized data/tool use;
- weak/reference-only content promoted to authoritative output;
- policy or approval bypass;
- destructive side effect without permission.

These are commonly hard gates, not average metrics.

## 4. Provenance / Traceability

Measures whether an output can be traced to the correct source and lineage.

Examples:
- correct source/document/chunk IDs;
- valid span offsets;
- source hash consistency;
- correct citation target;
- no cross-document context contamination.

## 5. Contract / Availability

Measures whether the model/runtime response is usable by the product.

Examples:
- schema-valid final response;
- required fields present;
- runtime identity available;
- Provider reached;
- validation failure class;
- abstention / unavailable rate.

## 6. System Performance / Cost

Examples:
- Provider attempts;
- retries;
- latency P50/P95;
- token usage;
- monetary cost;
- timeout/rate-limit rate;
- cost per successful task.

Only include actual Provider calls in Provider latency statistics.

## 7. Experiment Comparison

Use deltas to compare a candidate with a known baseline.

Examples:
- fixed case count;
- regressed case count;
- unchanged pass/fail;
- new hard-fail count;
- quality delta;
- latency delta;
- token/cost delta;
- Provider-error or retry delta.

A numerical delta is not meaningful if dataset, evaluator, runtime, or other material identity differences are unknown.

## 8. Evaluator Quality

When a learned/model-based evaluator is used, measure whether it agrees with trusted judgment well enough for its role.

Examples:
- confusion matrix;
- precision/recall or TPR/TNR;
- false-positive / false-negative rate;
- agreement rate by risk or difficulty slice;
- human-human disagreement when relevant.

Do not treat evaluator quality as permanently valid after its rubric/model/task distribution materially changes.

## 9. Product / Business Utility

Examples:
- user task success;
- edit distance or manual correction burden;
- time saved;
- completion rate;
- downstream conversion or acceptance;
- reviewer approval rate;
- user correction / override / escalation rate.

These should sit above lower-layer technical gates rather than replace them.

## Suite meaning

A metric target depends on suite purpose:

- **Capability:** measures the frontier; partial success can be informative.
- **Regression:** protects previously reliable behavior; thresholds are generally stricter.

Do not mix both populations into one headline score when doing so hides regressions or makes progress hard to interpret.

## Certification labels

Recommended Experiment-level states:

- `PROVISIONAL` — informative but not release-valid;
- `CERTIFIED` — required identities, adjudication, and gates are complete;
- `BLOCKED` — a prerequisite prevents valid completion;
- `INVALID_RUN` — run integrity cannot be proven.
