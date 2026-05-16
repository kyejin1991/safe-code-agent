# Advanced Note: Prototype to Production

Prototype-style work is useful for speed, but it should not silently become production code.

## Prototype-friendly work

Prototype-like handling is reasonable when:

- the work is exploratory
- changes are local
- no persistent data, auth, payment, schema, migration, or public API behavior is touched
- verification is visual, manual, or inferred
- the result is clearly labeled as prototype-only

## When to stabilize

Run a stabilization pass when prototype code:

- exceeds 3 files
- exceeds about 120 changed lines
- touches core logic
- becomes a dependency for future work
- starts affecting real user data or persistent state

## Stabilization pass

1. Freeze the prototype scope.
2. Identify behavior that must be preserved.
3. Add minimal verification.
4. Remove or label throwaway assumptions.
5. Promote only after Run or Manual verification.
