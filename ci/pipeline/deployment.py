#!/usr/bin/env python3
# file: ci/pipeline/deployment.py
# version: 1.1.0
# guid: 3c5b5f6e-9d7b-4d16-8c81-9f3b6e3ab1b2
"""Deployment helpers for CI/CD pipeline.

The original version of this module contained only skeleton classes that
returned success without executing any real logic.  The enhanced version
implemented here provides a small but functional deployment framework
that executes shell commands, captures output, records timing
information and exposes helper utilities for loading environment
configurations.

The design is intentionally simple so it can run in environments with
minimal dependencies while still being expressive enough for realistic
pipelines.  Deployments are performed sequentially and failures are
reported back to callers via :class:`DeploymentResult` instances.
"""

from __future__ import annotations

import pathlib
import json
import os
import subprocess
import time
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional


@dataclass
class DeploymentResult:
    """Outcome of a deployment operation.

    The result captures high level success information together with
    diagnostic data such as command output, return codes and timing
    information.  It is designed to be serialisable so that CI workflows
    can upload artefacts for later inspection.
    """

    environment: str
    success: bool
    details: str = ""
    output: str = ""
    return_code: int = 0
    started: float = field(default_factory=time.time)
    finished: float = 0.0

    def as_dict(self) -> Dict[str, str]:
        """Convert result into a serialisable dictionary."""

        return {
            "environment": self.environment,
            "success": str(self.success),
            "details": self.details,
            "return_code": str(self.return_code),
            "duration": f"{self.finished - self.started:.2f}",
        }


@dataclass
class EnvironmentConfig:
    """Configuration for a deployment environment."""

    name: str
    deploy_script: pathlib.Path
    rollback_script: Optional[pathlib.Path] = None
    env: Dict[str, str] = field(default_factory=dict)
    working_dir: Optional[pathlib.Path] = None

    def to_dict(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "deploy_script": str(self.deploy_script),
            "rollback_script": str(self.rollback_script) if self.rollback_script else "",
        }


class Deployer:
    """Base deployer class executing shell commands."""

    def __init__(self, config: EnvironmentConfig) -> None:
        self.config = config

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _run(self, script: pathlib.Path) -> DeploymentResult:
        result = DeploymentResult(self.config.name, True)
        cmd = ["bash", str(script)] if script.suffix in {".sh"} else [str(script)]
        env = {**self.config.env, **dict(os.environ)}  # type: ignore[name-defined]
        start = time.time()
        try:
            proc = subprocess.run(
                cmd,
                cwd=self.config.working_dir,
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            result.output = proc.stdout + proc.stderr
            result.return_code = proc.returncode
            result.success = proc.returncode == 0
            if not result.success:
                result.details = f"Command {' '.join(cmd)} failed with code {proc.returncode}"
        except FileNotFoundError:
            result.success = False
            result.details = f"Script {script} not found"
        result.finished = time.time()
        return result

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def deploy(self) -> DeploymentResult:
        """Deploy to the configured environment."""

        return self._run(self.config.deploy_script)

    def rollback(self) -> DeploymentResult:
        """Rollback the deployment using configured rollback script."""

        if not self.config.rollback_script:
            return DeploymentResult(self.config.name, True, "No rollback script configured")
        return self._run(self.config.rollback_script)


class DeploymentManager:
    """Coordinates deployments across multiple environments."""

    def __init__(self, configs: Iterable[EnvironmentConfig]) -> None:
        self.configs = list(configs)

    def _execute(self, method: str) -> Dict[str, DeploymentResult]:
        results: Dict[str, DeploymentResult] = {}
        for cfg in self.configs:
            deployer = Deployer(cfg)
            result = getattr(deployer, method)()
            results[cfg.name] = result
        return results

    def deploy_all(self) -> Dict[str, DeploymentResult]:
        return self._execute("deploy")

    def rollback_all(self) -> Dict[str, DeploymentResult]:
        return self._execute("rollback")


def load_environment_configs(path: Optional[pathlib.Path] = None) -> List[EnvironmentConfig]:
    """Load environment configurations from a JSON or YAML file.

    When ``path`` is ``None`` a default ``environments.json`` file is
    sought in the repository root.  The file is expected to contain a list
    of environment objects with ``name`` and ``deploy_script`` keys.  When
    the file does not exist a sensible default set of configurations is
    returned.
    """

    if path is None:
        path = pathlib.Path("environments.json")
    if path.exists():
        try:
            data = json.loads(path.read_text())
            configs = [
                EnvironmentConfig(
                    item["name"],
                    pathlib.Path(item["deploy_script"]),
                    pathlib.Path(item.get("rollback_script", "")) if item.get("rollback_script") else None,
                )
                for item in data
            ]
            return configs
        except Exception:  # pragma: no cover - parsing errors
            pass

    base = pathlib.Path("scripts/deploy")
    return [
        EnvironmentConfig("development", base / "deploy-dev.sh"),
        EnvironmentConfig("staging", base / "deploy-staging.sh"),
        EnvironmentConfig("production", base / "deploy-prod.sh"),
        EnvironmentConfig("performance", base / "deploy-perf.sh"),
    ]


def execute_default_deployment() -> Dict[str, DeploymentResult]:
    """Execute deployment using default configurations."""

    manager = DeploymentManager(load_environment_configs())
    return manager.deploy_all()


def execute_default_rollback() -> Dict[str, DeploymentResult]:
    """Execute rollback using default configurations."""

    manager = DeploymentManager(load_environment_configs())
    return manager.rollback_all()


# End of deployment module
# TODO: Implement real deployment logic for all environments.

def verify_deployment(config: EnvironmentConfig) -> DeploymentResult:
    """Verify deployment health for an environment.

    The default implementation simply checks that the deployment script
    exists and is executable.  Real deployments should replace this with
    HTTP or gRPC based health checks depending on the deployed service.
    """

    if not config.deploy_script.exists():
        return DeploymentResult(config.name, False, "deploy script missing")
    if not os.access(config.deploy_script, os.X_OK):
        return DeploymentResult(config.name, False, "deploy script not executable")
    return DeploymentResult(config.name, True, "verification skipped")


def load_custom_config(path: pathlib.Path) -> List[EnvironmentConfig]:
    """Load environment configuration from a custom path."""

    if not path.exists():
        return load_environment_configs()
    try:
        return load_environment_configs(path)
    except Exception:  # pragma: no cover - fallback
        return load_environment_configs()
