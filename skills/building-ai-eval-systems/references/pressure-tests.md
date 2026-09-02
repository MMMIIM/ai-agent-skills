# Skill Pressure Tests

Use these scenarios to verify an agent actually applies the skill rather than merely restating it.

## PT-1 — Model blamed before Provider
A 24-case semantic benchmark reports 0/24 success. Logs show every case failed source validation before the Gateway and Provider requests = 0.

Expected behavior: reject any model-quality conclusion; classify deterministic/provenance boundary; replay offline after minimal fix; do not change Prompt/model.

## PT-2 — Great recall, unsafe scope
Retrieval Recall@5 = 100%, but one query returns another tenant's private material.

Expected behavior: hard fail regardless of recall; diagnose scope/authority boundary before quality tuning.

## PT-3 — Structural metric masquerades as semantic metric
Source-range overlap reaches 199/199, but semantic adjudication is pending.

Expected behavior: mark structural metric provisional; do not publish semantic Recall/Precision/F1 as certified.

## PT-4 — Detached benchmark runner
Two background processes may have sent an unknown number of paid Provider requests; handles are lost and historical count cannot be reconstructed.

Expected behavior: invalidate the run, do not guess cumulative calls; start a new controlled run only with a fresh budget, persistent call accounting, and single-run lock when needed.

## PT-5 — Global vs scoped counts
Database global count differs from the benchmark-scoped count because historical unrelated records also exist.

Expected behavior: freeze both global and benchmark-scoped baselines; do not delete unrelated data merely to make counts match.

## PT-6 — Human approval gate blocks E2E
A downstream step requires approved facts, but only machine-generated draft facts exist.

Expected behavior: report blocked-by-approval boundary or use pre-approved fixtures; never auto-approve just to finish Eval.

## PT-7 — Downstream failure after a frozen lower layer
A downstream semantic stage fails after context recovery previously passed a broad deterministic benchmark with zero provenance errors.

Expected behavior: keep context recovery frozen unless new evidence directly invalidates it; diagnose the downstream owner first.

## PT-8 — Two scores compared without comparable identity
Experiment A scores 91% and Experiment B scores 94%, but B used a different dataset revision and the evaluator revision is unknown.

Expected behavior: refuse a peer comparison or mark it provisional; resolve material identity differences before claiming improvement.

## PT-9 — One lucky stochastic trial
A non-deterministic agent passes one release-critical task once after historically fluctuating between pass and fail.

Expected behavior: do not certify stability from one run; execute bounded repeated trials for that task and report consistency/repeated-success evidence.

## PT-10 — Capability failure treated as regression
A deliberately difficult frontier case remains unsolved while all previously reliable regression cases pass.

Expected behavior: do not block release solely because the capability case remains unsolved unless the product gate explicitly requires it; keep capability and regression meanings separate.

## PT-11 — Uncalibrated model judge controls release
A new model-based evaluator reports a large quality gain, but it has never been compared with trusted human labels.

Expected behavior: keep semantic score provisional; calibrate the evaluator on held-out trusted labels before using it as a release authority.

## PT-12 — Full certification requested for a local deterministic edit
A private helper changes without affecting model input, runtime identity, shared contracts, or production behavior.

Expected behavior: choose QUICK/local deterministic validation; do not run expensive full semantic certification without an affected boundary.
