# Preventing Engineering Drift

A compact Agent Skill for preventing silent divergence in long-lived AI and software systems without turning governance into continuous supervision.

The skill focuses on five questions:

1. **Definition** — are modules still using the same business meaning?
2. **Authority** — is there still one canonical owner?
3. **Identity** — are runtime, contract, evaluator, and object identities explicit?
4. **Parity** — do paths that should be equivalent still behave equivalently?
5. **Observability** — can the first divergence be located before changing the system?

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

This is especially useful for production/eval parity, prompt/schema parity, API/internal contracts, migrations, legacy coexistence, and AI pipelines with multiple semantic and deterministic stages.
