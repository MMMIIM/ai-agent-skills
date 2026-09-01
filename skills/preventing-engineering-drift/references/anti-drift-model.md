# Anti-Drift Model

Use this reference only when a change needs deeper diagnosis than the compact `SKILL.md`.

## Five consistency layers

| Layer | Question | Typical drift |
|---|---|---|
| Definition | Are we still talking about the same concept? | duplicate terms, semantic redefinition |
| Authority | Who is allowed to decide/write it? | multiple writers, approval leakage |
| Identity | Which exact version/runtime/object is this? | stale prompt/schema/runtime, unstable IDs |
| Parity | Are paths that should be equivalent still behaviorally equivalent? | production/eval split, API/internal split |
| Observability | Can the first divergence be located? | generic FAIL, hidden retry/fallback |

## Parity hierarchy

Prefer, in order:

1. **Shared canonical implementation** — both paths call the same owner.
2. **Executable parity assertion** — separate implementations are compared by test/invariant.
3. **Manual synchronization** — avoid; documentation and developer intention are not proof.

Common parity surfaces:

- production ↔ eval
- prompt/instruction ↔ output schema
- API DTO ↔ internal canonical contract
- frontend state ↔ backend state
- DB metadata ↔ loaded runtime
- code on disk ↔ running process
- expected endpoint/runtime ↔ actual endpoint/runtime
- legacy path ↔ replacement path during migration

## Event-triggered runtime certification

Runtime identity is not a continuous health ritual. Check it only before a result depends on a live process and one of these is true:

- runtime-loaded code, prompt, schema, contract, config, or environment changed;
- endpoint/base URL, branch, deployment, container, tunnel, or process changed;
- observed live behavior contradicts the current code;
- a live/provider/E2E run is about to begin after such a change;
- the result will become a benchmark, freeze, or release decision.

A cheap check should normally confirm the target endpoint plus `started_at` and/or runtime/build identity. Expand to prompt/schema/contract hashes only when certification requires it or the cheap check disagrees.

Reuse one valid certification inside the same unchanged session/run. Invalidate it only when a relevant runtime change occurs. Do not request `/info` for every fixture or ordinary local edit.

**Rule:** code on disk is not evidence of code in execution. A stale process is a runtime parity failure, not a semantic-model failure.

## Canonical vs derived representation

Identity-bearing data should be created once and reused:

```text
exact/canonical source
→ identity/hash/provenance
→ derived/model-facing representation
```

A derived representation may trim, format, expand context, or simplify structure, but must not be re-hashed or treated as a new canonical identity unless the contract explicitly defines that transformation.

## Silent drift accelerators

Treat these as risk multipliers:

- duplicated normalizers/builders
- permissive fallbacks (`A || B || legacy`)
- compatibility aliases without retirement state
- two active persistence writers for the same concept
- eval-only business semantics
- run-local locators used across runs
- implicit state promotion from an upstream approval
- metrics compared without dataset/evaluator/runtime identity

## Minimal response to drift

Do not redesign the system because drift exists. First identify the owning boundary. Fix the smallest canonical owner or parity assertion, replay failed fixtures, and keep unrelated passed layers frozen.
