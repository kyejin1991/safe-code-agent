# Changelog

## v0.2.0

### Added

- Instruction Precedence: resolves conflicts between global instructions and task-specific skill rules.
- Gate Router: activates only the gates required by the task.
- Micro Mode: for tiny, low-risk edits (1 file, <10 lines).
- Critical Mode: for high-risk changes (auth, schema, payment, etc.).
- Quantified mode limits: numeric boundaries for inspection, verification, and reporting.
- Assumption Gate: separates code-checkable, requirement-dependent, and safety assumptions.
- Simplicity Check: prevents overengineering.
- Design Interrogation Gate: limits blocking questions for design choices.
- Contract & Precedence Check: checks input precedence, fallbacks, and API boundaries.
- Negative Case Hygiene: ensures negative tests prove the intended failure path.
- Verification Budget: manages verification cost vs. time.
- Partial verification label: for honest reporting of incomplete checks.
- Completion Status: distinguishes Complete, Partial, Pending, and Failure.
- Evidence Report: structured summary of verification results.

### Changed

- Clarified the relationship between global defaults and task-specific skill rules.
- Made small tasks lighter through Micro Mode.
- Made risky tasks more explicit through Critical Mode.
- Added numeric limits to prevent the workflow from becoming too heavy.

### Removed

- Demo and proof assets from the clean v0.2 package.
