#!/usr/bin/env python3
# file: test/test_dependency_audit.py
# version: 1.0.0
# guid: 123e4567-e89b-12d3-a456-426614174999
"""Tests for dependency audit utilities."""

import json
from pathlib import Path

from scripts.dependency_audit import ConflictDetector, LicenseChecker, PackageInfo


def test_licensechecker_collects_node_license(tmp_path: Path) -> None:
    """Ensure Node package licenses are detected correctly."""
    node_dir = tmp_path / "node_modules" / "demo"
    node_dir.mkdir(parents=True)
    (node_dir / "package.json").write_text(
        json.dumps({"name": "demo", "version": "1.0.0", "license": "MIT"}),
        encoding="utf-8",
    )
    checker = LicenseChecker(tmp_path)
    packages = {"demo": PackageInfo(name="demo", version="1.0.0")}
    licenses = checker.collect_license_data(packages)
    assert licenses["demo"] == "MIT"


def test_conflictdetector_detects_multiple_versions() -> None:
    """Detect conflicting versions of the same package."""
    packages = {
        "a@1": PackageInfo(name="a", version="1.0.0"),
        "a@2": PackageInfo(name="a", version="2.0.0"),
        "b@1": PackageInfo(name="b", version="1.0.0"),
    }
    detector = ConflictDetector(packages)
    conflicts = detector.find_conflicts()
    assert any("a" in item for item in conflicts)
