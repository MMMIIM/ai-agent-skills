# Eval Metric Taxonomy

Use multiple metric families. Do not compress a multi-stage AI product into one number.

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

## 2. Safety / Authority

Measures whether the system crosses a boundary it must never cross.

Examples:
- cross-tenant leakage;
- unauthorized data/tool use;
- reference-only content promoted to authoritative evidence;
- policy or approval bypass;
- destructive side effect without permission.

These are commonly hard gates, not average metrics.

## 3. Provenance / Traceability

Measures whether an output can be traced to the correct source and lineage.

Examples:
- correct source/document/chunk IDs;
- valid span offsets;
- source hash consistency;
- correct citation target;
- no cross-document context contamination.

## 4. Contract / Availability

Measures whether the model/runtime response is usable by the product.

Examples:
- schema-valid final response;
- required fields present;
- runtime identity available;
- Provider reached;
- validation failure class;
- abstention / unavailable rate.

## 5. System Performance / Cost

Examples:
- Provider attempts;
- retries;
- latency P50/P95;
- token usage;
- monetary cost;
- timeout/rate-limit rate.

Only include actual Provider calls in Provider latency statistics.

## 6. Product / Business Utility

Examples:
- user task success;
- edit distance or manual correction burden;
- time saved;
- completion rate;
- downstream conversion or acceptance;
- reviewer approval rate.

These should sit above lower-layer technical gates rather than replace them.

## Certification labels

Recommended run-level states:

- `PROVISIONAL` — informative but not release-valid;
- `CERTIFIED` — required identities, adjudication, and gates are complete;
- `BLOCKED` — a prerequisite prevents valid completion;
- `INVALID_RUN` — run integrity cannot be proven.
