# Safe Code Agent Defaults

Use these defaults for coding work.

## Core Rules

- Understand the requested behavior before editing.
- Inspect relevant code before asking when the answer is in the codebase.
- Prefer the smallest safe change.
- Every changed line should directly support the requested behavior or verification.
- Preserve local conventions, naming, structure, and architecture.
- Avoid unrelated features, abstractions, rewrites, and refactors.
- Verify before claiming the task is complete.
- State remaining uncertainty instead of pretending everything is proven.

## Mode Defaults

Use a light process for simple, local, low-risk changes.

Use the full `safe-code-agent` skill for:

- debugging
- 2+ file changes
- 30+ changed lines
- unclear root causes
- architecture-sensitive work
- performance/security-sensitive changes
- public API, schema, auth, payment, async, concurrency, migration, or cross-module behavior
- rollback or data-loss risk

## Verification Labels

Report verification as one of:

- Run: command or automated check was executed
- Manual: manual scenario or reproduction step was checked
- Not run: verification could not be executed; explain why and what should run next
- Inferred: reasoned from code or context only; not runtime-verified
