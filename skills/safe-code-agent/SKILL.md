---
name: safe-code-agent
description: A coding skill for complex coding tasks such as debugging, multi-file changes, refactors, architecture-sensitive work, unclear root causes, and high-risk changes. Use it to reduce over-editing, context loss, hallucinated certainty, and unverified changes.
---

# safe-code-agent

## Core Loop

Goal -> Inspect -> Simulate -> Patch minimally -> Verify -> Report uncertainty

## Mode Selection

Use these thresholds as defaults, not hard limits.

Escalate to Full Mode when risk is high even if the patch is small.

De-escalate to Light Mode when the change is mechanical, local, and low-risk.

### Light Mode

Use Light Mode when all are true:

- expected change is 1 file
- expected patch is under 30 changed lines
- root cause or requested change is obvious
- no public API, schema, auth, payment, security, async, concurrency, migration, or cross-module behavior is touched
- verification can be handled with 1 focused test, typecheck, lint, or manual scenario

### Full Mode

Use Full Mode when any are true:

- 2 or more files may change
- expected patch is 30+ changed lines
- root cause is unclear
- behavior crosses module boundaries
- tests need to be added or updated
- public API, schema, auth, payment, security, async, concurrency, migration, or cross-module behavior is touched
- rollback or data-loss risk exists

## Patch Size Guidance

Use these size labels as default estimates:

- Tiny: 1 file and under 10 changed lines
- Small: 1 file and 10-30 changed lines
- Medium: 2-4 files or 30-120 changed lines
- Large: 5+ files or 120+ changed lines

Risk overrides size.

Small changes can require Full Mode when they touch high-risk behavior.

Large mechanical changes can use Light Mode only when they are local, repetitive, and low-risk.

## Rules

- Understand the requested behavior before editing.
- Inspect relevant code before asking when the answer is in the codebase.
- Prefer the smallest safe change.
- Every changed line should directly support the requested behavior or verification.
- Preserve local conventions, naming, structure, and architecture.
- Simulate the execution path before patching.
- Check failure modes, edge cases, regressions, and counterexamples.
- Avoid unrelated features, abstractions, rewrites, and refactors.
- Verify before claiming the task is complete.
- State remaining uncertainty instead of pretending everything is proven.

## Inspection Minimums

Before patching, inspect at least:

- the file to be changed
- the direct caller or direct callee when behavior crosses a function boundary
- the nearest related test file if one exists
- the error source when debugging

For Full Mode, inspect at least 2 relationship points when available:

- caller
- callee
- test
- config
- schema
- route
- API boundary
- state owner

If inspection is partial, state the inspected scope.

## Evidence Discipline

- Do not claim to have inspected code unless relevant files were actually opened or searched.
- Treat bug causes as hypotheses until supported by code, tests, logs, or reproduction.
- Distinguish inferred execution paths from verified runtime behavior.
- Treat relevant files as known relevant files unless the search scope was comprehensive.
- Do not claim there are no failure modes or counterexamples; state only what was checked.
- Report verification as one of: Run, Manual, Not run, or Inferred.

## Process

1. Confirm requested behavior vs current behavior.
2. Find known relevant files, dependencies, and data flow.
3. Identify the core issue or implementation goal.
4. Simulate the execution path.
5. Check failure modes and counterexamples.
6. Choose the smallest safe change.
7. Add or update tests when appropriate.
8. Patch.
9. Verify.
10. Report the result and remaining uncertainty.

## Failure Mode Minimums

For Light Mode, check at least 1 relevant failure mode if the change affects behavior.

For Full Mode, check at least 3 relevant failure modes.

Prefer failure modes from this list:

- invalid input
- empty/null state
- permission or auth boundary
- async/race condition
- backward compatibility
- performance degradation
- nearby behavior regression
- data loss or rollback risk
- public API compatibility
- configuration or environment mismatch

## Verification Minimums

For Tiny changes:

- 1 focused manual check or Inferred verification is acceptable
- label verification as Manual or Inferred

For Small changes:

- run 1 nearby test, typecheck, lint, or manual scenario when available
- if not run, label as Not run or Inferred

For Medium changes:

- run at least 1 targeted test or typecheck/build when available
- if not run, state the exact command that should be run next

For Large or high-risk changes:

- run targeted tests plus typecheck/build when available
- if not run, label as Not run and state exact commands to run next

Verification labels:

- Run: command or automated check was executed
- Manual: manual scenario or reproduction step was checked
- Not run: verification could not be executed; explain why and what should run next
- Inferred: reasoned from code or context only; not runtime-verified

Do not claim the task is complete unless verification was performed or remaining uncertainty is explicitly stated.

## Large Task Memory

For large tasks, preserve:

- goal
- success criteria
- known relevant files
- inferred or verified execution path
- decisions made and why
- changed files
- verification results
- remaining risks
- next action

When context grows:

1. Drop discarded hypotheses first.
2. Summarize files by responsibility.
3. Preserve decisions, changed files, tests, risks, and next action.

## Output

Small tasks:

- direct answer
- minimal explanation
- essential verification only

Medium tasks:

- brief plan
- change summary
- verification

Large tasks:

- goal
- findings
- plan
- risks
- verification

Debugging:

- likely cause
- evidence
- fix
- verification

## Optional

Use subagents only when explicitly requested and clearly beneficial.
