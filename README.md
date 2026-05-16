# Safe Code Agent v0.2.1-balanced-router

A coding-agent skill for reducing over-editing, context loss, hallucinated certainty, and unverified code changes.

Safe Code Agent is not a magic safety system. It is a practical workflow that makes AI coding agents inspect first, patch less, verify honestly, and report uncertainty.

## Design stance

The core skill is intentionally kept smaller than the advanced notes.

Use the core `SKILL.md` for normal risky coding work.

Use `docs/advanced/` only when you need deeper guidance on runtime enforcement, prototype stabilization, or structured hallucination risks.

## What changed in v0.2.1-balanced-router

v0.2.1 keeps the v0.2 gate-routing model, but adds safeguards against token overhead, workflow friction, skipped gates, and structured hallucination.

The goal is not to make every task heavier.

The goal is:

- small tasks stay light
- risky tasks become precise
- verification stays honest
- assumptions do not become facts
- partial verification is not reported as complete

## Core Loop

```text
Goal -> Inspect -> Simulate -> Patch minimally -> Verify -> Report uncertainty
```

## v0.2.1-balanced-router Additions

- **Instruction Precedence**: resolves conflicts between global instructions and task-specific skill rules.
- **Gate Router**: activates only the gates required by the task.
- **Micro Mode**: keeps tiny, low-risk edits lightweight.
- **Assumption Gate**: separates code-checkable assumptions, requirement-dependent assumptions, and safety defaults.
- **Simplicity Check**: prevents overengineering without breaking behavior contracts.
- **Design Interrogation Gate**: asks at most one blocking question for costly or ambiguous design decisions.
- **Contract & Precedence Check**: checks explicit input, config, env, persisted state, defaults, invalid vs missing behavior, and fallback risk.
- **Negative Case Hygiene**: makes negative tests prove the intended failure path.
- **Verification Budget**: avoids jumping straight to expensive full-suite checks while still reporting partial verification honestly.
- **Completion Status**: distinguishes Complete, partially verified, verification pending, and not complete.

- **Compression Rule**: do not load or apply every section for every task; start with mode selection, gate routing, and triggered gates only.
- **Prototype Mode**: allows exploratory UI, throwaway prototypes, and early idea tests without claiming production readiness.
- **Gate Router Report**: makes the selected mode, activated gates, skipped gates, and reason visible for non-trivial tasks.
- **Required Minimums Report**: reports inspected files, failure modes checked, verification commands, and completion status for Full/Critical tasks.
- **Evidence Source Labels**: every evidence claim must say whether it came from an opened file, search result, command output, manual check, user input, or inference.
- **Stricter Completion Rules**: prevents partial verification from being reported as complete.

## Mode Summary

| Mode | Use for | Default limits |
|---|---|---|
| Micro | tiny, obvious, low-risk edits | 1 file, under 10 changed lines |
| Prototype | exploratory UI, throwaway prototypes, early-stage idea testing | max 3 files, max 120 changed lines, no high-risk behavior |
| Light | small local changes | 1 file, under 30 changed lines |
| Full | unclear, multi-file, or verification-sensitive work | 2-4 files or 30-120 changed lines |
| Critical | auth, schema, payment, data loss, security, migration, public API, concurrency | risk-based, regardless of size |

Risk overrides size.

A 3-line auth change can be Critical.

A 100-line mechanical rename can be Light if it is local, repetitive, and low-risk.

## Verification Labels

- **Run**: command or automated check was executed.
- **Manual**: manual scenario or reproduction step was checked.
- **Not run**: verification could not be executed; explain why and what should run next.
- **Inferred**: reasoned from code or context only; not runtime-verified.
- **Partial**: some checks passed, but required full/negative/contract checks remain.

## Evidence Source Labels

Every evidence claim should use one of these labels:

- **Opened file**: an actual file was inspected.
- **Search result**: a search result was inspected.
- **Command output**: a command was run and output was observed.
- **Manual check**: a manual scenario or reproduction step was checked.
- **User-provided**: the user supplied the evidence.
- **Inferred**: reasoned from code or context only.

Do not use "verified" unless evidence comes from **Command output** or **Manual check**.

## Completion Status

- **Complete**: required verification passed.
- **Implemented, partially verified**: targeted checks passed but required full/negative/contract checks remain.
- **Implemented, verification pending**: code changed but verification was not run or was interrupted.
- **Not complete**: core verification failed or the cause remains unresolved.

## Best for

- unclear root-cause debugging
- multi-file changes
- risky edits
- verification-sensitive work
- contract/fallback/precedence logic
- negative tests or failure-path checks
- AI coding workflows where false confidence is costly

## Not for

This skill is intentionally not optimized for:

- trivial syntax questions
- formatting-only edits
- obvious one-line fixes
- tasks where a direct answer is enough

Use Micro Mode or the lightweight `AGENTS.md` defaults for small tasks.

## Install

Copy the skill file into your agent skills directory:

```text
skills/safe-code-agent/SKILL.md
```

For lightweight project-wide defaults, copy:

```text
AGENTS.md
```

Recommended structure:

```text
your-project/
├─ AGENTS.md
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

## Repository Structure

```text
safe-code-agent/
├─ README.md
├─ AGENTS.md
├─ CHANGELOG.md
├─ LICENSE
├─ docs/
│  ├─ scoring-rubric.md
│  ├─ v0.2.1-stability-notes.md
│  └─ advanced/
│     ├─ prototype-to-production.md
│     ├─ risk-signal-router.md
│     ├─ runtime-enforcement.md
│     └─ structured-hallucination.md
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

## Optional advanced notes

The advanced notes are not part of the default workflow.

They document known limits and deeper operational patterns:

- `docs/advanced/runtime-enforcement.md`
- `docs/advanced/prototype-to-production.md`
- `docs/advanced/structured-hallucination.md`
- `docs/advanced/risk-signal-router.md`

Keep these optional. Loading all of them for every task can make the workflow heavier than necessary.

## When to use advanced docs

The core skill should stay lightweight by default.

Use advanced docs only when the task shows a specific risk signal:

| Situation | Add this doc |
|---|---|
| The agent claims tests/build passed but no output is visible | `docs/advanced/runtime-enforcement.md` |
| Prototype code starts becoming core logic | `docs/advanced/prototype-to-production.md` |
| The final report looks polished but evidence is unclear | `docs/advanced/structured-hallucination.md` |
| Work touches auth, payment, data deletion, migration, public API, or persistence | consider `docs/advanced/runtime-enforcement.md` |

Do not load all advanced docs for every task. They are optional guardrails for higher-risk situations.

## Risk Signal Router

The user should not need to manually decide which advanced doc to use.

During the task, watch for risk signals and recommend the relevant advanced doc only when needed.

| Risk signal | Recommend |
|---|---|
| The agent claims tests, build, lint, or commands passed but visible output is missing | `docs/advanced/runtime-enforcement.md` |
| The task touches auth, payment, data deletion, migration, persistence, public API, or security-sensitive behavior | consider `docs/advanced/runtime-enforcement.md` |
| Prototype work grows beyond 3 files or about 120 changed lines | `docs/advanced/prototype-to-production.md` |
| Exploratory code starts becoming core logic or a dependency for future work | `docs/advanced/prototype-to-production.md` |
| The final report looks polished but evidence is unclear | `docs/advanced/structured-hallucination.md` |
| Claims use words like verified, passed, safe, complete, no regression, or fully tested without visible evidence | `docs/advanced/structured-hallucination.md` |

Recommended message format:

```text
Risk signal detected: [reason]
Recommended advanced doc: [doc]
Apply it now?
```

Router rules:

- Do not load all advanced docs by default.
- Recommend at most 1 advanced doc at a time.
- For Critical tasks, recommend up to 2 advanced docs.
- If the answer can be resolved with the core skill, do not escalate.
- If applying the advanced doc will noticeably slow the task, ask before applying it.

## Notes

This is a prompt/skill design, not a benchmark result.

It is intended to reduce common coding-agent failure modes, but it cannot guarantee correctness. Always review generated code and run your own tests.

## License

MIT License - Copyright (c) 2026 kyejin1991
