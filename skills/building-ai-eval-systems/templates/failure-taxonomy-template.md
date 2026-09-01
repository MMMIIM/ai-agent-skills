# Failure Taxonomy Template

Use one primary failure class per case. Record secondary diagnostics separately.

| Class | Definition | Example first-failure boundary | Model-quality conclusion allowed? |
|---|---|---|---|
| `DETERMINISTIC_BOUNDARY` | deterministic preprocessing/routing/validation failed first | input normalization mismatch | No |
| `SEMANTIC_QUALITY` | Provider produced a valid response but semantic decision was wrong | incorrect support/classification | Yes |
| `SCHEMA_CONTRACT` | final response violates required structured contract | missing required field | Not until schema behavior is isolated |
| `AUTHORITY_SAFETY` | system crosses a permission/source/policy boundary | unauthorized source promoted | No; hard gate first |
| `PROVENANCE` | source identity/lineage is incorrect or unverifiable | wrong span/hash/document | No |
| `TRANSPORT_PROVIDER` | request failed at network/provider boundary | timeout / HTTP error | No semantic conclusion |
| `AVAILABILITY` | required runtime/assessment is unavailable | evaluator cannot produce decision | No |
| `PERSISTENCE` | unexpected or invalid durable state transition | unintended DB write | No |
| `EVAL_HARNESS` | benchmark itself cannot prove integrity | lost run identity/call count | Run may be invalid |

## Required per-case record

```json
{
  "case_id": "",
  "phase": "",
  "first_failure_stage": "",
  "failure_class": "",
  "cause_code": "",
  "provider_reached": false,
  "retry_eligible": false,
  "final_outcome": "",
  "safe_diagnostic": ""
}
```

## Attribution rule

If `provider_reached = false`, do not label the result as a model semantic failure.
