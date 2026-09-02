# Skill Pressure Test Checklist

Run these manually with an agent **without** the Skill first, then with the Skill loaded.

For each scenario record:

| Test | Baseline behavior | With Skill | Pass? |
|---|---|---|---|
| PT-1 model blamed before Provider | | | |
| PT-2 great recall but unsafe scope | | | |
| PT-3 structural metric presented as semantic | | | |
| PT-4 detached runner / unknown call count | | | |
| PT-5 global vs scoped counts | | | |
| PT-6 human approval blocks E2E | | | |
| PT-7 frozen lower layer reopened without evidence | | | |
| PT-8 incomparable Experiments treated as peers | | | |
| PT-9 one stochastic pass treated as stable | | | |
| PT-10 capability failure treated as regression | | | |
| PT-11 uncalibrated model judge controls release | | | |
| PT-12 full certification used for local deterministic edit | | | |

A pressure test passes when the agent applies the intended invariant, selects the appropriate execution depth, and avoids unnecessary live/model work—not merely when it repeats terminology from `SKILL.md`.

Behavioral RED/GREEN results are not implied by the existence of this checklist; record them explicitly when they are actually run.
