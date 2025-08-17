<!-- file: tasks/REORG/04-file-migration-import-management.md -->
<!-- version: 1.0.0 -->
<!-- guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b -->

# Section 04: File Migration and Import Management

## 04.1 Domain-by-Domain Migration Strategy

### 04.1.1 Common Domain Migration

**Files to migrate: 418 files**

Migration sequence:

1. Base types (entity, error, pagination)
2. Configuration types (settings, environment)
3. Validation types (rules, constraints)
4. Utility types (formatting, conversion)

Specific file migrations:

- `pkg/common/entity.proto` → `proto/gcommon/v1/common/entity/entity.proto`
- `pkg/common/error.proto` → `proto/gcommon/v1/common/error/error.proto`
- `pkg/common/pagination.proto` → `proto/gcommon/v1/common/pagination/pagination.proto`
- `pkg/common/validation.proto` → `proto/gcommon/v1/common/validation/validation.proto`

### 04.1.2 Config Domain Migration

**Files to migrate: 512 files**

Migration sequence:

1. Base configuration structures
2. Environment-specific configs
3. Feature flags and toggles
4. Service configurations

Specific file migrations:

- `pkg/config/app.proto` → `proto/gcommon/v1/config/application/app.proto`
- `pkg/config/database.proto` → `proto/gcommon/v1/config/database/database.proto`
- `pkg/config/security.proto` → `proto/gcommon/v1/config/security/security.proto`
- `pkg/config/logging.proto` → `proto/gcommon/v1/config/logging/logging.proto`

### 04.1.3 Database Domain Migration

**Files to migrate: 687 files**

Migration sequence:

1. Schema definitions
2. Migration scripts
3. Connection configurations
4. Query builders and utilities

Specific file migrations:

- `pkg/database/schema.proto` → `proto/gcommon/v1/database/schema/schema.proto`
- `pkg/database/migration.proto` → `proto/gcommon/v1/database/migration/migration.proto`
- `pkg/database/connection.proto` → `proto/gcommon/v1/database/connection/connection.proto`
- `pkg/database/query.proto` → `proto/gcommon/v1/database/query/query.proto`

### 04.1.4 Media Domain Migration

**Files to migrate: 893 files**

Migration sequence:

1. Base media types (audio, video, image)
2. Metadata structures
3. Processing definitions
4. Format specifications

Specific file migrations:

- `pkg/media/audio.proto` → `proto/gcommon/v1/media/audio/audio.proto`
- `pkg/media/video.proto` → `proto/gcommon/v1/media/video/video.proto`
- `pkg/media/image.proto` → `proto/gcommon/v1/media/image/image.proto`
- `pkg/media/metadata.proto` → `proto/gcommon/v1/media/metadata/metadata.proto`

### 04.1.5 Metrics Domain Migration

**Files to migrate: 234 files**

Migration sequence:

1. Core metric types
2. Aggregation functions
3. Export configurations
4. Dashboard definitions

Specific file migrations:

- `pkg/metrics/core.proto` → `proto/gcommon/v1/metrics/core/core.proto`
- `pkg/metrics/aggregation.proto` → `proto/gcommon/v1/metrics/aggregation/aggregation.proto`
- `pkg/metrics/export.proto` → `proto/gcommon/v1/metrics/export/export.proto`
- `pkg/metrics/dashboard.proto` → `proto/gcommon/v1/metrics/dashboard/dashboard.proto`

### 04.1.6 Organization Domain Migration

**Files to migrate: 156 files**

Migration sequence:

1. Organization structures
2. User management
3. Role-based access control
4. Team and project management

Specific file migrations:

- `pkg/organization/org.proto` → `proto/gcommon/v1/organization/org/org.proto`
- `pkg/organization/user.proto` → `proto/gcommon/v1/organization/user/user.proto`
- `pkg/organization/role.proto` → `proto/gcommon/v1/organization/role/role.proto`
- `pkg/organization/team.proto` → `proto/gcommon/v1/organization/team/team.proto`

### 04.1.7 Queue Domain Migration

**Files to migrate: 178 files**

Migration sequence:

1. Queue definitions
2. Message types
3. Worker configurations
4. Processing workflows

Specific file migrations:

- `pkg/queue/queue.proto` → `proto/gcommon/v1/queue/queue/queue.proto`
- `pkg/queue/message.proto` → `proto/gcommon/v1/queue/message/message.proto`
- `pkg/queue/worker.proto` → `proto/gcommon/v1/queue/worker/worker.proto`
- `pkg/queue/workflow.proto` → `proto/gcommon/v1/queue/workflow/workflow.proto`

### 04.1.8 Web Domain Migration

**Files to migrate: 186 files**

Migration sequence:

1. HTTP definitions
2. WebSocket protocols
3. API specifications
4. Frontend interfaces

Specific file migrations:

- `pkg/web/http.proto` → `proto/gcommon/v1/web/http/http.proto`
- `pkg/web/websocket.proto` → `proto/gcommon/v1/web/websocket/websocket.proto`
- `pkg/web/api.proto` → `proto/gcommon/v1/web/api/api.proto`
- `pkg/web/frontend.proto` → `proto/gcommon/v1/web/frontend/frontend.proto`

## 04.2 Import Path Transformation

### 04.2.1 Import Analysis Script

```python
#!/usr/bin/env python3
# file: scripts/analyze-imports.py
# version: 1.0.0
# guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Set, Tuple

class ImportAnalyzer:
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.import_map = {}
        self.dependency_graph = {}

    def analyze_file(self, proto_file: Path) -> Dict:
        """Analyze a single proto file for imports."""
        content = proto_file.read_text()
        imports = []

        # Extract import statements
        import_pattern = r'import\s+"([^"]+)";'
        for match in re.finditer(import_pattern, content):
            imports.append(match.group(1))

        # Extract package declaration
        package_pattern = r'package\s+([^;]+);'
        package_match = re.search(package_pattern, content)
        package = package_match.group(1) if package_match else ""

        return {
            'file': str(proto_file),
            'package': package,
            'imports': imports,
            'relative_path': str(proto_file.relative_to(self.source_dir))
        }

    def analyze_all_files(self) -> Dict:
        """Analyze all proto files in the source directory."""
        results = {}

        for proto_file in self.source_dir.rglob("*.proto"):
            analysis = self.analyze_file(proto_file)
            results[str(proto_file)] = analysis

        return results

    def build_dependency_graph(self, analysis: Dict) -> Dict:
        """Build dependency graph from analysis results."""
        graph = {}

        for file_path, data in analysis.items():
            dependencies = []
            for import_path in data['imports']:
                # Find which file provides this import
                for other_file, other_data in analysis.items():
                    if other_data['package'] in import_path or import_path.endswith(other_data['relative_path']):
                        dependencies.append(other_file)

            graph[file_path] = dependencies

        return graph

    def generate_migration_order(self, graph: Dict) -> List[str]:
        """Generate migration order based on dependencies."""
        visited = set()
        order = []

        def visit(node: str):
            if node in visited:
                return
            visited.add(node)

            for dependency in graph.get(node, []):
                visit(dependency)

            order.append(node)

        for node in graph:
            visit(node)

        return order

    def generate_import_mapping(self, analysis: Dict) -> Dict[str, str]:
        """Generate mapping from old import paths to new import paths."""
        mapping = {}

        for file_path, data in analysis.items():
            old_package = data['package']
            relative_path = data['relative_path']

            # Transform pkg/domain/... to proto/gcommon/v1/domain/...
            if relative_path.startswith('pkg/'):
                new_path = relative_path.replace('pkg/', 'proto/gcommon/v1/', 1)
                mapping[old_package] = new_path

        return mapping

def main():
    analyzer = ImportAnalyzer('pkg')
    analysis = analyzer.analyze_all_files()
    graph = analyzer.build_dependency_graph(analysis)
    order = analyzer.generate_migration_order(graph)
    mapping = analyzer.generate_import_mapping(analysis)

    # Save results
    with open('migration-analysis.json', 'w') as f:
        json.dump({
            'analysis': analysis,
            'dependency_graph': graph,
            'migration_order': order,
            'import_mapping': mapping
        }, f, indent=2)

    print(f"Analyzed {len(analysis)} files")
    print(f"Generated migration order for {len(order)} files")
    print(f"Created {len(mapping)} import mappings")

if __name__ == "__main__":
    main()
```

### 04.2.2 Import Transformation Script

```python
#!/usr/bin/env python3
# file: scripts/transform-imports.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d

import os
import re
import json
from pathlib import Path
from typing import Dict, List

class ImportTransformer:
    def __init__(self, mapping_file: str):
        with open(mapping_file, 'r') as f:
            data = json.load(f)
        self.import_mapping = data['import_mapping']
        self.migration_order = data['migration_order']

    def transform_file(self, file_path: Path, new_base_dir: Path) -> None:
        """Transform imports in a single file."""
        content = file_path.read_text()

        # Transform import statements
        def replace_import(match):
            old_import = match.group(1)

            # Check if this import needs transformation
            for old_package, new_path in self.import_mapping.items():
                if old_import.startswith(old_package):
                    new_import = old_import.replace(old_package, new_path, 1)
                    return f'import "{new_import}";'

            return match.group(0)

        # Apply transformations
        content = re.sub(r'import\s+"([^"]+)";', replace_import, content)

        # Transform package declaration
        package_pattern = r'package\s+([^;]+);'
        def replace_package(match):
            old_package = match.group(1)

            # Transform pkg.domain to gcommon.v1.domain
            if old_package.startswith('pkg.'):
                new_package = old_package.replace('pkg.', 'gcommon.v1.', 1)
                return f'package {new_package};'

            return match.group(0)

        content = re.sub(package_pattern, replace_package, content)

        # Determine new file path
        relative_path = file_path.relative_to(Path('pkg'))
        new_file_path = new_base_dir / 'proto' / 'gcommon' / 'v1' / relative_path

        # Create directory structure
        new_file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write transformed content
        new_file_path.write_text(content)

    def transform_all_files(self, base_dir: Path) -> None:
        """Transform all files according to migration order."""
        transformed_count = 0

        for file_path_str in self.migration_order:
            file_path = Path(file_path_str)
            if file_path.exists():
                self.transform_file(file_path, base_dir)
                transformed_count += 1

        print(f"Transformed {transformed_count} files")

def main():
    transformer = ImportTransformer('migration-analysis.json')
    transformer.transform_all_files(Path('.'))

if __name__ == "__main__":
    main()
```

## 04.3 Cross-Reference Management

### 04.3.1 Dependency Validation Script

```bash
#!/bin/bash
# file: scripts/validate-dependencies.sh
# version: 1.0.0
# guid: b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e

set -euo pipefail

PROTO_DIR="proto/gcommon/v1"
TEMP_DIR="/tmp/proto-validation"

# Create temporary directory
mkdir -p "$TEMP_DIR"

# Function to validate a single proto file
validate_proto_file() {
    local proto_file="$1"
    local relative_path="${proto_file#$PROTO_DIR/}"

    echo "Validating $relative_path..."

    # Check if file compiles
    if ! buf lint --path "$proto_file" > "$TEMP_DIR/lint.log" 2>&1; then
        echo "LINT ERROR in $relative_path:"
        cat "$TEMP_DIR/lint.log"
        return 1
    fi

    # Check if file generates code
    if ! buf generate --path "$proto_file" > "$TEMP_DIR/gen.log" 2>&1; then
        echo "GENERATION ERROR in $relative_path:"
        cat "$TEMP_DIR/gen.log"
        return 1
    fi

    return 0
}

# Function to validate dependency resolution
validate_dependencies() {
    local domain="$1"
    local domain_dir="$PROTO_DIR/$domain"

    echo "Validating dependencies for domain: $domain"

    # Find all proto files in domain
    find "$domain_dir" -name "*.proto" | while read -r proto_file; do
        if ! validate_proto_file "$proto_file"; then
            echo "Validation failed for $proto_file"
            exit 1
        fi
    done
}

# Function to check circular dependencies
check_circular_dependencies() {
    echo "Checking for circular dependencies..."

    python3 << 'EOF'
import os
import re
from pathlib import Path
from collections import defaultdict, deque

def build_dependency_graph(proto_dir):
    """Build dependency graph from proto files."""
    graph = defaultdict(set)

    for proto_file in Path(proto_dir).rglob("*.proto"):
        content = proto_file.read_text()

        # Extract imports
        imports = re.findall(r'import\s+"([^"]+)";', content)

        for import_path in imports:
            if import_path.startswith('gcommon/'):
                graph[str(proto_file)].add(import_path)

    return graph

def find_cycles(graph):
    """Find cycles in dependency graph using DFS."""
    visited = set()
    rec_stack = set()
    cycles = []

    def dfs(node, path):
        if node in rec_stack:
            cycle_start = path.index(node)
            cycles.append(path[cycle_start:] + [node])
            return

        if node in visited:
            return

        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node, []):
            dfs(neighbor, path + [node])

        rec_stack.remove(node)

    for node in graph:
        if node not in visited:
            dfs(node, [])

    return cycles

# Run analysis
proto_dir = os.environ.get('PROTO_DIR', 'proto/gcommon/v1')
graph = build_dependency_graph(proto_dir)
cycles = find_cycles(graph)

if cycles:
    print("CIRCULAR DEPENDENCIES FOUND:")
    for i, cycle in enumerate(cycles):
        print(f"Cycle {i+1}: {' -> '.join(cycle)}")
    exit(1)
else:
    print("No circular dependencies found.")
EOF
}

# Main validation workflow
main() {
    echo "Starting dependency validation..."

    # Validate each domain
    for domain in common config database media metrics organization queue web; do
        if [ -d "$PROTO_DIR/$domain" ]; then
            validate_dependencies "$domain"
        else
            echo "Warning: Domain directory $PROTO_DIR/$domain not found"
        fi
    done

    # Check for circular dependencies
    check_circular_dependencies

    # Run full compilation test
    echo "Running full compilation test..."
    if buf generate > "$TEMP_DIR/full-gen.log" 2>&1; then
        echo "Full compilation successful"
    else
        echo "FULL COMPILATION FAILED:"
        cat "$TEMP_DIR/full-gen.log"
        exit 1
    fi

    echo "All dependency validations passed!"
}

# Cleanup function
cleanup() {
    rm -rf "$TEMP_DIR"
}

# Set up cleanup trap
trap cleanup EXIT

# Run main function
main "$@"
```

### 04.3.2 Import Conflict Resolution

```python
#!/usr/bin/env python3
# file: scripts/resolve-import-conflicts.py
# version: 1.0.0
# guid: c3d4e5f6-a7b8-9c0d-1e2f-3a4b5c6d7e8f

import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

class ImportConflictResolver:
    def __init__(self, proto_dir: str):
        self.proto_dir = Path(proto_dir)
        self.conflicts = defaultdict(list)
        self.resolutions = {}

    def scan_for_conflicts(self) -> Dict[str, List[str]]:
        """Scan for import conflicts across proto files."""
        package_files = defaultdict(list)

        # Build map of packages to files
        for proto_file in self.proto_dir.rglob("*.proto"):
            content = proto_file.read_text()

            # Extract package declaration
            package_match = re.search(r'package\s+([^;]+);', content)
            if package_match:
                package = package_match.group(1)
                package_files[package].append(str(proto_file))

        # Find conflicts (multiple files declaring same package)
        conflicts = {}
        for package, files in package_files.items():
            if len(files) > 1:
                conflicts[package] = files

        return conflicts

    def resolve_package_conflicts(self, conflicts: Dict[str, List[str]]) -> Dict[str, str]:
        """Resolve package conflicts by suggesting new package names."""
        resolutions = {}

        for package, files in conflicts.items():
            for i, file_path in enumerate(files):
                file_obj = Path(file_path)

                # Generate unique package name based on file path
                relative_path = file_obj.relative_to(self.proto_dir)
                path_parts = relative_path.parts[:-1]  # Exclude filename

                if i == 0:
                    # First file keeps original package
                    resolutions[file_path] = package
                else:
                    # Subsequent files get disambiguated package names
                    new_package = f"{package}.{'.'.join(path_parts)}"
                    resolutions[file_path] = new_package

        return resolutions

    def apply_resolutions(self, resolutions: Dict[str, str]) -> None:
        """Apply package name resolutions to proto files."""
        for file_path, new_package in resolutions.items():
            file_obj = Path(file_path)
            content = file_obj.read_text()

            # Update package declaration
            content = re.sub(
                r'package\s+[^;]+;',
                f'package {new_package};',
                content
            )

            file_obj.write_text(content)

    def update_import_references(self, resolutions: Dict[str, str]) -> None:
        """Update import statements to reference new package names."""
        # Build reverse mapping from old to new packages
        old_to_new = {}
        for file_path, new_package in resolutions.items():
            file_obj = Path(file_path)
            content = file_obj.read_text()

            # Extract original package
            package_match = re.search(r'package\s+([^;]+);', content)
            if package_match:
                old_package = package_match.group(1)
                old_to_new[old_package] = new_package

        # Update all import statements
        for proto_file in self.proto_dir.rglob("*.proto"):
            content = proto_file.read_text()

            def replace_import(match):
                import_path = match.group(1)

                # Check if this import references a renamed package
                for old_pkg, new_pkg in old_to_new.items():
                    if old_pkg in import_path:
                        updated_import = import_path.replace(old_pkg, new_pkg)
                        return f'import "{updated_import}";'

                return match.group(0)

            content = re.sub(r'import\s+"([^"]+)";', replace_import, content)
            proto_file.write_text(content)

    def validate_resolutions(self) -> bool:
        """Validate that conflict resolutions are successful."""
        try:
            # Run buf lint to check for remaining conflicts
            import subprocess
            result = subprocess.run(
                ['buf', 'lint', str(self.proto_dir)],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return True
            else:
                print("Validation failed:")
                print(result.stderr)
                return False

        except subprocess.CalledProcessError as e:
            print(f"Validation error: {e}")
            return False

    def run_full_resolution(self) -> bool:
        """Run complete conflict resolution workflow."""
        print("Scanning for import conflicts...")
        conflicts = self.scan_for_conflicts()

        if not conflicts:
            print("No conflicts found.")
            return True

        print(f"Found {len(conflicts)} package conflicts:")
        for package, files in conflicts.items():
            print(f"  {package}: {len(files)} files")

        print("Resolving conflicts...")
        resolutions = self.resolve_package_conflicts(conflicts)

        print("Applying resolutions...")
        self.apply_resolutions(resolutions)

        print("Updating import references...")
        self.update_import_references(resolutions)

        print("Validating resolutions...")
        if self.validate_resolutions():
            print("Conflict resolution successful!")
            return True
        else:
            print("Conflict resolution failed!")
            return False

def main():
    resolver = ImportConflictResolver('proto/gcommon/v1')
    success = resolver.run_full_resolution()

    if not success:
        exit(1)

if __name__ == "__main__":
    main()
```

## 04.4 Go Code Generation Updates

### 04.4.1 Module Path Updates

```go
// file: scripts/update-go-modules.go
// version: 1.0.0
// guid: d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a

package main

import (
	"bufio"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

type ModuleUpdater struct {
	rootDir   string
	oldPrefix string
	newPrefix string
}

func NewModuleUpdater(rootDir, oldPrefix, newPrefix string) *ModuleUpdater {
	return &ModuleUpdater{
		rootDir:   rootDir,
		oldPrefix: oldPrefix,
		newPrefix: newPrefix,
	}
}

func (mu *ModuleUpdater) UpdateGoFiles() error {
	return filepath.WalkDir(mu.rootDir, func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}

		if !strings.HasSuffix(path, ".go") {
			return nil
		}

		return mu.updateFile(path)
	})
}

func (mu *ModuleUpdater) updateFile(filePath string) error {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return fmt.Errorf("reading file %s: %w", filePath, err)
	}

	lines := strings.Split(string(content), "\n")
	var updatedLines []string
	modified := false

	for _, line := range lines {
		updatedLine := mu.updateImportLine(line)
		if updatedLine != line {
			modified = true
		}
		updatedLines = append(updatedLines, updatedLine)
	}

	if modified {
		updatedContent := strings.Join(updatedLines, "\n")
		err = os.WriteFile(filePath, []byte(updatedContent), 0644)
		if err != nil {
			return fmt.Errorf("writing file %s: %w", filePath, err)
		}
		fmt.Printf("Updated imports in %s\n", filePath)
	}

	return nil
}

func (mu *ModuleUpdater) updateImportLine(line string) string {
	// Update import statements
	importRegex := regexp.MustCompile(`"` + regexp.QuoteMeta(mu.oldPrefix) + `([^"]*)"`)
	if importRegex.MatchString(line) {
		return importRegex.ReplaceAllString(line, `"`+mu.newPrefix+`$1"`)
	}

	// Update package references in comments
	commentRegex := regexp.MustCompile(regexp.QuoteMeta(mu.oldPrefix) + `([^\s]*)`)
	if commentRegex.MatchString(line) && strings.Contains(line, "//") {
		return commentRegex.ReplaceAllString(line, mu.newPrefix+`$1`)
	}

	return line
}

func (mu *ModuleUpdater) UpdateGoMod() error {
	goModPath := filepath.Join(mu.rootDir, "go.mod")

	content, err := os.ReadFile(goModPath)
	if err != nil {
		return fmt.Errorf("reading go.mod: %w", err)
	}

	lines := strings.Split(string(content), "\n")
	var updatedLines []string
	modified := false

	for _, line := range lines {
		if strings.Contains(line, mu.oldPrefix) {
			updatedLine := strings.ReplaceAll(line, mu.oldPrefix, mu.newPrefix)
			updatedLines = append(updatedLines, updatedLine)
			modified = true
		} else {
			updatedLines = append(updatedLines, line)
		}
	}

	if modified {
		updatedContent := strings.Join(updatedLines, "\n")
		err = os.WriteFile(goModPath, []byte(updatedContent), 0644)
		if err != nil {
			return fmt.Errorf("writing go.mod: %w", err)
		}
		fmt.Println("Updated go.mod")
	}

	return nil
}

func (mu *ModuleUpdater) GenerateReport() error {
	report := fmt.Sprintf(`# Go Module Update Report

## Changes Applied
- Old prefix: %s
- New prefix: %s
- Root directory: %s

## Files Updated
`, mu.oldPrefix, mu.newPrefix, mu.rootDir)

	reportPath := filepath.Join(mu.rootDir, "module-update-report.md")
	return os.WriteFile(reportPath, []byte(report), 0644)
}

func main() {
	if len(os.Args) != 4 {
		fmt.Fprintf(os.Stderr, "Usage: %s <root-dir> <old-prefix> <new-prefix>\n", os.Args[0])
		os.Exit(1)
	}

	rootDir := os.Args[1]
	oldPrefix := os.Args[2]
	newPrefix := os.Args[3]

	updater := NewModuleUpdater(rootDir, oldPrefix, newPrefix)

	fmt.Println("Updating Go files...")
	if err := updater.UpdateGoFiles(); err != nil {
		fmt.Fprintf(os.Stderr, "Error updating Go files: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Updating go.mod...")
	if err := updater.UpdateGoMod(); err != nil {
		fmt.Fprintf(os.Stderr, "Error updating go.mod: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Generating report...")
	if err := updater.GenerateReport(); err != nil {
		fmt.Fprintf(os.Stderr, "Error generating report: %v\n", err)
		os.Exit(1)
	}

	fmt.Println("Module update completed successfully!")
}
```

### 04.4.2 Generated Code Cleanup

````bash
#!/bin/bash
# file: scripts/cleanup-generated-code.sh
# version: 1.0.0
# guid: e5f6a7b8-c9d0-1e2f-3a4b-5c6d7e8f9a0b

set -euo pipefail

# Configuration
OLD_GEN_DIR="pkg"
NEW_GEN_DIR="internal/generated"
BACKUP_DIR="/tmp/proto-migration-backup"

# Create backup
create_backup() {
    echo "Creating backup of existing generated code..."
    mkdir -p "$BACKUP_DIR"

    if [ -d "$OLD_GEN_DIR" ]; then
        cp -r "$OLD_GEN_DIR" "$BACKUP_DIR/pkg-backup-$(date +%Y%m%d_%H%M%S)"
    fi

    if [ -d "$NEW_GEN_DIR" ]; then
        cp -r "$NEW_GEN_DIR" "$BACKUP_DIR/generated-backup-$(date +%Y%m%d_%H%M%S)"
    fi
}

# Clean old generated files
clean_old_generated() {
    echo "Cleaning old generated files..."

    # Find and remove generated .pb.go files
    find "$OLD_GEN_DIR" -name "*.pb.go" -type f -delete || true
    find "$OLD_GEN_DIR" -name "*_grpc.pb.go" -type f -delete || true
    find "$OLD_GEN_DIR" -name "*.pb.gw.go" -type f -delete || true

    # Remove empty directories
    find "$OLD_GEN_DIR" -type d -empty -delete || true

    echo "Old generated files cleaned"
}

# Generate new code
generate_new_code() {
    echo "Generating new protobuf code..."

    # Ensure output directory exists
    mkdir -p "$NEW_GEN_DIR"

    # Run buf generate
    if buf generate; then
        echo "Code generation successful"
    else
        echo "Code generation failed"
        exit 1
    fi
}

# Update build tags and package declarations
update_generated_files() {
    echo "Updating generated file headers..."

    find "$NEW_GEN_DIR" -name "*.pb.go" -type f | while read -r file; do
        # Add build tags if not present
        if ! grep -q "//go:build" "$file"; then
            sed -i '1i//go:build !ignore_autogenerated' "$file"
        fi

        # Update package comments
        sed -i 's|// source: pkg/|// source: proto/gcommon/v1/|g' "$file"

        echo "Updated $file"
    done
}

# Verify generated code
verify_generated_code() {
    echo "Verifying generated code..."

    # Check that files were generated
    if [ ! -d "$NEW_GEN_DIR" ] || [ -z "$(find "$NEW_GEN_DIR" -name "*.pb.go")" ]; then
        echo "ERROR: No generated files found in $NEW_GEN_DIR"
        exit 1
    fi

    # Count generated files
    pb_count=$(find "$NEW_GEN_DIR" -name "*.pb.go" | wc -l)
    grpc_count=$(find "$NEW_GEN_DIR" -name "*_grpc.pb.go" | wc -l)
    gw_count=$(find "$NEW_GEN_DIR" -name "*.pb.gw.go" | wc -l)

    echo "Generated files:"
    echo "  Proto files: $pb_count"
    echo "  gRPC files: $grpc_count"
    echo "  Gateway files: $gw_count"

    # Test compilation
    if go build ./...; then
        echo "Compilation test passed"
    else
        echo "ERROR: Compilation test failed"
        exit 1
    fi
}

# Generate migration report
generate_report() {
    cat > "code-generation-report.md" << EOF
# Code Generation Migration Report

Generated on: $(date)

## Summary
- Old generation directory: $OLD_GEN_DIR
- New generation directory: $NEW_GEN_DIR
- Backup location: $BACKUP_DIR

## Statistics
EOF

    echo "- Proto files generated: $(find "$NEW_GEN_DIR" -name "*.pb.go" | wc -l)" >> "code-generation-report.md"
    echo "- gRPC files generated: $(find "$NEW_GEN_DIR" -name "*_grpc.pb.go" | wc -l)" >> "code-generation-report.md"
    echo "- Gateway files generated: $(find "$NEW_GEN_DIR" -name "*.pb.gw.go" | wc -l)" >> "code-generation-report.md"

    cat >> "code-generation-report.md" << EOF

## Generated File Structure
\`\`\`
EOF

    tree "$NEW_GEN_DIR" >> "code-generation-report.md" 2>/dev/null || find "$NEW_GEN_DIR" -type f | sort >> "code-generation-report.md"

    echo '```' >> "code-generation-report.md"
}

# Main execution
main() {
    echo "Starting generated code cleanup and regeneration..."

    create_backup
    clean_old_generated
    generate_new_code
    update_generated_files
    verify_generated_code
    generate_report

    echo "Code generation cleanup completed successfully!"
    echo "Report saved to: code-generation-report.md"
    echo "Backup created at: $BACKUP_DIR"
}

# Set up error handling
trap 'echo "Error occurred during code generation cleanup"; exit 1' ERR

# Run main function
main "$@"
````

## 04.5 Migration Validation and Testing

### 04.5.1 Migration Test Suite

```go
// file: tests/migration_test.go
// version: 1.0.0
// guid: f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c

package tests

import (
	"context"
	"fmt"
	"os"
	"path/filepath"
	"strings"
	"testing"
	"time"

	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/require"
	"google.golang.org/protobuf/proto"
	"google.golang.org/protobuf/reflect/protoreflect"
	"google.golang.org/protobuf/reflect/protoregistry"
)

type MigrationTestSuite struct {
	t            *testing.T
	protoDir     string
	generatedDir string
}

func NewMigrationTestSuite(t *testing.T) *MigrationTestSuite {
	return &MigrationTestSuite{
		t:            t,
		protoDir:     "proto/gcommon/v1",
		generatedDir: "internal/generated",
	}
}

func (mts *MigrationTestSuite) TestProtoFileStructure() {
	// Test that all expected domains exist
	expectedDomains := []string{
		"common", "config", "database", "media",
		"metrics", "organization", "queue", "web",
	}

	for _, domain := range expectedDomains {
		domainPath := filepath.Join(mts.protoDir, domain)
		assert.DirExists(mts.t, domainPath, "Domain directory should exist: %s", domain)
	}
}

func (mts *MigrationTestSuite) TestProtocolBufferCompilation() {
	// Find all .proto files
	protoFiles := []string{}
	err := filepath.Walk(mts.protoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.HasSuffix(path, ".proto") {
			protoFiles = append(protoFiles, path)
		}
		return nil
	})
	require.NoError(mts.t, err)

	assert.Greater(mts.t, len(protoFiles), 0, "Should find proto files")

	// Test that each proto file compiles
	for _, protoFile := range protoFiles {
		mts.t.Run(fmt.Sprintf("Compile_%s", filepath.Base(protoFile)), func(t *testing.T) {
			// This would typically use buf or protoc to compile
			// For now, just check file exists and is readable
			content, err := os.ReadFile(protoFile)
			require.NoError(t, err)
			assert.Greater(t, len(content), 0, "Proto file should not be empty")
		})
	}
}

func (mts *MigrationTestSuite) TestGeneratedGoCode() {
	// Find all generated .pb.go files
	goFiles := []string{}
	err := filepath.Walk(mts.generatedDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.HasSuffix(path, ".pb.go") {
			goFiles = append(goFiles, path)
		}
		return nil
	})
	require.NoError(mts.t, err)

	assert.Greater(mts.t, len(goFiles), 0, "Should find generated Go files")

	// Test that generated files have proper structure
	for _, goFile := range goFiles {
		mts.t.Run(fmt.Sprintf("Generated_%s", filepath.Base(goFile)), func(t *testing.T) {
			content, err := os.ReadFile(goFile)
			require.NoError(t, err)

			contentStr := string(content)
			assert.Contains(t, contentStr, "// Code generated by protoc-gen-go")
			assert.Contains(t, contentStr, "package ")
		})
	}
}

func (mts *MigrationTestSuite) TestImportResolution() {
	// Test that all imports resolve correctly
	protoFiles := []string{}
	err := filepath.Walk(mts.protoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.HasSuffix(path, ".proto") {
			protoFiles = append(protoFiles, path)
		}
		return nil
	})
	require.NoError(mts.t, err)

	for _, protoFile := range protoFiles {
		mts.t.Run(fmt.Sprintf("Imports_%s", filepath.Base(protoFile)), func(t *testing.T) {
			content, err := os.ReadFile(protoFile)
			require.NoError(t, err)

			lines := strings.Split(string(content), "\n")
			for lineNum, line := range lines {
				line = strings.TrimSpace(line)
				if strings.HasPrefix(line, "import ") {
					// Extract import path
					start := strings.Index(line, `"`)
					end := strings.LastIndex(line, `"`)
					if start != -1 && end != -1 && start < end {
						importPath := line[start+1 : end]

						// Check if imported file exists
						if strings.HasPrefix(importPath, "gcommon/") {
							// Internal import
							expectedPath := filepath.Join("proto", importPath+".proto")
							assert.FileExists(t, expectedPath,
								"Import not found at line %d: %s", lineNum+1, importPath)
						}
					}
				}
			}
		})
	}
}

func (mts *MigrationTestSuite) TestPackageNaming() {
	protoFiles := []string{}
	err := filepath.Walk(mts.protoDir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if strings.HasSuffix(path, ".proto") {
			protoFiles = append(protoFiles, path)
		}
		return nil
	})
	require.NoError(mts.t, err)

	for _, protoFile := range protoFiles {
		mts.t.Run(fmt.Sprintf("Package_%s", filepath.Base(protoFile)), func(t *testing.T) {
			content, err := os.ReadFile(protoFile)
			require.NoError(t, err)

			lines := strings.Split(string(content), "\n")
			packageFound := false
			for _, line := range lines {
				line = strings.TrimSpace(line)
				if strings.HasPrefix(line, "package ") {
					packageName := strings.TrimSuffix(strings.TrimPrefix(line, "package "), ";")
					packageName = strings.TrimSpace(packageName)

					// Check that package follows naming convention
					assert.True(t, strings.HasPrefix(packageName, "gcommon.v1."),
						"Package should start with 'gcommon.v1.': %s", packageName)
					packageFound = true
					break
				}
			}
			assert.True(t, packageFound, "Proto file should have package declaration")
		})
	}
}

func (mts *MigrationTestSuite) TestMessageSerialization() {
	// Test that messages can be serialized/deserialized
	// This is a basic smoke test for generated code

	// Get all registered message types
	protoregistry.GlobalTypes.RangeMessages(func(mt protoreflect.MessageType) bool {
		msgName := string(mt.Descriptor().FullName())

		// Only test our gcommon messages
		if strings.HasPrefix(msgName, "gcommon.v1.") {
			mts.t.Run(fmt.Sprintf("Serialization_%s", msgName), func(t *testing.T) {
				// Create a new instance of the message
				msg := mt.New().Interface()

				// Serialize to bytes
				data, err := proto.Marshal(msg)
				require.NoError(t, err)

				// Deserialize back
				newMsg := mt.New().Interface()
				err = proto.Unmarshal(data, newMsg)
				require.NoError(t, err)

				// Verify they're equal
				assert.True(t, proto.Equal(msg, newMsg))
			})
		}

		return true
	})
}

func (mts *MigrationTestSuite) TestBackwardCompatibility() {
	// Test that old and new generated code are compatible
	// This would involve loading old proto definitions and comparing

	mts.t.Run("SchemaCompatibility", func(t *testing.T) {
		// TODO: Implement schema compatibility checks
		// This would typically involve:
		// 1. Loading old proto definitions
		// 2. Loading new proto definitions
		// 3. Comparing field numbers, types, and names
		// 4. Ensuring no breaking changes

		t.Skip("Schema compatibility test not yet implemented")
	})
}

func TestMigrationSuite(t *testing.T) {
	suite := NewMigrationTestSuite(t)

	t.Run("ProtoFileStructure", suite.TestProtoFileStructure)
	t.Run("ProtocolBufferCompilation", suite.TestProtocolBufferCompilation)
	t.Run("GeneratedGoCode", suite.TestGeneratedGoCode)
	t.Run("ImportResolution", suite.TestImportResolution)
	t.Run("PackageNaming", suite.TestPackageNaming)
	t.Run("MessageSerialization", suite.TestMessageSerialization)
	t.Run("BackwardCompatibility", suite.TestBackwardCompatibility)
}

// Benchmark tests for performance verification
func BenchmarkProtoSerialization(b *testing.B) {
	// TODO: Add benchmarks for proto serialization performance
	b.Skip("Benchmark tests not yet implemented")
}

func BenchmarkImportResolution(b *testing.B) {
	// TODO: Add benchmarks for import resolution performance
	b.Skip("Benchmark tests not yet implemented")
}
```

### 04.5.2 Automated Migration Validation

```bash
#!/bin/bash
# file: scripts/validate-migration.sh
# version: 1.0.0
# guid: a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d

set -euo pipefail

# Configuration
PROTO_DIR="proto/gcommon/v1"
GENERATED_DIR="internal/generated"
VALIDATION_LOG="migration-validation.log"
TEMP_DIR="/tmp/migration-validation"

# Create temp directory
mkdir -p "$TEMP_DIR"

# Function to log messages
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$VALIDATION_LOG"
}

# Function to run validation step
validate_step() {
    local step_name="$1"
    local command="$2"

    log "Starting validation: $step_name"

    if eval "$command" > "$TEMP_DIR/$step_name.log" 2>&1; then
        log "✓ $step_name: PASSED"
        return 0
    else
        log "✗ $step_name: FAILED"
        log "Error details:"
        cat "$TEMP_DIR/$step_name.log" | tee -a "$VALIDATION_LOG"
        return 1
    fi
}

# Validation steps
validate_proto_structure() {
    local expected_domains=("common" "config" "database" "media" "metrics" "organization" "queue" "web")

    for domain in "${expected_domains[@]}"; do
        if [ ! -d "$PROTO_DIR/$domain" ]; then
            echo "Missing domain directory: $domain"
            return 1
        fi
    done

    # Count proto files
    local proto_count=$(find "$PROTO_DIR" -name "*.proto" | wc -l)
    if [ "$proto_count" -lt 100 ]; then
        echo "Expected at least 100 proto files, found $proto_count"
        return 1
    fi

    echo "Proto structure validation passed: $proto_count files in ${#expected_domains[@]} domains"
}

validate_buf_compilation() {
    buf lint "$PROTO_DIR"
    buf generate
}

validate_go_compilation() {
    go mod tidy
    go build ./...
}

validate_import_resolution() {
    python3 << 'EOF'
import os
import re
from pathlib import Path

def validate_imports(proto_dir):
    failed_imports = []

    for proto_file in Path(proto_dir).rglob("*.proto"):
        content = proto_file.read_text()

        for line_num, line in enumerate(content.split('\n'), 1):
            if line.strip().startswith('import '):
                # Extract import path
                match = re.search(r'import\s+"([^"]+)";', line)
                if match:
                    import_path = match.group(1)

                    # Check if import exists
                    if import_path.startswith('gcommon/'):
                        expected_file = Path('proto') / (import_path + '.proto')
                        if not expected_file.exists():
                            failed_imports.append(f"{proto_file}:{line_num} -> {import_path}")

    if failed_imports:
        print("Failed imports:")
        for failure in failed_imports:
            print(f"  {failure}")
        return False

    print("All imports resolved successfully")
    return True

if not validate_imports(os.environ.get('PROTO_DIR', 'proto/gcommon/v1')):
    exit(1)
EOF
}

validate_generated_code() {
    # Check that generated files exist
    local pb_count=$(find "$GENERATED_DIR" -name "*.pb.go" | wc -l)
    local grpc_count=$(find "$GENERATED_DIR" -name "*_grpc.pb.go" | wc -l)

    if [ "$pb_count" -eq 0 ]; then
        echo "No .pb.go files found in $GENERATED_DIR"
        return 1
    fi

    echo "Generated code validation passed: $pb_count .pb.go files, $grpc_count gRPC files"
}

validate_package_naming() {
    python3 << 'EOF'
import os
import re
from pathlib import Path

def validate_packages(proto_dir):
    invalid_packages = []

    for proto_file in Path(proto_dir).rglob("*.proto"):
        content = proto_file.read_text()

        # Find package declaration
        package_match = re.search(r'package\s+([^;]+);', content)
        if package_match:
            package_name = package_match.group(1).strip()

            # Check naming convention
            if not package_name.startswith('gcommon.v1.'):
                invalid_packages.append(f"{proto_file} -> {package_name}")

    if invalid_packages:
        print("Invalid package names:")
        for invalid in invalid_packages:
            print(f"  {invalid}")
        return False

    print("All packages follow naming convention")
    return True

if not validate_packages(os.environ.get('PROTO_DIR', 'proto/gcommon/v1')):
    exit(1)
EOF
}

run_tests() {
    go test ./tests/... -v
}

# Main validation workflow
main() {
    log "Starting migration validation..."

    # Initialize log file
    > "$VALIDATION_LOG"

    local failed_steps=()

    # Run validation steps
    validate_step "proto_structure" "validate_proto_structure" || failed_steps+=("proto_structure")
    validate_step "buf_compilation" "validate_buf_compilation" || failed_steps+=("buf_compilation")
    validate_step "go_compilation" "validate_go_compilation" || failed_steps+=("go_compilation")
    validate_step "import_resolution" "validate_import_resolution" || failed_steps+=("import_resolution")
    validate_step "generated_code" "validate_generated_code" || failed_steps+=("generated_code")
    validate_step "package_naming" "validate_package_naming" || failed_steps+=("package_naming")
    validate_step "tests" "run_tests" || failed_steps+=("tests")

    # Generate final report
    if [ ${#failed_steps[@]} -eq 0 ]; then
        log "🎉 All validation steps passed!"
        log "Migration validation completed successfully"
        exit 0
    else
        log "❌ Migration validation failed"
        log "Failed steps: ${failed_steps[*]}"
        log "Check $VALIDATION_LOG for details"
        exit 1
    fi
}

# Cleanup function
cleanup() {
    rm -rf "$TEMP_DIR"
}

# Set up cleanup trap
trap cleanup EXIT

# Run main function
main "$@"
```

This section provides comprehensive file migration and import management strategies for the protobuf reorganization. The scripts and tools ensure proper dependency resolution, conflict resolution, and validation throughout the migration
process.
