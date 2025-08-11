#!/usr/bin/env python3
# file: ci/pipeline/__init__.py
# version: 1.1.0
# guid: 6f0c1e88-fbd1-4c82-8614-91c0ef9b1a0e
"""CI/CD pipeline package.

The package now provides a functional pipeline implementation including
configuration management, stage execution, quality gates, deployment
helpers and reporting utilities.  It can be used programmatically via
the :class:`PipelineRunner` class or individual components may be
integrated into other tooling.
"""

# Expose primary entry points for convenience
from .config import (
    PipelineConfig,
    load_default_config,
    override_with_env,
    validate_config,
    pipeline_config_to_dict,
    pipeline_config_from_dict,
)
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
from .deployment import execute_default_deployment, execute_default_rollback
from .runner import PipelineRunner

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
    "PipelineRunner",
    "override_with_env",
    "validate_config",
    "pipeline_config_to_dict",
    "pipeline_config_from_dict",
]

# End of package initialization
# TODO: Add package-level configuration helpers.
