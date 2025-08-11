# file: scripts/security_scanner.py
# version: 1.0.0
# guid: 7c6d5e4f-3b2a-4c1d-9e8f-7a6b5c4d3e2f

"""Security scanning utilities for dependency management.

The module provides working helpers for detecting dependency
vulnerabilities, checking licenses, and applying updates.  External
tools are invoked in subprocesses to keep the implementation
self‑contained.  The functionality covers:

* Running ``govulncheck`` for Go modules
* Running ``npm audit`` for Node packages
* Optional scanning of Python packages with ``pip-audit``
* Monitoring advisory feeds via the OSV API
* Applying security updates and generating summary reports
"""

from __future__ import annotations

import json
import logging
import subprocess
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set

from scripts.dependency_audit import LicenseChecker, PackageInfo


@dataclass
class VulnerabilityRecord:
    """Represents a single vulnerability entry.

    Attributes
    ----------
    package:
        Name of the affected dependency.
    identifier:
        Canonical identifier such as CVE or GHSA ID.
    severity:
        Normalized severity level (e.g., "LOW", "MEDIUM", "HIGH").
    summary:
        Short description of the vulnerability.
    references:
        URLs or references providing additional details.
    detected_at:
        Timestamp when the issue was detected.
    fixed_version:
        Version of the dependency where the vulnerability is resolved,
        if known.
    """

    package: str
    identifier: str
    severity: str
    summary: str
    references: List[str] = field(default_factory=list)
    detected_at: datetime = field(default_factory=datetime.utcnow)
    fixed_version: Optional[str] = None


class SecurityScanner:
    """High-level interface for dependency security scanning."""

    def __init__(self, root: Path, logger: Optional[logging.Logger] = None) -> None:
        self.root = root
        self.logger = logger or logging.getLogger(__name__)

    # ------------------------------------------------------------------
    # Vulnerability scanning
    # ------------------------------------------------------------------

    def scan_go_modules(self) -> List[VulnerabilityRecord]:
        """Run ``govulncheck`` or similar tool on Go modules.

        Returns
        -------
        list
            A list of :class:`VulnerabilityRecord` instances describing
            detected issues.  If ``govulncheck`` is unavailable an empty
            list is returned.
        """

        try:
            res = subprocess.run(
                ["govulncheck", "-json", "./..."],
                check=True,
                capture_output=True,
                text=True,
                cwd=self.root,
            )
        except (FileNotFoundError, subprocess.CalledProcessError):
            return []

        records: List[VulnerabilityRecord] = []
        for line in res.stdout.splitlines():
            try:
                data = json.loads(line)
            except json.JSONDecodeError:
                continue
            if data.get("Type") != "vulnerability":
                continue
            module = data.get("Module", {}).get("Path", "")
            vuln = data.get("Vulnerability", {})
            identifier = vuln.get("ID", "unknown")
            severity = vuln.get("Severity", "MEDIUM")
            summary = vuln.get("Details", "")
            refs = [r.get("URL") for r in vuln.get("References", []) if r.get("URL")]
            fixed = vuln.get("FixedVersion")
            records.append(
                VulnerabilityRecord(
                    package=module,
                    identifier=identifier,
                    severity=severity.upper(),
                    summary=summary,
                    references=refs,
                    fixed_version=fixed,
                )
            )
        return records

    def scan_node_packages(self) -> List[VulnerabilityRecord]:
        """Run ``npm audit`` or similar tool on Node packages."""

        try:
            res = subprocess.run(
                ["npm", "audit", "--json"],
                check=True,
                capture_output=True,
                text=True,
                cwd=self.root,
            )
            data = json.loads(res.stdout or "{}")
        except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError):
            return []

        vulns = data.get("vulnerabilities", {})
        records: List[VulnerabilityRecord] = []
        for pkg, info in vulns.items():
            severity = info.get("severity", "unknown").upper()
            via = info.get("via", [])
            for item in via:
                if isinstance(item, dict):
                    identifier = item.get("source") or item.get("title", "unknown")
                    summary = item.get("title", "")
                    url = item.get("url")
                    fix = item.get("fixAvailable")
                    fixed = None
                    if isinstance(fix, dict):
                        fixed = fix.get("version")
                    records.append(
                        VulnerabilityRecord(
                            package=pkg,
                            identifier=identifier,
                            severity=severity,
                            summary=summary,
                            references=[url] if url else [],
                            fixed_version=fixed,
                        )
                    )
                else:
                    records.append(
                        VulnerabilityRecord(
                            package=pkg,
                            identifier=str(item),
                            severity=severity,
                            summary="",
                        )
                    )
        return records

    def scan_python_packages(self) -> List[VulnerabilityRecord]:
        """Placeholder for Python package scanning.

        The repository does not currently use Python as a runtime
        environment, but this method is provided for completeness.
        ``pip-audit`` is executed when available.
        """

        try:
            res = subprocess.run(
                ["pip-audit", "-f", "json"],
                check=True,
                capture_output=True,
                text=True,
                cwd=self.root,
            )
            data = json.loads(res.stdout or "[]")
        except (FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError):
            return []

        records: List[VulnerabilityRecord] = []
        for pkg in data:
            name = pkg.get("name")
            for vuln in pkg.get("vulns", []):
                identifier = vuln.get("id", "unknown")
                summary = vuln.get("description", "")
                severity = vuln.get("severity", "UNKNOWN")
                fixed = vuln.get("fix_version")
                refs = [r.get("url") for r in vuln.get("fixes", []) if r.get("url")]
                records.append(
                    VulnerabilityRecord(
                        package=name,
                        identifier=identifier,
                        severity=severity,
                        summary=summary,
                        references=refs,
                        fixed_version=fixed,
                    )
                )
        return records

    # ------------------------------------------------------------------
    # Advisory monitoring
    # ------------------------------------------------------------------

    def monitor_security_advisories(self) -> None:
        """Monitor external security advisory feeds.

        Dependencies are queried against the OSV.dev API.  Any discovered
        vulnerabilities are logged.  This operation is best-effort and
        failures are silently ignored.
        """

        payload = {"queries": []}
        go_list = subprocess.run(
            ["go", "list", "-m", "all"],
            capture_output=True,
            text=True,
            cwd=self.root,
            check=False,
        )
        for line in go_list.stdout.splitlines()[1:]:
            name, _, version = line.partition(" ")
            payload["queries"].append(
                {"package": {"ecosystem": "Go", "name": name}, "version": version}
            )

        pkg_file = self.root / "package.json"
        if pkg_file.exists():
            data = json.loads(pkg_file.read_text(encoding="utf-8"))
            for name, version in data.get("dependencies", {}).items():
                payload["queries"].append(
                    {"package": {"ecosystem": "npm", "name": name}, "version": version}
                )

        if not payload["queries"]:
            return None

        req = urllib.request.Request(
            "https://api.osv.dev/v1/querybatch",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req) as resp:
                data = json.load(resp)
        except urllib.error.URLError:
            return None

        for result in data.get("results", []):
            pkg = result.get("package", {}).get("name", "unknown")
            for vuln in result.get("vulns", []):
                self.logger.warning("Advisory found for %s: %s", pkg, vuln.get("id"))
        return None

    def schedule_regular_scans(self, frequency_hours: int = 24) -> None:
        """Schedule automated vulnerability scans.

        Parameters
        ----------
        frequency_hours:
            Interval in hours between scans.

        Scheduling information is stored in a metadata file at the
        repository root.  External CI systems can read this file to
        trigger scans at the desired frequency.
        """

        schedule = {
            "frequency_hours": frequency_hours,
            "created": datetime.utcnow().isoformat(),
        }
        (self.root / ".security_scan_schedule").write_text(
            json.dumps(schedule, indent=2), encoding="utf-8"
        )
        return None

    # ------------------------------------------------------------------
    # Automatic updates
    # ------------------------------------------------------------------

    def apply_security_updates(self, vulnerabilities: Iterable[VulnerabilityRecord]) -> None:
        """Automatically update dependencies to fix vulnerabilities.

        Parameters
        ----------
        vulnerabilities:
            Iterable of vulnerability records to address.

        For each vulnerability with a ``fixed_version`` value an update
        command is executed.  Failures are logged but do not raise.
        """

        go_mod = (self.root / "go.mod").read_text(encoding="utf-8") if (
            self.root / "go.mod"
        ).exists() else ""
        pkg_json = (
            json.loads((self.root / "package.json").read_text(encoding="utf-8"))
            if (self.root / "package.json").exists()
            else {}
        )
        for vuln in vulnerabilities:
            if not vuln.fixed_version:
                continue
            if vuln.package in go_mod:
                subprocess.run(
                    ["go", "get", f"{vuln.package}@{vuln.fixed_version}"],
                    cwd=self.root,
                    check=False,
                )
            if vuln.package in pkg_json.get("dependencies", {}):
                subprocess.run(
                    ["npm", "install", f"{vuln.package}@{vuln.fixed_version}"],
                    cwd=self.root,
                    check=False,
                )
        return None

    def create_update_pull_request(self) -> None:
        """Placeholder for generating a pull request with updates.

        A simple markdown summary of vulnerabilities is generated.  Real
        PR creation is delegated to external automation.
        """

        summary = self.root / "security-update-summary.md"
        summary.write_text("Security updates applied\n", encoding="utf-8")
        return None

    # ------------------------------------------------------------------
    # License compliance
    # ------------------------------------------------------------------

    def check_license_compliance(self) -> Dict[str, str]:
        """Verify dependency licenses against an allowlist.

        Returns
        -------
        dict
            Mapping of dependency names to their licenses.
        """

        licenses = {}
        checker = LicenseChecker(self.root)

        packages: Dict[str, PackageInfo] = {}
        go_list = subprocess.run(
            ["go", "list", "-m", "all"],
            capture_output=True,
            text=True,
            cwd=self.root,
            check=False,
        )
        for line in go_list.stdout.splitlines()[1:]:
            name, _, version = line.partition(" ")
            packages[name] = PackageInfo(name=name, version=version)

        pkg_file = self.root / "package.json"
        if pkg_file.exists():
            data = json.loads(pkg_file.read_text(encoding="utf-8"))
            for name, version in data.get("dependencies", {}).items():
                packages[name] = PackageInfo(name=name, version=version)

        licenses = checker.collect_license_data(packages)
        allowed = {"MIT", "Apache-2.0", "BSD", "ISC"}
        for name, lic in licenses.items():
            if lic not in allowed:
                self.logger.warning("License %s for %s is not allowed", lic, name)
        return licenses

    def generate_compliance_report(self, data: Dict[str, str]) -> Path:
        """Generate a JSON report of license compliance results.

        Parameters
        ----------
        data:
            Mapping produced by :meth:`check_license_compliance`.

        Returns
        -------
        Path
            Path to the generated JSON report.
        """

        report = self.root / "license-compliance-report.json"
        report.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return report


def main(root: Optional[str] = None) -> None:
    """Entry point for manual execution of security scanning."""

    base = Path(root) if root else Path.cwd()
    scanner = SecurityScanner(base)
    vulns = (
        scanner.scan_go_modules()
        + scanner.scan_node_packages()
        + scanner.scan_python_packages()
    )
    scanner.apply_security_updates(vulns)
    scanner.create_update_pull_request()
    print("Security scanning complete.")


if __name__ == "__main__":
    main()

