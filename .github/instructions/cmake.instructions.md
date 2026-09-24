---
description: This file describes the CMake code style and development guidelines for the project.
applyTo: "**/CMakeLists.txt,**/*.cmake"
---

# CMake Development Guidelines

## General

* Follow the existing CMake structure and conventions of the project.
* Do not restructure the build system unless the task explicitly requires it.
* Prefer the smallest CMake change that solves the problem.
* Do not introduce unnecessary CMake features or abstractions.
* Keep the build configuration understandable and maintainable.

## CMake Version

* Use the CMake version already required by the project.
* Do not raise the minimum required CMake version unless necessary.
* Prefer commands and features supported by the project's minimum CMake version.

## Project Structure

* Prefer a clear target-oriented structure.
* Configure targets with `target_*` commands rather than global commands where practical.
* Avoid unnecessary global settings such as `include_directories()`, `link_libraries()`, and `add_definitions()`.
* Prefer target-specific configuration such as:

  * `target_include_directories()`
  * `target_compile_definitions()`
  * `target_compile_options()`
  * `target_link_libraries()`

## Targets

* Keep each target's dependencies explicit.
* Link libraries to the target that actually uses them.
* Prefer `PRIVATE`, `PUBLIC`, and `INTERFACE` correctly rather than making dependencies global.
* Do not add unnecessary dependencies to a target.
* Preserve existing target names unless a rename is explicitly required.

## Source Files

* Add source files to the appropriate existing target.
* Do not automatically add every source file in a directory using `file(GLOB ...)`.
* Prefer explicit source file lists when that is the existing project convention.
* Do not remove or reorganize source files solely to simplify CMake.

## Compiler Configuration

* Keep compiler options target-specific where practical.
* Do not globally override compiler flags that may affect unrelated targets.
* Do not add optimization, warning, or language-standard flags without understanding the existing build configuration.
* Respect the compiler and toolchain specified by the project.

## Dependencies

* Reuse existing dependencies whenever possible.
* Do not introduce a new external dependency solely to simplify the build.
* Before adding a dependency, consider:

  * target platform support
  * cross-compilation requirements
  * package availability
  * binary size
  * deployment requirements
* Do not silently download or fetch external dependencies during configuration unless the project already uses that approach.

### Windows GoogleTest via vcpkg

* Use the shared vcpkg installation identified by the `VCPKG_ROOT` environment variable for GoogleTest.
* Assume the `gtest:x64-windows` package is installed.
* Configure projects with `$env:VCPKG_ROOT\scripts\buildsystems\vcpkg.cmake` as `CMAKE_TOOLCHAIN_FILE` and use the `x64-windows` triplet.
* For projects that use GoogleTest, use `find_package(GTest CONFIG REQUIRED)`.
* Link test targets with `GTest::gtest` or `GTest::gtest_main` as appropriate.
* Do not use `FetchContent`, `ExternalProject`, or copy/download GoogleTest into the project.

## Build Options

* Use CMake options for configuration that genuinely needs to be selectable.
* Avoid adding options for one-off development changes.
* Give options clear names and document non-obvious behavior.
* Preserve existing option names and semantics.

## Platform and Toolchain

* Respect existing toolchain files and cross-compilation settings.
* Do not modify platform-specific configuration without understanding its purpose.
* Avoid hard-coded host paths, compiler paths, SDK paths, or library paths.
* Prefer CMake variables, toolchain configuration, or existing project mechanisms.

## Installation and Packaging

* Preserve existing install and packaging behavior unless the task requires a change.
* When adding a library or executable intended for deployment, update the relevant install configuration if required.
* Keep runtime dependencies explicit.

## Validation

After changing CMake configuration:

* Configure the project using the project's normal configuration procedure.
* Build the affected target.
* Verify that existing targets still configure and build when the change may affect them.
* Check the generated build configuration for unintended changes.
* Do not claim that CMake configuration or builds succeeded unless they were actually executed.

## Change Discipline

* Do not rewrite an existing CMakeLists.txt merely to modernize its style.
* Do not perform unrelated CMake cleanup during a functional change.
* Preserve working project-specific conventions even if another CMake style would normally be preferred.
* If the required change conflicts with the existing build architecture, explain the impact before making a broad structural change.
