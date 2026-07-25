<!-- file: docs/PROJECT_STATUS.md -->
<!-- version: 1.0.0 -->
<!-- guid: f1aa2e13-be5d-4ce7-a99b-eecc8b25b46f -->
<!-- last-edited: 2026-07-25 -->

# gcommon — Project Status & Resume Guide

**Read this first if you're picking this back up cold.** It is the single source of
truth for what this repo is, how it's distributed, what state it's in, and what to do
next. Last updated 2026-07-25.

---

## 1. TL;DR — what this repo is now

`falkcorp/gcommon` is a **protos-only repository**. It contains ~1,774 Protobuf
definitions and **no generated language code and no service implementations**. It is
published to the **Buf Schema Registry (BSR)** at `buf.build/falkcorp/gcommon`, and
**consumers pull generated SDKs from BSR** for their language.

- Latest release: **v2.4.0** (2026-07-25), live on BSR.
- v2-only (all `v1` packages were dropped).
- CI = `buf lint` + `buf breaking` + `buf format` (no build/test — there's no code).

If you remember nothing else: **edit protos → `buf lint`/`format` clean → PR → merge →
tag `vX.Y.Z` → `buf-push.yml` publishes to BSR automatically.**

---

## 2. Repo topology (three repos, don't mix them up)

| GitHub repo | Role | Local working copy | Status |
|---|---|---|---|
| **`falkcorp/gcommon`** | THE proto source (this repo) | `~/repos/github.com/jdfalk/gcommon-proto` (git remote → `falkcorp/gcommon`; symlink `gcommon-proto` also points here) | Active |
| **`falkcorp/gcommon-go`** | Old hand-maintained Go SDK/service module | `~/repos/github.com/jdfalk/gcommon` (remote → `gcommon-go`) | **ARCHIVED** (read-only) — retired on purpose to start fresh |
| **`falkcorp/subtitle-manager`** | The one real consumer | `~/repos/github.com/jdfalk/subtitle-manager` | Active; now consumes gcommon from BSR |

> The local directory names are historically swapped: the folder called `gcommon-proto`
> is the proto SOURCE, and the folder called `gcommon` is the archived Go SDK. Go by the
> git remote, not the folder name.

Also on disk: `~/repos/github.com/jdfalk/gcommon-plan-phase-c-services/docs/` holds the
**shelved** 33-service implementation plan package (see §7).

---

## 3. How distribution works (the runbook)

- **Source of truth:** protos in git, grouped as `<pkg>pb/v2/*.proto` (e.g.
  `commonpb/v2`, `queuepb/v2`). Packages: authpb, commonpb, configpb, databasepb,
  healthpb, mediapb, metricspb, organizationpb, queuepb, webpb.
- **Publishing:** `.github/workflows/buf-push.yml` runs `buf push --create
  --create-visibility public --git-metadata` on **version tags (`v*`) and manual
  dispatch only** — NOT on every merge. It needs the `BUF_TOKEN` secret (see §8).
- **Consuming (Go):** `go get buf.build/gen/go/falkcorp/gcommon/protocolbuffers/go@latest`
  (messages) and `.../grpc/go@latest` (service stubs). These verify against the public
  Go checksum DB — **no `GOSUMDB`/`GONOSUMDB` config needed.**
  - Message import: `buf.build/gen/go/falkcorp/gcommon/protocolbuffers/go/<pkg>pb/v2`
    (Go package name e.g. `commonv2`, `queuev2`).
  - Service import: `buf.build/gen/go/falkcorp/gcommon/grpc/go/<pkg>pb/v2/<pkg>v2grpc`
    (Go package name e.g. `commonv2grpc`). **BSR splits messages and services into
    separate modules/packages** — this is the main gotcha when migrating code.
- **Consuming (Python/Rust/other):** pull the equivalent BSR-generated SDK, or add
  `buf.build/falkcorp/gcommon` as a buf dep and `buf generate`.

---

## 4. Current status (as of 2026-07-25)

- **Released & live:** `v2.4.0` on BSR (module commit `e6284ae1c9aa`; Go SDK
  `v1.36.11-20260725232151-e6284ae1c9aa.1`). Previous: `v2.3.0` (`436a1c85`).
- **main is green** on the buf CI job. `buf lint`/`format`/`breaking` all clean.
- **Only real consumer** = subtitle-manager, now fully on the BSR SDK (see §6).
- **No open proto work in flight.** No blocking PRs.
- **Known non-blocking noise:** `maintenance.yml` fails at 0s on main — pre-existing
  **org-automation debt** (log-not-found), unrelated to protos. Ignore unless you're
  fixing org automation broadly.

---

## 5. What was done (work log)

The 2026-07 arc, newest first. All PRs against `falkcorp/gcommon` unless noted.

- **v2.4.0 release** (2026-07-25) — published typed workflows + metadata cleanup to BSR.
- **#1140** — docs: proto-gap status (this kind of doc; audit updated).
- **#1138 + #1139** — feat: **queuepb typed workflow DAG** (`WorkflowStep` with
  `depends_on` edges + `Any config`; `QueueWorkflow.steps`; typed
  `StartWorkflowRequest.definition`; deprecated the opaque `workflow_definition`
  string). #1139 fixed a follow-on unused-import that broke CI.
- **#1137** — chore: normalized all `// file:` headers to real paths; fixed `authpb`
  `go_package` `/v2` suffix.
- **#1136** — chore: **Phase C close-out** — repointed all 1,774 protos' `go_package`
  from retired `jdfalk` → `falkcorp/gcommon/v2/...`; one-time `buf format -w`; enabled
  the format gate; added `FILE_SAME_GO_PACKAGE` to the breaking `except`. Also added
  `docs/CONSUMER_PROTO_AUDIT.md`.
- **v2.3.0 release** — first release under the protos-only model; re-established the BSR
  module (which had been deleted).
- **#1132–#1135** (earlier this arc) — archived all SDK-building machinery into
  `archive/`; replaced multi-language CI with buf-native `ci.yml`; added `buf-push.yml`;
  rewrote README for the protos-only/BSR model; dropped all `v1` packages.
- **subtitle-manager #2203** — migrated the consumer off the `github.com/falkcorp/
  gcommon/v2` Go module onto the BSR-generated SDKs; then **archived `gcommon-go`**.

Earlier phases (context): Phase A regenerated 3,521 corrupted `.pb.go` files; Phase B
consolidated 13 Go modules → 1; Phase C started as "build 31 Go services" and then
**pivoted to protos-only + BSR** (the current model).

---

## 6. The consumer: subtitle-manager

- Consumes gcommon **from BSR** (`buf.build/gen/go/...`) as of PR #2203.
- Actually uses (production-wired): **commonpb** message types (SubtitleFormat,
  LogLevel/LoggerConfig, ConfigValue, CachePolicy, User/Session/APIKey).
- Everything else it imports is placeholder/unwired: queuepb (only `QueueMessage`,
  logged not transported), mediapb (client/server stubbed, not registered), metricspb
  (behind `//go:build gcommonmetrics`), databasepb (`Row` used as a positional `Any`
  hack). Its auth is **local SQL** in `pkg/gcommonauth` (NOT gcommon, despite the name).
- Full detail: `docs/CONSUMER_PROTO_AUDIT.md`.

---

## 7. What's DEFERRED (and why) — the two parked piles

### 7a. webpb (proto gap, deferred)
`webpb` is a ~46-operation **web-framework-as-gRPC API** (routing, handlers, middleware,
static files, templates, websockets, cookies, CSRF, CORS, security, server lifecycle,
auth, metrics). 94 of its message files are `string placeholder = 1` stubs — and they're
missing **both fields AND RPC wiring** (only 5 of ~46 operations are wired). **Nothing
consumes webpb.** Designing all of that blind, with no implementation to validate it,
would be throwaway. **Decision (owner, 2026-07-25): leave webpb intentionally unbuilt;
design it in the implementations effort below, against a real implementation.**

### 7b. The 33 service implementations (parked for a dedicated session)
gcommon defines gRPC services but implements none (protos-only). The owner wants, in the
future, **reusable common service implementations across multiple languages** (Go /
Python / Rust / …) that consumers can grab off the shelf — this is why `gcommon-go` was
archived rather than kept (clean slate). This is to be planned in a dedicated
**`ultracode` (multi-agent) session** — "about all the implementations and what to do."
The shelved planning package (superseded, reframe for multi-language) lives at
`~/repos/github.com/jdfalk/gcommon-plan-phase-c-services/docs/` — `IMPLEMENTATION_
STRATEGY.md`, `specs/2026-07-23-gcommon-phase-c-design.md`, and wave0/1/2 `TASK-*.md`
briefs, plus a 23-agent investigation (6 infra gaps + 4 bugs) that applies only if
services are revived.

---

## 8. Operational notes / gotchas (things that bit us)

- **`BUF_TOKEN`** is a **falkcorp ORG secret** (visibility: selected → gcommon). It's the
  personal BSR token from `~/.netrc` (`buf registry login` as `jdfalk`). If BSR pushes
  start failing with auth errors, re-check this secret.
- **`buf-push.yml` needs `--create`.** Without it, `buf push` targets an existing module
  and fails `not_found` on first publish. `--create` is idempotent; leave it in.
- **buf version skew:** CI uses **buf ~1.50** (via `buf-setup-action`); local dev often
  has **buf 1.71**. 1.50 flags **unused imports** (IMPORT_USED); 1.71 does NOT. So a
  locally-clean proto can fail CI. **After removing all `buf.validate` constraints from a
  file, remove the `buf/validate/validate.proto` import** or CI will fail.
- **`go_package` is excepted from breaking checks** (`FILE_SAME_GO_PACKAGE` in
  `buf.yaml`) — it's vestigial under BSR-managed distribution.
- **BSR Go SDKs work with the public sumdb** — an initial `sum.golang.org` 500 right after
  a push is just transient indexing lag; retry.
- **Merge discipline:** the repo is **rebase-only** and **not branch-protected**.
  Beware: merging a PR auto-deletes its branch, so pushing a late fix commit can silently
  re-create an orphan branch that never reaches the PR (this happened with #1138 →
  fixed via #1139). Verify a merge included ALL intended commits.
- **Force-push requires explicit per-instance confirmation** from the owner, even under
  broad "just do it" instructions.

---

## 9. How to resume — concrete next steps

Nothing is broken or half-finished on the proto side. When you come back:

1. **The big next thing:** run the **implementations `ultracode` session** — plan reusable
   multi-language common service implementations (and design webpb properly there). Start
   from §7b's planning package, reframed for multi-language + clean slate.
2. **If you just need to change a proto:** edit → `buf lint && buf format -w && buf breaking
   --against '.git#branch=main'` → PR → merge → `git tag -a vX.Y.Z && git push origin
   vX.Y.Z` (publishes to BSR) → optional `gh release create`.
3. **If a new repo starts consuming gcommon:** point it at the BSR SDKs (§3), not at the
   archived `gcommon-go`.

### Related docs & memory
- `docs/CONSUMER_PROTO_AUDIT.md` — deep audit of what the consumer uses + gap analysis.
- `docs/README.md` / repo `README.md` — the protos-only/BSR consumption model.
- Assistant memory (for AI sessions): `project_gcommon_phase_c`,
  `project_gcommon_impls_future`.
