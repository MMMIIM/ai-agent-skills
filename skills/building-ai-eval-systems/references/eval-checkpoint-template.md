# AI Eval Checkpoint Template

## RUN IDENTITY
- run_id:
- dataset/gold version:
- evaluator version/hash:
- runtime/build identity:
- production contract/schema identity:
- prompt/instruction identity:
- provider/model:
- retry policy:
- source/provenance identity:
- certification state: PROVISIONAL / CERTIFIED / BLOCKED / INVALID_RUN

## SCOPE
- system path under test:
- data/project/tenant scope:
- cases:
- excluded phases:
- DB write policy:
- Provider call budget:

## PHASE SCORECARD
| Phase | Cases | Pass | Fail | Hard Fail | Provider Reached |
|---|---:|---:|---:|---:|---:|
| Deterministic boundary | | | | | |
| Retrieval/context | | | | | |
| Semantic/model | | | | | |
| Canonicalization/persistence | | | | | |
| E2E | | | | | |

## QUALITY
- primary quality metric:
- secondary metrics:
- usability metric:

## HARD GATES
- scope/tenant violations:
- authority contamination:
- provenance failures:
- unsupported facts/hallucinations:
- approval bypass:
- unexpected DB mutation:

## FIRST FAILURES
For each failure:
- case_id:
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
- call-ledger complete:
- latency min/mean/P50/P95/max:
- prompt/input tokens:
- completion/output tokens:
- estimated/actual cost:

## DB / SIDE EFFECT
- pre counts:
- post counts:
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
