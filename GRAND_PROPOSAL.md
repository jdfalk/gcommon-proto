<!-- file: GRAND_PROPOSAL.md -->
<!-- version: 1.1.0 -->
<!-- guid: 7f3b9b2e-8d5a-4b7a-9c3d-1a2f4e6b8c9d -->

# Grand Proposal: SDK Repos, Templates, and Distributed Architecture

This document evaluates the following updates:

- Splitting SDKs into language-specific repositories
- A lightweight template repository for shared GitHub resources
- Adding opinionated implementations on top of protobuf SDKs
- A distributed, locked-down service architecture with leader election and gossip-based membership

## 1) Split gcommon into three repos (protos-only + language SDKs)

Proposed split:

- gcommon (protos only)
- gcommon-go (generated Go SDK only)
- gcommon-py (generated Python SDK only)

Each SDK repo pulls protobufs from gcommon and runs buf generate to commit the outputs directly in the SDK repos (with go.mod/setup.py), making the SDKs clean, consumable artifacts.

### Advantages

- Clean module boundaries
- Each SDK becomes a first-class package with a simple import path and independent versioning/release cadence.
- Reduces confusion on pkg.go.dev and pip/packaging by removing nested modules.
- Consumer simplicity
- Go: `go get github.com/jdfalk/gcommon-go@vX.Y.Z` with clear import roots (e.g.,
	`github.com/jdfalk/gcommon-go/gcommon/v1/...`).
- Python: `pip install gcommon` (or `gcommon-proto`) via PyPI publishing from gcommon-py.
- CI isolation
- Linting, generation, and tests for each language are isolated and faster.
- SDK releases don’t require touching the proto repo (beyond tags), enabling independent hotfixes.
- Supply-chain clarity
- Least-privilege policies per repo; easier permissions, CODEOWNERS, and visibility controls.

### Disadvantages

- Coordination overhead
- Cross-repo changes require automation to keep versions in sync and avoid skew.
- Requires release choreography: proto tag → SDK generation → SDK tag/publish.
- More repos to maintain
	- Issues, discussions, and CI settings are spread across 3 repos.
	- Renovate/Dependabot and security policies duplicated (mitigated by template repo).
- Generated code as source
	- Committing generated artifacts can create large diffs and PR noise; mitigated by CI discipline and code owners.

### Automation plan (recommended)

Trigger: A tagged release (or merged PR) in gcommon → GitHub Actions pipeline:

1. Emit release metadata from gcommon: proto module version, changed packages set.
2. For each SDK repo:
  - Checkout SDK repo and gcommon at the tag.
  - Run `buf generate` (module=SDK module path) to regenerate SDK code.
  - Post-process (format, headers, init files) using existing helper scripts.
  - Bump SDK version (semantic mapping: patch/minor/major) based on proto change scope.
  - Commit, tag, and push.
  - Publish: Go—tag only; Python—build wheel, publish to PyPI.

Implementation options for “pulling protos”:

- Submodule gcommon in each SDK repo at `proto/` (fixed ref pinned to tag). Simple local dev; CI updates submodule then generates.
- Action-based checkout (no submodule). CI checks out gcommon@tag each run; keeps SDK repo clean.

Recommendation: Start with action-based checkout (no submodule) to reduce local tooling friction. Add a developer convenience script that fetches the same tag locally for iterative development.

### Effort estimate

- CI and scripts (per language): 1–2 days to implement robustly (lint, gen, version bumping, signing/releasing), plus 1 day for stabilization.
- Migration from monorepo SDKs: 0.5–1 day for repo scaffolding, first generation, and consumer testing.

## 2) Lightweight template repository

Create a small GitHub template repo (e.g., `template-repo-minimal`) that contains only the cross-repo essentials. This precedes any split so new repos start consistent.

### Contents

- .github/
	- workflows/
		- ci.yml (lint, build, test)
		- release.yml (language-agnostic scaffolding; call language-specific jobs via matrix/inputs)
		- security.yml (code scanning placeholder)
	- ISSUE_TEMPLATE/
		- bug_report.md
		- feature_request.md
	- PULL_REQUEST_TEMPLATE.md (align with our PR guidelines)
	- CODEOWNERS
	- Dependabot config (minimal)
- LICENSE (MIT or repo-standard)
- README.md (template with placeholders)
- CONTRIBUTING.md (short)

Optional per-language branches or folders with example configs (e.g., Go, Python) that can be cherry-picked.

### Process

1. Build `template-repo-minimal` first with the above structure.
2. When creating `gcommon-go` and `gcommon-py`, use GitHub “Use this template”.
3. Immediately add language-specific CI (buf generate, build/test, release jobs) and secrets.

### Effort estimate

- 0.5 day to curate a crisp template from ghcommon without the heavy bits.

## 3) Opinionated implementations on top of protobuf SDKs

Idea: In `gcommon-py` and `gcommon-go`, provide “common implementations” (e.g., CRUD for User) that encapsulate typical workflows on top of generated messages and services.

### Advantages

- Faster onboarding for app teams: batteries-included clients/services.
- Reduces duplication of glue code (serialization, validation, pagination patterns).
- Can enforce best practices (timeouts, retries, auth, metrics) centrally.

### Disadvantages

- Scope creep and tight coupling
	- Conflates transport schema (protos) with business behaviors/opinions; consumers may need different semantics.
	- Divergence risk across languages; maintaining feature parity is costly.
- Release complexity
	- Bugfixes in opinionated layers require coordinated releases independent of proto changes.
	- Larger surface area → higher stability expectations.
- Testing burden
	- Requires integration tests and perhaps test servers/mocks, increasing CI time.

### Recommendation

- Keep SDK repos “thin” (generated code + tiny helpers only). Put opinionated implementations in separate, language-specific libraries:
	- `gcommon-go-extras` and `gcommon-py-extras` (or `clients-*`).
	- These depend on the SDKs, not vice versa. This preserves a clean layering and gives adopters choice.

### Automation feasibility

- Feasible to scaffold with cookiecutter (Py) and templates (Go) plus CI to verify API stability and examples.
- Effort: 1–2 days per language for initial set (auth helpers, basic CRUD wrappers), then incremental.

## 4) Distributed architecture: locked-down web, distributed coordinator

Design goals:

- Web servers are minimal, stateless, and not part of cluster membership.
- Translation servers form a distributed control plane with leader election for coordination tasks.
- File servers provide storage/access and register with the translation cluster.
- Communication:
	- Web → Translation: gRPC (client-side load-balancing, mTLS, ACLs).
	- Translation ↔ File: gRPC.
	- Translation ↔ Translation: gossip for membership, Raft (or equivalent) for leadership/consensus tasks.

Terminology: “Translation server” (replace with the current canonical name if it has changed in docs).

### Membership and discovery

- Gossip: Use HashiCorp memberlist/Serf (Go) for failure detection and membership within the translation cluster.
- Bootstrapping: Seed list via config, DNS, or a well-known address.
- Web servers do not join gossip; they discover translation servers via DNS SRV, static list, or a small sidecar registry.
- File servers do not join gossip (per requirement). They register with any translation node via gRPC; the cluster replicates the registration (see below).

### Leader election and coordination

- Use a Raft library (e.g., hashicorp/raft) embedded in translation servers for:
	- Leader election.
	- Replicated metadata: service registry of file servers, job assignments, caches metadata.
	- Optional: scheduled tasks (cache warmups, periodic compaction, metrics rollups).
- Alternatively, rely on etcd/Consul as an external CP if we prefer managed infra over embedded consensus (trade-off: extra dependency vs. less maintenance code).

### Request flow

1. Client → Web server.
2. Web server checks cache/ACL; on miss, forwards request via gRPC to translation cluster (round-robin or pick-2).
3. Translation server executes business logic; if it needs storage, it uses the replicated registry to contact file server(s).
4. Translation returns response; web server caches according to policy and responds to client.

### ACLs and security

- mTLS between all internal hops.
- Fine-grained ACLs at the translation tier; web tier enforces coarse authN/Z and passes principal context.
- Rotate certificates via short-lived credentials (SPIFFE/SPIRE or Vault PKI) if feasible.

### Operational considerations

- Observability: OpenTelemetry tracing and metrics on all services.
- Backpressure and timeouts: enforce budgets across hops (web→translation→file).
- Rolling upgrades: translation cluster supports M-of-N without downtime; web servers are stateless and easy to roll.
- Disaster scenarios: leader loss (auto re-elect), split brain (Raft resolves), node churn (gossip stabilizes).

### Minimal tech stack (Go-first)

- Gossip: github.com/hashicorp/memberlist or github.com/hashicorp/serf
- Consensus: github.com/hashicorp/raft (or external etcd/Consul)
- gRPC: google.golang.org/grpc with xDS or pick_first/round_robin LB
- Discovery for web → translation: DNS SRV/Cloud Map/K8s headless service

### Incremental rollout plan

1. Introduce gossip-only membership in translation servers (no leader yet), observability wired.
2. Add Raft for leader election and a single replicated registry (file servers).
3. Point web servers to translation via DNS SRV; validate cache/miss flows.
4. Add advanced features: job orchestration, cache warmup, adaptive routing.

## 5) Recommended path and next steps

1. Create `template-repo-minimal` and standardize common GitHub configs. (0.5 day)
2. Keep opinionated logic out of SDK repos; create optional `*-extras` libraries later if needed.
3. Decide split vs. monorepo for SDKs:
	 - If current pkg.go.dev confusion persists or consumers prefer separate modules, proceed with split.
	 - Otherwise, we can remain monorepo and improve docs and release automation; the distributed architecture work is orthogonal.
4. Begin distributed architecture prototype in a feature branch:
	 - Memberlist + Raft scaffolding in translation service.
	 - Simple registry replication and a basic web→translation gRPC flow.

## 6) Scripting and CI details (sketch)

### Repo split automation

- One Python script (GitHub API):
	- Create `gcommon-go` and `gcommon-py` from template.
	- Set secrets (GH token, PyPI creds, etc.).
	- Push initial skeleton (README, buf.gen.yaml, go.mod/setup.py placeholders).
- Two CI workflows in each SDK repo:
	- `ci.yml`: lint, build, test (no generation on PRs unless desired for verification).
	- `release.yml`: on gcommon release webhook or manual dispatch → checkout gcommon@tag → buf generate → postprocess → bump version → tag/publish.

### Local developer scripts

- `scripts/fetch-protos.sh|py`: checkout gcommon at a tag/branch into a temp dir.
- `scripts/generate-sdk.sh`: run buf generate with correct module, run formatters, verify headers.

---

Questions to confirm:

- Final naming for translation service; adjust all references.
- Package name for Python on PyPI (`gcommon` vs `gcommon-proto`) to avoid clashes.
- Version mapping policy between proto and SDK repos (strict alignment vs. independent semver).

Appendix A: Risks

- Cross-repo synchronization bugs; mitigate by end-to-end release workflows and integration tests.
- Template repo drift; mitigate with periodic automation to sync workflow updates.
- Overly opinionated SDKs; mitigate by keeping opinions in separate `*-extras` repos.

