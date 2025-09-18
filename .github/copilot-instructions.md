<!-- file: .github/copilot-instructions.md -->
<!-- version: 2.1.3 -->
<!-- guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a -->

# Copilot/AI Agent Instructions (gcommon)

This repo uses a centralized instruction system. Keep this short, actionable, and repo-specific.

## Required workflow
- Edit docs directly in their files. Always keep the file header (file path, version, guid) and bump the version on any change.
- Prefer VS Code Tasks over manual commands. Available tasks include: `Buf Lint with Output`, `Buf Generate with Output`, `Git Add All`, `Git Commit Auto`, `Git Push`, plus module-scoped Buf tasks.
- Use Conventional Commits. All source/docs must include the required header (file path, version, guid) and bump version on change.

## Project shape (what matters)
- Protobuf-first repo. Source protos live under `proto/gcommon/v1/<module>/<area>/<name>.proto` using a strict 1-1-1 pattern (one type/service per file).
- Generated SDKs: Go in `sdks/go/gcommon/v1/...` and Python in `sdks/python/gcommon/v1/...`. Never hand-edit generated code.
- Core config: `buf.yaml` (module + lint/breaking rules) and `buf.gen.yaml` (plugins/output).
- Utility scripts in `scripts/` power generation and post-processing; Makefile provides a developer-friendly wrapper.

## Build/generation flow
- Lint protos: run the VS Code task “Buf Lint with Output” (or `make lint`). The repo’s buf rules allow: service suffix `Service`, enum zero value suffix `_UNSPECIFIED`, and google.empty messages.
- Generate SDKs: run the task “Buf Generate with Output” (or `make generate`). Always prefer `make generate` when updating protobufs because it runs required post-processing scripts. This executes:
  - buf generate → Go via `protoc-gen-go` and `protoc-gen-go-grpc` to `sdks/go` (module=github.com/jdfalk/gcommon/sdks/go) and Python via built-in `python` and `pyi` to `sdks/python`.
  - scripts/setup-go-modules.py v2.9.0 (minimal): root `go mod tidy`, remove legacy per-package `go.mod`, ensure Python package markers.
  - scripts/setup-python-sdk.py: ensures Python package layout and creates `sdks/python/setup.py` if missing.
  - scripts/generate_proto_docs.py: emits docs to `proto-docs/` (threshold=50).

## Conventions and patterns
- File headers: every source, script, and doc begins with repo-absolute path + semantic version + GUID. Update the version (patch/minor/major) whenever you change content.
- Protos: do not add disable blocks to `buf.gen.yaml`; plugins are listed explicitly. Keep imports consistent with the 1-1-1 layout; fix by moving shared types to `common` if you see cycles.
- Go usage: consumers import from `github.com/jdfalk/gcommon/sdks/go/gcommon/v1/<package>`; run `go mod tidy` in the consumer after updates.
- Python usage: `pip install -e sdks/python` and import from `gcommon.v1.<package>`.

## What to touch vs. generate
- Make changes in `proto/gcommon/v1/**` and rerun generation. Don’t hand-edit anything in `sdks/**`.
- If you add a new proto: follow the 1-1-1 rule, pick the correct module (common, config, queue, metrics, database, web, organization, health, media, etc.), and include clear comments—docs are auto-generated.

## Tasks and examples
- Quick path: use VS Code tasks → “Buf Lint with Output” → “Buf Generate with Output” → “Git Add All” → “Git Commit Auto” → “Git Push”.
- Makefile equivalents: `make dev` (lint+format+generate), `make generate`, `make proto-docs`, `make clean`.

## Canonical instruction sources
- General rules: `.github/instructions/general-coding.instructions.md`
- Language/task-specific: `.github/instructions/*.instructions.md`
- Agent docs/pointers: `.github/README.md`, `AGENTS.md`, `.github/CLAUDE.md`

Tip: When in doubt, start from `make generate` or the Buf tasks and inspect `proto-docs/` for expected changes.

## Documentation updates (no scripts)

- Do not use any doc-update scripts in this repository.
- Make edits directly in the target files and bump the version header accordingly.
- Follow the guidance in `.github/instructions/general-coding.instructions.md` for formatting and workflow.
