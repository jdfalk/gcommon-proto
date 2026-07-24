<!-- file: archive/README.md -->
<!-- version: 1.0.0 -->
<!-- guid: 6639f495-2557-429e-8a83-fb01240e155b -->
<!-- last-edited: 2026-07-23 -->

# Archive — retired SDK-building machinery

`gcommon` is now a **protos-only** repository. Protocol buffer definitions are the
product; they are published to the **Buf Schema Registry** (`buf.build/falkcorp/gcommon`)
and **consumers pull generated SDKs from BSR** for Go, Python, Rust, etc. This repo
is deliberately **not in the code-generation / SDK-building business** anymore.

Everything in this `archive/` directory belonged to the previous model — where this
repo (and per-language `gcommon-go` / `gcommon-py` SDK repos) generated, committed,
versioned, and released language SDKs, and fanned changes out across repos. It is
kept for reference and history, not run.

## What was archived and why

| Path | Was | Why retired |
|------|-----|-------------|
| `workflows/release.yml`, `release-{go,python,rust,docker,frontend,protobuf}.yml` | per-language SDK release builds + coordinator | We don't build/release SDKs; BSR generates them on demand. |
| `workflows/protobuf-generation.yml` | generated + committed Go SDK code | No committed generated code. |
| `workflows/notify-sdk-repos.yml`, `workflows/sync-receiver.yml` | fan-out to `gcommon-go`/`gcommon-py` SDK repos | No SDK repos. |
| `scripts/version_sync_manager.py`, `create-module-tags.py`, `post-buf-generate.py`, `post-tag-hook.py` | cross-repo version sync, Go nested-module tagging, post-generate fixups | Tied to the SDK-repo fan-out + committed-code model. |
| `scripts/cleanup_bad_tags.py`, `cleanup_complex_tags.py`, `fix_go_tagging.py`, `fix_malformed_tags.py` | Go nested-module tag cleanup | No Go module tags live here anymore. |
| `docs/GRAND_PROPOSAL.md` | proposed committed per-language SDK repos | Superseded by the BSR-managed / pull model. |
| `docs/compatibility-matrix.md` | gcommon / gcommon-go / gcommon-py version matrix | No per-language SDK repos to track. |
| `docs/COSIGN_VERIFICATION.md`, `tooling/cosign.pub` | signing of released SDK artifacts | No released artifacts from this repo. |
| `docs/README_old.md`, `docs/REPOSITORY_AUTOMATION.md` | old readme / sync-automation guide | Describe the retired model. |
| `tooling/buf` (44 MB), `tooling/protoc-32.1-linux-x86_64.zip` (3.4 MB), `tooling/alltags` | committed build binaries + tag dump | "Not in the buf-building business" — tools come from PATH/CI, not the repo. |

## The current model (for reference)

- **Source of truth:** the `.proto` files in this repo.
- **Publish:** `buf push` to `buf.build/falkcorp/gcommon` (public).
- **Consume (Go):** `go get buf.build/gen/go/falkcorp/gcommon/protocolbuffers/go` (+ grpc plugin).
- **Consume (Python):** `pip install` from the BSR Python index.
- **Consume (Rust):** BSR-generated Rust SDK / local `buf generate`.
- No committed generated code, no per-language SDK repos, no fan-out.

> These files are intentionally out of `.github/workflows/` and the active tree so
> they no longer run. Restore from history if a decision reverses.
