# file: scripts/dependency_metrics.py
# version: 0.1.0
# guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d

"""Dependency metrics collection utilities.

This module gathers performance metrics related to project dependencies.
The goal is to evaluate the impact of dependencies on build times,
binary sizes, and runtime performance.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional


@dataclass
class MetricRecord:
    """Represents a single metric value for a dependency."""

    dependency: str
    metric: str
    value: float
    unit: str


class DependencyMetricsCollector:
    """Collects metrics for dependencies across ecosystems."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.results: List[MetricRecord] = []

    # ------------------------------------------------------------------
    # Build time metrics
    # ------------------------------------------------------------------

    def measure_go_build_time(self) -> None:
        """Measure the time required to build Go modules."""

        start = time.time()
        subprocess.run(
            ["go", "build", "./..."],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        duration = time.time() - start
        self.results.append(
            MetricRecord("go", "build_time", duration, "s")
        )
        return None

    def measure_node_install_time(self) -> None:
        """Measure installation time for Node packages."""

        start = time.time()
        subprocess.run(
            ["npm", "install", "--ignore-scripts"],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        duration = time.time() - start
        self.results.append(
            MetricRecord("node", "install_time", duration, "s")
        )
        return None

    # ------------------------------------------------------------------
    # Binary size metrics
    # ------------------------------------------------------------------

    def measure_go_binary_sizes(self) -> None:
        """Measure sizes of compiled Go binaries."""

        out = self.root / "_metric_bin"
        subprocess.run(
            ["go", "build", "-o", str(out), "./..."],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if out.exists():
            size = out.stat().st_size
            self.results.append(
                MetricRecord("go", "binary_size", float(size), "bytes")
            )
            out.unlink()
        return None

    def measure_node_bundle_sizes(self) -> None:
        """Measure sizes of bundled Node.js artifacts."""

        subprocess.run(
            ["npm", "run", "build"],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        dist = self.root / "dist"
        size = 0
        if dist.exists():
            size = sum(f.stat().st_size for f in dist.rglob("*") if f.is_file())
        self.results.append(
            MetricRecord("node", "bundle_size", float(size), "bytes")
        )
        return None

    # ------------------------------------------------------------------
    # Runtime performance metrics
    # ------------------------------------------------------------------

    def benchmark_go_runtime(self) -> None:
        """Run benchmarks to assess Go runtime performance."""

        res = subprocess.run(
            ["go", "test", "-bench=.", "-run", "^$", "./..."],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        for line in res.stdout.splitlines():
            parts = line.split()
            if len(parts) >= 3 and parts[0].startswith("Benchmark"):
                try:
                    ns = float(parts[2])
                except ValueError:
                    continue
                self.results.append(
                    MetricRecord(parts[0], "time_per_op", ns, "ns/op")
                )
        return None

    def benchmark_node_runtime(self) -> None:
        """Run benchmarks to assess Node runtime performance."""

        script = (
            "console.time('b'); for(let i=0;i<1e6;i++); console.timeEnd('b');"
        )
        res = subprocess.run(
            ["node", "-e", script],
            cwd=self.root,
            capture_output=True,
            text=True,
            check=False,
        )
        duration = 0.0
        for line in res.stdout.splitlines():
            if line.startswith("b:"):
                try:
                    duration = float(line.split()[1])
                except ValueError:
                    duration = 0.0
        self.results.append(
            MetricRecord("node", "loop_benchmark", duration, "ms")
        )
        return None

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def summarize_metrics(self) -> Dict[str, List[MetricRecord]]:
        """Summarize collected metrics by dependency.

        Returns
        -------
        dict
            Mapping of dependency names to metric records.
        """

        summary: Dict[str, List[MetricRecord]] = {}
        for record in self.results:
            summary.setdefault(record.dependency, []).append(record)
        return summary

    def save_report(self, path: Path) -> None:
        """Save metrics summary to *path* in JSON format."""

        summary = self.summarize_metrics()
        data = {
            dep: [record.__dict__ for record in records]
            for dep, records in summary.items()
        }
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        return None


def main(root: Optional[str] = None) -> None:
    """Entry point for manual metric collection."""

    base = Path(root) if root else Path.cwd()
    collector = DependencyMetricsCollector(base)
    collector.measure_go_build_time()
    collector.measure_node_install_time()
    collector.measure_go_binary_sizes()
    collector.measure_node_bundle_sizes()
    collector.benchmark_go_runtime()
    collector.benchmark_node_runtime()
    summary = collector.summarize_metrics()
    print("Collected {} metric categories.".format(len(summary)))


if __name__ == "__main__":
    main()

