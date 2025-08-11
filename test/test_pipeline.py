# file: test/test_pipeline.py
# version: 1.0.0
# guid: 0f7c8652-e16f-4a98-987c-4a96b20291fa
"""Tests for CI/CD pipeline components."""

from __future__ import annotations

import json
import pathlib

from ci.pipeline.config import PipelineConfig, merge_configs
from ci.pipeline.quality_gates import CoverageGate, QualityGateRunner
from ci.pipeline.stages import PipelineStage


class DummyStage(PipelineStage):
    """Simple stage executing an echo command for testing."""

    name = "dummy"

    def __init__(self, message: str) -> None:
        super().__init__([["echo", message]])

    def run(self):
        return self.run_command(self.commands[0])


def test_merge_configs_deep():
    base = PipelineConfig()
    override = PipelineConfig()
    override.lint.enabled = False
    merged = merge_configs(base, override)
    assert merged.lint.enabled is False
    assert base.lint.enabled is True  # ensure original not modified


def test_coverage_gate(tmp_path: pathlib.Path):
    report = tmp_path / "coverage.out"
    report.write_text("mode: set\nfile.go:1.1,1.1 1 1\ntotal: (statements) 50.0%")
    gate = CoverageGate(60.0, report)
    result = gate.evaluate()
    assert not result.passed
    assert "50.00" in result.details


def test_quality_gate_runner_handles_missing_files(tmp_path: pathlib.Path):
    gate = CoverageGate(80.0, tmp_path / "missing.out")
    runner = QualityGateRunner()
    runner.add_gate(gate)
    results = runner.run()
    assert "CoverageGate" in results
    assert not results["CoverageGate"].passed


def test_pipeline_stage_run_command():
    stage = DummyStage("hello")
    result = stage.run()
    assert result.success
    assert "hello" in result.output


def test_override_with_env(monkeypatch):
    from ci.pipeline.config import override_with_env

    config = PipelineConfig()
    monkeypatch.setenv("LINT_ENABLED", "false")
    monkeypatch.setenv("UNIT_TESTS_COVERAGE_THRESHOLD", "90")
    override_with_env(config)
    assert not config.lint.enabled
    assert config.unit_tests.coverage_threshold == 90


def test_validate_config_errors():
    from ci.pipeline.config import validate_config

    cfg = PipelineConfig()
    cfg.unit_tests.coverage_threshold = 200  # invalid
    cfg.performance.regression_threshold = -1
    valid, errors = validate_config(cfg)
    assert not valid
    assert "coverage_threshold" in errors[0]


def test_config_serialization(tmp_path: pathlib.Path):
    from ci.pipeline.config import pipeline_config_to_dict, pipeline_config_from_dict, load_config_file

    cfg = PipelineConfig()
    cfg.lint.enabled = False
    data = pipeline_config_to_dict(cfg)
    assert data["lint"]["enabled"] is False
    file = tmp_path / "config.json"
    file.write_text(json.dumps(data))
    loaded = load_config_file(file)
    assert loaded.lint.enabled is False
