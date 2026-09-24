---

name: uv-init
description: Initialize and configure Python projects using uv, including Python version selection, virtual environments, dependencies, development tools, and project execution.
---

# uv Init Skill

## Objective

Initialize and configure Python projects using `uv`.

The goal is to create a reproducible, maintainable Python development environment without introducing unnecessary configuration or dependencies.

Use this Skill when:

* Creating a new Python project
* Initializing an existing directory as a uv project
* Setting up a Python virtual environment with uv
* Adding initial project dependencies
* Configuring development dependencies and tools
* Converting an existing simple Python project to uv when appropriate

Do not use this Skill for Python coding style or general Python implementation rules. Those are defined in the Python-specific instructions.

---

# Workflow

## 1. Inspect the Existing Environment

Before initializing a project:

* Check whether `pyproject.toml` already exists.
* Check whether the project is already managed by `uv`.
* Check the existing Python version requirements.
* Check for existing dependency files such as:

  * `requirements.txt`
  * `requirements-dev.txt`
  * `setup.py`
  * `setup.cfg`
  * `Pipfile`
  * `poetry.lock`
* Check the existing project structure.
* Check whether a virtual environment already exists.
* Avoid overwriting existing project configuration without understanding it.

If the project is already correctly configured for uv, do not reinitialize it unnecessarily.

---

## 2. Initialize the Project

For a new Python project:

* Use `uv init`.
* Prefer the appropriate project layout for the intended project type.
* Use the project's required Python version when one is specified.
* If no version is specified, use a currently supported Python version appropriate for the project.

Do not introduce unnecessary project files or configuration.

The resulting project should normally contain:

* `pyproject.toml`
* `uv.lock` after dependencies are resolved
* `.venv` when a local virtual environment is required

Follow the existing repository conventions when they differ.

---

## 3. Configure Python

Determine the Python version from the project requirements before selecting one.

Prefer:

1. Explicit project requirement
2. Existing CI/build configuration
3. Existing project documentation
4. Compatible currently supported Python version

Do not arbitrarily upgrade the project's Python version.

When the project requires a specific Python version, configure uv accordingly.

---

## 4. Configure Dependencies

Use uv for dependency management.

For runtime dependencies:

```text
uv add <package>
```

For development-only dependencies:

```text
uv add --dev <package>
```

Prefer adding dependencies through uv rather than manually editing dependency metadata.

Before adding a dependency:

* Check whether the functionality already exists in the standard library.
* Check whether an existing project dependency can provide the required functionality.
* Avoid duplicate libraries serving the same purpose.
* Consider supported Python versions and target platforms.

Do not add dependencies speculatively.

---

## 5. Development Tools

Add development tools as development dependencies when they are required by the project.

Typical examples include:

* `pytest`
* `ruff`
* `mypy`
* Other project-specific test, lint, format, or type-check tools

Use the project's existing tooling when present.

Do not automatically add every available Python development tool.

Only add tools that are required by the project or its established development workflow.

---

## 6. Synchronize the Environment

After project configuration or dependency changes:

```text
uv sync
```

Use `uv sync` to create or update the project environment and lockfile.

Do not manually install packages into `.venv` when they are intended to be project dependencies.

---

## 7. Run the Project

Prefer `uv run` for project commands.

Examples:

```text
uv run python main.py
uv run pytest
```

For development tools installed through the project configuration, invoke them through `uv run`.

This keeps execution tied to the project's managed environment.

---

## 8. Existing Project Migration

When introducing uv into an existing Python project:

* Inspect the current dependency and build configuration first.
* Preserve the existing Python version requirements.
* Preserve existing package metadata and entry points where applicable.
* Convert dependencies carefully into `pyproject.toml`.
* Avoid unnecessary restructuring.
* Preserve existing behavior.
* Remove obsolete dependency-management files only when their replacement is verified and the project no longer requires them.

Do not blindly run `uv init` over an existing configured project.

---

# Project Configuration

## pyproject.toml

Use `pyproject.toml` as the primary project configuration and dependency definition.

Keep configuration minimal and project-specific.

Typical information may include:

* Project name
* Version
* Description
* Python requirement
* Runtime dependencies
* Development dependencies
* Build configuration
* Project entry points
* Tool configuration

Do not add configuration unrelated to the current project requirements.

---

## uv.lock

Use `uv.lock` to provide reproducible dependency resolution.

When dependencies change:

* Update the lockfile through uv.
* Keep the lockfile synchronized with `pyproject.toml`.
* Do not manually edit dependency resolution entries.

Do not remove `uv.lock` merely to resolve an ordinary dependency issue without first understanding the cause.

---

## Virtual Environment

Use the project-local `.venv` when a local virtual environment is appropriate.

Do not commit `.venv` to version control.

Ensure the repository's `.gitignore` excludes the virtual environment when appropriate.

Do not create multiple unnecessary virtual environments for the same project.

---

# Project Structure

Do not impose a package layout without considering the project.

For a simple executable project, a minimal structure may be sufficient:

```text
project/
├── pyproject.toml
├── uv.lock
├── .venv/
└── main.py
```

For a reusable library or larger application, follow the existing or intended package structure.

Do not introduce `src/` layout, package restructuring, or additional directories unless they provide a clear benefit for the project.

---

# Commands

Prefer the following uv workflow:

| Purpose                    | Command                  |
| -------------------------- | ------------------------ |
| Initialize project         | `uv init`                |
| Add runtime dependency     | `uv add <package>`       |
| Add development dependency | `uv add --dev <package>` |
| Remove dependency          | `uv remove <package>`    |
| Synchronize environment    | `uv sync`                |
| Run Python                 | `uv run python ...`      |
| Run tests                  | `uv run pytest`          |
| Run development tool       | `uv run <tool>`          |
| Inspect environment        | `uv ...`                 |

Use the current uv command syntax supported by the installed version.

Do not assume command-line options that may not exist in the installed uv version.

---

# Environment and Secrets

Do not store secrets in:

* `pyproject.toml`
* source code
* `.env` files committed to the repository
* uv configuration committed to the repository

Use the project's established environment-variable or secret-management mechanism.

Do not expose credentials while inspecting or configuring the environment.

---

# Validation

After initialization or configuration:

* Confirm `pyproject.toml` is valid.
* Confirm dependencies resolve successfully.
* Run `uv sync`.
* Confirm the expected Python version is being used.
* Run relevant tests when available.
* Run the application or relevant entry point when appropriate.
* Confirm `uv.lock` is synchronized.
* Review the resulting file changes.
* Check that `.venv` is not unintentionally tracked.
* Confirm no unrelated files were modified.

Do not claim successful setup, installation, testing, or execution unless it was actually performed.

---

# Change Discipline

* Prefer the smallest configuration change that solves the problem.
* Preserve existing project conventions.
* Do not overwrite existing configuration without inspection.
* Do not upgrade Python or dependencies without a reason.
* Do not add unnecessary dependencies.
* Do not introduce unnecessary tooling.
* Do not restructure the project merely to conform to a preferred layout.
* Do not modify unrelated files.

The resulting environment should be reproducible and understandable to another developer.
