<!-- file: docs/CONSUMER_PROTO_AUDIT.md -->
<!-- version: 1.1.0 -->
<!-- guid: 9c2f4a71-6d38-4b0e-9f21-1a7c5e83d4b6 -->
<!-- last-edited: 2026-07-25 -->

# gcommon Phase C — Consumer-Driven Proto Audit

Date: 2026-07-24. Scope: task #6 of the Phase C protos-only pivot — audit what
actual consumers use from the gcommon v2 protos and what they need that is
missing, so the "required proto set" is consumer-driven rather than speculative.

## Consumers examined

- **subtitle-manager** (`falkcorp/subtitle-manager`) — the **only real consumer**.
  Imports `github.com/falkcorp/gcommon/v2` at `v2.2.0`; 28 non-test files use 5
  proto subpackages.
- **audiobook-organizer** — **NOT a consumer.** Zero gcommon imports, no go.mod
  require. The "~1 reference" in prior notes was a false positive from the shared
  `falkcorp` org prefix in its own module path. Drop it from consumer scope.

**Consumer set verified org-wide** (not just inherited from notes): a code search
across the `falkcorp` and `jdfalk` orgs for any `go.mod` requiring `falkcorp/gcommon`
or the old `jdfalk/gcommon` path returns only `gcommon-go` (the SDK module declaring
itself) and `subtitle-manager`. Since a Go consumer must pin the dep in `go.mod`, this
is definitive for Go. No non-Go (Python/Rust) consumers exist — the BSR module is
currently deleted and nothing pulls generated SDKs yet. **subtitle-manager is the sole
consumer.**

## Per-package usage (subtitle-manager)

| Package | Symbols actually used | Character |
|---|---|---|
| `commonpb/v2` | SubtitleFormat, LogLevel/LoggerConfig, ConfigValue, CachePolicy, User/Session/APIKey, Auth* service+messages | **Data types real & deeply wired.** AuthService implemented (`pkg/authserver`) but **never registered** (no `RegisterAuthServiceServer`, no non-test caller). |
| `queuepb/v2` | `QueueMessage` only | **Placeholder.** Built in `pkg/queue/jobs.go` then only logged; real dispatch is in-memory Go channels. Local mirror struct + `// TODO: Replace with gcommon…QueueMessage` at `pkg/queue/message.go:12`. |
| `mediapb/v2` | full client/server/message surface | Client wrapper real; server RPCs **stubbed**; **not wired** (test-only, no importer, no `Register…`). |
| `metricspb/v2` | Provider/Counter/Histogram/Gauge/Config | Real wiring but gated behind `//go:build gcommonmetrics` — **not compiled in default builds**. |
| `databasepb/v2` | `Row` only | Used as a **positional `[]*anypb.Any` hack** (`pkg/database/pb_conversions.go`) to marshal local `SubtitleRecord`/`DownloadRecord`. Brittle (order-dependent, `len<12` guards). |

Confirmed absent (memory was right): **no `authpb`, no `healthpb` import.** The
`authpb` alias in `pkg/authserver` actually aliases `commonpb`. Auth is local SQL
in the misleadingly named **local** package `pkg/gcommonauth`. Health uses stock
`grpc_health_v1` in one test. Any claim that subtitle-manager "switched to gcommon
auth/health" is **false**.

## Conclusion: no consumer-required NEW proto work

Every apparent "gap" is one of:
1. **subtitle-manager choosing not to adopt gcommon** (in-memory queue instead of
   queuepb transport; mediapb server left stubbed; metricspb behind a build tag), or
2. **app-specific domain types that do not belong in a shared proto lib**
   (`SubtitleRecord`, `DownloadRecord` — correctly local; `databasepb.Row` being a
   generic opaque container is arguably the right design).

The commonpb types subtitle-manager actually depends on are real and working. **The
consumer-driven "required proto set" is effectively empty of new work.** gcommon's
*consumed* surface is adequate for its one real consumer today.

### One ergonomics finding the proto repo actually owns

Distinct from the adoption choices above: `pkg/media/server.go:626` — *"can't
directly set fields due to protobuf opaque generation … would need proper protobuf
message construction"* — is the sole gap attributable to a decision the **proto repo
controls**, not the consumer. The protos set `option features.(pb.go).api_level =
API_OPAQUE`, which forces the setter/getter builder API and makes message
construction more verbose for consumers. Not required work — the opaque API is a
deliberate, defensible choice — but it is the one place a consumer hit friction the
proto repo owns, worth noting for future ergonomics discussion.

## Real quality gaps found (NOT consumer-demanded) — status 2026-07-25

- **queuepb workflow — FIXED (PR #1138 + #1139, merged).** `QueueWorkflow` now carries
  a typed `repeated WorkflowStep steps` DAG (`WorkflowStep` = step_id + name +
  `depends_on` edges + `Any config`), and `StartWorkflowRequest` takes a typed
  `QueueWorkflow definition`; the opaque `workflow_definition` string is deprecated. No
  workflow engine was modeled (no retries/conditionals/timeouts) — just a typed graph.
- **webpb is hollow — DEFERRED to the multi-language-implementations ultracode session.**
  94 files are `string placeholder = 1` stub bodies, and they are not merely missing
  fields: they are ~46 orphaned request/response pairs (only 5 of the ~46 implied
  operations are wired as RPCs across `web_service.proto` / `web_admin_service.proto`).
  So "filling webpb" means designing AND wiring a whole 46-operation web-framework API
  (routing, handlers, middleware, static files, templates, websockets, cookies, CSRF,
  CORS, security, server lifecycle, auth, metrics) with **zero consumers and no
  implementation to validate it**. Per owner decision (2026-07-25), webpb is left
  intentionally unbuilt and will be designed in the dedicated implementations ultracode
  session, where the API can be co-designed against a real implementation instead of
  guessed.

## Cross-cutting finding: stale `go_package` — FIXED (PR #1136)

Originally all 1774 protos declared `option go_package = "github.com/jdfalk/gcommon/..."`
(the retired `jdfalk` path; zero used `falkcorp`). Repointed to
`github.com/falkcorp/gcommon/v2/pkg/<pkg>/v2` in PR #1136 — the path consumers actually
import — so the source metadata is honest. `FILE_SAME_GO_PACKAGE` was added to the
buf.yaml breaking `except` (go_package is vestigial under BSR-managed distribution).

## Phase C close-out — all residuals DONE

1. ✅ `BUF_TOKEN` set (falkcorp **org** secret, selected→gcommon); `v2.3.0` tagged →
   `buf-push.yml` re-established `buf.build/falkcorp/gcommon` (public, live).
2. ✅ One-time `buf format -w` applied tree-wide; the format gate is enforced in `ci.yml`.
3. ✅ `go_package` repointed to `falkcorp` (PR #1136), see above.
4. ✅ subtitle-manager migrated onto the BSR-generated Go SDK (PR #2203); the old
   `gcommon-go` Go-SDK repo is archived.
5. ✅ Proto-metadata debt fixed (PR #1137): `// file:` headers normalized, authpb
   go_package `/v2` suffix.
6. ✅ queuepb workflow typed (PR #1138/#1139). webpb deferred (see above).
