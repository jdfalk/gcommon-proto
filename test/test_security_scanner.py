#!/usr/bin/env python3
"""Tests for security scanning and metrics utilities."""

from pathlib import Path
from unittest import mock

from scripts.security_scanner import SecurityScanner
from scripts.security_scanner import VulnerabilityRecord
from scripts.dependency_metrics import DependencyMetricsCollector, MetricRecord


def test_check_license_compliance_flags_unapproved(tmp_path: Path) -> None:
    scanner = SecurityScanner(tmp_path)
    with mock.patch(
        "scripts.security_scanner.LicenseChecker.collect_license_data",
        return_value={"badpkg": "GPL-3.0"},
    ):
        licenses = scanner.check_license_compliance()
    assert licenses["badpkg"] == "GPL-3.0"


def test_monitor_security_advisories_empty(tmp_path: Path) -> None:
    scanner = SecurityScanner(tmp_path)
    scanner.monitor_security_advisories()


def test_dependency_metrics_summary() -> None:
    collector = DependencyMetricsCollector(Path("."))
    collector.results.append(MetricRecord("mod", "metric", 1.0, "unit"))
    summary = collector.summarize_metrics()
    assert "mod" in summary


def test_apply_security_updates_runs_commands(tmp_path: Path) -> None:
    scanner = SecurityScanner(tmp_path)
    vuln = VulnerabilityRecord(
        package="a", identifier="1", severity="HIGH", summary="", fixed_version="v1"
    )
    (tmp_path / "go.mod").write_text("module x\n\nrequire a v0.0.0\n", encoding="utf-8")
    with mock.patch("subprocess.run") as run:
        scanner.apply_security_updates([vuln])
        assert run.called


def test_schedule_regular_scans_creates_file(tmp_path: Path) -> None:
    scanner = SecurityScanner(tmp_path)
    scanner.schedule_regular_scans(1)
    assert (tmp_path / ".security_scan_schedule").exists()


def test_save_report(tmp_path: Path) -> None:
    collector = DependencyMetricsCollector(Path("."))
    collector.results.append(MetricRecord("mod", "metric", 2.0, "unit"))
    out = tmp_path / "report.json"
    collector.save_report(out)
    data = out.read_text()
    assert "mod" in data
