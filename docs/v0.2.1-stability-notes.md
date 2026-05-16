# v0.2.1 Stability Notes

v0.2.1 addresses the main risks introduced by making Safe Code Agent more detailed.

## Problems addressed

1. Token and context overhead
2. Friction during rapid prototyping
3. Skipped or forgotten gates
4. Structured hallucination in polished reports
5. Partial verification being reported as complete

## Design response

- Use the Compression Rule so only triggered sections are applied.
- Use Prototype Mode for exploratory work.
- Require Gate Router Report for non-trivial tasks.
- Require Evidence Source Labels for evidence claims.
- Use stricter Completion Status Rules.

## Important note

This is still a prompt/skill design, not a benchmark or a runtime enforcement system.

It can reduce bad behavior, but it cannot guarantee correctness.
Always review generated code and run appropriate tests.
