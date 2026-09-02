# Online Eval Loop

Use this reference when offline Eval is already reliable and production behavior needs to feed future quality work.

## Purpose

Offline Eval answers whether a known candidate performs well on a governed dataset. Online Eval observes real production behavior and discovers failures or distribution shifts that the offline suite did not anticipate.

They are complementary, not substitutes.

## Loop

```text
production traces / user feedback
→ privacy-safe sampling
→ lightweight online scoring or review
→ confirmed failure / useful example
→ dataset candidate
→ human or governed adjudication when needed
→ regression/capability suite
→ offline Experiment
```

## Sampling

Do not score every production interaction by default. Sample based on product risk and learning value, for example:

- random representative traffic;
- low-confidence or low-score outputs;
- tool/runtime errors;
- user corrections or negative feedback;
- high-value or high-risk workflows;
- novel input clusters or distribution shifts.

Keep sampling rules explicit so observed rates are not misrepresented as population rates.

## Online scorers

Prefer cheap deterministic signals when possible: schema validity, tool success, latency, retries, policy violations, missing citations, or known invariants.

Use model-based online scorers selectively for semantic properties that cannot be checked deterministically. Treat their outputs according to evaluator-calibration evidence.

## Privacy and authority

Production data may contain sensitive information. Apply the product's privacy, retention, tenant-isolation, and access rules before adding traces to Eval artifacts.

Online evaluation must not silently mutate production state, approve content, or bypass existing authority/human-review gates.

## Dataset feedback

A production failure should not automatically become Gold. First preserve the trace and failure context, then decide whether it is:

- a true system failure;
- an infrastructure/availability incident;
- an ambiguous request;
- invalid or adversarial input;
- evaluator error;
- a new capability requirement.

Only after adjudication should the example enter a capability or regression suite.

## Product metrics

Connect system quality to product outcomes when available, such as task completion, user correction rate, human override rate, acceptance/edit rate, time saved, escalation rate, or cost per successful task.

Do not replace technical quality metrics with business metrics; use both to understand whether a technically better system is actually more useful.

## When not to build this yet

Stay offline-first when the product has little real traffic, privacy/observability foundations are missing, or the current bottleneck is still deterministic correctness. A production dashboard is not a prerequisite for a sound Eval system.
