#!/usr/bin/env python3
# file: ci/pipeline/config.py
# version: 1.1.0
# guid: 1e4a8e06-5f9d-4c66-9bfd-1c47bba2d4a9
"""Pipeline configuration models.

This module defines dataclass based configuration structures used by the
pipeline runner.  Earlier versions of this file only provided the data
containers themselves.  The enhanced version implements comprehensive
configuration management utilities including loading from YAML/JSON
files, environment variable overrides, deep merging and validation.

The goal of this module is to provide a single, well typed source of
truth for all pipeline behaviour.  Each configuration section mirrors a
pipeline stage and exposes helper methods to serialise/deserialise the
settings.  The :func:`load_default_config` function now searches for a
configuration file named ``pipeline.json`` or ``pipeline.yaml`` and will
fall back to built in defaults when none is found.
"""

from __future__ import annotations

import json
import os
import pathlib
from dataclasses import asdict, dataclass, field, fields
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, get_type_hints

try:  # pragma: no cover - optional dependency
    import yaml  # type: ignore
except Exception:  # pragma: no cover - fallback when PyYAML is missing
    yaml = None  # type: ignore


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


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------
T = TypeVar("T")


def _dataclass_from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
    """Instantiate ``cls`` from a dictionary.

    The helper recursively constructs dataclass instances by matching keys in
    ``data`` to dataclass fields.  Unknown keys are ignored which allows users
    to supply partially specified configuration files without causing
    hard failures.

    Args:
        cls: Dataclass type to instantiate.
        data: Mapping of field names to values.

    Returns:
        Instance of ``cls`` populated with values from ``data``.
    """

    kwargs: Dict[str, Any] = {}
    hints = get_type_hints(cls)
    for f in fields(cls):
        value = data.get(f.name, None)
        if value is None:
            continue
        f_type = hints.get(f.name, f.type)
        if hasattr(f_type, "__dataclass_fields__") and isinstance(value, dict):
            kwargs[f.name] = _dataclass_from_dict(f_type, value)
        else:
            kwargs[f.name] = value
    return cls(**kwargs)  # type: ignore[arg-type]


def pipeline_config_from_dict(data: Dict[str, Any]) -> PipelineConfig:
    """Create a :class:`PipelineConfig` from a raw dictionary."""

    return _dataclass_from_dict(PipelineConfig, data)


def pipeline_config_to_dict(config: PipelineConfig) -> Dict[str, Any]:
    """Convert a :class:`PipelineConfig` into a serialisable dictionary."""

    return asdict(config)


def load_config_file(path: pathlib.Path) -> PipelineConfig:
    """Load configuration from a YAML or JSON file.

    The format is detected from the file extension.  YAML loading requires the
    optional ``pyyaml`` package.  When parsing fails or the file is empty a
    :class:`ValueError` is raised to signal misconfiguration.
    """

    if not path.exists():
        raise ValueError(f"Configuration file {path} does not exist")

    raw: Dict[str, Any]
    if path.suffix in {".yaml", ".yml"}:
        if yaml is None:  # pragma: no cover - optional dependency
            raise ValueError("PyYAML is required to load YAML configuration")
        raw = yaml.safe_load(path.read_text()) or {}
    else:
        raw = json.loads(path.read_text())

    if not isinstance(raw, dict):  # pragma: no cover - defensive check
        raise ValueError("Configuration file must contain a JSON/YAML object")

    return pipeline_config_from_dict(raw)


def load_default_config() -> PipelineConfig:
    """Load pipeline configuration.

    The function checks the ``PIPELINE_CONFIG`` environment variable for the
    path to a configuration file.  If not provided it searches for
    ``pipeline.yaml`` and ``pipeline.json`` in the current working directory.
    When no configuration is found, a config with default values is returned.
    """

    env_path = os.getenv("PIPELINE_CONFIG")
    candidate_paths = [
        pathlib.Path(env_path) if env_path else None,
        pathlib.Path("pipeline.yaml"),
        pathlib.Path("pipeline.yml"),
        pathlib.Path("pipeline.json"),
    ]

    for path in candidate_paths:
        if path and path.exists():
            try:
                cfg = load_config_file(path)
            except Exception:
                continue
            else:
                return cfg
    return PipelineConfig()


def deep_merge(base: Any, overrides: Any) -> Any:
    """Recursively merge ``overrides`` into ``base``.

    Dataclasses, dictionaries and lists are merged recursively.  Primitive
    values are replaced entirely.  This function returns a new merged object
    leaving the inputs untouched.
    """

    if isinstance(base, list) and isinstance(overrides, list):
        return base + [item for item in overrides if item not in base]
    if isinstance(base, dict) and isinstance(overrides, dict):
        result = {k: base.get(k) for k in base}
        for key, value in overrides.items():
            if key in result:
                result[key] = deep_merge(result[key], value)
            else:
                result[key] = value
        return result
    if hasattr(base, "__dataclass_fields__") and hasattr(overrides, "__dataclass_fields__"):
        merged: Dict[str, Any] = {}
        for f in fields(base):
            left = getattr(base, f.name)
            right = getattr(overrides, f.name)
            merged[f.name] = deep_merge(left, right)
        return type(base)(**merged)  # type: ignore[call-arg]
    return overrides


def merge_configs(base: PipelineConfig, overrides: PipelineConfig) -> PipelineConfig:
    """Merge two pipeline configurations deeply."""

    return deep_merge(base, overrides)


def override_with_env(config: PipelineConfig) -> PipelineConfig:
    """Override configuration values using environment variables.

    Only a limited subset of options is currently supported.  Environment
    variables are expected in upper case with sections separated by
    underscores, e.g. ``LINT_ENABLED`` or ``UNIT_TESTS_COVERAGE_THRESHOLD``.
    """

    mapping = {
        ("lint", "enabled"): "LINT_ENABLED",
        ("unit_tests", "coverage_threshold"): "UNIT_TESTS_COVERAGE_THRESHOLD",
        ("performance", "regression_threshold"): "PERFORMANCE_REGRESSION_THRESHOLD",
    }

    for (section, field_name), env_var in mapping.items():
        value = os.getenv(env_var)
        if value is None:
            continue
        section_obj = getattr(config, section)
        field_type = type(getattr(section_obj, field_name))
        try:
            if field_type is bool:
                cast_value = value.lower() in {"1", "true", "yes"}
            else:
                cast_value = field_type(value)
            setattr(section_obj, field_name, cast_value)
        except Exception:  # pragma: no cover - defensive
            continue
    return config


def validate_config(config: PipelineConfig) -> Tuple[bool, List[str]]:
    """Validate configuration and return (status, errors)."""

    errors: List[str] = []
    if config.unit_tests.coverage_threshold < 0 or config.unit_tests.coverage_threshold > 100:
        errors.append("coverage_threshold must be between 0 and 100")
    if config.performance.regression_threshold < 0:
        errors.append("regression_threshold cannot be negative")
    if config.performance.benchmark_iterations <= 0:
        errors.append("benchmark_iterations must be positive")
    return not errors, errors


# End of config module
