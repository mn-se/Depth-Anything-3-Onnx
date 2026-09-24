---

name: debugging
description: Systematically reproduce, isolate, diagnose, fix, and validate software defects using evidence-driven debugging.
---

# Debugging Skill

## Objective

Diagnose and resolve software defects systematically.

The debugging process should be evidence-driven:

1. Reproduce the problem
2. Observe and characterize the failure
3. Narrow the failure scope
4. Form a hypothesis
5. Verify the hypothesis
6. Implement the smallest appropriate fix
7. Validate the fix
8. Check for regression

Do not modify code simply to see whether the problem disappears.

Do not treat an unverified hypothesis as a root cause.

---

# Workflow

## 1. Understand the Problem

Before changing code:

* Read the user's description of the failure.
* Identify the expected behavior.
* Identify the actual behavior.
* Determine the affected component, feature, or execution path.
* Check whether the problem is deterministic or intermittent.
* Identify relevant inputs, configuration, environment, platform, and dependencies.

Distinguish clearly between:

* Observed facts
* User-reported symptoms
* Assumptions
* Hypotheses
* Verified root causes

Do not invent missing information.

If the reported behavior is ambiguous and the ambiguity materially affects diagnosis, ask for the missing information.

---

## 2. Reproduce

Attempt to reproduce the failure using the smallest practical reproduction.

Check:

* Exact command or operation
* Input data
* Configuration
* Build configuration
* Runtime environment
* Relevant logs
* Error messages
* Stack traces
* Return values
* Assertions
* Exit codes
* Timing or ordering when relevant

Prefer a minimal reproduction over a large end-to-end execution when possible.

If the failure cannot be reproduced:

* Do not claim that the bug is confirmed.
* Identify what was actually verified.
* Use available evidence to narrow possible causes.
* Consider adding targeted diagnostics when appropriate.

---

## 3. Inspect the Relevant Code

Trace the execution path related to the failure.

Inspect:

* Entry point
* Callers and callees
* Relevant state changes
* Input validation
* Error handling
* Data ownership and lifetime
* Threading or synchronization
* Resource management
* Configuration
* External interfaces
* Recent changes
* Related tests

Do not inspect or modify unrelated code unless evidence indicates that it may contribute to the failure.

---

## 4. Narrow the Failure

Reduce the possible cause systematically.

Use appropriate techniques such as:

* Logging
* Assertions
* Return-value checks
* State inspection
* Breakpoints
* Watchpoints
* Stack traces
* Sanitizers
* Static analysis
* Unit tests
* Targeted experiments
* Git history or diff inspection
* Input reduction
* Configuration comparison

For each diagnostic step:

* State what is being tested.
* Explain what result would support or reject the hypothesis.
* Use the result to update the diagnosis.

Avoid adding permanent diagnostic code unless it provides lasting value.

---

## 5. Form and Verify Hypotheses

Create one or more concrete hypotheses based on evidence.

A useful hypothesis should identify:

* Suspected cause
* Relevant code or condition
* Evidence supporting it
* Evidence that would disprove it
* Verification method

Example:

> Hypothesis: the output becomes invalid because an empty input bypasses validation and reaches the processing stage.

Then perform a targeted check rather than immediately changing the implementation.

Do not make multiple unrelated changes before verifying the suspected cause.

---

# 6. Implement the Fix

Once the cause has been sufficiently verified:

* Fix the root cause rather than only the visible symptom.
* Make the smallest change that addresses the defect.
* Preserve existing behavior outside the affected case.
* Reuse existing abstractions and utilities.
* Avoid unrelated refactoring.
* Avoid speculative hardening unless it is directly relevant.
* Preserve public interfaces unless the defect requires an interface change.

If debugging reveals that the approved design or scope must materially change, follow the planning and approval process defined in AGENTS.md.

---

# 7. Add Regression Coverage

Add or update tests when practical.

A regression test should:

* Reproduce the original failure condition.
* Fail before the fix when practical.
* Pass after the fix.
* Verify observable behavior rather than implementation details.
* Be deterministic.
* Be as small as practical.

Consider additional tests for:

* Boundary conditions
* Invalid inputs
* Empty inputs
* Related failure modes
* Previously supported behavior

Use the project's established test framework and conventions.

---

# 8. Validate

After fixing the defect:

* Reproduce the original scenario.
* Confirm the original failure no longer occurs.
* Run the relevant regression test.
* Run related tests.
* Build affected components.
* Check compiler warnings/errors where applicable.
* Run broader validation when the change may affect other components.
* Review the final diff.

Do not claim that a test, build, or diagnostic was performed unless it was actually executed.

If the original problem cannot be reproduced after the change, distinguish:

* What was directly verified
* What was inferred
* What remains unverified

---

# Debugging Priorities

When multiple possible causes exist, prioritize:

1. Evidence directly connected to the failure
2. Recent changes affecting the failing path
3. Reproducible conditions
4. Boundary and invalid-input handling
5. Resource/lifetime/concurrency problems
6. Configuration and environment differences
7. Less likely or speculative causes

Do not spend significant effort on speculative causes while simpler explanations remain untested.

---

# Diagnostic Changes

Temporary diagnostics may include:

* Debug logging
* Assertions
* Additional test cases
* Instrumentation
* Debugger breakpoints
* Sanitizer configurations

Keep diagnostic changes focused.

Remove temporary diagnostics that are no longer useful before completing the task unless they provide ongoing diagnostic value.

Do not leave sensitive information in logs.

---
# Debugging Output

When reporting debugging results:

- Clearly distinguish observed facts, verified root causes, hypotheses, fixes, and validation results.
- Report reproduction status.
- Report tests and validation that were actually performed.
- Report remaining uncertainty when relevant.

For non-trivial debugging tasks, structure the report using:

- Symptom
- Reproduction
- Root Cause
- Fix
- Regression Test
- Validation
- Remaining Uncertainty

Keep the report concise and evidence-based.

---

# Change Discipline

* Do not modify unrelated files.
* Do not combine debugging with unrelated cleanup.
* Do not rewrite working code without evidence.
* Do not hide the symptom by suppressing errors or weakening assertions.
* Do not change tests merely to make them pass.
* Do not remove validation because it exposes a failure.
* Do not claim a root cause without sufficient evidence.
* Do not claim a fix is validated unless validation was actually performed.
* Preserve unrelated user changes in the working tree.
