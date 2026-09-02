# Experiment System

Use this reference when separate Eval runners, reports, or benchmarks need to become one comparable and continuously usable system.

## Core entities

- **Dataset** — immutable or versioned inputs plus trusted labels/metadata.
- **Task** — one evaluation problem or case.
- **Trial** — one execution of a task. Deterministic tasks usually need one; non-deterministic tasks may need several.
- **Scorer / Evaluator** — converts outputs/traces into structured judgments or metrics.
- **Suite** — a governed collection of tasks, metrics, and gates with one purpose.
- **Experiment** — the comparable run unit: suite + dataset + candidate system identity + evaluator identity + execution policy + results.
- **Baseline** — a prior certified or explicitly selected Experiment used for comparison.

## Experiment identity

An Experiment should capture enough identity to answer: "What exactly changed between these two results?"

Recommended identity fields:

- experiment ID and schema version;
- suite ID/type/version;
- dataset ID/version/hash;
- build/runtime identity;
- provider/model identity when applicable;
- prompt/instruction hash when applicable;
- schema/contract identity;
- evaluator ID/version;
- execution mode and retry policy;
- baseline experiment ID when comparing.

Do not require fields that the evaluated system does not have. Unknown identity that matters to interpretation should make the result provisional or invalid rather than silently omitted.

## Execution modes

### QUICK

Use for local diagnosis and deterministic/offline replay.

- prefer cached or captured outputs;
- avoid live Provider calls unless the changed boundary requires them;
- run the smallest affected set;
- do not present the result as release certification.

### TARGETED

Use after a meaningful semantic, retrieval, tool, prompt, or runtime change.

- run affected regression cases;
- include historical failures and representative boundary/negative cases;
- use bounded live-call budgets;
- repeat only unstable or high-risk tasks.

### CERTIFICATION

Use for freeze, release, major model/runtime migrations, or other formal quality decisions.

- require complete identity and lineage;
- enforce all applicable hard/quality/operational gates;
- use the governed suite rather than ad hoc case selection;
- persist the artifact needed to reproduce or audit the decision.

## Capability vs Regression suites

**Capability suites** measure the frontier. They may contain intentionally difficult or unsolved tasks and are useful for model/prompt/system selection.

**Regression suites** protect known behavior. Their thresholds should be stricter and failures should be treated as product regressions rather than ordinary exploration.

A capability task may graduate into regression after it is repeatedly solved under the relevant system conditions. Graduation should be explicit; do not move cases only to improve headline scores.

## Repeated trials

Do not multiply every task by an arbitrary trial count. Repeated trials are justified when:

- the evaluated behavior is stochastic;
- prior runs show instability;
- the task is high risk;
- a capability comparison depends on reliability, not one lucky success;
- a release decision requires confidence in repeated success.

Useful summaries include success rate, failure rate, consistency, pass-at-k style success, or repeated-success requirements. Keep task-level and trial-level records separate.

## Comparison contract

A useful Experiment comparison should report more than aggregate score deltas.

At minimum classify cases as:

- fixed;
- regressed;
- unchanged pass;
- unchanged fail;
- newly blocked/invalid;
- hard-gate change.

Also compare operational dimensions when available: latency, tokens/cost, Provider errors, retry rate, and side effects.

Never compare two Experiments as peers when a material identity difference is unknown or one run is uncertified in a way that changes metric meaning.

## Cost control

Use the cheapest evidence that can answer the current question:

1. deterministic/unit checks;
2. offline replay;
3. affected-case live run;
4. repeated trials for selected tasks;
5. full certification.

Cache artifacts only when reuse does not hide a changed boundary. Preserve Provider-call accounting across retries and detached processes when formal cost or semantic conclusions depend on it.

## Migration from legacy Eval runners

Do not rewrite working evaluators first. Wrap them.

A legacy adapter should map existing outputs into the common Experiment and Case Result contracts while leaving the original scoring logic intact. Replace legacy internals only when a separate product reason exists.

Prefer:

```text
legacy runner
→ adapter
→ common Experiment artifact
→ comparison / gate
```

over a repository-wide Eval rewrite.

## Persistence

Start with the simplest durable store that supports comparison and audit. Local files or CI artifacts are often sufficient for a small team. Add a database or hosted Eval platform only when concurrency, search, dashboards, retention, or online feedback justify it.

The Experiment contract should remain portable across storage choices.
