---
name: preventing-engineering-drift
description: Use when shared concepts, contracts, runtimes, evals, migrations, compatibility paths, or equivalent execution paths may diverge across changes.
---

# Preventing Engineering Drift

Prevent silent divergence without supervising ordinary development.

**Core principle:** Prefer one canonical implementation. If two paths must be equivalent, reuse the same owner or prove executable parity.

## Routing

- **GREEN** — local implementation detail, no shared meaning/boundary change: skip this skill.
- **YELLOW** — shared schema, prompt, API, evaluator, duplicated transformation, compatibility path, or runtime-facing change: run the fast check.
- **RED** — authority, canonical identity, persistence, migration, security, destructive action, or production contract cut: stop if ownership/evidence is unclear.

Classify only the surfaces actually changed. Do not scan unrelated subsystems.

## Fast drift check

Check only relevant invariants:

1. **Definition** — one canonical meaning; do not create a second business term for the same concept.
2. **Authority** — one owner for canonical identity, state, persistence, and critical transformation.
3. **Identity** — runtime/contract/prompt/schema/evaluator versions are explicit where comparison matters.
4. **Parity** — equivalent paths share canonical code or have executable parity assertions. Documentation or intent is not parity.
5. **Stable identity** — run-local positions, ranks, chunk numbers, or temporary refs never become cross-run identity.
6. **Representation** — preserve exact/canonical data; derived/model-facing forms must not redefine provenance or identity.
7. **Fallback** — no silent fallback, compatibility alias, or legacy path may hide a contract break unless explicitly governed.

## Change discipline

When drift is found: locate the **first failure boundary**, choose one primary root cause, make the smallest owner-level fix, replay affected cases, then rerun only impacted layers. Passed layers stay frozen unless new evidence invalidates them.

## Boundaries

This skill is a checkpoint, not a continuous reviewer. It does not grant authority to redesign architecture, migrate data, bypass approval, deploy, or broaden scope. Project instructions and explicit user authorization remain authoritative.
