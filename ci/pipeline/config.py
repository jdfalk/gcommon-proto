#!/usr/bin/env python3
# file: ci/pipeline/config.py
# version: 1.0.0
# guid: 1e4a8e06-5f9d-4c66-9bfd-1c47bba2d4a9
"""Pipeline configuration models.

This module contains dataclass-based configuration structures for the
CI/CD pipeline. Each structure defines settings for a specific stage or
feature. The actual loading from files or environment variables is not
implemented yet.

TODO: Implement configuration loading logic.
TODO: Validate configuration values and handle errors.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class RetryPolicy:
    """Policy describing retry behavior for a pipeline action.

    Attributes:
        attempts: Number of times to retry the action.
        delay_seconds: Delay between attempts in seconds.
        backoff_factor: Factor to multiply delay after each retry.

    TODO: Add jitter support to randomize delays.
    TODO: Integrate with workflow-level retry configuration.
    """

    attempts: int = 3
    delay_seconds: int = 30
    backoff_factor: float = 2.0


@dataclass
class StageBaseConfig:
    """Base configuration shared by all stages.

    Attributes:
        enabled: Whether the stage should run.
        retries: Retry policy for the stage.
        timeout_minutes: Optional timeout in minutes.

    TODO: Support conditional execution rules.
    TODO: Add environment variable overrides.
    """

    enabled: bool = True
    retries: RetryPolicy = field(default_factory=RetryPolicy)
    timeout_minutes: Optional[int] = None


@dataclass
class LintConfig(StageBaseConfig):
    """Configuration for lint stage.

    Attributes:
        gofmt: Whether to run gofmt.
        eslint: Whether to run ESLint.
        markdownlint: Whether to lint markdown files.

    TODO: Add configuration for additional linters.
    TODO: Allow selective directory linting.
    """

    gofmt: bool = True
    eslint: bool = True
    markdownlint: bool = True


@dataclass
class UnitTestConfig(StageBaseConfig):
    """Configuration for unit test stage.

    Attributes:
        coverage: Whether to collect coverage data.
        coverage_threshold: Minimum acceptable coverage percentage.
        race_detector: Enable Go race detector.

    TODO: Add support for parallel test execution.
    TODO: Allow per-module coverage thresholds.
    """

    coverage: bool = True
    coverage_threshold: float = 80.0
    race_detector: bool = False


@dataclass
class IntegrationTestConfig(StageBaseConfig):
    """Configuration for integration tests across modules.

    Attributes:
        environments: List of environments to test.
        matrix: Optional additional matrix dimensions.
        include_e2e: Whether to run end-to-end tests.

    TODO: Implement matrix combination handling.
    TODO: Support selective module inclusion.
    """

    environments: List[str] = field(
        default_factory=lambda: ["development", "staging", "production"]
    )
    matrix: Dict[str, List[str]] = field(default_factory=dict)
    include_e2e: bool = True


@dataclass
class PerformanceConfig(StageBaseConfig):
    """Configuration for performance benchmarks.

    Attributes:
        benchmark_iterations: Number of iterations for each benchmark.
        regression_threshold: Allowed regression percentage.
        track_trends: Whether to append results to trend log.

    TODO: Add notification thresholds for severe regressions.
    TODO: Support automated baseline generation.
    """

    benchmark_iterations: int = 5
    regression_threshold: float = 5.0
    track_trends: bool = True


@dataclass
class SecurityConfig(StageBaseConfig):
    """Configuration for security scanning.

    Attributes:
        gosec: Enable gosec scanning.
        npm_audit: Enable npm audit.
        trivy: Enable container image scanning with Trivy.

    TODO: Add configuration for SAST tools.
    TODO: Integrate with dependency review rules.
    """

    gosec: bool = True
    npm_audit: bool = True
    trivy: bool = True


@dataclass
class DocumentationConfig(StageBaseConfig):
    """Configuration for documentation build and validation.

    Attributes:
        build: Build documentation artifacts.
        lint: Lint markdown files.
        deploy: Deploy documentation site.

    TODO: Add link validation configuration.
    TODO: Support alternative documentation generators.
    """

    build: bool = True
    lint: bool = True
    deploy: bool = False


@dataclass
class ReleaseConfig(StageBaseConfig):
    """Configuration for release process.

    Attributes:
        semantic_versioning: Use semantic versioning.
        changelog: Generate changelog automatically.
        publish: Publish releases to remote registries.

    TODO: Implement pre-release channels.
    TODO: Allow custom release notes templates.
    """

    semantic_versioning: bool = True
    changelog: bool = True
    publish: bool = True


@dataclass
class DeploymentEnvironmentConfig(StageBaseConfig):
    """Configuration for a deployment environment.

    Attributes:
        name: Environment name.
        url: Base URL for deployment target.
        credentials: Optional credentials reference.

    TODO: Add rollout strategy options.
    TODO: Support infrastructure-as-code integration.
    """

    name: str = "development"
    url: str = "http://localhost"
    credentials: Optional[str] = None


@dataclass
class DeploymentConfig(StageBaseConfig):
    """Deployment configuration specifying environments.

    Attributes:
        environments: List of deployment environments.

    TODO: Implement canary and blue/green options.
    TODO: Add rollback configuration.
    """

    environments: List[DeploymentEnvironmentConfig] = field(
        default_factory=lambda: [DeploymentEnvironmentConfig()]
    )


@dataclass
class NotificationConfig(StageBaseConfig):
    """Configuration for notifications and reporting.

    Attributes:
        github_comments: Post status comments on GitHub.
        slack_webhook: Optional Slack webhook for notifications.
        email_recipients: Optional list of email addresses for reports.

    TODO: Add template customization.
    TODO: Support webhook retries on failure.
    """

    github_comments: bool = True
    slack_webhook: Optional[str] = None
    email_recipients: List[str] = field(default_factory=list)


@dataclass
class PipelineConfig:
    """Top-level configuration for the entire pipeline.

    Attributes:
        lint: Linting configuration.
        unit_tests: Unit test configuration.
        integration_tests: Integration test configuration.
        performance: Performance test configuration.
        security: Security scanning configuration.
        documentation: Documentation configuration.
        release: Release configuration.
        deployment: Deployment configuration.
        notification: Notification configuration.

    TODO: Provide method to load configuration from YAML/JSON.
    TODO: Validate configuration consistency across sections.
    """

    lint: LintConfig = field(default_factory=LintConfig)
    unit_tests: UnitTestConfig = field(default_factory=UnitTestConfig)
    integration_tests: IntegrationTestConfig = field(
        default_factory=IntegrationTestConfig
    )
    performance: PerformanceConfig = field(default_factory=PerformanceConfig)
    security: SecurityConfig = field(default_factory=SecurityConfig)
    documentation: DocumentationConfig = field(default_factory=DocumentationConfig)
    release: ReleaseConfig = field(default_factory=ReleaseConfig)
    deployment: DeploymentConfig = field(default_factory=DeploymentConfig)
    notification: NotificationConfig = field(default_factory=NotificationConfig)


def load_default_config() -> PipelineConfig:
    """Load a default configuration instance.

    This function currently returns a configuration with all default values.
    In the future it will parse a configuration file or environment variables
    to construct a customized configuration.

    TODO: Parse configuration from file or environment variables.
    TODO: Allow partial configuration overrides.
    """

    return PipelineConfig()


def merge_configs(base: PipelineConfig, overrides: PipelineConfig) -> PipelineConfig:
    """Merge two pipeline configurations.

    The overrides parameter takes precedence over values in the base
    configuration. Only shallow merging is performed at this time.

    TODO: Implement deep merge for nested dataclasses.
    TODO: Handle list merging strategies.
    """

    result = base
    if overrides.lint != base.lint:
        result.lint = overrides.lint
    if overrides.unit_tests != base.unit_tests:
        result.unit_tests = overrides.unit_tests
    if overrides.integration_tests != base.integration_tests:
        result.integration_tests = overrides.integration_tests
    if overrides.performance != base.performance:
        result.performance = overrides.performance
    if overrides.security != base.security:
        result.security = overrides.security
    if overrides.documentation != base.documentation:
        result.documentation = overrides.documentation
    if overrides.release != base.release:
        result.release = overrides.release
    if overrides.deployment != base.deployment:
        result.deployment = overrides.deployment
    if overrides.notification != base.notification:
        result.notification = overrides.notification
    return result


# End of config module
# TODO: Expand with serialization and validation utilities.
