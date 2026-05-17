# Safe Code Agent Defaults v0.2.2

Use these lightweight defaults for all coding work. Keep this file short. Use the full `safe-code-agent` skill only when the task is complex, risky, unclear, or verification-sensitive.

## Instruction Precedence

When global instructions and a task-specific skill conflict:

1. Safety and correctness override speed.
2. Explicit user instructions override default workflow preferences.
3. Task-specific skill rules override global defaults only when the skill is triggered.
4. Global instructions remain active unless the skill explicitly narrows or escalates them.
5. Risk overrides size: small changes can require deeper checks when risk is high.
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

## Pre-Approval Planning

Before asking the user to approve implementation, real execution, broad edits, external effects, or risky actions, provide a compact pre-approval plan.

Include:

- Task Contract: requested behavior, current behavior or failure, success criteria
- Mode and gates: selected mode, activated gates, why the mode is not lighter
- Planned inspection: files, functions, logs, configs, tests, or docs to inspect before patching
- Planned change points: likely files or modules to change and why
- Minimal-change boundary: what will change, what will not change, existing behavior to preserve
- Approval reason: exact action needing approval, why approval is needed, reversibility
- Verification plan: exact commands or manual checks when known, evidence label, stop condition if verification fails

Use this approval format:

```text
Approval needed: <specific action>
Scope: <files/commands/effects>
Risk: <main risk>
Verification after approval: <commands/checks>
Proceed?
```

Do not ask for approval with only a vague plan. Approval does not authorize unrelated refactors, broad cleanup, hidden behavior changes, or weaker verification.

## Trigger the Full Skill

Use `skills/safe-code-agent/SKILL.md` for:

- unclear root causes
- 2+ file changes
- 30+ changed lines
- risky code paths
- public API, schema, auth, permission, payment, persistence, migration, security, async, concurrency, or data-loss behavior
- contract, fallback, configuration, or input-precedence logic
- negative tests or failure-path verification
- long-running or expensive verification

## Verification Labels

Report verification as one of:

- Run: command or automated check was executed.
- Manual: manual scenario or reproduction step was checked.
- Not run: verification could not be executed; explain why and what should run next.
- Inferred: reasoned from code or context only; not runtime-verified.
- Partial: some checks passed, but required full/negative/contract checks remain.

## Lightweight Stability Rules

- Do not load or apply every safe-code-agent section for every task.
- Start with mode selection, then activate only triggered gates.
- For exploratory prototypes, label the result as prototype-only and do not claim production readiness.
- For non-trivial work, report selected mode, activated gates, skipped gates, and why.
- Evidence claims must identify their source: opened file, search result, command output, manual check, user-provided, or inferred.
- Partial verification must not be reported as complete.

## Advanced Notes

Do not load advanced docs by default.

Use advanced docs only when relevant:

- runtime-enforcement: when verification claims require auditable command output
- prototype-to-production: when exploratory code starts becoming production code
- structured-hallucination: when reports look polished but evidence is unclear

## Advanced Docs Trigger Table

Use advanced docs only when a specific risk signal appears:

| Situation | Add this doc |
|---|---|
| Tests/build are claimed as passed but no output is visible | `docs/advanced/runtime-enforcement.md` |
| Prototype code starts becoming core logic | `docs/advanced/prototype-to-production.md` |
| Report looks polished but evidence is unclear | `docs/advanced/structured-hallucination.md` |
| Work touches auth, payment, data deletion, migration, public API, or persistence | consider `docs/advanced/runtime-enforcement.md` |

## Risk Signal Router

The user should not need to know which advanced doc to load.

Watch for risk signals and recommend the relevant advanced doc when needed:

- Missing command output for claimed tests/build/lint/commands -> `docs/advanced/runtime-enforcement.md`
- Auth, payment, data deletion, migration, persistence, public API, or security-sensitive behavior -> consider `docs/advanced/runtime-enforcement.md`
- Prototype code grows beyond 3 files or about 120 changed lines -> `docs/advanced/prototype-to-production.md`
- Prototype code becomes core logic or future dependency -> `docs/advanced/prototype-to-production.md`
- Polished report but weak evidence -> `docs/advanced/structured-hallucination.md`
- Claims like verified, passed, safe, complete, no regression, or fully tested without visible evidence -> `docs/advanced/structured-hallucination.md`

Recommend one advanced doc at a time.

Use this format:

```text
Risk signal detected: [reason]
Recommended advanced doc: [doc]
Apply it now?
```
