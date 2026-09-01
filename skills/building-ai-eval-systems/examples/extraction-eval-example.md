# Example — Structured Extraction Eval

## Production path

```text
Document
→ parser
→ chunk/segment selection
→ production input builder
→ LLM extraction
→ schema validation
→ grounding/provenance validation
→ canonical record
```

## A. Production-input parity

Eval should reuse the same input builder as production or assert executable parity.

Capture:
- exact model-visible text;
- segment IDs;
- prompt/instruction version;
- response-schema identity.

## B. Fixture matrix

Include:
- clear explicit field;
- field with qualifiers;
- negative statement;
- missing field;
- table/structured text;
- multi-paragraph field;
- high-similarity non-target text.

## C. Metrics

Structural:
- schema validity;
- source range reachable;
- required field presence.

Semantic:
- field accuracy;
- omission rate;
- false-positive rate;
- qualifier preservation.

Provenance:
- correct source span;
- source hash/identity;
- no unsupported values.

Do not publish a structural source-overlap score as semantic extraction accuracy.

## Example diagnosis

```text
0/24 valid canonical records
Provider calls = 0
All failed exact-source validation before Gateway
→ deterministic/provenance blocker
→ no model-quality conclusion
```
