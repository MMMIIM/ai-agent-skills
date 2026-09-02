# AI Agent Skills

A growing collection of reusable Agent Skills for building, evaluating, and governing production AI systems.

The repository is intentionally organized as a multi-skill library: each skill is self-contained under `skills/<skill-name>/` with its own `SKILL.md`, references, templates, examples, and tests when needed.

## How skill triggering works

These skills are designed for **on-demand discovery**, not continuous execution.

Installing a skill does **not** mean every task should load or run it. The agent/runtime should first compare the current task with the skill's `description` trigger. Only a matching task should load the full `SKILL.md`; deeper references should be opened only when the compact skill says they are needed.

```text
current task
   ↓
match a skill description?
   ├─ no  → normal work; zero skill overhead
   └─ yes → load SKILL.md
               ↓
          need deeper guidance?
               ├─ no  → execute compact rules
               └─ yes → open only relevant reference/template/test
```

This is intentional **progressive disclosure**: keep common development fast and low-token while making specialized governance available at the moment it becomes useful.

Runtime-specific discovery behavior varies. The trigger descriptions in this repository define the intended activation conditions; they are not a requirement to preload every skill into every task.

## Skills

| Skill | Purpose | Intended trigger | Status |
|---|---|---|---|
| [`building-ai-eval-systems`](./skills/building-ai-eval-systems/) | Design repeatable Eval/Experiment systems with failure attribution, comparable baselines, cost-aware execution, evaluator calibration, and release gates. | Creating, repairing, comparing, certifying, or diagnosing an AI Eval/benchmark/Experiment system. | v0.2.0 |
| [`preventing-engineering-drift`](./skills/preventing-engineering-drift/) | Prevent definition, authority, identity, parity, compatibility, and execution-path drift without supervising ordinary local work. | Shared concepts/contracts/runtimes/evals/migrations or equivalent paths may diverge. GREEN local work should skip it. | v0.1.0 |

## Repository principles

- **On-demand over always-on.** Load a skill only when its trigger matches the current task.
- **Reusable over project-specific.** Skills should encode patterns that generalize across products.
- **Small skill core, deeper references.** Keep `SKILL.md` focused; move heavy material into `references/`, `templates/`, or `examples/`.
- **Progressive disclosure.** References are optional depth, not mandatory context for ordinary use.
- **Production-aware.** Skills should respect runtime identity, contracts, side effects, authority boundaries, experiment comparability, and release gates.
- **Cost-aware.** Use the cheapest valid evaluation depth; do not turn every local change into a full live certification run.
- **Test the skill itself.** Where behavior matters, include pressure tests or checklists that demonstrate the skill changes agent behavior.
- **No hidden product coupling.** Do not embed private project paths, credentials, customer data, or proprietary identifiers.

## Layout

```text
ai-agent-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── skills/
    ├── building-ai-eval-systems/
    │   ├── SKILL.md
    │   ├── README.md
    │   ├── references/
    │   ├── templates/
    │   ├── examples/
    │   ├── scripts/
    │   └── tests/
    └── preventing-engineering-drift/
        ├── SKILL.md
        ├── README.md
        ├── references/
        └── tests/
```

## Using a skill

Copy or symlink the individual skill directory into the skill location supported by your agent runtime. A common cross-runtime convention is:

```text
~/.agents/skills/<skill-name>/
```

Runtime discovery rules vary, so verify the conventions of the coding agent you use.

## Adding another skill

Create a new self-contained directory:

```text
skills/<new-skill-name>/
└── SKILL.md
```

The frontmatter `description` should describe **when to use the skill**, not summarize its workflow. Keep the core compact and place optional depth in supporting files. Then add the skill and its intended trigger to the table above.

## License

Apache-2.0. See [`LICENSE`](./LICENSE).
