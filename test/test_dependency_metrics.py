#!/usr/bin/env python3
"""Tests for dependency metrics collector."""

from pathlib import Path
from unittest import mock

from scripts.dependency_metrics import DependencyMetricsCollector, MetricRecord


def test_summarize_and_save(tmp_path: Path) -> None:
    collector = DependencyMetricsCollector(Path("."))
    collector.results.append(MetricRecord("mod", "metric", 1.0, "u"))
    collector.results.append(MetricRecord("mod", "metric2", 2.0, "u"))
    report = tmp_path / "report.json"
    collector.save_report(report)
    data = report.read_text()
    assert "metric2" in data


def test_measure_go_build_time_handles_missing(tmp_path: Path) -> None:
    collector = DependencyMetricsCollector(tmp_path)
    with mock.patch("subprocess.run"):
        collector.measure_go_build_time()
    assert collector.results
