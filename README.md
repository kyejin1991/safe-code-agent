# Safe Code Agent

A coding-agent skill for reducing over-editing, context loss, hallucinated certainty, and unverified changes.

Most coding-agent failures come from the same pattern:

- editing before understanding the goal
- changing too much
- assuming the root cause
- skipping code inspection
- claiming tests passed when they did not run
- hiding uncertainty

Safe Code Agent adds a simple loop:

```text
Goal -> Inspect -> Simulate -> Patch minimally -> Verify -> Report uncertainty
```

## Best for

- debugging
- multi-file changes
- refactors
- architecture-sensitive work
- unclear root causes
- performance/security-sensitive changes
- high-risk changes

## What it does

Safe Code Agent makes a coding agent:

- inspect relevant code before patching
- classify small vs full-process work using file and line-count thresholds
- preserve existing conventions and architecture
- avoid unrelated features, abstractions, rewrites, and refactors
- treat bug causes as hypotheses until supported by evidence
- distinguish inferred execution paths from verified runtime behavior
- report verification as `Run`, `Manual`, `Not run`, or `Inferred`
- state remaining uncertainty honestly

## Repository structure

```text
safe-code-agent/
├─ README.md
├─ AGENTS.md
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

## Install

Copy this file into your agent skills directory:

```text
skills/safe-code-agent/SKILL.md
```

Optionally copy `AGENTS.md` into your project root for lightweight global defaults.

## When to use full mode

Use the full process when any of these are true:

- 2 or more files may change
- expected patch is 30+ changed lines
- root cause is unclear
- behavior crosses module boundaries
- tests need to be added or updated
- public API, schema, auth, payment, security, async, concurrency, migration, or cross-module behavior is touched
- rollback or data-loss risk exists

## License

MIT
