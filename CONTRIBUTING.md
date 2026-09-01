# Contributing

Contributions are welcome when they improve reusable Agent Skills rather than add one-project instructions.

## Add a skill

Create a directory under:

```text
skills/<skill-name>/
```

Every skill must contain `SKILL.md` with valid YAML frontmatter including `name` and `description`.

Prefer:

- project-agnostic triggers and guidance;
- compact `SKILL.md` files;
- detailed material in `references/`;
- reusable templates in `templates/`;
- concrete examples in `examples/`;
- pressure tests/checklists when the skill changes consequential agent behavior.

Avoid:

- secrets, credentials, customer data, local absolute paths, or private identifiers;
- hard-coded dataset counts or model-specific rules unless the skill is explicitly scoped to them;
- duplicating behavior that should be enforced mechanically in code;
- presenting a one-off incident report as a reusable skill.

## Before opening a contribution

1. Verify the skill's trigger conditions are clear.
2. Confirm it does not depend on hidden project context.
3. Check links and referenced files.
4. Run any validation or pressure tests included with the skill.
5. Update the root skills table when adding a new skill.

## License

By contributing, you agree that your contribution is licensed under Apache-2.0.
