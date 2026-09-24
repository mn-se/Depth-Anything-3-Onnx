---
description: This file describes the C++ test code style and development guidelines for the project.
applyTo: "**/tests/**/*.{cpp,h,hpp,cc,cxx},**/*/test/**/*.{cpp,h,hpp,cc,cxx},**/*_test.{cpp,h,hpp,cc,cxx},**/*_tests.{cpp,h,hpp,cc,cxx}"
---

# C++ Test Guidelines

## Test Framework

* Use GoogleTest (gtest) as the standard C++ test framework.
* Use GoogleMock (gmock) when mocking or verifying interactions with dependencies is appropriate.
* Follow the version of GoogleTest already used by the project.
* Do not introduce another test framework when GoogleTest can be used.
* If the existing project already uses a different test framework, preserve the existing framework unless migration is explicitly requested.

## GoogleTest Environment

* On Windows, use the shared vcpkg installation identified by `VCPKG_ROOT`.
* Assume `gtest:x64-windows` is installed for C++ test projects.
* Follow `cmake.instructions.md` for CMake toolchain, package discovery, and target linking configuration.
* Do not use project-local copies of GoogleTest.

## Test Design

* Tests should verify observable behavior, not implementation details.
* Keep each test focused on one behavior or scenario.
* Prefer deterministic tests that produce the same result when executed repeatedly.
* Keep tests independent from one another.
* Do not rely on test execution order.
* Cover normal cases, boundary conditions, invalid inputs, and important failure cases.
* Add regression tests for bugs that are likely to recur.

## GoogleTest Conventions

* Use `TEST()` for simple independent tests.
* Use `TEST_F()` when shared setup or teardown is required.
* Use parameterized tests when the same behavior must be verified across multiple inputs.
* Prefer standard GoogleTest assertions such as `EXPECT_EQ`, `ASSERT_EQ`, `EXPECT_NE`, `EXPECT_TRUE`, and `EXPECT_FALSE` according to whether execution should continue after a failure.
* Use floating-point assertions such as `EXPECT_NEAR` when numerical tolerance is required.
* Use GoogleMock only when interaction-based testing provides meaningful value.
* Avoid excessive mocking when direct behavioral testing is possible.

## Test Code

* Keep test code simple and readable.
* Prefer explicit test setup over complex test helpers when the setup is short.
* Reuse existing test utilities when they already exist.
* Do not duplicate production logic inside tests.
* Do not modify production code solely to make a test easier unless the design genuinely requires better testability.

## Test Data

* Use small, representative test data where possible.
* Make expected values explicit.
* Avoid unnecessarily large datasets unless testing performance, resource limits, or scalability.
* Do not depend on external files, network services, hardware, or system state unless the test specifically requires them.

## Numerical Tests

* Do not compare floating-point values using exact equality when numerical error is expected.
* Use an appropriate absolute or relative tolerance.
* Prefer `EXPECT_NEAR` or `ASSERT_NEAR` for scalar floating-point comparisons.
* Choose tolerances based on the expected numerical accuracy.
* Document non-obvious tolerances.

## Test Scope

* Unit tests should remain independent of hardware and external systems whenever practical.
* Integration or hardware-dependent tests should be clearly separated from unit tests.
* Do not turn a unit test into an integration test without an explicit reason.

## Failure Diagnosis

* Test failures should provide enough information to identify the failing condition.
* Prefer assertions that clearly identify expected and actual values.
* Avoid excessive abstraction that makes failures difficult to diagnose.

## Validation

* Run the affected GoogleTest tests after making changes.
* Run relevant regression tests when modifying shared functionality.
* Ensure that a new test actually detects the behavior it is intended to verify when practical.
* Do not claim test results or coverage that were not actually verified.

## Change Discipline

* Add or modify tests together with the corresponding functional change when appropriate.
* Do not rewrite unrelated tests.
* Do not weaken or remove an existing test merely to make the implementation pass.
* If an existing test encodes behavior that conflicts with an intentional specification change, update the test as part of that change.
