<!-- file: README.md -->
<!-- version: 3.0.0 -->
<!-- guid: 1a2b3c4d-e5f6-7a8b-9c0d-1e2f3a4b5c6d -->
<!-- last-edited: 2026-07-23 -->

# gcommon — Protocol Buffer definitions

[![BSR](https://img.shields.io/badge/buf.build-falkcorp%2Fgcommon-blue)](https://buf.build/falkcorp/gcommon)
[![CI](https://github.com/falkcorp/gcommon/actions/workflows/ci.yml/badge.svg)](https://github.com/falkcorp/gcommon/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**gcommon is a protobuf-definitions-only repository.** The `.proto` files here are
the single source of truth for a set of common gRPC services and message types.
They are published to the **[Buf Schema Registry](https://buf.build/falkcorp/gcommon)**,
and **consumers pull generated SDKs from BSR** for Go, Python, Rust, and any other
language buf supports.

> This repo does **not** build, commit, or release language SDKs, and there are no
> per-language SDK repositories. That machinery was retired — see [`archive/`](archive/README.md).
> "We're not in the buf-building business; we just pull it."

## Consuming these protos

### Go — pull the generated SDK from BSR

```bash
go get buf.build/gen/go/falkcorp/gcommon/protocolbuffers/go   # message types
go get buf.build/gen/go/falkcorp/gcommon/grpc/go              # gRPC service stubs
```

```go
import commonv2 "buf.build/gen/go/falkcorp/gcommon/protocolbuffers/go/common/v2"
```

BSR runs a Go module proxy, so `go get` resolves the generated code directly — no
`gcommon-go` repo, no committed generated code.

### Python — pull from the BSR Python index

```bash
pip install falkcorp-gcommon-protocolbuffers-python --extra-index-url https://buf.build/gen/python
```

### Rust / other languages

Add gcommon as a buf dependency and generate locally, or pull the BSR-generated SDK:

```yaml
# your project's buf.yaml
version: v2
deps:
  - buf.build/falkcorp/gcommon
```

```bash
buf generate   # against your own buf.gen.yaml with the plugins you want
```

> Exact BSR SDK package names resolve once the module is published and its
> per-language plugins are configured on BSR (see **Publishing** below).

## Modules

Ten families, each with a `v1` and a `v2` package (v2 is current):

| Family (`*pb`)     | Description                                                     |
| ------------------ | -------------------------------------------------------------- |
| **authpb**         | Authentication: login, tokens, API keys, OAuth, sessions       |
| **commonpb**       | Shared types, errors, pagination, auth/log/notification/health |
| **configpb**       | Configuration management and settings                          |
| **databasepb**     | Database ops, cache, migrations, transactions                  |
| **healthpb**       | Health checks, monitoring, service status                      |
| **mediapb**        | Media processing, audio, subtitles, content management         |
| **metricspb**      | System metrics, alerting, performance monitoring               |
| **organizationpb** | Multi-tenant organization, hierarchy, tenant management        |
| **queuepb**        | Message queuing, job processing, workflow                      |
| **webpb**          | HTTP services and web application utilities                    |

## Repository structure

```text
gcommon/
├── <family>pb/v1/       # v1 definitions (legacy)
├── <family>pb/v2/       # v2 definitions (current)   e.g. commonpb/v2/, mediapb/v2/
├── buf.yaml             # buf module config (name: buf.build/falkcorp/gcommon)
├── buf.lock             # pinned buf dependencies
├── buf.gen.yaml         # validation-only (no language generation here)
├── proto-docs/          # generated protobuf documentation
└── archive/             # retired SDK-building machinery (reference only)
```

## Development

### Prerequisites

- [Buf CLI](https://buf.build/docs/installation) v1.50+

### Working on protos

```bash
git clone https://github.com/falkcorp/gcommon.git
cd gcommon

buf lint                                     # lint all definitions
buf format -w                                # auto-format
buf breaking --against '.git#branch=main'    # check for breaking changes vs main
```

### Adding or changing definitions

1. Add/edit `.proto` files under the appropriate `<family>pb/v2/` directory.
2. Keep imports pointed at the real paths, e.g. `import "commonpb/v2/error.proto";`.
3. Run `buf lint` (and `buf breaking` for changes to existing messages — this repo
   treats consumer wire-compatibility as a hard constraint).
4. Open a PR. CI runs `buf lint` + `buf breaking`.

## Publishing (to BSR)

Publishing is **automated on version tags** via
[`.github/workflows/buf-push.yml`](.github/workflows/buf-push.yml): tagging `vX.Y.Z`
(or a manual `workflow_dispatch`) runs `buf push` to `buf.build/falkcorp/gcommon`.
The module is created public on first push.

Requires a repository secret `BUF_TOKEN` (a BSR API token with write access):

```bash
gh secret set BUF_TOKEN --repo falkcorp/gcommon
```

## CI

- **`ci.yml`** — `buf lint` + `buf breaking` (vs `main`) on every PR. Protos-only;
  no language builds.
- Security: the repo is public, so GitHub-native secret scanning + Dependabot apply.

## Documentation

- **[Buf Schema Registry](https://buf.build/falkcorp/gcommon)** — browse definitions
- **[proto-docs/](proto-docs/)** — generated API documentation
- **[Contributing Guide](CONTRIBUTING.md)**
- **[archive/README.md](archive/README.md)** — the retired SDK-building model and why

## License

MIT — see [LICENSE](LICENSE).
