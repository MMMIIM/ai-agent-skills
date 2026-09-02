# Building AI Eval Systems

> **Evaluate the system, not just the model.**

A reusable Agent Skill and practical framework for designing evaluation and Experiment systems for production AI products: RAG, tool-using agents, structured extraction, classification, generation, and multi-stage LLM pipelines.

## Trigger model

This is an **on-demand Eval skill**, not a permanent project rule.

Use it when the current task is about creating, repairing, comparing, certifying, or diagnosing an AI evaluation system—for example benchmark design, fixture design, Experiment comparison, release gates, metric interpretation, first-failure attribution, production/eval parity, evaluator calibration, or regression strategy.

Do **not** load it for ordinary feature development, UI work, local refactors, or unrelated bug fixes just because the repository happens to contain AI components.

```text
ordinary development
→ do not load this skill

Eval / benchmark / Experiment / release-quality task
→ load SKILL.md
→ use only the references/templates needed for that task
```

The `SKILL.md` frontmatter description is the discovery trigger. Supporting references, templates, examples, and pressure tests are progressive disclosure and should not be preloaded by default.

## What changed in v0.2

The Skill now treats **Experiment** as the comparable run unit rather than accumulating disconnected score files.

It also formalizes:

- Task vs Trial for non-deterministic systems;
- Capability vs Regression suites;
- model-evaluator calibration against trusted human labels;
- `QUICK` / `TARGETED` / `CERTIFICATION` execution modes;
- offline-to-online Eval feedback as an optional production maturity layer.

These additions remain framework-agnostic. They do not require a hosted Eval platform, database, specific model provider, or product domain.

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
- Was Eval input equivalent to production input?
- Did a deterministic contract, authority rule, or provenance check fail first?
- Is the metric structural, semantic, or release-certified?
- Are two Experiments actually comparable?
- Is a stochastic task stable across the number of trials its risk justifies?
- Is the evaluator itself calibrated well enough for the decision?

## Core workflow

```text
Map production
→ freeze Eval identity
→ prove production parity
→ choose cheapest valid execution mode
→ test deterministic boundaries
→ test semantic behavior
→ capture first failure
→ compare Experiment with baseline
→ diagnose one root cause
→ minimal fix
→ offline replay / affected regression
→ freeze or certify passed capability
```

See [`SKILL.md`](./SKILL.md) for the compact agent-facing rules.

## Included material

Core references:

- [`references/experiment-system.md`](./references/experiment-system.md) — Experiment, Task/Trial, suite, baseline, comparison, cost control, and legacy-runner adaptation.
- [`references/evaluator-calibration.md`](./references/evaluator-calibration.md) — model-grader calibration against trusted labels and revalidation triggers.
- [`references/online-eval-loop.md`](./references/online-eval-loop.md) — optional production sampling and offline-regression feedback loop.
- [`references/eval-checkpoint-template.md`](./references/eval-checkpoint-template.md) — release-facing checkpoint format.
- [`references/metric-taxonomy.md`](./references/metric-taxonomy.md) — quality, safety, provenance, availability, cost, and product metrics.
- [`references/release-gates.md`](./references/release-gates.md) — hard, quality, and operational release gates.
- [`references/pressure-tests.md`](./references/pressure-tests.md) — scenarios that test whether an agent actually applies the Skill.

Machine-readable templates:

- [`templates/experiment.schema.json`](./templates/experiment.schema.json)
- [`templates/suite.schema.json`](./templates/suite.schema.json)
- [`templates/case-result.schema.json`](./templates/case-result.schema.json)
- [`templates/provider-call-ledger.schema.json`](./templates/provider-call-ledger.schema.json)
- [`templates/eval-plan-template.md`](./templates/eval-plan-template.md)
- [`templates/failure-taxonomy-template.md`](./templates/failure-taxonomy-template.md)

Examples:

- [`examples/rag-eval-example.md`](./examples/rag-eval-example.md)
- [`examples/agent-eval-example.md`](./examples/agent-eval-example.md)
- [`examples/extraction-eval-example.md`](./examples/extraction-eval-example.md)

## Key invariants

- **Production parity over shadow Eval paths.**
- **First failure over final symptom.**
- **Hard gates over misleading averages.**
- **Experiments over disconnected score files.**
- **Task/Trial separation where non-determinism matters.**
- **Capability and Regression have different meanings.**
- **Evaluators need calibration evidence.**
- **Cheapest valid execution mode over reflexive full reruns.**
- **Certified metrics over provisional scores.**
- **Minimal fix over architecture churn.**
- If `provider_reached = false`, do not call the result a model semantic failure.
- If run history becomes unverifiable, mark it `INVALID_RUN` instead of guessing.

## Validation

Run:

```bash
python scripts/validate_skill.py
```

The validator checks required assets, frontmatter, JSON syntax, a maximum core-Skill size, and known project-specific leakage patterns.

Manual pressure-test guidance is in [`tests/skill-pressure-test-checklist.md`](./tests/skill-pressure-test-checklist.md). The repository does **not** claim behavioral RED/GREEN pressure-test completion unless actual results are recorded there or in a future test artifact.

## Version

Current Skill release: **v0.2.0**. See [`CHANGELOG.md`](./CHANGELOG.md).

## License and contributions

This Skill is part of the [`ai-agent-skills`](../../) repository and is distributed under the repository-level [Apache-2.0 license](../../LICENSE).

Contribution guidance: [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

---

## 中文说明

这是一个面向**生产级 AI 产品 Eval / Experiment 体系设计**的按需通用 Skill。

它不绑定具体业务、模型或 Eval 平台。只有在“建立 Eval、设计 benchmark、比较 Experiment、诊断评测失败、校准 Judge、做 release/freeze 认证”等任务出现时才应加载；普通开发不需要读取它。

核心目标是先证明评测对象与评测过程可信，再判断模型或系统质量，并用最小必要成本完成诊断、比较、回归和发布决策。
