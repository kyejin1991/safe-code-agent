# v0.2.1-balanced-router

This release keeps the core Safe Code Agent workflow lightweight while making advanced docs easier to apply.

## Added

- Risk Signal Router in README.md, AGENTS.md, and SKILL.md
- docs/advanced/risk-signal-router.md
- Trigger rules for recommending:
  - runtime-enforcement.md
  - prototype-to-production.md
  - structured-hallucination.md

## Why

The previous balanced version made advanced docs optional, but users still had to know when to apply them.

This release lets the agent detect risk signals and recommend the relevant advanced doc instead of expecting the user to choose manually.

## Examples

- Missing command output for a claimed test/build pass
  → recommend runtime-enforcement.md

- Prototype code becomes core logic
  → recommend prototype-to-production.md

- Polished report but weak evidence
  → recommend structured-hallucination.md

## Note

This is still a prompt/skill design, not a runtime enforcement system or benchmark result.

The goal is to keep the core workflow lightweight while making risky situations easier to escalate.
