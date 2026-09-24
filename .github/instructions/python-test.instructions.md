---
description: This file describes the Python test code style and development guidelines for the project.
applyTo: "**/tests/**/*.py,**/*/test/**/*.py,**/**test.py,**/test**.py"
---

# Python Test Guidelines

## Test Framework

* Use pytest as the standard Python test framework.
* Follow the version of pytest already used by the project.
* Do not introduce another test framework when pytest can be used.
* Follow the existing project test configuration and conventions.

## Test Design

* Test observable behavior rather than implementation details.
* Keep each test focused on one behavior or scenario.
* Prefer deterministic tests that produce the same result when executed repeatedly.
* Keep tests independent from one another.
* Do not rely on test execution order.
* Cover normal cases, boundary conditions, invalid inputs, and important failure cases.
* Add regression tests for bugs that are likely to recur.

## pytest Conventions

* Use plain `assert` statements for normal assertions.
* Use `pytest.raises()` to verify expected exceptions.
* Use `pytest.approx()` for floating-point comparisons when numerical tolerance is required.
* Use fixtures for shared setup and resources.
* Prefer fixtures over duplicated setup code.
* Use parametrization with `@pytest.mark.parametrize` when the same behavior should be tested with multiple inputs.
* Use `conftest.py` for fixtures that are shared across multiple test modules.
* Keep fixtures focused and avoid overly complex fixture dependencies.

## Mocking

* Prefer testing actual behavior over mocking implementation details.
* Use `unittest.mock` or the project's existing mocking utilities when mocking is necessary.
* Mock external systems such as network services, hardware, or unavailable external resources when appropriate.
* Avoid excessive mocking that makes tests verify the mock configuration rather than the actual behavior.
* Do not mock the component under test merely to make the test easier to write.

## Test Data

* Use small, representative test data where possible.
* Make expected values explicit.
* Prefer deterministic test data.
* Avoid unnecessary dependence on large external datasets.
* Use temporary directories and files through pytest facilities such as `tmp_path` when appropriate.
* Do not depend on a developer's local filesystem layout.

## External Resources

* Unit tests should not require network access unless the test specifically validates network behavior.
* Avoid requiring physical hardware for ordinary unit tests.
* Separate hardware-dependent and integration tests from unit tests.
* Clearly identify tests that require external services, special hardware, or environment-specific configuration.

## Numerical Tests

* Do not compare floating-point values using exact equality when numerical error is expected.
* Use `pytest.approx()` with an appropriate absolute or relative tolerance.
* Choose tolerances based on the expected numerical accuracy.
* Document non-obvious tolerances.

## Test Organization

* Keep test modules reasonably aligned with the production modules they test.
* Use descriptive test names that explain the expected behavior.
* Group related tests logically.
* Avoid excessively large test modules.
* Keep test helpers separate from production code unless they are genuinely part of the production API.

## Failure Diagnosis

* Make assertion failures easy to understand.
* Prefer assertions that expose the expected and actual values.
* Avoid unnecessary abstraction that makes failures difficult to diagnose.
* Include relevant context in assertion messages when the failure would otherwise be unclear.

## Verification

* Run the affected pytest tests after making changes.
* Run relevant regression tests when modifying shared functionality.
* Ensure that new tests actually exercise the behavior they are intended to verify when practical.
* Do not claim test results or coverage that were not actually verified.

## Change Discipline

* Add or update tests together with the corresponding functional change when appropriate.
* Do not modify unrelated tests.
* Do not weaken or remove an existing test merely to make the implementation pass.
* If an existing test reflects behavior that is intentionally changed, update the test as part of the same change.
