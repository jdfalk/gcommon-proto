#!/usr/bin/env python3
# file: ci/pipeline/__init__.py
# version: 1.0.0
# guid: 6f0c1e88-fbd1-4c82-8614-91c0ef9b1a0e
"""CI/CD pipeline package.

This package contains modules that provide a skeleton for advanced
CI/CD pipeline features such as configuration management, stage
execution, quality gates, reporting, and deployment automation.

Each module is currently a placeholder and must be fully implemented.

TODO: Implement actual pipeline integration logic.
TODO: Add unit tests for all modules in this package.
"""

# Expose primary entry points for convenience
from .config import PipelineConfig, load_default_config
from .stages import (
    LintStage,
    UnitTestStage,
    IntegrationTestStage,
    EndToEndStage,
    CompatibilityStage,
    PerformanceStage,
    SecurityStage,
    DocumentationStage,
    ReleaseStage,
    DeploymentStage,
    NotificationStage,
)
from .quality_gates import run_default_gates
from .reports import generate_and_send_report
from .deployment import (
    execute_default_deployment,
    execute_default_rollback,
)

__all__ = [
    "PipelineConfig",
    "load_default_config",
    "LintStage",
    "UnitTestStage",
    "IntegrationTestStage",
    "EndToEndStage",
    "CompatibilityStage",
    "PerformanceStage",
    "SecurityStage",
    "DocumentationStage",
    "ReleaseStage",
    "DeploymentStage",
    "NotificationStage",
    "run_default_gates",
    "generate_and_send_report",
    "execute_default_deployment",
    "execute_default_rollback",
]

# End of package initialization
# TODO: Add package-level configuration helpers.
