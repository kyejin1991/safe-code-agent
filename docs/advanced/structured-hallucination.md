# Advanced Note: Structured Hallucination

A detailed report format can make hallucination look more credible.

The goal is not to produce better-looking reports.
The goal is to make evidence easier to inspect.

## Risk

An agent may write:

```text
Verification: Run
Completion: Complete
Evidence: tests passed
```

without actually observing command output.

## Guardrail

For serious work, evidence claims should identify their source:

- Opened file
- Search result
- Command output
- Manual check
- User-provided
- Inferred

Do not treat a formatted report as proof.
Proof requires an observable source.
