---
description: This file describes the Python code style and development guidelines for the project.
applyTo: "**/*.py"
---

# Python Development Guidelines

## Language

* Use the Python version already specified by the project.
* Follow the existing project's conventions and runtime constraints.
* Prefer standard Python features over unnecessary framework-specific abstractions.

## Coding Style

* Follow PEP 8 unless the project has an established alternative.
* Use clear and descriptive names.
* Use `snake_case` for variables and functions.
* Use `UpperCamelCase` for classes.
* Use `UPPER_SNAKE_CASE` for module-level constants when appropriate.
* Prefer small, focused functions.
* Keep functions and modules understandable without excessive abstraction.
* Add type hints to new code where they improve clarity and maintainability.

## Dependencies

* Prefer the Python standard library when it is sufficient.
* Reuse existing project dependencies before introducing new ones.
* Do not add a dependency solely to avoid a small amount of straightforward code.
* Consider compatibility, maintenance, installation, and deployment requirements before adding dependencies.
* Follow the project's existing dependency management mechanism.

## Error Handling

* Handle expected errors explicitly.
* Raise appropriate exceptions rather than returning ambiguous error values.
* Do not use broad `except Exception` unless there is a specific reason to catch unknown failures.
* Do not silently ignore exceptions.
* Preserve useful error information when propagating failures.

## Resource Management

* Use context managers for resources that require deterministic cleanup.
* Avoid unnecessary global state.
* Ensure files, sockets, subprocesses, and other external resources are properly released.

## Interfaces

* Preserve existing public interfaces unless the task explicitly requires an API change.
* Avoid unnecessary changes to function signatures or data structures.
* Consider compatibility with existing callers when modifying public APIs.

## Documentation

* Write docstrings for public modules, classes, and functions when appropriate.
* Document non-obvious behavior, assumptions, and constraints.
* Comments should explain intent or non-obvious implementation details.
* Do not add comments that merely restate the code.

## External Processes and Files

* Handle subprocesses explicitly and check their return status when appropriate.
* Avoid hard-coded paths.
* Use `pathlib` for filesystem paths in new code unless the existing project uses another established mechanism.
* Do not assume a specific working directory unless the project explicitly requires it.

## Configuration

* Do not hard-code environment-specific configuration.
* Reuse the project's existing configuration mechanism.
* Keep secrets and credentials out of source code.
* Do not commit API keys, passwords, tokens, or other credentials.

## Performance

* Prefer clear and maintainable code over premature optimization.
* Avoid obviously unnecessary copies, conversions, and repeated I/O.
* When performance is important, measure before and after optimization when practical.
* Do not introduce complex optimization without evidence that it is necessary.

## Verification

* Run the relevant Python tests after making changes.
* Run static analysis, formatting, or type checking when these are part of the project's existing workflow.
* Review the final diff for unintended changes.
* Do not claim that code was tested or verified unless it was actually done.
