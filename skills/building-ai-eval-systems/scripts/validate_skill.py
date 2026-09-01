#!/usr/bin/env python3
"""Stdlib-only validation for the building-ai-eval-systems skill."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

REQUIRED = [
    "README.md",
    "SKILL.md",
    "CHANGELOG.md",
    "references/eval-checkpoint-template.md",
    "references/metric-taxonomy.md",
    "references/pressure-tests.md",
    "references/release-gates.md",
    "templates/eval-plan-template.md",
    "templates/failure-taxonomy-template.md",
    "templates/provider-call-ledger.schema.json",
    "examples/rag-eval-example.md",
    "examples/agent-eval-example.md",
    "examples/extraction-eval-example.md",
]

PROJECT_SPECIFIC_PATTERNS = [
    r"V43_",
    r"COM-04",
    r"GOV-02",
    r"EvidenceSourceFactService",
    r"requirement_evidence",
    r"[A-Za-z]:\\",
]


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def validate_structure() -> None:
    missing = [rel for rel in REQUIRED if not (ROOT / rel).is_file()]
    if missing:
        fail("missing required skill files: " + ", ".join(missing))


def validate_frontmatter() -> None:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
    front = text[4:end]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if not name or not desc:
        fail("frontmatter requires name and description")
    if not re.fullmatch(r"[A-Za-z0-9-]+", name.group(1).strip()):
        fail("skill name must contain only letters, digits, and hyphens")
    description = desc.group(1).strip()
    if not description.startswith("Use when"):
        fail("description should start with 'Use when'")
    if len(description) > 500:
        fail("description should remain concise (<=500 chars)")


def validate_json() -> None:
    path = ROOT / "templates/provider-call-ledger.schema.json"
    json.loads(path.read_text(encoding="utf-8"))


def validate_generic_content() -> None:
    text_files = list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.json"))
    violations: list[str] = []
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        for pattern in PROJECT_SPECIFIC_PATTERNS:
            if re.search(pattern, text, re.I):
                violations.append(f"{path.relative_to(ROOT)} matches {pattern}")
    if violations:
        fail("project-specific leakage detected: " + "; ".join(violations))


def main() -> None:
    validate_structure()
    validate_frontmatter()
    validate_json()
    validate_generic_content()
    print("PASS: skill structure, frontmatter, JSON, and generic-content checks")


if __name__ == "__main__":
    main()
