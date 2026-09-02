# AI Eval Checkpoint Template

## EXPERIMENT IDENTITY
- experiment_id:
- baseline_experiment_id:
- suite id/type/version: CAPABILITY / REGRESSION
- dataset/gold version/hash:
- evaluator version/hash/calibration status:
- runtime/build identity:
- production contract/schema identity:
- prompt/instruction identity:
- provider/model:
- retry policy:
- source/provenance identity:
- execution mode: QUICK / TARGETED / CERTIFICATION
- certification state: PROVISIONAL / CERTIFIED / BLOCKED / INVALID_RUN

## SCOPE
- system path under test:
- data/project/tenant scope when applicable:
- cases:
- repeated-trial cases and trial count:
- excluded phases:
- write/side-effect policy:
- Provider call budget:

## PHASE SCORECARD
| Phase | Cases | Pass | Fail | Hard Fail | Provider Reached |
|---|---:|---:|---:|---:|---:|
| Deterministic boundary | | | | | |
| Retrieval/context/tools | | | | | |
| Semantic/model | | | | | |
| Canonicalization/persistence | | | | | |
| E2E | | | | | |

## QUALITY
- primary quality metric:
- secondary metrics:
- repeated-trial stability metric when applicable:
- product/usability metric:

## BASELINE COMPARISON
- fixed cases:
- regressed cases:
- unchanged pass:
- unchanged fail:
- newly blocked/invalid:
- hard-gate delta:
- latency/cost delta:

## HARD GATES
- scope/privacy violations:
- authority contamination:
- provenance failures:
- unsupported high-risk facts/hallucinations:
- approval/policy bypass:
- unauthorized or unexpected persistent mutation:

## FIRST FAILURES
For each failure:
- case_id:
- trial_id:
- stage:
- boundary:
- cause_code:
- provider_reached:
- retry_eligible:
- final_outcome:
- safe diagnostic:

## PROVIDER / COST
- attempts:
- successes:
- retries:
- call accounting complete:
- latency min/mean/P50/P95/max:
- prompt/input tokens:
- completion/output tokens:
- estimated/actual cost:

## SIDE EFFECTS
- expected mutations:
- pre state/counts:
- post state/counts:
- unexpected delta:

## PRIMARY ROOT CAUSE
Choose exactly one.

## SECONDARY FINDINGS
Maximum five.

## NEXT ACTIONS
### P0
- problem:
- evidence:
- minimal change:
- expected benefit:
- architecture impact:

### P1
### P2
