---
name: building-ai-eval-systems
description: Use when an AI or LLM product needs a repeatable evaluation system, benchmark design, release gates, failure attribution, regression strategy, or when a single accuracy score cannot explain where a multi-stage AI pipeline fails.
---

# Building AI Eval Systems

## Overview

Build Eval as a product-quality system, not a model leaderboard. Every result should be attributable to a layer, reproducible under a known runtime, and safe to use for release decisions.

**Core principle:** Never tune the model until deterministic boundaries below it are proven healthy.

## Workflow

1. **Map production.** Write the real path from input to user-visible output. Mark deterministic stages, LLM stages, authority gates, persistence, and human approvals.
2. **Freeze the Eval contract.** Record dataset/gold, evaluator revision, runtime/build, prompt/instruction, provider/model, schema/contract, provenance identity, retry policy, fixture snapshot, and `run_id`.
3. **Enforce parity.** Reuse production resolvers/builders or assert executable parity. Do not create shadow Eval semantics.
4. **Evaluate bottom-up.** Contract/unit → deterministic boundary → smoke → boundary/adversarial → semantic benchmark → E2E. Do not spend Provider calls above a failing lower layer.
5. **Build a fixture matrix.** Include positives, limited/partial cases, negatives, high-similarity false positives, invalid/missing inputs, unauthorized/reference-only sources, and cross-scope isolation.
6. **Use metric families.** Measure quality, safety/authority, provenance, schema/availability, latency/cost, and product utility.
7. **Separate hard gates from quality targets.** Leakage, authority contamination, wrong provenance, unsupported critical facts, approval bypass, unauthorized side effects, or unexpected persistent mutations should not be hidden by average scores.
8. **Capture first failure.** Record stage, cause code, Provider reached/not reached, retry eligibility, and final outcome. Never report only `FAIL`.
9. **Control the run.** Use a unique run ID, single-run lock, persistent Provider-call ledger, explicit call budget, and pre/post side-effect checks. If run history becomes unverifiable, mark it invalid instead of guessing.
10. **Diagnose before fixing.** Choose one primary root cause, make the smallest change at the owning layer, replay failed cases offline, then rerun affected phases only.
11. **Freeze passed layers.** Reopen them only when new evidence invalidates the previous gate.
12. **Certify metrics.** Structural or provisional metrics must not be presented as semantic or release-valid until required adjudication and identity checks complete.

## Failure Classes

Use one primary class: `DETERMINISTIC_BOUNDARY`, `SEMANTIC_QUALITY`, `SCHEMA_CONTRACT`, `AUTHORITY_SAFETY`, `PROVENANCE`, `TRANSPORT_PROVIDER`, `AVAILABILITY`, `PERSISTENCE`, or `EVAL_HARNESS`.

If the Provider was never reached, do not draw a model-quality conclusion.

## Minimum Run Artifact

Emit: run identity, scope, phase scorecard, hard gates, per-case first failure, Provider attempts/retries/latency/cost when available, side-effect deltas, one primary root cause, up to three next actions, and certification state: `PROVISIONAL`, `CERTIFIED`, `BLOCKED`, or `INVALID_RUN`.

## Completion Rule

Eval is release-ready only when production parity, evaluator identity, artifact lineage, first-failure observability, hard safety gates, and semantic certification are explicit and reproducible.
