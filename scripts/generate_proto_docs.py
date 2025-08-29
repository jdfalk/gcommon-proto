#!/usr/bin/env python3
# file: scripts/generate_proto_docs.py
# version: 1.1.0
# guid: 9f4c4d9e-2d2b-4c53-9457-3a5bb0d6f8aa
"""
Automated Protocol Buffer Markdown documentation generator.

Design Goals:
  * Zero external dependencies (stdlib only) for portability in CI.
  * Deterministic output (sorted file ordering, stable grouping) for clean diffs.
  * Reasonable module splitting so very large domains are broken into numbered chunks.
  * Heuristic grouping to mirror existing structure (base, api_N, config(_N), services, events).
  * Lightweight dependency graph between modules inferred from import paths.
  * Automatic prettier formatting for consistent markdown output.

Grouping Heuristics:
  Domain = immediate directory under proto/gcommon/v1 (e.g. auth, queue, web).
  File classification precedence (first match wins):
    1. services: name contains "service" and endswith .proto
    2. events:   name contains "event"
    3. config:   name contains "config"
    4. api:      name ends with _request.proto or _response.proto OR starts with an action verb
    5. base:     everything else (core model / enum definitions)

  Large groups are split when file count > threshold (default 50) into suffixed chunks _1, _2, ...
  api groups always receive numeric suffixes when split (api_1, api_2, ...).

Issue Detection (Placeholder):
  The prior manually created docs referenced per-file issue counts. Implementing
  detailed lint-based issue extraction would require integrating buf or a linter
  parser. For now we expose a simple hook (detect_issues_for_file) that returns 0.
  Future enhancement: call `buf lint --path` and parse stderr for each file.

Output Structure:
  proto-docs/
    README.md               Master index & summary
    <module>.md             One file per generated module

Prettier Formatting:
  After generating all markdown files, the script automatically runs prettier to ensure
  consistent formatting. It first tries to use the local copilot-agent-util binary
  (if available), then falls back to direct prettier command. This eliminates the need
  for manual formatting fixes and ensures consistent output across all generated docs.

Idempotency:
  Existing generated files (matching current module naming patterns) are removed
  before regeneration unless --no-clean is supplied.

CLI:
  --proto-dir DIR     Root proto directory (default: proto/gcommon/v1)
  --out DIR           Output directory (default: proto-docs)
  --threshold N       Split threshold (default: 50)
  --dry-run           Compute & log plan without writing files
  --no-clean          Do not delete existing module docs
  --verbose           Extra logging

This script is considered generated-doc automation (not hand-authored docs); direct
commits are acceptable per repository documentation policy.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Set, Tuple

ACTION_VERBS = {
    "add",
    "ack",
    "acknowledge",
    "assign",
    "authenticate",
    "authorize",
    "backup",
    "batch",
    "begin",
    "change",
    "commit",
    "complete",
    "configure",
    "connect",
    "create",
    "delete",
    "disable",
    "enable",
    "finalize",
    "generate",
    "get",
    "import",
    "list",
    "lock",
    "migrate",
    "publish",
    "queue",
    "receive",
    "recover",
    "register",
    "remove",
    "render",
    "reset",
    "restore",
    "revoke",
    "rollback",
    "schedule",
    "set",
    "start",
    "stop",
    "subscribe",
    "unwatch",
    "update",
    "upgrade",
    "validate",
    "watch",
}

MSG_RE = re.compile(r"^\s*message\s+([A-Za-z0-9_]+)", re.MULTILINE)
ENUM_RE = re.compile(r"^\s*enum\s+([A-Za-z0-9_]+)", re.MULTILINE)
SERVICE_RE = re.compile(r"^\s*service\s+([A-Za-z0-9_]+)", re.MULTILINE)
IMPORT_RE = re.compile(r'^\s*import\s+"([^"]+)";', re.MULTILINE)
PACKAGE_RE = re.compile(r"^\s*package\s+([A-Za-z0-9_.]+);", re.MULTILINE)


@dataclass
class ProtoFileInfo:
    path: Path
    rel_path: str
    domain: str
    classification: str
    package: str = ""
    messages: List[str] = field(default_factory=list)
    enums: List[str] = field(default_factory=list)
    services: List[str] = field(default_factory=list)
    imports: List[str] = field(default_factory=list)
    line_count: int = 0
    issues: int = 0


@dataclass
class ModuleDoc:
    name: str
    files: List[ProtoFileInfo] = field(default_factory=list)
    dependencies: Set[str] = field(default_factory=set)
    dependents: Set[str] = field(default_factory=set)  # populated after graph build

    @property
    def counts(self) -> Tuple[int, int, int, int, int]:
        pf = len(self.files)
        msgs = sum(len(f.messages) for f in self.files)
        svcs = sum(len(f.services) for f in self.files)
        ens = sum(len(f.enums) for f in self.files)
        issues = sum(f.issues for f in self.files)
        return pf, msgs, svcs, ens, issues


def detect_issues_for_file(_text: str) -> int:
    # Placeholder: always zero.
    return 0


def classify_file(filename: str) -> str:
    base = filename.lower()
    if "service" in base:
        return "services"
    if "event" in base:
        return "events"
    if "config" in base:
        return "config"
    stem = base.rsplit(".", 1)[0]
    if stem.endswith("_request") or stem.endswith("_response"):
        return "api"
    first_token = stem.split("_")[0]
    if first_token in ACTION_VERBS:
        return "api"
    return "base"


def scan_proto_file(path: Path, rel_root: Path) -> ProtoFileInfo:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        # If we can't read the file, return minimal info
        return ProtoFileInfo(
            path=path,
            rel_path=str(path),
            domain="unknown",
            classification="base",
            line_count=0,
        )

    rel_path = (
        str(path.relative_to(rel_root.parent.parent))
        if "gcommon" in path.parts
        else str(path)
    )
    # domain = part after v1
    try:
        idx = path.parts.index("v1")
        domain = path.parts[idx + 1]
    except ValueError:
        domain = "unknown"
    classification = classify_file(path.name)

    # Parse package name
    package_match = PACKAGE_RE.search(text)
    package = package_match.group(1) if package_match else ""

    # Parse messages, enums, services
    messages = [m.group(1) for m in MSG_RE.finditer(text)]
    enums = [e.group(1) for e in ENUM_RE.finditer(text)]
    services = [s.group(1) for s in SERVICE_RE.finditer(text)]
    imports = [i.group(1) for i in IMPORT_RE.finditer(text)]

    line_count = len(text.splitlines())
    issues = detect_issues_for_file(text)

    return ProtoFileInfo(
        path=path,
        rel_path=rel_path,
        domain=domain,
        classification=classification,
        package=package,
        messages=messages,
        enums=enums,
        services=services,
        imports=imports,
        line_count=line_count,
        issues=issues,
    )


def build_modules(files: List[ProtoFileInfo], threshold: int) -> Dict[str, ModuleDoc]:
    modules: Dict[str, ModuleDoc] = {}
    # Organize by domain + classification bucket
    buckets: Dict[Tuple[str, str], List[ProtoFileInfo]] = {}
    for f in files:
        key = (f.domain, f.classification)
        buckets.setdefault(key, []).append(f)

    for (domain, classification), flist in buckets.items():
        flist.sort(key=lambda x: x.rel_path)
        base_module_name = (
            domain if classification == "base" else f"{domain}_{classification}"
        )

        # Create type-specific modules for each classification
        # Collect all files for this domain+classification
        modules[base_module_name] = ModuleDoc(name=base_module_name, files=flist)
    return modules


def build_type_modules(base_modules: Dict[str, ModuleDoc]) -> Dict[str, ModuleDoc]:
    """Split each base module into type-specific modules (enums, services, messages)."""
    type_modules: Dict[str, ModuleDoc] = {}

    # Collect files by domain only (not domain_classification)
    domain_files: Dict[str, List[ProtoFileInfo]] = {}

    for base_name, base_module in base_modules.items():
        for file_info in base_module.files:
            domain = file_info.domain
            domain_files.setdefault(domain, []).extend([file_info])

    # Remove duplicates and create type-specific modules per domain
    for domain, all_files in domain_files.items():
        # Remove duplicates
        unique_files = list({f.path: f for f in all_files}.values())

        # Separate by content type
        enums_files = [f for f in unique_files if f.enums]
        services_files = [f for f in unique_files if f.services]
        messages_files = [f for f in unique_files if f.messages]

        # Create type-specific modules only if they have content
        if enums_files:
            type_modules[f"{domain}_enums"] = ModuleDoc(
                name=f"{domain}_enums", files=enums_files
            )
        if services_files:
            type_modules[f"{domain}_services"] = ModuleDoc(
                name=f"{domain}_services", files=services_files
            )
        if messages_files:
            type_modules[f"{domain}_messages"] = ModuleDoc(
                name=f"{domain}_messages", files=messages_files
            )

    return type_modules


def infer_dependencies(modules: Dict[str, ModuleDoc], rel_root: Path):
    # Map proto path (import string) to module
    file_to_module: Dict[str, str] = {}
    for m in modules.values():
        for f in m.files:
            # The import statements likely use paths relative to proto/ root
            # We'll try normalization to match patterns like pkg/<domain>/proto/filename.proto OR google/...
            file_to_module[f.rel_path.split("/proto/")[-1]] = m.name

    for m in modules.values():
        dep_modules: Set[str] = set()
        for f in m.files:
            for imp in f.imports:
                # Only map if it's one of our local paths containing /proto/
                if "/proto/" in imp:
                    local_key = imp.split("/proto/")[-1]
                    for candidate, mod_name in file_to_module.items():
                        if candidate.endswith(local_key):
                            if mod_name != m.name:
                                dep_modules.add(mod_name)
        m.dependencies = dep_modules
    # Populate dependents
    for m in modules.values():
        for dep in m.dependencies:
            if dep in modules:
                modules[dep].dependents.add(m.name)


def write_module_doc(module: ModuleDoc, out_dir: Path):
    pf, msgs, svcs, ens, issues = module.counts

    # Determine the type focus based on module name
    if module.name.endswith("_enums"):
        type_focus = "enums"
        type_title = "Enums"
    elif module.name.endswith("_services"):
        type_focus = "services"
        type_title = "Services"
    elif module.name.endswith("_messages"):
        type_focus = "messages"
        type_title = "Messages"
    else:
        type_focus = "all"
        type_title = "All Types"

    lines: List[str] = []
    lines.append(f"# {module.name.replace('_', ' ').title()} Documentation\n")
    lines.append("[← Back to Index](./README.md)\n")

    lines.append("## Module Overview\n")
    lines.append(f"- **Proto Files**: {pf}")
    if type_focus == "enums" or type_focus == "all":
        lines.append(f"- **Enums**: {ens}")
    if type_focus == "services" or type_focus == "all":
        lines.append(f"- **Services**: {svcs}")
    if type_focus == "messages" or type_focus == "all":
        lines.append(f"- **Messages**: {msgs}")
    if issues:
        lines.append(f"- ⚠️ **Issues**: {issues}")
    lines.append("")

    # Create table of contents for the specific type
    lines.append("## Table of Contents\n")

    if type_focus == "enums" or type_focus == "all":
        all_enums = []
        for f in module.files:
            for enum_name in f.enums:
                all_enums.append((enum_name, f.path.name, f.path.stem))
        if all_enums:
            lines.append("### Enums\n")
            for enum_name, file_name, anchor in sorted(all_enums):
                lines.append(f"- [`{enum_name}`](#{anchor}) - from {file_name}")
            lines.append("")

    if type_focus == "services" or type_focus == "all":
        all_services = []
        for f in module.files:
            for service_name in f.services:
                all_services.append((service_name, f.path.name, f.path.stem))
        if all_services:
            lines.append("### Services\n")
            for service_name, file_name, anchor in sorted(all_services):
                lines.append(f"- [`{service_name}`](#{anchor}) - from {file_name}")
            lines.append("")

    if type_focus == "messages" or type_focus == "all":
        all_messages = []
        for f in module.files:
            for message_name in f.messages:
                all_messages.append((message_name, f.path.name, f.path.stem))
        if all_messages:
            lines.append("### Messages\n")
            for message_name, file_name, anchor in sorted(all_messages):
                lines.append(f"- [`{message_name}`](#{anchor}) - from {file_name}")
            lines.append("")

    # Files section
    lines.append("### Files in this Module\n")
    for f in module.files:
        anchor = f.path.stem
        issue_suffix = f" ⚠️ {f.issues} issues" if f.issues else ""
        lines.append(f"- [{f.path.name}](#{anchor}){issue_suffix}")
    lines.append("")

    if module.dependencies:
        lines.append("## Module Dependencies\n")
        if module.dependencies:
            lines.append("**This module depends on**:\n")
            for dep in sorted(module.dependencies):
                lines.append(f"- [{dep}](./{dep}.md)")
            lines.append("")
        if module.dependents:
            lines.append("**Modules that depend on this one**:\n")
            for dep in sorted(module.dependents):
                lines.append(f"- [{dep}](./{dep}.md)")
            lines.append("")

    lines.append("---\n")
    lines.append(f"\n## {type_title} Documentation\n")

    for f in module.files:
        anchor = f.path.stem
        lines.append(f"### {f.path.name} {{#{anchor}}}\n")
        package_info = (
            f"**Package**: `{f.package}`" if f.package else "**Package**: *(not found)*"
        )
        lines.append(
            f"**Path**: `{f.rel_path}` {package_info} **Lines**: {f.line_count}\n"
        )

        # Only show relevant types based on focus
        if type_focus == "enums" or type_focus == "all":
            if f.enums:
                lines.append(
                    f"**Enums** ({len(f.enums)}): `" + "`, `".join(f.enums) + "`"
                )
        if type_focus == "services" or type_focus == "all":
            if f.services:
                lines.append(
                    f"**Services** ({len(f.services)}): `"
                    + "`, `".join(f.services)
                    + "`"
                )
        if type_focus == "messages" or type_focus == "all":
            if f.messages:
                lines.append(
                    f"**Messages** ({len(f.messages)}): `"
                    + "`, `".join(f.messages)
                    + "`"
                )

        if f.imports:
            lines.append("\n**Imports** ({}):\n".format(len(f.imports)))
            for imp in f.imports:
                lines.append(f"- `{imp}`")
        lines.append("\n#### Source Code\n")
        lines.append("```protobuf")
        try:
            lines.extend(f.path.read_text().splitlines())
        except Exception as e:  # pragma: no cover
            lines.append(f"// Error reading file: {e}")
        lines.append("``" + "`")
        lines.append("\n---\n")

    out_path = out_dir / f"{module.name}.md"
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(modules: Dict[str, ModuleDoc], out_dir: Path):
    total_files = sum(len(m.files) for m in modules.values())
    total_msgs = sum(sum(len(f.messages) for f in m.files) for m in modules.values())
    total_svcs = sum(sum(len(f.services) for f in m.files) for m in modules.values())
    total_enums = sum(sum(len(f.enums) for f in m.files) for m in modules.values())
    total_issues = sum(sum(f.issues for f in m.files) for m in modules.values())
    lines: List[str] = []
    lines.append("# Protocol Buffer Documentation\n")
    lines.append(
        f"Generated on: {dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}\n"
    )
    lines.append("## Overview\n")
    lines.append(
        f"This documentation covers {total_files} protocol buffer files organized into {len(modules)} modules, containing:\n"
    )
    lines.append(f"- **{total_msgs}** message definitions")
    lines.append(f"- **{total_svcs}** service definitions")
    lines.append(f"- **{total_enums}** enum definitions")
    if total_issues:
        lines.append(f"- ⚠️ **{total_issues}** issues requiring attention")
    lines.append("\n## Modules\n")

    # Group modules by domain
    domains: Dict[str, List[str]] = {}
    for name in sorted(modules.keys()):
        # Extract domain from module name (e.g., "common_enums" -> "common")
        domain = name.split("_")[0]
        domains.setdefault(domain, []).append(name)

    # Write grouped sections
    for domain in sorted(domains.keys()):
        lines.append(f"### {domain}\n")

        # Group by type within domain
        domain_modules = domains[domain]
        enums_modules = [n for n in domain_modules if n.endswith("_enums")]
        services_modules = [n for n in domain_modules if n.endswith("_services")]
        messages_modules = [n for n in domain_modules if n.endswith("_messages")]

        # Write each type
        for module_name in enums_modules + services_modules + messages_modules:
            m = modules[module_name]
            pf, msgs, svcs, ens, issues = m.counts

            # Extract type from module name
            module_type = module_name.split("_")[-1]
            lines.append(f"#### [{domain}_{module_type}](./{module_name}.md)\n")

            lines.append(f"- **Files**: {pf}")
            if msgs > 0:
                lines.append(f"- **Messages**: {msgs}")
            if svcs > 0:
                lines.append(f"- **Services**: {svcs}")
            if ens > 0:
                lines.append(f"- **Enums**: {ens}")
            if issues:
                lines.append(f"- ⚠️ **Issues**: {issues}")
            lines.append("")

        lines.append("")  # Extra spacing between domains
    (out_dir / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def remove_existing(out_dir: Path, verbose: bool):
    if not out_dir.exists():
        return
    for p in out_dir.glob("*.md"):
        if p.name == "README.md":
            continue
        p.unlink()
        if verbose:
            print(f"Removed {p}")


def run_prettier(out_dir: Path, verbose: bool):
    """Run prettier on the generated markdown files to ensure consistent formatting."""
    # Check if copilot-agent-util is available first
    copilot_util_path = Path("./copilot-agent-util")
    if copilot_util_path.exists():
        if verbose:
            print("Running prettier via copilot-agent-util...")
        try:
            result = subprocess.run(
                [str(copilot_util_path), "prettier", "prettier", "--write", str(out_dir)],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0:
                if verbose:
                    print("✅ Prettier formatting completed successfully")
            else:
                if verbose:
                    print(f"⚠️ Prettier via copilot-agent-util failed: {result.stderr}")
                # Fall back to direct prettier
                _run_direct_prettier(out_dir, verbose)
        except Exception as e:
            if verbose:
                print(f"⚠️ Error running copilot-agent-util prettier: {e}")
            # Fall back to direct prettier
            _run_direct_prettier(out_dir, verbose)
    else:
        # Try direct prettier
        _run_direct_prettier(out_dir, verbose)


def _run_direct_prettier(out_dir: Path, verbose: bool):
    """Fall back to running prettier directly."""
    try:
        result = subprocess.run(
            ["prettier", "--write", f"{out_dir}/*.md"],
            capture_output=True,
            text=True,
            check=False,
            shell=True
        )
        if result.returncode == 0:
            if verbose:
                print("✅ Direct prettier formatting completed successfully")
        else:
            if verbose:
                print(f"⚠️ Direct prettier failed: {result.stderr}")
                print("📝 Generated docs without prettier formatting")
    except Exception as e:
        if verbose:
            print(f"⚠️ Error running direct prettier: {e}")
            print("📝 Generated docs without prettier formatting")


def parse_args(argv: List[str]) -> argparse.Namespace:
    ap = argparse.ArgumentParser(
        description="Generate markdown docs for protobuf definitions"
    )
    ap.add_argument(
        "--proto-dir", default="proto/gcommon/v1", help="Root proto directory"
    )
    ap.add_argument("--out", default="proto-docs", help="Output directory")
    ap.add_argument(
        "--threshold", type=int, default=50, help="Split threshold per module"
    )
    ap.add_argument("--dry-run", action="store_true", help="Do not write files")
    ap.add_argument(
        "--no-clean", action="store_true", help="Do not remove existing docs"
    )
    ap.add_argument("--verbose", action="store_true", help="Verbose logging")
    return ap.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    proto_root = Path(args.proto_dir).resolve()
    out_dir = Path(args.out).resolve()
    if not proto_root.exists():
        print(f"Proto root not found: {proto_root}", file=sys.stderr)
        return 2
    # Collect proto files
    proto_files: List[ProtoFileInfo] = []
    for path in proto_root.rglob("*.proto"):
        proto_files.append(scan_proto_file(path, proto_root))
    if args.verbose:
        print(f"Discovered {len(proto_files)} .proto files under {proto_root}")

    # First build base modules by domain+classification
    base_modules = build_modules(proto_files, args.threshold)

    # Then split into type-specific modules
    modules = build_type_modules(base_modules)

    infer_dependencies(modules, proto_root)
    if args.dry_run:
        print("DRY RUN: Planned modules:")
        for name in sorted(modules):
            m = modules[name]
            pf, msgs, svcs, ens, issues = m.counts
            print(
                f"  {name}: files={pf} msgs={msgs} svcs={svcs} enums={ens} issues={issues}"
            )
        return 0
    out_dir.mkdir(parents=True, exist_ok=True)
    if not args.no_clean:
        remove_existing(out_dir, args.verbose)
    for m in modules.values():
        write_module_doc(m, out_dir)
    write_index(modules, out_dir)
    
    # Run prettier to format the generated markdown files
    run_prettier(out_dir, args.verbose)
    
    if args.verbose:
        print(f"Wrote {len(modules)} module docs to {out_dir}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main(sys.argv[1:]))
