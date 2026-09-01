# Preventing Engineering Drift

A compact Agent Skill for preventing silent divergence in long-lived AI and software systems without turning governance into continuous supervision.

## Trigger model

This is a **risk-triggered governance skill**, not an always-on reviewer.

Load it when the current change may cause shared definitions, authority, identities, contracts, runtimes, eval paths, migrations, compatibility paths, or equivalent implementations to diverge.

Do **not** load it for GREEN work such as isolated UI changes, private helper refactors, documentation edits, or other local implementation details with no shared meaning, boundary, or runtime impact.

```text
GREEN local change
→ skip this skill

shared/boundary/runtime drift risk
→ load SKILL.md
→ check only affected invariants

runtime identity needed?
→ only when live results are about to be trusted and runtime may be stale/wrong
→ certify once and reuse until invalidated
```

The `SKILL.md` frontmatter description is the discovery trigger. `references/anti-drift-model.md` is optional depth for diagnosis; it should not be preloaded for ordinary work.

## What it checks

The skill focuses on five questions:

1. **Definition** — are modules still using the same business meaning?
2. **Authority** — is there still one canonical owner?
3. **Identity** — are runtime, contract, evaluator, and object identities explicit?
4. **Parity** — do paths that should be equivalent still behave equivalently?
5. **Observability** — can the first divergence be located before changing the system?

## Runtime identity escalation

Runtime identity is **event-triggered, not continuous**. Check it before relying on live/provider/E2E results only when runtime-loaded code/config changed, the endpoint/environment/runtime target changed, observed behavior contradicts current code, or the result will be used for benchmark/freeze/release decisions.

A passing runtime certification is reused within the same unchanged session or evaluation run. Re-check only after an invalidating event such as a relevant code/contract change, restart/deploy, endpoint/environment change, or runtime-target change.

## Design goals

- low token footprint;
- no full-repository scans for local changes;
- GREEN changes proceed normally;
- shared/contract/runtime changes receive a bounded checkpoint;
- prefer shared canonical implementations over duplicated synchronization;
- fail visibly instead of hiding breaks behind silent fallback;
- fix one owning boundary, then rerun only affected layers.

## Files

- [`SKILL.md`](./SKILL.md) — compact runtime skill.
- [`references/anti-drift-model.md`](./references/anti-drift-model.md) — deeper model and parity guidance.
- [`tests/pressure-tests.md`](./tests/pressure-tests.md) — pressure scenarios for verifying low-interference behavior.

## Key rule

> Equivalent paths must either reuse the same canonical implementation or prove executable parity. Documentation parity and developer intention are not proof.

This is especially useful for production/eval parity, prompt/schema parity, code/runtime parity, API/internal contracts, migrations, legacy coexistence, and AI pipelines with multiple semantic and deterministic stages.
