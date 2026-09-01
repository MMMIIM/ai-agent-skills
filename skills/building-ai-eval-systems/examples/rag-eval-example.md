# Example — RAG Eval

## Production path

```text
User query
→ query normalization
→ retrieval
→ context expansion
→ answer generation
→ citation/provenance validation
→ response
```

## Bottom-up Eval

### A. Deterministic

Check:
- tenant/project filters;
- chunk/document identity;
- context expansion bounds;
- citation span validity;
- no unexpected DB writes.

Hard gates:
- cross-tenant leakage = 0;
- cross-document context contamination = 0;
- invalid provenance = 0.

### B. Retrieval/context

Possible metrics:
- expected document hit;
- Recall@K / Relevant@K;
- useful-context rate;
- final context not heading-only or metadata-only.

Do not interpret retrieval quality before scope isolation passes.

### C. Semantic answer

Fixture categories:
- directly supported answer;
- partially supported answer;
- no-answer/insufficient context;
- high-similarity distractor;
- contradictory sources;
- reference-only source.

Possible metrics:
- grounded correctness;
- refusal/abstention correctness;
- citation entailment;
- unsupported claim count.

### D. E2E

Measure:
- user task success;
- reviewer correction burden;
- time saved;
- critical hallucination rate.

## Example diagnosis

```text
Answer accuracy looks poor
↓
20/30 failed before generation because context validator rejected source IDs
↓
Provider reached only 10/30
↓
Primary root cause = deterministic provenance boundary
↓
Do not tune answer prompt yet
```
