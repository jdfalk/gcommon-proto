#!/usr/bin/env python3
"""Tests for dependency optimizer utilities."""

import json
from pathlib import Path
from unittest import mock

from scripts.dependency_optimizer import (
    DependencyRecord,
    GoDependencyOptimizer,
    NodeDependencyOptimizer,
)


def test_go_scan_modules_parses_output(tmp_path: Path) -> None:
    optimizer = GoDependencyOptimizer(tmp_path)
    go_json = '{"Path":"example.com/mod","Version":"v1.0.0","Dir":"%s"}' % tmp_path
    with mock.patch("subprocess.run") as run:
        run.return_value.stdout = go_json
        modules = optimizer.scan_modules()
    assert "example.com/mod" in modules


def test_node_find_unused_packages(tmp_path: Path) -> None:
    (tmp_path / "package-lock.json").write_text(
        json.dumps({"packages": {"node_modules/a": {"name": "a", "version": "1.0.0"}}}),
        encoding="utf-8",
    )
    optimizer = NodeDependencyOptimizer(tmp_path)
    with mock.patch("subprocess.run") as run:
        run.return_value.stdout = json.dumps({"dependencies": ["a"]})
        unused = optimizer.find_unused_packages({})
    assert unused == ["a"]
