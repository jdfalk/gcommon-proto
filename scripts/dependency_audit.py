#!/usr/bin/env python3
# file: scripts/dependency_audit.py
# version: 1.1.0
# guid: 5f49bb34-5d21-4aa8-80aa-1a08fe123456

"""Dependency audit and optimization utilities.

This script analyzes Go and Node.js dependencies in the repository and
produces a JSON report highlighting used packages, unused packages, and
potential conflicts. It is intentionally written in a modular style so it can
be expanded with deeper analysis like license checks or automatic fixes.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set


@dataclass
class PackageInfo:
    """Represents metadata for a single package."""

    name: str
    version: str
    size: Optional[int] = None
    dependents: List[str] = field(default_factory=list)
    vulnerabilities: List[str] = field(default_factory=list)


@dataclass
class AuditReport:
    """Container for the full audit report."""

    go_packages: Dict[str, PackageInfo] = field(default_factory=dict)
    node_packages: Dict[str, PackageInfo] = field(default_factory=dict)
    unused_packages: List[str] = field(default_factory=list)
    conflicts: List[str] = field(default_factory=list)

    def to_json(self) -> str:
        """Serialize the report to a JSON string."""
        return json.dumps(
            {
                "go_packages": {k: vars(v) for k, v in self.go_packages.items()},
                "node_packages": {k: vars(v) for k, v in self.node_packages.items()},
                "unused_packages": self.unused_packages,
                "conflicts": self.conflicts,
            },
            indent=2,
            sort_keys=True,
        )

    def save(self, path: Path) -> None:
        """Save the report to *path* as pretty JSON."""
        path.write_text(self.to_json(), encoding="utf-8")


def _run_command(cmd: List[str]) -> str:
    """Run *cmd* and return its stdout as a string.

    Raises:
        RuntimeError: If the command exits with a non-zero status.
    """

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as exc:  # pragma: no cover - defensive
        raise RuntimeError("Command failed: {}".format(" ".join(cmd))) from exc
    return result.stdout


def _parse_go_list(raw: str) -> Dict[str, PackageInfo]:
    """Parse output from ``go list -m -json all``."""

    packages: Dict[str, PackageInfo] = {}
    for block in raw.split("}\n{"):
        block = block.strip().strip("{}")
        if not block:
            continue
        data = json.loads("{" + block + "}")
        packages[data["Path"]] = PackageInfo(
            name=data["Path"], version=data.get("Version", "unknown")
        )
    return packages


def collect_go_packages() -> Dict[str, PackageInfo]:
    """Collect Go modules used by the repository."""

    raw = _run_command(["go", "list", "-m", "-json", "all"])
    return _parse_go_list(raw)


def collect_node_packages(root: Path) -> Dict[str, PackageInfo]:
    """Collect Node.js packages using ``npm ls --json``."""

    raw = _run_command(["npm", "ls", "--json", "--depth=0"])
    data = json.loads(raw)
    packages: Dict[str, PackageInfo] = {}
    deps = data.get("dependencies", {})
    for name, meta in deps.items():
        packages[name] = PackageInfo(name=name, version=meta.get("version", "?"))
    return packages


def find_unused_go_packages(root: Path) -> List[str]:
    """Return a list of unused Go modules.

    The Go toolchain currently provides limited machine-readable output for
    unused modules. Rather than executing ``go mod tidy`` and parsing its text
    output, which can be brittle and disruptive, this function acts as a
    placeholder. It returns an empty list, but the structure allows future
    enhancements to analyze module usage more precisely.
    """

    _run_command(["go", "list", "-m", "all"])
    return []


def generate_report(root: Path) -> AuditReport:
    """Generate an :class:`AuditReport` for *root* repository."""

    report = AuditReport()
    report.go_packages = collect_go_packages()
    report.node_packages = collect_node_packages(root)
    report.unused_packages = find_unused_go_packages(root)
    return report


class LicenseChecker:
    """Utility class to verify dependency licenses.

    This placeholder exists to show where license verification logic
    would live.  It is intentionally verbose so future contributors know
    exactly what needs to be implemented.  The checker should eventually
    read license information from installed modules and compare it against
    an allowlist maintained by the project.
    """

    def __init__(self, root: Path) -> None:
        self.root = root

    def collect_license_data(self, packages: Dict[str, PackageInfo]) -> Dict[str, str]:
        """Collect license identifiers for *packages*.
        Returns a mapping of package name to license identifier.

        The function currently supports two ecosystems:

        * **Node.js** – Looks for ``package.json`` files under the
          ``node_modules`` directory and reads the ``license`` field.
        * **Go modules** – Executes ``go list -m -json`` to locate the module
          directory and attempts to read a ``LICENSE`` or ``COPYING`` file.  A
          very small subset of common licenses (MIT, Apache-2.0, BSD) is
          detected via keyword matching.  Modules without a detectable license
          are reported as ``UNKNOWN`` so they can be reviewed manually.
        """

        licenses: Dict[str, str] = {}
        node_root = self.root / "node_modules"

        for name in packages:
            pkg_license: Optional[str] = None

            # Node.js package detection
            pkg_json = node_root / name / "package.json"
            if pkg_json.exists():
                try:
                    data = json.loads(pkg_json.read_text(encoding="utf-8"))
                    pkg_license = data.get("license")
                except json.JSONDecodeError:
                    pkg_license = None

            if pkg_license:
                licenses[name] = pkg_license
                continue

            # Go module detection
            try:
                raw = _run_command(["go", "list", "-m", "-json", name])
                meta = json.loads(raw)
                module_dir = Path(meta.get("Dir", ""))
                for candidate in ["LICENSE", "LICENSE.txt", "LICENSE.md", "COPYING"]:
                    lic_path = module_dir / candidate
                    if lic_path.exists():
                        text = lic_path.read_text(encoding="utf-8", errors="ignore")
                        if "MIT" in text:
                            pkg_license = "MIT"
                        elif "Apache" in text:
                            pkg_license = "Apache-2.0"
                        elif "BSD" in text:
                            pkg_license = "BSD"
                        else:
                            pkg_license = "UNKNOWN"
                        break
            except RuntimeError:
                pkg_license = None

            licenses[name] = pkg_license or "UNKNOWN"

        return licenses

    def check_compliance(self, licenses: Dict[str, str]) -> List[str]:
        """Check collected *licenses* against an allowlist.

        Parameters
        ----------
        licenses:
            Mapping produced by :meth:`collect_license_data`.

        Returns
        -------
        list
            Names of packages with unapproved licenses.
        """

        allowed = {"MIT", "Apache-2.0", "BSD"}
        violations: List[str] = []
        for name, lic in licenses.items():
            if lic not in allowed:
                violations.append(name)
        return violations


class ConflictDetector:
    """Detects conflicting dependency versions.

    A conflict occurs when two different parts of the project require
    incompatible versions of the same dependency.  This class outlines
    the data structures and algorithms that would be used to detect such
    issues.
    """

    def __init__(self, packages: Dict[str, PackageInfo]) -> None:
        self.packages = packages

    def find_conflicts(self) -> List[str]:
        """Identify dependency conflicts.

        TODO
        ----
        Implement a dependency graph analysis that records version
        requirements for each package.  If multiple versions of the same
        package are detected, the method should return descriptive
        conflict messages.
        """

        versions: Dict[str, Set[str]] = {}
        for pkg in self.packages.values():
            versions.setdefault(pkg.name, set()).add(pkg.version)

        conflicts: List[str] = []
        for name, vers in versions.items():
            if len(vers) > 1:
                conflicts.append(f"{name}: {', '.join(sorted(vers))}")
        return conflicts


def extended_generate_report(root: Path) -> AuditReport:
    """Generate an extended audit report including license checks."""

    report = generate_report(root)
    checker = LicenseChecker(root)
    licenses = checker.collect_license_data({**report.go_packages, **report.node_packages})
    non_compliant = checker.check_compliance(licenses)
    detector = ConflictDetector({**report.go_packages, **report.node_packages})
    conflicts = detector.find_conflicts()
    report.conflicts.extend(conflicts)
    report.unused_packages.extend(non_compliant)
    return report


def main() -> None:
    """Entry point for command-line execution."""

    root = Path(os.getcwd())
    report = generate_report(root)
    output = root / "dependency-report.json"
    report.save(output)
    print("📦 Dependency report written to {}".format(output))


if __name__ == "__main__":
    main()
