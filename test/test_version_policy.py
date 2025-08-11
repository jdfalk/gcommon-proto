#!/usr/bin/env python3
"""Tests for version policy utilities."""

from pathlib import Path
from unittest import mock

import yaml

from scripts.version_policy import VersionPolicyManager


def test_enforce_go_versions(tmp_path: Path) -> None:
    policy = {
        "go": {"example.com/mod": {"minimum": "1.2.0"}},
        "node": {},
    }
    config = tmp_path / "config"
    config.mkdir()
    policy_file = config / "version-policy.yml"
    policy_file.write_text(yaml.safe_dump(policy), encoding="utf-8")

    manager = VersionPolicyManager(tmp_path)
    manager.load_default_policy()

    fake_output = "module\nexample.com/mod v1.0.0\n"
    with mock.patch("subprocess.run") as run:
        run.return_value.stdout = fake_output
        run.return_value.returncode = 0
        violations = manager.enforce_go_versions()
    assert violations and "example.com/mod" in violations[0][0]
