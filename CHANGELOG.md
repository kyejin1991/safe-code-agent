# Changelog

## v0.2.1-balanced-router

### Added

- Risk Signal Router in `README.md`, `AGENTS.md`, and `SKILL.md`.
- `docs/advanced/risk-signal-router.md`.
- Clear trigger rules for recommending runtime enforcement, prototype-to-production, and structured hallucination docs.

### Rationale

Balanced-plus made advanced docs optional, but users still had to know when to apply them.

The Risk Signal Router lets the agent detect risk signals and recommend the relevant advanced doc instead of expecting the user to choose manually.


## v0.2.1-balanced-plus

### Added

- Advanced docs trigger table in `README.md`.
- Advanced docs trigger table in `AGENTS.md`.


## v0.2.1-balanced

### Changed

- Kept the main `SKILL.md` based on v0.2.1 instead of expanding it with heavier v0.2.2 rules.
- Moved heavier v0.2.2 ideas into optional `docs/advanced/` notes.
- Clarified that advanced notes should not be loaded by default.
- Preserved the core goal: small tasks stay light, risky tasks become precise, verification stays honest.

### Added

- `docs/advanced/runtime-enforcement.md`
- `docs/advanced/prototype-to-production.md`
- `docs/advanced/structured-hallucination.md`

### Rationale

v0.2.2-style additions were useful as analysis, but too heavy for the default skill.
This balanced package keeps the core workflow practical while retaining advanced guidance as optional documentation.


## v0.2.1

### Added

- Compression Rule to reduce token overhead and avoid applying every section to every task.
- Prototype Mode for exploratory UI, throwaway prototypes, and early idea tests.
- Gate Router Report to make activated and skipped gates visible.
- Required Minimums Report for Full and Critical tasks.
- Evidence Source Labels for evidence claims.
- Stricter Completion Status Rules to prevent partial verification from being reported as complete.

### Changed

- Clarified that v0.2.1 is a stability release, not a heavier workflow.
- Improved guardrails against structured hallucination.
- Made fast prototyping possible without claiming production readiness.


## v0.2.0 - Gate Router and quantified safety rules

Added:

- Instruction Precedence for resolving global-vs-skill conflicts
- Gate Router for activating only the needed gates
- Micro Mode for tiny low-risk changes
- quantified mode limits for Micro, Light, Full, and Critical work
- Assumption Gate
- Simplicity Check
- Design Interrogation Gate
- Contract & Precedence Check
- Negative Case Hygiene
- Verification Budget
- Partial verification label
- Completion Status
- Evidence Report format
- Real-world proof example

Changed:

- The skill now treats small-task lightness and risky-task rigor as separate goals.
- Verification reporting now distinguishes partial verification from completion.
- Contract/fallback/precedence logic has explicit pre-patch checks.

## v0.1.0 - Initial release

Initial public release.

Included:

- Light / Full mode selection
- patch size guidance
- inspection minimums
- evidence discipline
- failure mode minimums
- verification labels
- large task memory rules
- lightweight AGENTS.md defaults
