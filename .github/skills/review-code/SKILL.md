---

name: review-code
description: Review code changes for correctness, design consistency, regressions, maintainability, error handling, and test coverage against the task requirements and project conventions.
---

# Code Review Skill

## Objective

Review code changes systematically against the task requirements, approved plan, existing architecture, and project conventions.

The goal is to identify meaningful problems before the change is accepted.

This Skill is language-independent.

Language-specific coding rules are defined in the applicable project instructions, such as:

* `cpp.instructions.md`
* `python.instructions.md`
* `cmake.instructions.md`
* Test-specific instructions

Do not duplicate language-specific coding rules in this Skill.

---

# Workflow

## 1. Understand the Change

Before reviewing:

* Read the task requirements.
* Read the approved implementation plan when available.
* Inspect the relevant existing code.
* Inspect the resulting diff.
* Identify affected components and interfaces.
* Inspect relevant tests.
* Identify dependencies and external interfaces affected by the change.

Do not review a change based only on the diff when surrounding code is necessary to understand its behavior.

---

## 2. Check Requirement Compliance

Verify that the implementation:

* Addresses the requested problem.
* Implements the approved approach.
* Preserves required existing behavior.
* Does not omit important requirements.
* Does not introduce behavior outside the intended scope.

If the implementation differs from the approved plan, determine whether the difference is:

* An implementation detail that does not affect the design or scope.
* A necessary correction.
* A significant design or scope change.

A significant design or scope change should be reported explicitly.

---

## 3. Review Correctness

Look for defects that could cause incorrect behavior.

Check:

* Normal execution paths
* Boundary conditions
* Invalid inputs
* Null or missing data
* Empty data
* State transitions
* Error paths
* Resource lifetime
* Initialization and cleanup
* Concurrency where applicable
* Numerical behavior where applicable
* Platform-specific behavior
* Unexpected side effects

Focus on concrete, technically meaningful problems.

Do not report purely theoretical issues without a plausible failure mechanism.

---

## 4. Review Existing Behavior

Determine whether the change unintentionally modifies existing behavior.

Pay particular attention to:

* Public APIs
* Function signatures
* Data formats
* Units
* Coordinate systems
* Default behavior
* Configuration
* Error handling
* Performance-sensitive paths
* Hardware interfaces

When behavior intentionally changes, verify that the change is consistent with the requirements.

---

## 5. Review Design

Check whether the implementation fits the existing architecture.

Consider:

* Separation of responsibilities
* Appropriate abstraction boundaries
* Reuse of existing functionality
* Dependency direction
* Coupling
* Ownership
* Interface stability
* Unnecessary duplication
* Unnecessary abstraction
* Unnecessary refactoring

Prefer the smallest design that correctly solves the problem.

Do not recommend architectural changes merely because another design could be possible.

---

## 6. Review Error Handling

Check whether failures are handled consistently with the existing project.

Look for:

* Ignored errors
* Lost error information
* Incorrect return values
* Missing validation
* Incorrect fallback behavior
* Resource leaks
* Invalid state after failure
* Inconsistent error propagation

Do not introduce a different error-handling model merely for stylistic reasons.

Follow the project's established error-handling mechanism.

---

## 7. Review Performance and Resources

Consider performance when it is relevant to the affected code.

Check for:

* Unnecessary allocations
* Unnecessary copies
* Repeated expensive operations
* Excessive I/O
* Unnecessary synchronization
* Inefficient algorithms
* Excessive memory usage
* Embedded resource constraints

Do not flag minor theoretical optimizations without evidence that they matter.

For performance-sensitive changes, recommend measurement or benchmarking when appropriate rather than assuming a performance impact.

---

## 8. Review Tests

Check whether the change is adequately validated.

Determine:

* Which behavior changed.
* Which existing tests cover it.
* Whether new tests are required.
* Whether boundary and error cases are covered.
* Whether regression tests are appropriate.
* Whether tests are deterministic.
* Whether tests actually exercise the changed behavior.

Do not require tests for changes where testing is genuinely unnecessary.

If tests are missing, explain the behavior that should be tested rather than simply stating "add more tests."

---

## 9. Review Dependencies

Check newly introduced dependencies.

Consider:

* Whether an existing dependency already provides the functionality.
* Whether the dependency is necessary.
* Supported platforms.
* Build-system impact.
* Runtime impact.
* Binary size.
* Licensing requirements when relevant.
* Dependency version constraints.

Do not recommend adding dependencies when existing project functionality is sufficient.

---

## 10. Review Documentation

When behavior, interfaces, configuration, or architecture changes, check whether relevant documentation should also be updated.

Consider:

* API documentation
* Technical documentation
* Configuration documentation
* Build instructions
* Architecture diagrams
* Mermaid diagrams
* README or usage documentation

Do not require documentation changes for purely internal or self-explanatory changes.

---

# Review Priority

Classify findings by practical impact.

## Critical

A problem that can cause:

* Data corruption
* Security vulnerability
* Severe runtime failure
* Irrecoverable system failure
* Serious violation of required behavior

## High

A significant defect that can cause:

* Incorrect results
* Runtime failures
* Important regressions
* Broken interfaces
* Significant resource problems

## Medium

A meaningful issue that should be addressed but does not normally cause immediate system failure.

Examples:

* Missing important validation
* Missing regression coverage
* Maintainability problems likely to cause defects
* Inconsistent behavior

## Low

A minor issue with limited practical impact.

Examples:

* Minor maintainability concerns
* Small clarity issues
* Non-critical documentation gaps

Do not report purely stylistic preferences as review findings unless they violate an explicit project convention.

---

# Review Output

Report findings in priority order.

For each finding include:

1. Priority
2. Location
3. Problem
4. Why it matters
5. Recommended direction

Use the smallest relevant code location.

Example:

```text
[High] src/processor.cpp:142

The failure returned by ProcessInput() is ignored here.

If processing fails, the caller continues using the previous result as if it were valid. This can produce stale output.

Propagate the failure or explicitly invalidate the result before continuing.
```

Do not provide vague findings such as:

> This code could be improved.

Explain the concrete problem and its consequence.

---

# Review Conclusions

After reporting findings, summarize:

* Whether the implementation matches the requested scope.
* Whether significant correctness issues were found.
* Whether tests adequately cover the change.
* Whether there are significant design or maintainability concerns.
* Whether further investigation is required.

Do not give an overall score or arbitrary quality rating.

If no significant issues are found, state that no significant issues were identified based on the reviewed scope and available validation.

Do not claim that the code is bug-free.

---

# Validation

When the environment allows:

* Build the affected targets.
* Run relevant tests.
* Run static analysis or linting when part of the project workflow.
* Inspect the final diff.
* Check generated files and configuration changes.
* Verify that validation results correspond to the reviewed code.

Never claim that a build, test, or analysis was performed unless it was actually executed.

If validation cannot be performed, clearly identify what could not be verified and why.

---

# Change Discipline

* Review the actual change, not hypothetical future code.
* Prioritize correctness and behavioral impact over style.
* Respect the project's existing architecture and conventions.
* Do not recommend unrelated refactoring.
* Do not require unnecessary abstractions.
* Do not duplicate language-specific instructions.
* Do not invent requirements.
* Distinguish confirmed defects from assumptions or suggestions.
* Prefer concrete evidence from the implementation and tests.
* Keep review findings actionable and concise.
