# Scoring Rubric Notes

This project may be compared with other AI coding guidelines, but any score should be described as a practical rubric review, not a benchmark.

## Suggested Criteria

Each criterion can be scored from 1 to 10:

1. Generality
2. Clarity
3. Executability
4. Over-edit prevention
5. Verification discipline
6. Uncertainty handling
7. Complex-task fit
8. Lightweight for small tasks
9. Adoption ease
10. Originality

## Important Disclaimer

These scores are not empirical benchmark results.

A real benchmark would require:

- the same task set
- the same model
- the same repository state
- the same time and token budget
- measured outcomes such as success rate, unnecessary diff size, verification failure rate, and rework rate

Use scoring tables as communication aids, not proof of superiority.


## v0.2.1 note

v0.2.1 adds stability mechanisms for token overhead, prototyping friction, skipped gates, and structured hallucination.

These changes should be evaluated separately from raw scoring because they are primarily risk controls, not performance claims.


## Risk Signal Router note

The Risk Signal Router does not make the core workflow heavier by default.

It is intended to reduce user orchestration burden by letting the agent recommend advanced docs only when specific risk signals appear.
