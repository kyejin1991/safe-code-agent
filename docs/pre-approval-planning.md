# Pre-Approval Planning

Safe Code Agent should not ask the user to approve risky work with only a vague question.

The agent must first explain what approval permits, what it does not permit, and how the result will be verified.

## When to use this

Use this before asking for approval when the next step may:

- edit files
- run real subprocesses
- install packages
- call network services
- commit or push
- delete or move files
- run migrations
- touch persistence
- use secrets
- change public API, auth, payment, security, or data-loss behavior

Also use it for Full Mode and Critical Mode work.

## Required report

Before asking for approval, report:

1. Task Contract
   - requested behavior
   - current behavior or known failure
   - success criteria
2. Mode and gates
   - selected mode
   - activated gates
   - why the mode is not lighter
3. Planned inspection
   - files, functions, logs, configs, tests, or docs to inspect before patching
4. Planned change points
   - likely files or modules to change
   - what each change is expected to do
5. Minimal-change boundary
   - what will change
   - what will not change
   - existing behavior that must be preserved
6. Approval reason
   - exact action needing approval
   - why approval is needed now
   - whether the action is reversible
7. Verification plan
   - exact commands or manual checks when known
   - expected evidence label
   - stop condition if verification fails

## Approval format

```text
Approval needed: <specific action>
Scope: <files/commands/effects>
Risk: <main risk>
Verification after approval: <commands/checks>
Proceed?
```

## Boundary rule

Approval does not authorize unrelated refactors, broad cleanup, hidden behavior changes, or weaker verification.

If new evidence changes the scope after approval, stop and issue a new pre-approval planning report.
