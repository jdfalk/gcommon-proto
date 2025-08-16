# 3. Pre-Migration Preparation

## 3.1 Environment Setup

### 3.1.1 Required Tools Verification
```bash
# Verify buf installation
buf --version  # Should be v1.28.0 or later

# Verify protoc (for validation)
protoc --version  # Should be 3.21.0 or later

# Verify Go version
go version  # Should be 1.19 or later

# Verify Python version (for migration scripts)
python3 --version  # Should be 3.8 or later

# Verify git version
git --version  # Should be 2.30 or later
```

### 3.1.2 Backup Creation
```bash
# Create comprehensive backup
git checkout -b pre-reorg-backup
git push origin pre-reorg-backup

# Create file system backup
tar -czf gcommon-backup-$(date +%Y%m%d_%H%M%S).tar.gz \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='target' \
  --exclude='*.log' \
  .

# Store backup in safe location
mv gcommon-backup-*.tar.gz ~/backups/
```

### 3.1.3 Working Branch Setup
```bash
# Create and switch to migration branch
git checkout -b proto-reorg-migration

# Ensure clean working directory
git status
# Should show "working tree clean"

# Set up migration tracking
mkdir -p migration-logs
touch migration-logs/migration-progress.log
```

## 3.2 Analysis and Planning Scripts

### 3.2.1 Proto File Discovery Script
Create `scripts/analyze-proto-files.py`:
```python
#!/usr/bin/env python3
"""
Proto file analysis script for GCommon repository reorganization.
Analyzes current proto file structure and generates migration plan.
"""

import os
import sys
import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Optional

@dataclass
class ProtoFile:
    path: str
    package: str
    go_package: str
    imports: List[str]
    messages: List[str]
    services: List[str]
    enums: List[str]
    file_size: int
    issues: List[str]

class ProtoAnalyzer:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.proto_files: List[ProtoFile] = []
        self.package_map: Dict[str, List[str]] = defaultdict(list)
        self.import_graph: Dict[str, Set[str]] = defaultdict(set)
        self.issues: List[str] = []

    def analyze_repository(self) -> Dict:
        """Analyze the entire repository for proto files."""
        print("🔍 Analyzing repository structure...")

        # Find all proto files
        proto_paths = list(self.repo_root.rglob("*.proto"))
        print(f"📁 Found {len(proto_paths)} proto files")

        # Analyze each file
        for proto_path in proto_paths:
            try:
                proto_file = self._analyze_proto_file(proto_path)
                if proto_file:
                    self.proto_files.append(proto_file)
                    self.package_map[proto_file.package].append(proto_file.path)
            except Exception as e:
                self.issues.append(f"Error analyzing {proto_path}: {e}")

        # Build import graph
        self._build_import_graph()

        # Generate analysis results
        return {
            "summary": self._generate_summary(),
            "proto_files": [asdict(pf) for pf in self.proto_files],
            "packages": dict(self.package_map),
            "import_graph": {k: list(v) for k, v in self.import_graph.items()},
            "issues": self.issues,
            "migration_order": self._calculate_migration_order(),
            "domain_analysis": self._analyze_domains()
        }

    def _analyze_proto_file(self, path: Path) -> Optional[ProtoFile]:
        """Analyze a single proto file."""
        try:
            content = path.read_text(encoding='utf-8')
            relative_path = str(path.relative_to(self.repo_root))

            # Extract package name
            package_match = re.search(r'package\s+([^;]+);', content)
            package = package_match.group(1) if package_match else ""

            # Extract go_package option
            go_package_match = re.search(r'option\s+go_package\s*=\s*"([^"]+)";', content)
            go_package = go_package_match.group(1) if go_package_match else ""

            # Extract imports
            imports = re.findall(r'import\s+"([^"]+)";', content)

            # Extract messages
            messages = re.findall(r'message\s+([A-Za-z_][A-Za-z0-9_]*)', content)

            # Extract services
            services = re.findall(r'service\s+([A-Za-z_][A-Za-z0-9_]*)', content)

            # Extract enums
            enums = re.findall(r'enum\s+([A-Za-z_][A-Za-z0-9_]*)', content)

            # Detect issues
            issues = self._detect_file_issues(relative_path, content, package, go_package)

            return ProtoFile(
                path=relative_path,
                package=package,
                go_package=go_package,
                imports=imports,
                messages=messages,
                services=services,
                enums=enums,
                file_size=len(content),
                issues=issues
            )
        except Exception as e:
            self.issues.append(f"Failed to analyze {path}: {e}")
            return None

    def _detect_file_issues(self, path: str, content: str, package: str, go_package: str) -> List[str]:
        """Detect issues in a proto file."""
        issues = []

        # Check file header
        if "// file:" in content:
            header_match = re.search(r'// file:\s*([^\n]+)', content)
            if header_match:
                header_path = header_match.group(1).strip()
                if header_path != path:
                    issues.append(f"Header path mismatch: header='{header_path}' actual='{path}'")

        # Check package naming
        if package and not package.startswith("gcommon"):
            issues.append(f"Package doesn't follow gcommon convention: '{package}'")

        # Check go_package consistency
        if go_package and "pkg/" in go_package and "proto" in go_package:
            issues.append(f"go_package uses old pkg/proto pattern: '{go_package}'")

        # Check import paths
        for imp in re.findall(r'import\s+"([^"]+)";', content):
            if imp.startswith("pkg/") and not imp.startswith("pkg/google"):
                issues.append(f"Import uses old pkg/ pattern: '{imp}'")

        return issues

    def _build_import_graph(self):
        """Build dependency graph between proto files."""
        file_map = {pf.path: pf for pf in self.proto_files}

        for proto_file in self.proto_files:
            for import_path in proto_file.imports:
                # Normalize import path
                if import_path.startswith("pkg/"):
                    # Convert pkg/ imports to file paths
                    normalized = import_path
                elif import_path.startswith("google/"):
                    # Skip google imports
                    continue
                else:
                    normalized = import_path

                # Find matching file
                for file_path in file_map:
                    if file_path.endswith(normalized) or normalized in file_path:
                        self.import_graph[proto_file.path].add(file_path)

    def _generate_summary(self) -> Dict:
        """Generate analysis summary."""
        total_files = len(self.proto_files)
        total_messages = sum(len(pf.messages) for pf in self.proto_files)
        total_services = sum(len(pf.services) for pf in self.proto_files)
        total_enums = sum(len(pf.enums) for pf in self.proto_files)
        total_issues = sum(len(pf.issues) for pf in self.proto_files)

        # Package distribution
        package_dist = Counter(pf.package.split('.')[0] if pf.package else 'unknown'
                              for pf in self.proto_files)

        # Domain analysis
        domain_dist = Counter()
        for pf in self.proto_files:
            path_parts = pf.path.split('/')
            if 'pkg' in path_parts:
                domain_idx = path_parts.index('pkg') + 1
                if domain_idx < len(path_parts):
                    domain = path_parts[domain_idx]
                    domain_dist[domain] += 1

        return {
            "total_files": total_files,
            "total_messages": total_messages,
            "total_services": total_services,
            "total_enums": total_enums,
            "total_issues": total_issues,
            "package_distribution": dict(package_dist),
            "domain_distribution": dict(domain_dist),
            "average_file_size": sum(pf.file_size for pf in self.proto_files) // total_files if total_files > 0 else 0
        }

    def _calculate_migration_order(self) -> List[str]:
        """Calculate optimal migration order based on dependencies."""
        # Simple topological sort based on imports
        visited = set()
        order = []

        def visit(file_path: str):
            if file_path in visited:
                return
            visited.add(file_path)

            # Visit dependencies first
            for dep in self.import_graph.get(file_path, []):
                visit(dep)

            order.append(file_path)

        # Visit all files
        for proto_file in self.proto_files:
            visit(proto_file.path)

        return order

    def _analyze_domains(self) -> Dict:
        """Analyze domain-specific patterns."""
        domains = defaultdict(lambda: {
            "files": [],
            "total_messages": 0,
            "total_services": 0,
            "total_enums": 0,
            "issues": 0,
            "complexity_score": 0
        })

        for pf in self.proto_files:
            # Extract domain from path
            path_parts = pf.path.split('/')
            domain = "unknown"

            if 'pkg' in path_parts:
                domain_idx = path_parts.index('pkg') + 1
                if domain_idx < len(path_parts):
                    domain = path_parts[domain_idx]

            # Update domain stats
            domain_info = domains[domain]
            domain_info["files"].append(pf.path)
            domain_info["total_messages"] += len(pf.messages)
            domain_info["total_services"] += len(pf.services)
            domain_info["total_enums"] += len(pf.enums)
            domain_info["issues"] += len(pf.issues)

            # Calculate complexity score
            complexity = (
                len(pf.messages) * 2 +
                len(pf.services) * 5 +
                len(pf.enums) * 1 +
                len(pf.imports) * 1 +
                len(pf.issues) * 3
            )
            domain_info["complexity_score"] += complexity

        return dict(domains)

def main():
    if len(sys.argv) > 1:
        repo_root = sys.argv[1]
    else:
        repo_root = os.getcwd()

    analyzer = ProtoAnalyzer(repo_root)
    results = analyzer.analyze_repository()

    # Save results
    output_file = "migration-logs/proto-analysis.json"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    # Print summary
    summary = results["summary"]
    print("\n📊 Analysis Summary:")
    print(f"   Total files: {summary['total_files']}")
    print(f"   Total messages: {summary['total_messages']}")
    print(f"   Total services: {summary['total_services']}")
    print(f"   Total enums: {summary['total_enums']}")
    print(f"   Total issues: {summary['total_issues']}")

    print("\n🏗️ Domain Distribution:")
    for domain, count in summary["domain_distribution"].items():
        print(f"   {domain}: {count} files")

    print(f"\n📄 Analysis saved to: {output_file}")

if __name__ == "__main__":
    main()
```

### 3.2.2 Dependency Analysis Script
Create `scripts/analyze-dependencies.py`:
```python
#!/usr/bin/env python3
"""
Dependency analysis for proto file reorganization.
Analyzes import relationships and calculates migration order.
"""

import json
import sys
from pathlib import Path
from collections import defaultdict, deque
from typing import Dict, List, Set

class DependencyAnalyzer:
    def __init__(self, analysis_file: str):
        with open(analysis_file, 'r') as f:
            self.analysis = json.load(f)

        self.import_graph = self.analysis["import_graph"]
        self.files = {pf["path"]: pf for pf in self.analysis["proto_files"]}

    def find_circular_dependencies(self) -> List[List[str]]:
        """Find circular dependencies in the import graph."""
        visited = set()
        rec_stack = set()
        cycles = []

        def dfs(node: str, path: List[str]) -> bool:
            if node in rec_stack:
                # Found a cycle
                cycle_start = path.index(node)
                cycles.append(path[cycle_start:] + [node])
                return True

            if node in visited:
                return False

            visited.add(node)
            rec_stack.add(node)

            for neighbor in self.import_graph.get(node, []):
                if dfs(neighbor, path + [node]):
                    return True

            rec_stack.remove(node)
            return False

        for file_path in self.files:
            if file_path not in visited:
                dfs(file_path, [])

        return cycles

    def calculate_migration_phases(self) -> Dict[str, List[str]]:
        """Calculate migration phases based on dependencies."""
        # Build reverse dependency graph
        reverse_deps = defaultdict(set)
        for file_path, deps in self.import_graph.items():
            for dep in deps:
                reverse_deps[dep].add(file_path)

        # Calculate phases using topological sort
        phases = defaultdict(list)
        in_degree = {fp: len(deps) for fp, deps in self.import_graph.items()}

        # Add files with no dependencies to phase 0
        queue = deque()
        for file_path in self.files:
            if in_degree.get(file_path, 0) == 0:
                queue.append((file_path, 0))

        while queue:
            file_path, phase = queue.popleft()
            phases[f"phase_{phase}"].append(file_path)

            # Update dependents
            for dependent in reverse_deps.get(file_path, []):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append((dependent, phase + 1))

        return dict(phases)

    def analyze_domain_dependencies(self) -> Dict[str, Dict]:
        """Analyze dependencies between domains."""
        domain_deps = defaultdict(lambda: defaultdict(int))

        for file_path, deps in self.import_graph.items():
            source_domain = self._extract_domain(file_path)

            for dep_path in deps:
                target_domain = self._extract_domain(dep_path)
                if source_domain != target_domain:
                    domain_deps[source_domain][target_domain] += 1

        return dict(domain_deps)

    def _extract_domain(self, file_path: str) -> str:
        """Extract domain from file path."""
        parts = file_path.split('/')
        if 'pkg' in parts:
            domain_idx = parts.index('pkg') + 1
            if domain_idx < len(parts):
                return parts[domain_idx]
        return "unknown"

    def generate_migration_plan(self) -> Dict:
        """Generate comprehensive migration plan."""
        return {
            "circular_dependencies": self.find_circular_dependencies(),
            "migration_phases": self.calculate_migration_phases(),
            "domain_dependencies": self.analyze_domain_dependencies(),
            "recommendations": self._generate_recommendations()
        }

    def _generate_recommendations(self) -> List[str]:
        """Generate migration recommendations."""
        recommendations = []

        # Check for circular dependencies
        cycles = self.find_circular_dependencies()
        if cycles:
            recommendations.append(f"⚠️  Found {len(cycles)} circular dependencies that need resolution")

        # Analyze domain complexity
        domain_analysis = self.analysis["domain_analysis"]
        complex_domains = [(d, info["complexity_score"])
                          for d, info in domain_analysis.items()
                          if info["complexity_score"] > 100]

        if complex_domains:
            complex_domains.sort(key=lambda x: x[1], reverse=True)
            recommendations.append(f"🔧 High complexity domains: {[d[0] for d in complex_domains[:3]]}")

        # Check for issues
        total_issues = sum(info["issues"] for info in domain_analysis.values())
        if total_issues > 10:
            recommendations.append(f"🐛 {total_issues} issues detected across domains")

        return recommendations

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze-dependencies.py <analysis-file>")
        sys.exit(1)

    analyzer = DependencyAnalyzer(sys.argv[1])
    plan = analyzer.generate_migration_plan()

    # Save migration plan
    output_file = "migration-logs/migration-plan.json"
    with open(output_file, 'w') as f:
        json.dump(plan, f, indent=2)

    # Print results
    print("🔄 Dependency Analysis Results:")

    cycles = plan["circular_dependencies"]
    if cycles:
        print(f"\n⚠️  Circular Dependencies Found: {len(cycles)}")
        for i, cycle in enumerate(cycles):
            print(f"   Cycle {i+1}: {' -> '.join(cycle)}")
    else:
        print("\n✅ No circular dependencies found")

    phases = plan["migration_phases"]
    print(f"\n📋 Migration Phases: {len(phases)}")
    for phase_name, files in phases.items():
        print(f"   {phase_name}: {len(files)} files")

    print("\n💡 Recommendations:")
    for rec in plan["recommendations"]:
        print(f"   {rec}")

    print(f"\n📄 Migration plan saved to: {output_file}")

if __name__ == "__main__":
    main()
```

## 3.3 Pre-Migration Validation

### 3.3.1 Current State Validation Script
Create `scripts/validate-current-state.sh`:
```bash
#!/bin/bash
# file: scripts/validate-current-state.sh
# version: 1.0.0
# guid: 12345678-90ab-cdef-1234-567890abcdef

set -euo pipefail

echo "🔍 Validating current repository state..."

# Check if we're in the right directory
if [[ ! -f "buf.yaml" ]]; then
    echo "❌ Error: buf.yaml not found. Run from repository root."
    exit 1
fi

# Check buf installation
if ! command -v buf &> /dev/null; then
    echo "❌ Error: buf is not installed"
    exit 1
fi

echo "✅ buf found: $(buf --version)"

# Check protoc installation
if ! command -v protoc &> /dev/null; then
    echo "⚠️  Warning: protoc not found (optional for validation)"
else
    echo "✅ protoc found: $(protoc --version)"
fi

# Validate current buf configuration
echo "🔧 Validating current buf configuration..."
if buf lint; then
    echo "✅ Current buf lint passes"
else
    echo "⚠️  Current buf lint has issues (will be fixed in migration)"
fi

# Test current code generation
echo "🏗️ Testing current code generation..."
if buf generate; then
    echo "✅ Current buf generate works"
else
    echo "❌ Current buf generate fails"
    exit 1
fi

# Check git status
echo "📋 Checking git status..."
if [[ -n "$(git status --porcelain)" ]]; then
    echo "⚠️  Working directory is not clean:"
    git status --short
    echo "   Consider committing changes before migration"
else
    echo "✅ Working directory is clean"
fi

# Check for existing proto files
PROTO_COUNT=$(find . -name "*.proto" -type f | wc -l)
echo "📁 Found $PROTO_COUNT proto files"

if [[ $PROTO_COUNT -eq 0 ]]; then
    echo "❌ Error: No proto files found"
    exit 1
fi

# Check for pkg directory structure
if [[ -d "pkg" ]]; then
    PKG_PROTO_COUNT=$(find pkg -name "*.proto" -type f | wc -l)
    echo "📦 Found $PKG_PROTO_COUNT proto files in pkg/ directory"
else
    echo "⚠️  No pkg/ directory found"
fi

# Check for existing proto directory
if [[ -d "proto" ]]; then
    echo "⚠️  proto/ directory already exists - may need cleanup"
    EXISTING_PROTO_COUNT=$(find proto -name "*.proto" -type f | wc -l)
    echo "   Contains $EXISTING_PROTO_COUNT proto files"
fi

echo "✅ Current state validation complete"
```

### 3.3.2 Run Analysis Scripts
```bash
# Make scripts executable
chmod +x scripts/validate-current-state.sh
chmod +x scripts/analyze-proto-files.py
chmod +x scripts/analyze-dependencies.py

# Run current state validation
./scripts/validate-current-state.sh

# Run proto file analysis
python3 scripts/analyze-proto-files.py

# Run dependency analysis
python3 scripts/analyze-dependencies.py migration-logs/proto-analysis.json
```

## 3.4 Migration Infrastructure Setup

### 3.4.1 Migration Tracking System
Create `scripts/migration-tracker.py`:
```python
#!/usr/bin/env python3
"""
Migration tracking system for proto reorganization.
Tracks progress and manages rollback points.
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

class MigrationTracker:
    def __init__(self, log_dir: str = "migration-logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.progress_file = self.log_dir / "migration-progress.json"
        self.checkpoints_dir = self.log_dir / "checkpoints"
        self.checkpoints_dir.mkdir(exist_ok=True)

        self.progress = self._load_progress()

    def _load_progress(self) -> Dict:
        """Load existing progress or create new."""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                return json.load(f)

        return {
            "migration_id": f"reorg_{int(time.time())}",
            "started_at": datetime.now().isoformat(),
            "current_phase": None,
            "completed_phases": [],
            "failed_phases": [],
            "checkpoints": [],
            "total_files": 0,
            "migrated_files": 0,
            "status": "not_started"
        }

    def _save_progress(self):
        """Save current progress."""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def start_migration(self, total_files: int):
        """Start migration tracking."""
        self.progress.update({
            "status": "in_progress",
            "total_files": total_files,
            "started_at": datetime.now().isoformat()
        })
        self._save_progress()
        self._log("Migration started", {"total_files": total_files})

    def start_phase(self, phase_name: str, files: List[str]):
        """Start a migration phase."""
        self.progress["current_phase"] = {
            "name": phase_name,
            "files": files,
            "started_at": datetime.now().isoformat(),
            "completed_files": [],
            "failed_files": []
        }
        self._save_progress()
        self._log(f"Started phase: {phase_name}", {"file_count": len(files)})

    def complete_file(self, file_path: str):
        """Mark a file as migrated."""
        if self.progress["current_phase"]:
            self.progress["current_phase"]["completed_files"].append(file_path)
            self.progress["migrated_files"] += 1
            self._save_progress()

    def fail_file(self, file_path: str, error: str):
        """Mark a file as failed."""
        if self.progress["current_phase"]:
            self.progress["current_phase"]["failed_files"].append({
                "file": file_path,
                "error": error,
                "timestamp": datetime.now().isoformat()
            })
            self._save_progress()
            self._log(f"File failed: {file_path}", {"error": error})

    def complete_phase(self, phase_name: str):
        """Complete a migration phase."""
        if self.progress["current_phase"] and self.progress["current_phase"]["name"] == phase_name:
            phase = self.progress["current_phase"]
            phase["completed_at"] = datetime.now().isoformat()

            self.progress["completed_phases"].append(phase)
            self.progress["current_phase"] = None
            self._save_progress()

            self._log(f"Completed phase: {phase_name}", {
                "completed_files": len(phase["completed_files"]),
                "failed_files": len(phase["failed_files"])
            })

    def create_checkpoint(self, name: str, description: str) -> str:
        """Create a migration checkpoint."""
        checkpoint_id = f"checkpoint_{int(time.time())}"
        checkpoint = {
            "id": checkpoint_id,
            "name": name,
            "description": description,
            "timestamp": datetime.now().isoformat(),
            "git_commit": self._get_git_commit(),
            "progress_snapshot": dict(self.progress)
        }

        checkpoint_file = self.checkpoints_dir / f"{checkpoint_id}.json"
        with open(checkpoint_file, 'w') as f:
            json.dump(checkpoint, f, indent=2)

        self.progress["checkpoints"].append(checkpoint_id)
        self._save_progress()

        self._log(f"Created checkpoint: {name}", {"id": checkpoint_id})
        return checkpoint_id

    def _get_git_commit(self) -> Optional[str]:
        """Get current git commit hash."""
        try:
            import subprocess
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except:
            return None

    def _log(self, message: str, data: Dict = None):
        """Log migration event."""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "message": message,
            "data": data or {}
        }

        log_file = self.log_dir / "migration.log"
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\n")

    def get_status(self) -> Dict:
        """Get current migration status."""
        status = dict(self.progress)

        if status["total_files"] > 0:
            status["completion_percentage"] = (
                status["migrated_files"] / status["total_files"] * 100
            )
        else:
            status["completion_percentage"] = 0

        return status

    def print_status(self):
        """Print current migration status."""
        status = self.get_status()

        print(f"🚀 Migration Status: {status['status']}")
        print(f"📊 Progress: {status['migrated_files']}/{status['total_files']} files ({status['completion_percentage']:.1f}%)")

        if status.get("current_phase"):
            phase = status["current_phase"]
            print(f"🔄 Current Phase: {phase['name']}")
            print(f"   📁 Files: {len(phase['completed_files'])}/{len(phase['files'])} completed")

            if phase["failed_files"]:
                print(f"   ❌ Failed: {len(phase['failed_files'])} files")

        print(f"✅ Completed Phases: {len(status['completed_phases'])}")
        print(f"💾 Checkpoints: {len(status['checkpoints'])}")

def main():
    tracker = MigrationTracker()

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "status":
            tracker.print_status()
        elif command == "checkpoint":
            name = sys.argv[2] if len(sys.argv) > 2 else "Manual checkpoint"
            desc = sys.argv[3] if len(sys.argv) > 3 else "Manual checkpoint created"
            checkpoint_id = tracker.create_checkpoint(name, desc)
            print(f"✅ Created checkpoint: {checkpoint_id}")
    else:
        print("Usage: python migration-tracker.py [status|checkpoint [name] [description]]")

if __name__ == "__main__":
    import sys
    main()
```

### 3.4.2 Rollback System Setup
Create `scripts/rollback-system.sh`:
```bash
#!/bin/bash
# file: scripts/rollback-system.sh
# version: 1.0.0
# guid: 23456789-01bc-def2-3456-789012bcdef3

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MIGRATION_LOGS="$REPO_ROOT/migration-logs"
ROLLBACK_DIR="$MIGRATION_LOGS/rollbacks"

# Create rollback directory
mkdir -p "$ROLLBACK_DIR"

rollback_to_checkpoint() {
    local checkpoint_id="$1"
    local checkpoint_file="$MIGRATION_LOGS/checkpoints/${checkpoint_id}.json"

    if [[ ! -f "$checkpoint_file" ]]; then
        echo "❌ Checkpoint not found: $checkpoint_id"
        exit 1
    fi

    echo "🔄 Rolling back to checkpoint: $checkpoint_id"

    # Extract git commit from checkpoint
    local git_commit
    git_commit=$(jq -r '.git_commit // "unknown"' "$checkpoint_file")

    if [[ "$git_commit" != "unknown" && "$git_commit" != "null" ]]; then
        echo "📋 Rolling back to git commit: $git_commit"

        # Create rollback branch
        local rollback_branch="rollback-to-${checkpoint_id}"
        git checkout -b "$rollback_branch"

        # Reset to checkpoint commit
        git reset --hard "$git_commit"

        echo "✅ Rollback complete"
        echo "   Branch: $rollback_branch"
        echo "   Commit: $git_commit"
    else
        echo "⚠️  No git commit in checkpoint, manual rollback required"
    fi
}

create_rollback_script() {
    local phase_name="$1"
    local rollback_script="$ROLLBACK_DIR/rollback-${phase_name}.sh"

    cat > "$rollback_script" << 'EOF'
#!/bin/bash
# Auto-generated rollback script for phase: PHASE_NAME
set -euo pipefail

echo "🔄 Rolling back phase: PHASE_NAME"

# Add phase-specific rollback commands here
# This will be populated during migration

echo "✅ Phase rollback complete"
EOF

    sed -i "s/PHASE_NAME/$phase_name/g" "$rollback_script"
    chmod +x "$rollback_script"

    echo "📄 Created rollback script: $rollback_script"
}

list_checkpoints() {
    echo "💾 Available checkpoints:"

    if [[ -d "$MIGRATION_LOGS/checkpoints" ]]; then
        for checkpoint_file in "$MIGRATION_LOGS/checkpoints"/*.json; do
            if [[ -f "$checkpoint_file" ]]; then
                local id name timestamp
                id=$(basename "$checkpoint_file" .json)
                name=$(jq -r '.name' "$checkpoint_file")
                timestamp=$(jq -r '.timestamp' "$checkpoint_file")

                echo "   $id: $name ($timestamp)"
            fi
        done
    else
        echo "   No checkpoints found"
    fi
}

case "${1:-help}" in
    "rollback")
        if [[ $# -lt 2 ]]; then
            echo "Usage: $0 rollback <checkpoint-id>"
            exit 1
        fi
        rollback_to_checkpoint "$2"
        ;;
    "create-script")
        if [[ $# -lt 2 ]]; then
            echo "Usage: $0 create-script <phase-name>"
            exit 1
        fi
        create_rollback_script "$2"
        ;;
    "list")
        list_checkpoints
        ;;
    "help"|*)
        echo "Usage: $0 {rollback|create-script|list}"
        echo ""
        echo "Commands:"
        echo "  rollback <id>        Rollback to checkpoint"
        echo "  create-script <name> Create rollback script for phase"
        echo "  list                 List available checkpoints"
        ;;
esac
```

## 3.5 Testing Infrastructure

### 3.5.1 Migration Test Suite
Create `scripts/test-migration.py`:
```python
#!/usr/bin/env python3
"""
Test suite for proto migration validation.
"""

import os
import subprocess
import tempfile
import shutil
import json
from pathlib import Path
from typing import List, Dict, Tuple

class MigrationTester:
    def __init__(self, repo_root: str):
        self.repo_root = Path(repo_root)
        self.test_results = []

    def run_all_tests(self) -> bool:
        """Run all migration tests."""
        print("🧪 Running migration test suite...")

        tests = [
            ("Buf Lint Test", self.test_buf_lint),
            ("Buf Generate Test", self.test_buf_generate),
            ("Import Resolution Test", self.test_import_resolution),
            ("Go Build Test", self.test_go_build),
            ("Package Structure Test", self.test_package_structure),
        ]

        all_passed = True

        for test_name, test_func in tests:
            print(f"\n🔍 Running: {test_name}")
            try:
                result = test_func()
                self.test_results.append({"name": test_name, "passed": result, "error": None})

                if result:
                    print(f"✅ {test_name}: PASSED")
                else:
                    print(f"❌ {test_name}: FAILED")
                    all_passed = False

            except Exception as e:
                print(f"💥 {test_name}: ERROR - {e}")
                self.test_results.append({"name": test_name, "passed": False, "error": str(e)})
                all_passed = False

        self._save_test_results()
        return all_passed

    def test_buf_lint(self) -> bool:
        """Test buf lint passes."""
        try:
            result = subprocess.run(
                ["buf", "lint"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=False
            )
            return result.returncode == 0
        except Exception:
            return False

    def test_buf_generate(self) -> bool:
        """Test buf generate works."""
        try:
            # Create temporary directory for generation
            with tempfile.TemporaryDirectory() as temp_dir:
                result = subprocess.run(
                    ["buf", "generate", "--output", temp_dir],
                    cwd=self.repo_root,
                    capture_output=True,
                    text=True,
                    check=False
                )
                return result.returncode == 0
        except Exception:
            return False

    def test_import_resolution(self) -> bool:
        """Test that imports can be resolved."""
        proto_files = list(self.repo_root.rglob("*.proto"))

        for proto_file in proto_files:
            try:
                content = proto_file.read_text()

                # Check for problematic import patterns
                if 'import "pkg/' in content and not content.startswith("// Test file"):
                    # Check if the imported file exists
                    import_lines = [line.strip() for line in content.split('\n')
                                  if line.strip().startswith('import "pkg/')]

                    for import_line in import_lines:
                        import_path = import_line.split('"')[1]
                        import_file = self.repo_root / import_path

                        if not import_file.exists():
                            return False

            except Exception:
                return False

        return True

    def test_go_build(self) -> bool:
        """Test that generated Go code builds."""
        try:
            # First generate code
            subprocess.run(
                ["buf", "generate"],
                cwd=self.repo_root,
                check=True,
                capture_output=True
            )

            # Then try to build
            result = subprocess.run(
                ["go", "build", "./..."],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=False
            )

            return result.returncode == 0

        except Exception:
            return False

    def test_package_structure(self) -> bool:
        """Test that package structure is consistent."""
        try:
            # Check that pkg directory exists and contains generated code
            pkg_dir = self.repo_root / "pkg"
            if not pkg_dir.exists():
                return False

            # Check for .pb.go files
            pb_files = list(pkg_dir.rglob("*.pb.go"))
            return len(pb_files) > 0

        except Exception:
            return False

    def _save_test_results(self):
        """Save test results to file."""
        results_file = self.repo_root / "migration-logs" / "test-results.json"
        results_file.parent.mkdir(exist_ok=True)

        with open(results_file, 'w') as f:
            json.dump({
                "timestamp": subprocess.run(
                    ["date", "-Iseconds"],
                    capture_output=True,
                    text=True
                ).stdout.strip(),
                "results": self.test_results,
                "summary": {
                    "total": len(self.test_results),
                    "passed": sum(1 for r in self.test_results if r["passed"]),
                    "failed": sum(1 for r in self.test_results if not r["passed"])
                }
            }, f, indent=2)

def main():
    repo_root = os.getcwd()
    tester = MigrationTester(repo_root)

    success = tester.run_all_tests()

    if success:
        print("\n🎉 All tests passed!")
        exit(0)
    else:
        print("\n💥 Some tests failed!")
        exit(1)

if __name__ == "__main__":
    main()
```

## 3.6 Documentation Preparation

### 3.6.1 Migration Documentation Setup
```bash
# Create documentation structure
mkdir -p docs/migration
mkdir -p docs/migration/phases
mkdir -p docs/migration/troubleshooting

# Create migration README
cat > docs/migration/README.md << 'EOF'
# Proto Migration Documentation

This directory contains comprehensive documentation for the GCommon repository proto file reorganization.

## Structure

- `phases/` - Detailed documentation for each migration phase
- `troubleshooting/` - Common issues and solutions
- `rollback-procedures.md` - Rollback instructions
- `testing-procedures.md` - Testing and validation procedures

## Quick Start

1. Read the [Pre-Migration Checklist](pre-migration-checklist.md)
2. Follow the [Migration Guide](migration-guide.md)
3. Use [Testing Procedures](testing-procedures.md) for validation

## Support

If you encounter issues:
1. Check [Troubleshooting Guide](troubleshooting/README.md)
2. Review migration logs in `migration-logs/`
3. Use rollback procedures if necessary
EOF
```

### 3.6.2 Pre-Migration Checklist
Create `docs/migration/pre-migration-checklist.md`:
```markdown
# Pre-Migration Checklist

## Environment Preparation

- [ ] Buf v1.28.0+ installed
- [ ] Go v1.19+ installed
- [ ] Python 3.8+ installed
- [ ] Git repository is clean
- [ ] Backup branch created
- [ ] Migration scripts are executable

## Analysis Complete

- [ ] Proto file analysis completed
- [ ] Dependency analysis completed
- [ ] Migration plan generated
- [ ] Circular dependencies identified
- [ ] Domain complexity assessed

## Infrastructure Ready

- [ ] Migration tracking system set up
- [ ] Rollback system configured
- [ ] Test suite validated
- [ ] Documentation structure created

## Team Communication

- [ ] Team notified of migration schedule
- [ ] Downstream consumers identified
- [ ] Breaking change timeline communicated
- [ ] Support procedures documented

## Final Validation

- [ ] Current state tests pass
- [ ] Buf lint passes (or issues documented)
- [ ] Buf generate works
- [ ] Go build succeeds
- [ ] No uncommitted changes

## Ready to Proceed

When all items are checked, the migration can begin.
```

## 3.7 Final Preparation Steps

### 3.7.1 Environment Validation
```bash
# Run comprehensive validation
echo "🔍 Running final pre-migration validation..."

# Validate environment
./scripts/validate-current-state.sh

# Run analysis scripts
python3 scripts/analyze-proto-files.py
python3 scripts/analyze-dependencies.py migration-logs/proto-analysis.json

# Run test suite
python3 scripts/test-migration.py

# Create initial checkpoint
python3 scripts/migration-tracker.py checkpoint "pre-migration" "State before migration starts"

echo "✅ Pre-migration preparation complete"
```

### 3.7.2 Team Communication
```bash
# Generate migration summary for team
cat > migration-logs/migration-summary.md << 'EOF'
# Proto Migration Summary

## Migration Overview
- **Start Date**: $(date)
- **Total Files**: $(find . -name "*.proto" | wc -l)
- **Estimated Duration**: 2-4 hours
- **Risk Level**: Medium

## What's Changing
1. All proto files moved from `pkg/` to `proto/gcommon/v1/`
2. Import paths updated to new structure
3. Buf managed mode implemented
4. Package naming standardized

## Impact
- **Breaking**: Import paths change
- **Mitigation**: Managed mode preserves Go package paths
- **Rollback**: Full rollback capability available

## Timeline
1. **Phase 1**: Common domain (30 min)
2. **Phase 2**: Database domain (30 min)
3. **Phase 3**: Media domain (30 min)
4. **Phase 4**: Config domain (45 min)
5. **Phase 5**: Remaining domains (90 min)

## Support
- Migration logs: `migration-logs/`
- Rollback available at any point
- Team lead: Available during migration
EOF

echo "📋 Migration summary generated"
```

This completes the pre-migration preparation phase, setting up all necessary infrastructure, analysis tools, and safety systems for the proto file reorganization.
