<!-- file: .github/copilot-instructions.md -->
<!-- version: 2.4.0 -->
<!-- guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a -->
<!-- last-edited: 2026-06-13 -->

# gcommon-proto — Additional Context

Org-wide coding standards (file headers, language rules, commit format) are at
**https://github.com/falkcorp/.github** and apply automatically to this repo.

For full project context: **CLAUDE.md** at the repo root.

## Project overview

Common Go modules — protobuf definitions and SDK generation. Language: Protobuf.
Generated code is published to language-specific repos (gcommon-go, gcommon-py).

## Key directories

| Directory | Purpose |
|-----------|---------|
| `authpb/`, `commonpb/`, `configpb/`, etc. | Per-domain protobuf packages |
| `scripts/` | Python automation (proto docs, cycle analysis) |
| `proto-docs/` | Generated protocol buffer documentation |

## Build commands

```bash
make lint          # Lint protobuf files with buf
make format        # Format protobuf files
make generate      # Validate protobuf definitions
make proto-docs    # Generate proto documentation
make dev           # Full dev workflow (lint + format + generate + docs)
```

## Critical constraints

- This repo contains **only** protobuf definitions — no Go/Python source code.
- Use `buf` (included as `./buf` binary) for all protobuf operations.
- Use `tools/protobuf-cycle-fixer.py` to resolve import cycles if they arise.
