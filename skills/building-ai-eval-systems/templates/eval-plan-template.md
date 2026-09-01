# AI Eval Plan

## 1. Objective

- product capability under test:
- decision this Eval must support:
- out of scope:

## 2. Production path

```text
Input
→
→
User-visible result
```

For each stage mark:
- deterministic or semantic;
- owner/module;
- Provider call yes/no;
- persistence side effect;
- authority/policy gate;
- human approval gate.

## 3. Eval contract

- dataset/gold version:
- evaluator version/revision:
- runtime/build identity:
- production input resolver identity:
- prompt/instruction identity:
- schema/contract identity:
- provider/model:
- retry policy:
- provenance/source identity:
- run_id:

## 4. Fixture matrix

| Category | Count | Why it matters |
|---|---:|---|
| Clear positive | | |
| Partial / limited | | |
| Clear negative | | |
| High-similarity false positive | | |
| Missing / invalid | | |
| Unauthorized / reference-only | | |
| Cross-scope isolation | | |

Freeze fixtures before Provider calls.

## 5. Evaluation pyramid

### Layer A — contract / deterministic
- tests:
- pass gate:

### Layer B — retrieval / context / routing
- tests:
- pass gate:

### Layer C — semantic model
- tests:
- pass gate:

### Layer D — persistence / policy / authority
- tests:
- pass gate:

### Layer E — E2E product utility
- tests:
- pass gate:

## 6. Metrics

### Quality

### Safety / authority

### Provenance

### Availability / schema

### Latency / cost

### Product utility

## 7. Hard gates

| Gate | Threshold | Owner | Release consequence |
|---|---|---|---|
| | | | |

## 8. Provider budget

- maximum attempts:
- retry policy:
- call ledger path:
- single-run lock:
- stop conditions:

## 9. Persistence policy

- expected DB writes:
- pre-run counts:
- post-run counts:
- cleanup policy:

## 10. Failure handling

For every failure capture:
- case_id;
- first failure stage;
- cause code;
- Provider reached;
- retry eligibility;
- safe diagnostic;
- final outcome.

## 11. Certification

- current state: PROVISIONAL / CERTIFIED / BLOCKED / INVALID_RUN
- certification prerequisites:

## 12. Change policy

During the benchmark:
- production code changes allowed: NO by default;
- prompt/model changes allowed: NO by default;
- auto-fix allowed: NO;
- after failure: diagnose → minimal fix → offline replay → affected-phase rerun.
