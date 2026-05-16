# Advanced Note: Runtime Enforcement

Safe Code Agent is a prompt/skill design, not a runtime enforcement system.

It can guide an AI coding agent to behave more carefully, but it cannot prove runtime truth unless the harness provides auditable execution evidence.

## Stronger evidence

- terminal command output
- CI output
- pre-commit output
- test runner output
- build logs
- tool call transcripts
- manual reproduction notes from the user

## Weak evidence

- the agent saying "tests passed" without command output
- a polished report with no observed execution
- inferred behavior from code reading only
- partial inspection presented as full coverage

## Practical rule

Use `Run` only when actual command output is visible.

Use `Manual`, `Inferred`, `Partial`, or `Not run` when runtime evidence is incomplete.
