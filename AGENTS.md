<!-- file: AGENTS.md -->
<!-- version: 2.2.0 -->
<!-- guid: 2e7c1a4b-5d3f-4b8c-9e1f-7a6b2c3d4e5f -->

# AGENTS.md

> **NOTE:** This is a pointer file. All detailed Copilot, agent, and workflow
> instructions are in the [.github/instructions](.github/instructions) directory.

## ⚠️ CRITICAL: File Version Updates

**When modifying any file with a version header, ALWAYS update the version
number:**

- **Patch version** (x.y.Z): Bug fixes, typos, minor formatting changes
- **Minor version** (x.Y.z): New features, significant content additions,
  template changes
- **Major version** (X.y.z): Breaking changes, structural overhauls, format
  changes

**Examples:**

- Fix typo: `1.2.3` → `1.2.4`
- Add new section: `1.2.3` → `1.3.0`
- Change template structure: `1.2.3` → `2.0.0`

**This applies to ALL files with version headers including documentation,
templates, and configuration files.**

## Protobuf updates (repo policy)

- When you change any `.proto` files, always run `make generate` (or the VS Code task "Buf Generate with Output").
- Prefer `make generate` because it runs required post-processing scripts:
  - `scripts/setup-go-modules.py`
  - `scripts/setup-python-sdk.py`
  - `scripts/generate_proto_docs.py`
- Never hand-edit anything under `sdks/**` — those are generated artifacts.
