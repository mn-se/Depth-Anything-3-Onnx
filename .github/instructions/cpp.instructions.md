---
description: This file describes the C++ code style and development guidelines for the project.
applyTo: "**/*.{cpp,h,hpp,cc,cxx}"
---

# C++ Development Guidelines

## Language

* Use C++17 unless the existing project explicitly requires another standard.
* Follow the language standard and compiler constraints of the target project.
* Prefer simple, portable C++ over compiler-specific features unless required by the project.

## Coding Style

* Use `snake_case` for variables and functions.
* Use `UpperCamelCase` for classes and structs.
* Follow the existing project's naming conventions when they differ.
* Use `const` whenever a value or reference does not need to be modified.
* Prefer clear, explicit code over overly compact expressions.

## Memory and Resource Management

* Avoid unnecessary dynamic memory allocation.
* Prefer stack allocation and existing project-owned buffers where practical.
* Use RAII for resource ownership.
* Do not introduce raw owning pointers.
* Avoid unnecessary copies of large objects or buffers.

## Error Handling

* Follow the error-handling mechanism already used by the project.
* Do not introduce exceptions into code that is designed to operate without exceptions.
* Do not silently ignore errors.
* Preserve error information when propagating failures.

## Dependencies

* Prefer the existing project infrastructure and utilities.
* Do not introduce a new third-party dependency when existing functionality can solve the problem.
* Do not introduce Eigen or OpenCV unless explicitly required by the project.
* Before adding a dependency, consider its impact on target platforms, build systems, binary size, and runtime resources.

## Interfaces

* Preserve existing public interfaces unless the task explicitly requires an API change.
* Minimize unnecessary changes to function signatures and data structures.
* Consider ABI, binary compatibility, and downstream users when modifying public interfaces.

## Comments and Documentation

* Write comments and Doxygen documentation in English.
* Comments should explain intent, constraints, or non-obvious behavior.
* Do not add comments that merely restate the code.
* Update relevant documentation when an interface or important behavior changes.

## Verification

After modifying C++ code:

* Build the affected target when possible.
* Run relevant tests.
* Check compiler warnings and errors.
* Review the final diff for unintended changes.
* Do not claim that code was built or tested unless it was actually verified.
