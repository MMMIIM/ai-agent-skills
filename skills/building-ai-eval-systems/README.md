# Building AI Eval Systems

> **Evaluate the system, not just the model.**

A reusable Agent Skill and practical framework for designing evaluation systems for production AI products: RAG, tool-using agents, structured extraction, classification, generation, and multi-stage LLM pipelines.

## Why this exists

Weak AI evaluation often looks like:

```text
bad output
→ blame the prompt
→ change the model
→ rerun
→ get a different number
→ still do not know what failed
```

This Skill instead asks:

- Which layer owns the first failure?
- Did the Provider actually receive the request?
- Was Eval input identical to production input?
- Did a deterministic contract, authority rule, or provenance check fail first?
- Is the metric structural, semantic, or release-certified?
- Can the run be reproduced and compared with the next run?

## Core workflow

```text
Map production
→ freeze Eval identity
→ prove production parity
→ test deterministic boundaries
→ test semantic behavior
→ enforce hard safety gates
→ capture first failure
→ diagnose one root cause
→ minimal fix
→ offline replay
→ affected-phase regression
→ freeze passed layers
```

See [`SKILL.md`](./SKILL.md) for the compact agent-facing rules.

## Included material

- [`references/eval-checkpoint-template.md`](./references/eval-checkpoint-template.md) — release-facing checkpoint format.
- [`references/metric-taxonomy.md`](./references/metric-taxonomy.md) — quality, safety, provenance, availability, cost, and product metrics.
- [`references/pressure-tests.md`](./references/pressure-tests.md) — scenarios that test whether an agent actually applies the Skill.
- [`references/release-gates.md`](./references/release-gates.md) — hard, quality, and operational release gates.
- [`templates/eval-plan-template.md`](./templates/eval-plan-template.md) — reusable Eval plan.
- [`templates/failure-taxonomy-template.md`](./templates/failure-taxonomy-template.md) — first-failure classification.
- [`templates/provider-call-ledger.schema.json`](./templates/provider-call-ledger.schema.json) — persistent Provider-call ledger schema.

## Examples

- [`examples/rag-eval-example.md`](./examples/rag-eval-example.md)
- [`examples/agent-eval-example.md`](./examples/agent-eval-example.md)
- [`examples/extraction-eval-example.md`](./examples/extraction-eval-example.md)

## Key invariants

- **Production parity over shadow Eval paths.**
- **First failure over final symptom.**
- **Hard gates over misleading averages.**
- **Certified metrics over provisional scores.**
- **Minimal fix over architecture churn.**
- **Replay before full rerun.**
- **Freeze passed layers.**
- If `provider_reached = false`, do not call the result a model semantic failure.
- If run history becomes unverifiable, mark it `INVALID_RUN` instead of guessing.

## Validation

Run:

```bash
python scripts/validate_skill.py
```

Manual pressure-test guidance is in [`tests/skill-pressure-test-checklist.md`](./tests/skill-pressure-test-checklist.md).

## Version

Current Skill release: **v0.1.0**. See [`CHANGELOG.md`](./CHANGELOG.md).

## License and contributions

This Skill is part of the [`ai-agent-skills`](../../) repository and is distributed under the repository-level [Apache-2.0 license](../../LICENSE).

Contribution guidance: [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

---

## 中文说明

这是一个面向**生产级 AI 产品 Eval 体系设计**的通用 Skill。

它不只问“模型准确率是多少”，而是先判断失败到底发生在输入、检索、上下文、契约、模型、权限、溯源、持久化，还是 Eval 工具本身，再决定应该改 Prompt、模型、RAG 还是后端工程边界。
