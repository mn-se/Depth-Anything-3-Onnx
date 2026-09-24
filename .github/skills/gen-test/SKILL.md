---

name: gen-test
description: Analyze code changes and generate focused tests for normal behavior, boundaries, invalid inputs, regressions, and important error paths using the project's existing test framework and conventions.
---

# Test Generation Skill

## Objective

Analyze the implementation and generate tests that provide meaningful validation of its behavior.

The goal is to test the behavior that matters rather than maximize the number of test cases or code coverage.

This Skill is language-independent.

Language- and framework-specific test implementation rules are defined in the applicable project instructions, such as:

* `cpp-test.instructions.md`
* `python-test.instructions.md`

Do not duplicate framework-specific coding rules in this Skill.

---

# Workflow

## 1. Understand the Change

Before generating tests:

* Read the task requirements.
* Read the approved implementation plan when available.
* Inspect the changed implementation.
* Inspect surrounding code when necessary.
* Identify the public or externally observable behavior.
* Inspect existing tests.
* Identify the project's existing test framework and conventions.
* Identify relevant test utilities, fixtures, mocks, and helpers.

Do not generate tests based only on function names or signatures.

Understand the actual behavior before deciding what should be tested.

---

# 2. Identify Testable Behavior

Identify the behavior affected by the implementation.

Consider:

* Inputs
* Outputs
* State changes
* Side effects
* Return values
* Error conditions
* Boundary conditions
* External interactions
* Resource behavior
* Timing or ordering requirements when relevant

Focus on observable behavior.

Avoid testing private implementation details unless they are necessary to validate important behavior.

---

# 3. Build a Test Matrix

Before writing tests, determine the relevant scenarios.

Consider the following categories:

| Category    | Purpose                                      |
| ----------- | -------------------------------------------- |
| Normal      | Verify expected behavior                     |
| Boundary    | Verify behavior at important limits          |
| Invalid     | Verify rejection or error handling           |
| Empty       | Verify empty or missing data handling        |
| Regression  | Protect against the reported or fixed defect |
| State       | Verify important state transitions           |
| Error       | Verify failure propagation and recovery      |
| Integration | Verify important component interactions      |

Not every category is required for every change.

Prioritize scenarios based on actual risk.

---

# 4. Normal Cases

Create tests for representative valid inputs.

Verify:

* Expected outputs
* Expected state changes
* Important side effects
* Required interactions

Use a small number of representative cases.

Do not create many nearly identical tests merely to increase test count.

---

# 5. Boundary Cases

Identify meaningful boundaries from:

* Requirements
* Constants
* Valid ranges
* Array or buffer sizes
* Numerical thresholds
* Timeouts
* Resource limits
* State transitions

Test values:

* Just below the boundary when relevant
* At the boundary
* Just above the boundary when relevant

Do not invent arbitrary boundaries that are not supported by the implementation or requirements.

---

# 6. Invalid and Error Cases

Test invalid inputs and important failure paths.

Examples include:

* Null or missing input
* Empty input
* Invalid ranges
* Malformed data
* Unsupported values
* Dependency failures
* Resource failures
* Timeout conditions

Verify the actual expected behavior:

* Error return
* Exception
* Error status
* Fallback
* Rejection
* State preservation

Follow the project's existing error-handling conventions.

Do not introduce new error behavior merely to make a test possible.

---

# 7. Regression Tests

When the task fixes a bug:

* Identify the original failure condition.
* Reproduce it with the smallest useful test case.
* Verify the expected corrected behavior.
* Ensure the test would fail against the previous implementation when practical.

A regression test should protect the actual failure mode rather than only testing a nearby code path.

---

# 8. Test Data

Keep test data:

* Small
* Deterministic
* Understandable
* Representative

Prefer explicit test data when it improves readability.

Avoid unnecessarily large datasets.

For numerical algorithms, choose data that makes the expected behavior clear.

For floating-point calculations, use appropriate tolerances rather than exact equality when exact equality is not guaranteed.

---

# 9. Test Isolation

Tests should be independent and deterministic.

Avoid unnecessary dependence on:

* Test execution order
* Global state
* Current working directory
* Machine-specific paths
* Environment-specific configuration
* Network availability
* External services
* Real hardware

When external dependencies are unavoidable, follow the project's integration or hardware-test conventions.

Do not turn a unit test into an integration test merely to avoid creating a mock or test double.

---

# 10. Mocks and Test Doubles

Use mocks, stubs, or fakes when they provide meaningful isolation.

Use them for external or difficult-to-control dependencies such as:

* Hardware
* Network services
* Filesystem interfaces
* Time
* Randomness
* External processes

Avoid excessive mocking.

Do not mock the component under test.

Prefer testing real behavior when the dependency is simple, deterministic, and inexpensive.

Follow the project's existing mocking framework and conventions.

---

# 11. Existing Tests

Before adding tests:

* Check whether an existing test already covers the behavior.
* Extend an existing test when appropriate.
* Reuse existing fixtures and helpers.
* Avoid duplicate test coverage.
* Preserve existing test organization.

Do not create a new test utility when an appropriate existing utility can be reused.

---

# 12. Test Naming and Organization

Organize tests so that a failing test clearly communicates:

* What behavior is being tested
* Under what condition
* What result is expected

Follow the project's existing naming conventions.

Prefer focused tests over large tests covering many unrelated behaviors.

Keep setup explicit enough that the test intent is easy to understand.

---

# 13. Implement the Tests

After identifying the required scenarios:

* Use the project's existing test framework.
* Follow language-specific test instructions.
* Reuse existing fixtures and utilities.
* Add only the necessary test cases.
* Avoid changing production code solely to make testing convenient unless the design genuinely requires improvement.

Do not modify production behavior while generating tests.

---

# 14. Run and Validate

After implementing tests:

* Build the affected test target.
* Run the new tests.
* Run relevant existing tests.
* Check for deterministic results.
* Review test failures carefully.
* Confirm that tests exercise the intended code path.

When appropriate, run the broader test suite to detect regressions.

Do not claim that tests pass unless they were actually executed.

---

# 15. Evaluate Test Quality

After running the tests, verify that they:

* Test observable behavior.
* Cover the important risk areas.
* Fail for meaningful reasons.
* Do not depend on implementation details unnecessarily.
* Are deterministic.
* Are understandable to another developer.
* Do not duplicate existing coverage unnecessarily.
* Do not contain incorrect assumptions about the implementation.

A test that passes but does not meaningfully validate the changed behavior is not sufficient.

---

# Test Priority

Prioritize tests according to risk.

Prefer:

1. Regression cases for the reported defect
2. Core normal behavior
3. Important boundary conditions
4. Important error paths
5. Significant state transitions
6. Relevant integration behavior
7. Additional low-risk cases

Do not optimize for test count or coverage percentage alone.

---

# Test Generation Output

When planning tests before implementation, summarize the proposed cases.

Example:

```text id="3n8g6s"
Test cases:

1. Normal input
   - Valid input produces the expected result.

2. Lower boundary
   - Minimum supported value is accepted.

3. Invalid input
   - Value below the supported range is rejected.

4. Regression
   - Previously failing input now produces the expected result.

5. Dependency failure
   - Processing failure is propagated without updating the output state.
```

Keep the test plan proportional to the complexity and risk of the change.

---

# Change Discipline

* Test behavior, not implementation details.
* Prefer focused tests.
* Reuse existing test infrastructure.
* Do not introduce unnecessary dependencies.
* Do not create redundant tests.
* Do not modify production behavior merely to simplify testing.
* Do not introduce unrelated refactoring.
* Do not invent requirements or expected results.
* Clearly distinguish expected behavior from assumptions.
* Keep tests deterministic and maintainable.
