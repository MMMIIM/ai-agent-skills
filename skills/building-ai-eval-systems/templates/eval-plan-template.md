# AI Eval Plan

## 1. Objective

- product capability under test:
- decision this Eval must support:
- suite type: CAPABILITY / REGRESSION
- execution mode: QUICK / TARGETED / CERTIFICATION
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
- Provider/model/tool call yes/no;
- persistence side effect;
- authority/policy gate;
- human approval gate.

## 3. Experiment contract

- experiment_id:
- baseline_experiment_id:
- suite id/version:
- dataset/gold version/hash:
- evaluator version/revision/calibration status:
- runtime/build identity:
- production input resolver identity:
- prompt/instruction identity:
- schema/contract identity:
- provider/model:
- retry policy:
- provenance/source identity:

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

Freeze fixtures before live Provider calls.

## 5. Trial policy

- deterministic/stable cases default trials: 1
- repeated-trial case selectors:
- repeated trial count:
- stability metric:
- why repetition is necessary:

## 6. Evaluation pyramid

### Layer A — contract / deterministic
- tests:
- pass gate:

### Layer B — retrieval / context / routing / tools
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

## 7. Metrics

### Quality

### Stability / repeated trials

### Safety / authority

### Provenance

### Availability / schema

### Latency / cost

### Evaluator quality when model-based grading is used

### Product utility

## 8. Hard gates

| Gate | Threshold | Owner | Release consequence |
|---|---|---|---|
| | | | |

## 9. Provider budget

- maximum attempts:
- retry policy:
- call ledger/accounting path:
- single-run lock when needed:
- stop conditions:

## 10. Persistence policy

- expected writes/side effects:
- pre-run state/counts:
- post-run state/counts:
- cleanup policy:

## 11. Failure handling

For every failure capture:
- case_id;
- trial_id;
- first failure stage;
- cause code;
- Provider reached;
- retry eligibility;
- safe diagnostic;
- final outcome.

## 12. Baseline comparison

- fixed cases:
- regressed cases:
- unchanged pass/fail:
- new blocked/invalid cases:
- hard-gate delta:
- latency/cost delta:
- material identity differences:

## 13. Certification

- current state: PROVISIONAL / CERTIFIED / BLOCKED / INVALID_RUN
- certification prerequisites:
- evaluator calibration prerequisite when applicable:

## 14. Change policy

During a governed Experiment:
- production code changes allowed: NO by default;
- prompt/model changes allowed: NO by default;
- auto-fix allowed: NO;
- after failure: diagnose → minimal fix → offline replay → affected-phase rerun.
