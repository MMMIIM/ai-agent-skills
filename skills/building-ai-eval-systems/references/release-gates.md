# Release Gates

Release gates convert Eval evidence into a product decision.

## Gate types

### Hard gate

Any violation blocks release regardless of average quality.

Typical examples:
- private-data leakage;
- authority/policy bypass;
- wrong critical provenance;
- unauthorized side effects;
- unsupported high-risk facts;
- unexpected persistent mutations.

### Quality gate

Allows a bounded failure rate or threshold.

Examples:
- semantic accuracy >= target;
- recall@K >= target;
- task completion >= target;
- user-rubric score >= target.

### Operational gate

Examples:
- Provider error rate <= target;
- P95 latency <= target;
- cost per task <= target;
- retry rate <= target.

## Gate design checklist

For each gate define:

- owner;
- metric;
- scope;
- threshold;
- severity;
- evidence source;
- certification requirement;
- release consequence.

## Avoid

- allowing an average score to mask a hard safety failure;
- changing a threshold after seeing the current run;
- comparing uncertified and certified runs as peers;
- adding a new gate without a clear product risk it controls.
