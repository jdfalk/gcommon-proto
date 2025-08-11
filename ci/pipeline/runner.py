#!/usr/bin/env python3
# file: ci/pipeline/runner.py
# version: 1.0.0
# guid: d5a3f4a2-0f71-4c5a-b063-4e9b2c2b445e
"""Pipeline runner orchestrating stages, quality gates and reports.

This module ties together the configuration system, stage implementations,
quality gates and reporting utilities to provide a high level interface for
running the CI/CD pipeline programmatically.  It is intentionally lightweight
and does not depend on any external orchestration framework.
"""

from __future__ import annotations

import argparse
import json
import pathlib
from typing import Dict, List

from .config import (
    PipelineConfig,
    load_default_config,
    override_with_env,
    validate_config,
)
from .quality_gates import QualityGateRunner, CoverageGate, PerformanceGate, SecurityGate, DocumentationGate, DependencyGate
from .reports import generate_and_send_report
from .stages import (
    CompatibilityStage,
    DeploymentStage,
    DocumentationStage,
    EndToEndStage,
    IntegrationTestStage,
    LintStage,
    NotificationStage,
    PerformanceStage,
    ReleaseStage,
    SecurityStage,
    UnitTestStage,
)


class PipelineRunner:
    """Execute pipeline stages based on configuration."""

    def __init__(self, config: PipelineConfig) -> None:
        self.config = config
        self.results: Dict[str, Dict[str, str]] = {}

    # ------------------------------------------------------------------
    # Stage execution helpers
    # ------------------------------------------------------------------
    def _record(self, name: str, result) -> None:
        self.results[name] = {
            "status": "success" if result.success else "failure",
            "details": result.output,
        }

    def run_stages(self) -> None:
        if self.config.lint.enabled:
            stage = LintStage(
                self.config.lint.gofmt,
                self.config.lint.eslint,
                self.config.lint.markdownlint,
            )
            self._record("lint", stage.run())

        if self.config.unit_tests.enabled:
            stage = UnitTestStage(coverage=self.config.unit_tests.coverage)
            self._record("unit-tests", stage.run())

        if self.config.integration_tests.enabled:
            stage = IntegrationTestStage(self.config.integration_tests.environments)
            self._record("integration-tests", stage.run())

        if self.config.integration_tests.include_e2e:
            stage = EndToEndStage()
            self._record("e2e-tests", stage.run())

        stage = CompatibilityStage()
        self._record("compatibility-tests", stage.run())

        if self.config.performance.enabled:
            stage = PerformanceStage()
            self._record("performance", stage.run())

        if self.config.security.enabled:
            stage = SecurityStage(
                self.config.security.gosec,
                self.config.security.npm_audit,
            )
            self._record("security", stage.run())

        if self.config.documentation.enabled:
            stage = DocumentationStage(
                self.config.documentation.build,
                self.config.documentation.lint,
            )
            self._record("documentation", stage.run())

        if self.config.release.enabled:
            stage = ReleaseStage()
            self._record("release", stage.run())

        if self.config.deployment.enabled:
            stage = DeploymentStage([env.name for env in self.config.deployment.environments])
            self._record("deployment", stage.run())

        if self.config.notification.enabled:
            stage = NotificationStage()
            self._record("notification", stage.run())

    # ------------------------------------------------------------------
    # Quality gates
    # ------------------------------------------------------------------
    def run_quality_gates(self) -> Dict[str, Dict[str, str]]:
        runner = QualityGateRunner()
        runner.add_gate(CoverageGate(self.config.unit_tests.coverage_threshold, pathlib.Path("coverage.out")))
        runner.add_gate(PerformanceGate(self.config.performance.regression_threshold, pathlib.Path("benchmark.txt")))
        runner.add_gate(SecurityGate(0, pathlib.Path("security-report.json")))
        runner.add_gate(DocumentationGate([pathlib.Path("README.md"), pathlib.Path("CHANGELOG.md")]))
        runner.add_gate(DependencyGate(pathlib.Path("dependency-report.json")))
        gate_results = runner.run()
        for name, result in gate_results.items():
            self.results[f"gate-{name}"] = {
                "status": "passed" if result.passed else "failed",
                "details": result.details,
            }
        return self.results

    # ------------------------------------------------------------------
    def generate_reports(self) -> None:
        generate_and_send_report(self.results)


def main() -> None:  # pragma: no cover - CLI entry
    parser = argparse.ArgumentParser(description="Run CI pipeline")
    parser.add_argument("--config", help="Path to config file", default=None)
    args = parser.parse_args()

    config = load_default_config()
    config = override_with_env(config)
    valid, errors = validate_config(config)
    if not valid:
        raise SystemExit("Invalid configuration: " + "; ".join(errors))

    runner = PipelineRunner(config)
    runner.run_stages()
    runner.run_quality_gates()
    runner.generate_reports()
    print(json.dumps(runner.results, indent=2))


if __name__ == "__main__":  # pragma: no cover - CLI entry
    main()
