# Advanced Note: Risk Signal Router

The user should not need to manually decide which advanced doc to load.

The agent should watch for risk signals and recommend the relevant advanced doc only when needed.

## Runtime enforcement signals

Recommend `docs/advanced/runtime-enforcement.md` when:

- the agent claims tests/build/lint/commands passed but visible output is missing
- correctness depends on actual command output, CI, tool logs, or terminal output
- the work touches auth, payment, data deletion, migration, persistence, public API, or security-sensitive behavior

## Prototype-to-production signals

Recommend `docs/advanced/prototype-to-production.md` when:

- prototype work grows beyond 3 files
- prototype work grows beyond about 120 changed lines
- exploratory code starts touching core logic
- prototype code becomes a dependency for future work
- the user wants to ship, reuse, merge, or stabilize prototype code

## Structured hallucination signals

Recommend `docs/advanced/structured-hallucination.md` when:

- the final report looks polished but evidence is unclear
- claims use words like verified, safe, passed, complete, no regression, or fully tested without visible evidence
- evidence is mostly inferred
- report format is detailed but source labels are missing

## Recommendation format

```text
Risk signal detected: [reason]
Recommended advanced doc: [doc]
Apply it now?
```

## Rules

- Recommend one advanced doc at a time.
- For Critical tasks, recommend up to two advanced docs.
- Do not load all advanced docs by default.
- If the core skill is enough, do not escalate.
