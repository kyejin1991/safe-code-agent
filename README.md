# Safe Code Agent

A coding-agent skill for reducing over-editing, context loss, hallucinated certainty, and unverified code changes.

Most AI coding-agent failures are not caused by a lack of code generation ability. 

They usually come from the same pattern:
- Editing before understanding the goal
- Changing too much
- Assuming the root cause
- Skipping code inspection
- Claiming verification without running it
- Hiding uncertainty

Safe Code Agent adds a simple safety loop:
`Goal` → `Inspect` → `Simulate` → `Patch minimally` → `Verify` → `Report uncertainty`

---

## 🚀 Example Behavior

Instead of a generic:
> Fixed the bug. Tests should pass.

**Safe Code Agent** pushes the agent to report:

```text
Likely cause: The input branch was treating an empty value as valid.
Evidence: Checked the validation path in `src/validate.ts` and the related test in `validate.test.ts`.
Fix: Added a minimal guard for empty input.
Verification: Run — `npm test -- validate.test.ts`
Remaining uncertainty: Broader form flows were not tested.
```

---

## 🛠️ Install

Copy the skill file into your agent skills directory:

```text
skills/safe-code-agent/SKILL.md
```

For project-wide defaults, copy `AGENTS.md` into your project root.

**Recommended structure:**
```text
your-project/
├─ AGENTS.md
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

---

## Why?

AI coding agents are fast, but they often fail in predictable ways:
- They over-edit.
- They lose context.
- They infer runtime behavior without evidence.
- They call a guess a root cause.
- They skip verification.
- They say "done" when tests were not run.

This skill gives the agent concrete operating rules for safer code changes.

## 🚀 Key Features

- **Deep Inspection**: Mandates reading relevant code before applying patches.
- **Hypothesis-Driven**: Treats bug causes as hypotheses until proven by evidence.
- **Minimal Patches**: Prefers small, targeted changes over large refactors.
- **Verification First**: Distinguishes between verified runtime behavior and inferred execution.
- **Honest Reporting**: Explicitly states remaining uncertainty after work is done.

## 📂 Repository Structure

```text
safe-code-agent/
├─ README.md
├─ AGENTS.md
├─ LICENSE
└─ skills/
   └─ safe-code-agent/
      └─ SKILL.md
```

## Best for

- debugging
- multi-file changes
- refactors
- architecture-sensitive work
- unclear root causes
- performance or security-sensitive changes
- high-risk code changes

## Not for

This skill is intentionally not optimized for:
- trivial syntax questions
- formatting-only edits
- obvious one-line fixes
- tasks where a direct answer is enough

For small tasks, use the light process only.

## 📝 Notes

This is a prompt/skill design, not a benchmark result.  
It is intended to reduce common coding-agent failure modes, but it cannot guarantee correctness. Always review generated code and run your own tests.

## ⚖️ License

MIT License - Copyright (c) 2026 kyejin1991
