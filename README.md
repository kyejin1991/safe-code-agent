# Safe Code Agent v0.2

A coding-agent skill for reducing over-editing, context loss, hallucinated certainty, and unverified code changes.

Safe Code Agent is not a magic safety system. It is a practical workflow that makes AI coding agents inspect first, patch less, verify honestly, and report uncertainty.

## What changed in v0.2

v0.2 keeps the original safety loop, but adds mode selection, gate routing, quantified limits, and completion states.

The goal is not to make every task heavier.

The goal is:
- small tasks stay light
- risky tasks become precise
- verification stays honest
- assumptions do not become facts
- partial verification is not reported as complete

## Core Loop

Goal -> Inspect -> Simulate -> Patch minimally -> Verify -> Report uncertainty

## v0.2 Additions

- **Instruction Precedence**: Resolves conflicts between global instructions and task-specific skill rules.
- **Gate Router**: Activates only the gates required by the task.
- **Micro Mode**: Keeps tiny, low-risk edits lightweight.
- **Assumption Gate**: Separates code-checkable assumptions, requirement-dependent assumptions, and safety defaults.
- **Simplicity Check**: Prevents overengineering without breaking behavior contracts.
- **Design Interrogation Gate**: Asks at most one blocking question for costly or ambiguous design decisions.
- **Contract & Precedence Check**: Checks explicit input, config, env, persisted state, defaults, invalid vs missing behavior, and fallback risk.
- **Negative Case Hygiene**: Makes negative tests prove the intended failure path.
- **Verification Budget**: Avoids jumping straight to expensive full-suite checks while still reporting partial verification honestly.
- **Completion Status**: Distinguishes Complete, partially verified, verification pending, and not complete.
- **Evidence Report**: Provides a structured summary of what was actually checked.

## Mode Summary

| Mode | Use for | Default limits |
|---|---|---|
| Micro | tiny, obvious, low-risk edits | 1 file, under 10 changed lines |
| Light | small local changes | 1 file, under 30 changed lines |
| Full | unclear, multi-file, or verification-sensitive work | 2-4 files or 30-120 changed lines |
| Critical | auth, schema, payment, data loss, security, migration, public API, concurrency | risk-based, regardless of size |

## Verification Labels

- **Run**: command or automated check was executed.
- **Manual**: manual scenario or reproduction step was checked.
- **Not run**: verification could not be executed; explain why and what should run next.
- **Inferred**: reasoned from code or context only; not runtime-verified.
- **Partial**: some checks passed, but required full/negative/contract checks remain.

## Completion Status

- **Complete**: required verification passed.
- **Implemented, partially verified**: targeted checks passed but required full/negative/contract checks remain.
- **Implemented, verification pending**: code changed but verification was not run or was interrupted.
- **Not complete**: core verification failed or the cause remains unresolved.

## Install

Copy the skill file into your agent skills directory:

`skills/safe-code-agent/SKILL.md`

For lightweight project-wide defaults, copy:

`AGENTS.md`

## Repository Structure

```text
safe-code-agent/
├─ README.md
├─ AGENTS.md
├─ CHANGELOG.md
├─ LICENSE
├─ docs/
│  └─ scoring-rubric.md
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

## Best for

- unclear root-cause debugging
- multi-file changes
- risky edits
- verification-sensitive work

## Not for

- trivial syntax questions
- formatting-only edits

## Notes

### A Practical Reality Check
Safe Code Agent is not "magic that makes AI fail less," but a safe workflow that exposes AI errors quickly and fixes them based on evidence. It excels at minimal patching and rigorous re-verification, though it still requires human judgment for high-level design and complex verification strategies.

See the [Full Retrospective & Demo](./docs/retrospective.md) for details.

---

Always review generated code and run your own tests. This is a prompt/skill design, not a benchmark result.

## License

MIT License - Copyright (c) 2026 kyejin1991
