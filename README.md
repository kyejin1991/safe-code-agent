# Safe Code Agent

> A surgical coding-agent skill for reducing over-editing, context loss, and hallucinated certainty.

Most coding-agent failures come from the same pattern:
- Editing before understanding the goal
- Changing too much code unnecessarily
- Assuming the root cause without evidence
- Skipping code inspection
- Hiding uncertainty or false positives in testing

**Safe Code Agent** enforces a simple, robust loop:
`Goal` → `Inspect` → `Simulate` → `Patch Minimally` → `Verify` → `Report Uncertainty`

---

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

## 🛠️ Quick Start

1. **Install Skill**: Copy `skills/safe-code-agent/SKILL.md` into your agent's skills directory.
2. **Global Rules (Optional)**: Copy `AGENTS.md` into your project root for lightweight global defaults.

## ⚖️ License

MIT License - Copyright (c) 2026 kyejin1991
