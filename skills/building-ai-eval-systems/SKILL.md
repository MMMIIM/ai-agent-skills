---
name: building-ai-eval-systems
description: Use when an AI or LLM product needs a repeatable evaluation system, benchmark design, experiment comparison, release gates, failure attribution, regression strategy, or when a single accuracy score cannot explain where a multi-stage AI pipeline fails.
---

# Building AI Eval Systems

## Overview

Build Eval as a product-quality system, not a model leaderboard. Every result should be attributable to a layer, reproducible under a known identity, comparable with a baseline, and safe to use for release decisions.

**Core principle:** Never tune the model until deterministic boundaries below it are proven healthy.

## Workflow

1. **Map production.** Write the real path from input to user-visible output. Mark deterministic stages, model stages, authority gates, persistence, tools, and human approvals.
2. **Freeze the Eval contract.** Record dataset/gold, evaluator revision, runtime/build, prompt/instruction, provider/model, schema/contract, provenance identity, retry policy, fixture snapshot, and run identity.
3. **Enforce parity.** Reuse production resolvers/builders or assert executable parity. Do not create shadow Eval semantics.
4. **Evaluate bottom-up.** Contract/unit → deterministic boundary → smoke → boundary/adversarial → semantic benchmark → E2E. Do not spend Provider calls above a failing lower layer.
5. **Build a fixture matrix.** Include positives, limited/partial cases, negatives, high-similarity false positives, invalid/missing inputs, unauthorized/reference-only sources, and cross-scope isolation.
6. **Use metric families.** Measure quality, safety/authority, provenance, schema/availability, latency/cost, and product utility.
7. **Separate hard gates from quality targets.** Leakage, authority contamination, wrong provenance, unsupported critical facts, approval bypass, unauthorized side effects, or unexpected persistent mutations should not be hidden by average scores.
8. **Capture first failure.** Record stage, cause code, Provider reached/not reached, retry eligibility, and final outcome. Never report only `FAIL`.
9. **Control the run.** Use a unique run ID, single-run lock when needed, persistent Provider-call accounting, explicit call budget, and pre/post side-effect checks. If run history becomes unverifiable, mark it invalid instead of guessing.
10. **Diagnose before fixing.** Choose one primary root cause, make the smallest change at the owning layer, replay failed cases offline when possible, then rerun affected phases only.
11. **Freeze passed layers.** Reopen them only when new evidence invalidates the previous gate.
12. **Certify metrics.** Structural or provisional metrics must not be presented as semantic or release-valid until required adjudication and identity checks complete.
13. **Treat Experiment as the comparison unit.** An Experiment is an immutable evaluation snapshot over a known suite, dataset, candidate system identity, evaluator identity, execution policy, and baseline. Compare Experiments, not loose score files.
14. **Separate Task from Trial.** For non-deterministic behavior, a task may have multiple trials. Default to one trial for stable regression work; add repeated trials only for unstable, high-risk, capability, or release-critical cases. Report consistency or repeated-success behavior instead of collapsing trials into one boolean.
15. **Separate Capability from Regression.** Capability suites explore the frontier and may contain difficult unsolved cases. Regression suites protect previously reliable behavior and should have much stricter gates. Stable capability cases may graduate into regression.
16. **Calibrate model-based evaluators.** A model grader is another component, not ground truth. Compare it against trusted human labels on held-out examples, measure disagreement, and revalidate when the rubric, grader prompt/model, or task distribution changes.
17. **Choose the cheapest valid execution mode.** Use `QUICK` for local/offline diagnosis, `TARGETED` for affected cases with bounded live calls, and `CERTIFICATION` for freeze/release evidence. Do not run certification-level work for every local change.

## Failure Classes

Use one primary class: `DETERMINISTIC_BOUNDARY`, `SEMANTIC_QUALITY`, `SCHEMA_CONTRACT`, `AUTHORITY_SAFETY`, `PROVENANCE`, `TRANSPORT_PROVIDER`, `AVAILABILITY`, `PERSISTENCE`, or `EVAL_HARNESS`.

If the Provider was never reached, do not draw a model-quality conclusion.

## Minimum Experiment Artifact

Emit: experiment/run identity, suite and dataset identity, candidate and evaluator identity, baseline when applicable, execution mode, scope, phase scorecard, hard gates, per-case first failure, trial summary when repeated, Provider attempts/retries/latency/cost when available, side-effect deltas, one primary root cause, up to three next actions, and certification state: `PROVISIONAL`, `CERTIFIED`, `BLOCKED`, or `INVALID_RUN`.

## Completion Rule

Eval is release-ready only when production parity, evaluator identity, artifact lineage, first-failure observability, hard safety gates, semantic certification, and the Experiment identity used for comparison are explicit and reproducible.
