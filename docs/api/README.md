<!-- file: docs/api/README.md -->
<!-- version: 1.1.0 -->
<!-- guid: 3aa7517d-f590-425b-9c2d-4963faec14fd -->

# API Documentation

The `docs/api` directory contains all auto-generated references for the gcommon project.
It consolidates documentation for gRPC services, REST endpoints, and the underlying
Protobuf message definitions. All content in this directory is produced by automated
processes and should not be edited manually.

## Directory Structure

```
docs/api/
├── grpc/   # gRPC service and method docs with examples
├── rest/   # REST endpoint documentation and sample payloads
└── proto/  # Generated protobuf message and service references
```

Each subdirectory is regenerated during the release process to ensure accuracy and
freshness. Developers should rely on these artifacts when integrating with gcommon
services or generating client libraries.

## Generation Pipeline

The documentation pipeline performs several steps to keep API references current:

1. **Extract Comments** – Parses Go and Protobuf sources for doc comments.
2. **Compile Examples** – Collects runnable code snippets and example requests.
3. **Render Markdown** – Uses templates to convert metadata into human-readable pages.
4. **Link Cross References** – Builds hyperlinks between related messages, services,
   and REST resources.
5. **Validate Completeness** – Ensures every public type and endpoint is documented.
6. **Publish Artifacts** – Writes output to `docs/api/` and stages updates for commit.

The pipeline is triggered via the release script:

```bash
./scripts/release.sh docs
```

Developers can run the pipeline locally to preview changes.

## gRPC Documentation

The `grpc/` subdirectory contains a file for each gRPC service. Pages include:

- Service overview and purpose
- List of RPC methods with request and response types
- Example gRPC client invocations in Go and other languages
- Error codes and retry semantics
- Related messages and enums

To regenerate gRPC docs only:

```bash
make docs-grpc
```

## REST Documentation

REST documentation lives under `rest/` and mirrors the gRPC services where
applicable. Pages provide:

- Endpoint URLs and HTTP methods
- Query and path parameters
- Request and response body schemas
- CURL examples for quick testing
- Authentication and authorization requirements

To regenerate REST docs:

```bash
make docs-rest
```

## Protobuf Documentation

The `proto/` directory contains detailed references for all Protobuf messages,
services, and enums. Each file includes:

- Message and field descriptions
- Service RPC listings
- Cross-references to related messages
- Generated example payloads

Protobuf docs are built using `buf` and a custom renderer:

```bash
make docs-proto
```

## Go API Documentation

Although Go API docs are generated separately via `godoc`, this directory links to
external Go package documentation for convenience. Examples are extracted from
source code and surfaced in the gRPC and REST docs where relevant.

## Usage Guidelines

When adding or modifying APIs:

- Document all public fields and methods with clear comments.
- Provide example requests and responses in tests.
- Keep Protobuf comments in sync with Go structures.
- Run the documentation pipeline before submitting changes.

The automated system will flag missing documentation during CI if sections are
incomplete.

## Interactive Features

Future iterations will include interactive API explorers:

- **gRPC Playground** – Invoke RPCs directly from the docs using WebAssembly clients.
- **REST Console** – Craft and send HTTP requests with live responses.
- **Schema Browser** – Navigate message definitions with search and filtering.

These tools will enhance developer experience and reduce integration time.

## Versioning and Release

API documentation is versioned alongside the codebase. Each release captures the
state of the APIs at that point in time and publishes static assets for archival.
Older versions remain accessible for users pinned to previous releases.

## Contribution Workflow

1. Update code or Protobuf definitions with appropriate comments.
2. Run unit tests and ensure examples compile.
3. Execute the documentation pipeline locally:
   ```bash
   ./scripts/release.sh docs
   ```
4. Review generated files under `docs/api/`.
5. Submit doc updates via the documentation update system.

## Troubleshooting

- Ensure `buf` and required generators are installed.
- Verify that Protobuf packages have correct `go_package` options.
- Run `go vet` to catch malformed comments.
- Check the `docs/api` output for missing or malformed sections.

By maintaining comprehensive and up-to-date API documentation, gcommon enables
integrators to adopt modules quickly and confidently.