# AI Agent Skills

A growing collection of reusable Agent Skills for building, evaluating, and governing production AI systems.

The repository is intentionally organized as a multi-skill library: each skill is self-contained under `skills/<skill-name>/` with its own `SKILL.md`, references, templates, examples, and tests when needed.

## Skills

| Skill | Purpose | Status |
|---|---|---|
| [`building-ai-eval-systems`](./skills/building-ai-eval-systems/) | Design release-grade evaluation systems for RAG, agents, extraction, generation, and multi-stage LLM products. | v0.1.0 |

## Repository principles

- **Reusable over project-specific.** Skills should encode patterns that generalize across products.
- **Small skill core, deeper references.** Keep `SKILL.md` focused; move heavy material into `references/`, `templates/`, or `examples/`.
- **Production-aware.** Skills should respect runtime identity, contracts, side effects, authority boundaries, and release gates.
- **Test the skill itself.** Where behavior matters, include pressure tests or checklists that demonstrate the skill changes agent behavior.
- **No hidden product coupling.** Do not embed private project paths, credentials, customer data, or proprietary identifiers.

## Layout

```text
ai-agent-skills/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
└── skills/
    └── building-ai-eval-systems/
        ├── SKILL.md
        ├── README.md
        ├── references/
        ├── templates/
        ├── examples/
        ├── scripts/
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

Add references, examples, templates, scripts, or tests only when they materially improve reuse or verification. Then add the skill to the table above.

## License

Apache-2.0. See [`LICENSE`](./LICENSE).
