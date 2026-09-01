# Pressure Tests

Use these scenarios to verify the skill prevents drift without interrupting ordinary work.

## Expected behavior

1. **Local refactor** — Rename a private helper with no interface or semantic change. Expected: GREEN; proceed without governance ceremony.
2. **Production/eval split** — Eval rebuilds provider input separately from production. Expected: prefer shared production builder; otherwise require executable parity.
3. **Prompt/schema divergence** — Prompt requests flat fields while schema requires a nested object. Expected: classify as contract/parity risk; do not tune the model first.
4. **Silent fallback** — New response field is missing, so code reads a legacy field and continues. Expected: reject silent compatibility unless explicitly governed.
5. **Ephemeral identity** — A chunk rank or temporary source locator is reused across runs as permanent identity. Expected: reject; require stable identity/provenance.
6. **Duplicate authority** — A semantic worker starts assigning canonical IDs or approval state already owned by backend code. Expected: preserve single authority; worker remains semantic-only.
7. **Downstream failure after passed upstream gate** — A later semantic stage fails and someone proposes rewriting a frozen retrieval layer. Expected: keep passed layer frozen until new evidence implicates it.
8. **Unknown first failure** — Final output is wrong, but provider reach and validation boundaries are unknown. Expected: locate first failure before changing prompt/model/architecture.
9. **Stale gateway** — Code on disk has the fix but a long-running Gateway still behaves like the old version. Expected: check runtime freshness/identity before semantic debugging; classify mismatch as runtime parity, restart/reload the correct process, then retest.
10. **Runtime-check overuse** — A developer renames a local helper and runs offline unit tests. Expected: do not call `/info`, compute runtime hashes, or perform live parity checks.
11. **Certified live run** — A provider benchmark is about to start after Gateway/Prompt changes. Expected: perform one runtime certification before the run, record it, and reuse it across cases unless an invalidating runtime event occurs.

## Failure conditions for the skill

The skill fails its purpose if it:

- triggers repository-wide audits for GREEN changes;
- performs runtime identity checks for ordinary local work without a trigger;
- repeatedly checks runtime identity for every case in one unchanged run;
- recommends new architecture without evidence;
- treats documentation parity as proof;
- permits two authorities for one canonical object;
- hides contract breaks behind fallbacks;
- changes multiple layers before identifying the first failure;
- confuses runtime identity with behavioral parity.
