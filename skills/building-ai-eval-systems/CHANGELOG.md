# Changelog

All notable changes to this project are documented here.

## [0.2.0] - 2026-09-02

### Added

- Experiment as the canonical comparable Eval run unit.
- Task/Trial separation for non-deterministic systems with selective repeated-trial guidance.
- Capability vs Regression suite semantics and explicit graduation guidance.
- Model-evaluator calibration against held-out trusted human labels.
- `QUICK`, `TARGETED`, and `CERTIFICATION` execution modes for cost-aware evaluation depth.
- Generic Experiment, Suite, and Case Result JSON Schemas.
- Experiment-system reference covering baseline comparison, legacy-runner adapters, persistence, and cost control.
- Evaluator-calibration reference covering disagreement, calibration metrics, and revalidation triggers.
- Online-Eval reference for privacy-safe production sampling and regression feedback.
- Pressure tests for Experiment comparability, stochastic stability, suite semantics, evaluator calibration, and over-testing.
- Core-Skill size validation and JSON validation across all template schemas.

### Changed

- `SKILL.md` remains compact and framework-agnostic while adding the new Experiment-system invariants.
- README now documents progressive disclosure for Experiment, evaluator-calibration, and online-Eval depth.
- Minimum run artifact is now a minimum Experiment artifact with baseline and trial context when applicable.

### Validation status

- Structural/static validation is supported by `scripts/validate_skill.py`.
- Behavioral RED/GREEN pressure-test results are still not claimed until they are explicitly executed and recorded.

## [0.1.0] - 2026-09-01

### Added

- Initial `building-ai-eval-systems` Agent Skill.
- Bottom-up Eval workflow from deterministic gates to semantic and E2E quality.
- First-failure attribution taxonomy.
- Hard-gate vs quality-target model.
- Eval run identity and certification states.
- Provider-call budget, persistent ledger, and detached-run invalidation guidance.
- RAG, tool-using Agent, and structured extraction examples.
- Eval plan, checkpoint, failure-taxonomy, and call-ledger templates.
- Pressure-test checklist for evolving the Skill safely.
