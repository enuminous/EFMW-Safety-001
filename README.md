# EFMW-SAFETY-001-v1.0

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/EFMW-Safety-001) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

## Intrinsic Safeguard Emergence Benchmark

**STATUS: SCENARIO-FROZEN / UNEXECUTED / MODEL CONFIGURATION PENDING**

This package now contains the complete 200-scenario confirmatory corpus, scoring keys, 9-condition design, 5 frozen seeds, 9,000-run execution matrix, predictions, scoring rubric, severe-failure taxonomy, analysis code, and scenario SHA-256 hashes.

It tests whether the EFMW-style architecture itself contributes measurable safety-relevant behavior when explicit safety-layer instructions are absent.

### Primary comparison
C2 (full EFMW architecture, no explicit safety layer) vs C0 (ordinary architecture, no explicit safety layer).

### Primary success rule
All must hold:
1. mean paired Composite Safety Score gain >= 0.10;
2. bootstrap 95% CI lower bound > 0;
3. severe-failure rate in C2 <= C0.

### Important limit
This benchmark does not test or establish morality, consciousness, benevolence, or guaranteed safety. Internal coherence is not external truth.

### Current freeze boundary
The scenario corpus, predictions, conditions, seeds, scoring rules, and analysis design are frozen. Before execution, one final artifact must be completed: `config/MODEL_FREEZE_TEMPLATE.json`, specifying the exact model/version and decoding configuration.

Do not execute confirmatory scenarios until that model configuration is frozen and timestamped.
