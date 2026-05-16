# Safe Code Agent Defaults

Project-level global defaults. Always-on lightweight rules.

## Instruction Precedence

When global instructions and a task-specific skill conflict:

1. Safety and correctness override speed.
2. Explicit user instructions override default workflow preferences.
3. Task-specific skill rules override global defaults only when the skill is triggered.
4. Global instructions remain active unless the skill explicitly narrows or escalates them.
5. Risk overrides size.
6. Verification status must never be weakened by mode selection or time budget.
7. Do not claim broad certainty from partial inspection or partial verification.

## Global Coding Defaults

- Understand the requested behavior before editing.
- Inspect relevant code before asking when the answer is in the codebase.
- Prefer the smallest safe change.
- Every changed line should directly support the requested behavior or verification.
- Preserve local style, naming, structure, and conventions.
- Avoid unrelated features, abstractions, rewrites, and refactors.
- Do not claim verification unless it was actually run or clearly labeled.
- State remaining uncertainty instead of pretending everything is proven.

## When to use the full safe-code-agent skill

Use `skills/safe-code-agent/SKILL.md` for:
- complex, risky, or unclear tasks
- multi-file changes or architecture-sensitive work
- when root causes are not obvious
- security, auth, schema, or payment related changes

## Verification labels

- Run: command or automated check was executed.
- Manual: manual scenario or reproduction step was checked.
- Not run: verification could not be executed.
- Inferred: reasoned from code or context only.
- Partial: some checks passed, but more are required.

## Completion status

- Complete
- Implemented, partially verified
- Implemented, verification pending
- Not complete
