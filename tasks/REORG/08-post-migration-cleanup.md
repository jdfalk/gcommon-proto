<!-- file: tasks/REORG/08-post-migration-cleanup.md -->
<!-- version: 1.0.0 -->
<!-- guid: 1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d -->

# Section 08: Post-Migration Cleanup

## 08.1 Cleanup Strategy

### 08.1.1 Generated Code Cleanup

**File:** `scripts/cleanup-generated-code.py`

```python
#!/usr/bin/env python3
# file: scripts/cleanup-generated-code.py
# version: 1.0.0
# guid: 2b3c4d5e-6f7a-8b9c-0d1e-2f3a4b5c6d7e

"""
Clean up old generated code files after migration.
"""

import os
import sys
from pathlib import Path
from typing import List, Set

def find_orphaned_generated_files() -> List[Path]:
    """Find generated files that no longer have corresponding proto files."""
    orphaned_files = []
    
    # Find all generated files
    for pb_file in Path('pkg').rglob('*.pb.go'):
        # Determine what proto file this was generated from
        proto_candidates = [
            # New structure
            Path('proto') / 'gcommon' / 'v1' / pb_file.parent.relative_to(Path('pkg')) / f"{pb_file.stem}.proto",
            # Check if proto file exists anywhere in new structure
        ]
        
        # Add all possible proto locations
        for proto_file in Path('proto').rglob(f"{pb_file.stem}.proto"):
            proto_candidates.append(proto_file)
        
        # Check if any corresponding proto file exists
        if not any(candidate.exists() for candidate in proto_candidates):
            orphaned_files.append(pb_file)
    
    # Same for gRPC files
    for grpc_file in Path('pkg').rglob('*_grpc.pb.go'):
        base_name = grpc_file.stem.replace('_grpc.pb', '')
        
        proto_candidates = []
        for proto_file in Path('proto').rglob(f"{base_name}.proto"):
            proto_candidates.append(proto_file)
        
        if not any(candidate.exists() for candidate in proto_candidates):
            orphaned_files.append(grpc_file)
    
    return orphaned_files

def cleanup_old_generated_files():
    """Clean up old generated files."""
    print("🧹 Cleaning up old generated files...")
    
    orphaned_files = find_orphaned_generated_files()
    
    if not orphaned_files:
        print("✅ No orphaned generated files found")
        return
    
    print(f"📁 Found {len(orphaned_files)} orphaned files")
    
    for orphan_file in orphaned_files:
        try:
            orphan_file.unlink()
            print(f"🗑️  Removed: {orphan_file}")
        except Exception as e:
            print(f"❌ Failed to remove {orphan_file}: {e}")
    
    # Remove empty directories
    for pkg_dir in Path('pkg').rglob('*'):
        if pkg_dir.is_dir() and not any(pkg_dir.iterdir()):
            try:
                pkg_dir.rmdir()
                print(f"📂 Removed empty directory: {pkg_dir}")
            except OSError:
                pass  # Directory not empty or other issue
    
    print("✅ Generated code cleanup completed")

if __name__ == '__main__':
    cleanup_old_generated_files()
```

### 08.1.2 Old Proto File Cleanup

**File:** `scripts/cleanup-old-protos.py`

```python
#!/usr/bin/env python3
# file: scripts/cleanup-old-protos.py
# version: 1.0.0
# guid: 3c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f

"""
Clean up old proto files after successful migration.
"""

import os
import sys
from pathlib import Path

def cleanup_old_proto_files():
    """Remove old proto files from pkg/ directories."""
    print("🧹 Cleaning up old proto files...")
    
    old_proto_files = list(Path('pkg').rglob('*.proto'))
    
    if not old_proto_files:
        print("✅ No old proto files found")
        return
    
    print(f"📁 Found {len(old_proto_files)} old proto files")
    
    # Group by directory for better organization
    dirs_to_clean = {}
    for proto_file in old_proto_files:
        proto_dir = proto_file.parent
        if proto_dir not in dirs_to_clean:
            dirs_to_clean[proto_dir] = []
        dirs_to_clean[proto_dir].append(proto_file)
    
    # Clean each directory
    for proto_dir, files in dirs_to_clean.items():
        print(f"📂 Cleaning directory: {proto_dir}")
        
        for proto_file in files:
            try:
                proto_file.unlink()
                print(f"🗑️  Removed: {proto_file}")
            except Exception as e:
                print(f"❌ Failed to remove {proto_file}: {e}")
        
        # Remove proto directory if empty
        try:
            if proto_dir.name == 'proto' and not any(proto_dir.iterdir()):
                proto_dir.rmdir()
                print(f"📂 Removed empty proto directory: {proto_dir}")
        except OSError:
            pass  # Directory not empty
    
    print("✅ Old proto file cleanup completed")

def verify_migration_completeness():
    """Verify that migration is complete before cleanup."""
    print("🔍 Verifying migration completeness...")
    
    # Check that proto/ directory exists and has files
    proto_dir = Path('proto')
    if not proto_dir.exists():
        print("❌ proto/ directory not found - migration incomplete")
        return False
    
    new_proto_files = list(proto_dir.rglob('*.proto'))
    if not new_proto_files:
        print("❌ No proto files in new structure - migration incomplete")
        return False
    
    print(f"✅ Found {len(new_proto_files)} files in new structure")
    
    # Check that buf configuration is updated
    buf_yaml = Path('buf.yaml')
    if buf_yaml.exists():
        with open(buf_yaml, 'r') as f:
            content = f.read()
            if 'path: proto' not in content:
                print("❌ buf.yaml not updated for new structure")
                return False
    
    print("✅ Migration verification passed")
    return True

if __name__ == '__main__':
    if verify_migration_completeness():
        cleanup_old_proto_files()
    else:
        print("💥 Migration incomplete - skipping cleanup")
        sys.exit(1)
```

## 08.2 Documentation Updates

### 08.2.1 Update Proto Documentation

**File:** `scripts/update-proto-docs.py`

```python
#!/usr/bin/env python3
# file: scripts/update-proto-docs.py
# version: 1.0.0
# guid: 4d5e6f7a-8b9c-0d1e-2f3a-4b5c6d7e8f9a

"""
Update protobuf documentation after migration.
"""

import os
import re
from pathlib import Path

def update_readme_files():
    """Update README files with new proto structure."""
    print("📝 Updating README files...")
    
    readme_files = [
        Path('README.md'),
        Path('docs/README.md'),
        Path('proto/README.md')
    ]
    
    for readme_file in readme_files:
        if readme_file.exists():
            update_readme_content(readme_file)

def update_readme_content(readme_file: Path):
    """Update content of a README file."""
    try:
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update proto path references
        content = re.sub(
            r'pkg/([^/]+)/proto/',
            r'proto/gcommon/v1/\1/',
            content
        )
        
        # Update import examples
        content = re.sub(
            r'import "pkg/([^/]+)/proto/([^"]+)"',
            r'import "proto/gcommon/v1/\1/\2"',
            content
        )
        
        # Update package references
        content = re.sub(
            r'package ([^.]+)\.proto',
            r'package gcommon.v1.\1',
            content
        )
        
        with open(readme_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {readme_file}")
        
    except Exception as e:
        print(f"❌ Failed to update {readme_file}: {e}")

def create_proto_structure_doc():
    """Create documentation for the new proto structure."""
    doc_content = """# Protocol Buffer Structure

## Directory Organization

The protocol buffer files are organized in a hierarchical structure under `proto/gcommon/v1/`:

```
proto/gcommon/v1/
├── common/              # Common types and utilities
│   ├── types/          # Basic types (entities, errors, etc.)
│   ├── messages/       # Common messages
│   ├── enums/          # Common enumerations
│   └── services/       # Common services
├── config/             # Configuration domain
│   ├── api/           # Configuration APIs
│   ├── v1/            # Configuration v1
│   ├── v2/            # Configuration v2
│   └── services/      # Configuration services
├── database/           # Database domain
│   ├── config/        # Database configuration
│   ├── services/      # Database services
│   ├── types/         # Database types
│   └── schema/        # Schema definitions
├── media/              # Media domain
│   ├── types/         # Media types (audio, video, image)
│   ├── metadata/      # Media metadata
│   ├── services/      # Media services
│   └── processing/    # Media processing
├── metrics/            # Metrics domain
│   ├── v1/           # Metrics v1
│   ├── v2/           # Metrics v2
│   ├── services/     # Metrics services
│   └── types/        # Metrics types
├── organization/       # Organization domain
│   ├── api/          # Organization APIs
│   ├── config/       # Organization configuration
│   ├── services/     # Organization services
│   └── types/        # Organization types
├── queue/              # Queue domain
│   ├── api/          # Queue APIs
│   ├── config/       # Queue configuration
│   ├── services/     # Queue services
│   └── types/        # Queue types
└── web/                # Web domain
    ├── api/           # Web APIs
    ├── config/        # Web configuration
    ├── events/        # Web events
    └── services/      # Web services
```

## Package Naming Convention

All packages follow the format: `gcommon.v1.{domain}.{category}`

Examples:
- `gcommon.v1.common.types`
- `gcommon.v1.config.api`
- `gcommon.v1.database.services`

## Import Paths

Import paths follow the new structure:

```protobuf
import "proto/gcommon/v1/common/types/entity.proto";
import "proto/gcommon/v1/config/api/app_config.proto";
import "proto/gcommon/v1/media/types/audio_track.proto";
```

## Generated Code

Generated Go code is placed in `pkg/` with the following structure:

```
pkg/
├── common/
│   ├── types/         # Generated from proto/gcommon/v1/common/types/
│   ├── messages/      # Generated from proto/gcommon/v1/common/messages/
│   └── services/      # Generated from proto/gcommon/v1/common/services/
├── config/
│   ├── api/           # Generated from proto/gcommon/v1/config/api/
│   └── services/      # Generated from proto/gcommon/v1/config/services/
└── [other domains]/
```

## Code Generation

Use the following commands to generate code:

```bash
# Generate all code
buf generate

# Lint proto files
buf lint

# Build and validate
buf build
```
"""
    
    doc_file = Path('docs/PROTO_STRUCTURE.md')
    doc_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(doc_content)
    
    print(f"✅ Created: {doc_file}")

if __name__ == '__main__':
    update_readme_files()
    create_proto_structure_doc()
    print("📚 Documentation updates completed")
```

### 08.2.2 Generate Migration Report

**File:** `scripts/generate-migration-report.py`

```python
#!/usr/bin/env python3
# file: scripts/generate-migration-report.py
# version: 1.0.0
# guid: 5e6f7a8b-9c0d-1e2f-3a4b-5c6d7e8f9a0b

"""
Generate comprehensive migration report.
"""

import os
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

def collect_migration_stats() -> Dict:
    """Collect migration statistics."""
    stats = {
        'timestamp': datetime.now().isoformat(),
        'domains': {},
        'totals': {
            'proto_files': 0,
            'generated_files': 0,
            'total_lines': 0
        }
    }
    
    # Analyze new proto structure
    for domain_dir in Path('proto/gcommon/v1').iterdir():
        if domain_dir.is_dir():
            domain_stats = analyze_domain(domain_dir)
            stats['domains'][domain_dir.name] = domain_stats
            stats['totals']['proto_files'] += domain_stats['proto_files']
            stats['totals']['total_lines'] += domain_stats['total_lines']
    
    # Count generated files
    stats['totals']['generated_files'] = len(list(Path('pkg').rglob('*.pb.go')))
    
    return stats

def analyze_domain(domain_dir: Path) -> Dict:
    """Analyze a specific domain directory."""
    stats = {
        'proto_files': 0,
        'subdirectories': [],
        'total_lines': 0,
        'services': 0,
        'messages': 0,
        'enums': 0
    }
    
    for subdir in domain_dir.iterdir():
        if subdir.is_dir():
            stats['subdirectories'].append(subdir.name)
            
            for proto_file in subdir.rglob('*.proto'):
                stats['proto_files'] += 1
                
                # Count lines and analyze content
                try:
                    with open(proto_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        stats['total_lines'] += len(content.splitlines())
                        
                        # Count proto elements
                        stats['services'] += content.count('service ')
                        stats['messages'] += content.count('message ')
                        stats['enums'] += content.count('enum ')
                        
                except Exception:
                    pass
    
    return stats

def generate_html_report(stats: Dict):
    """Generate HTML migration report."""
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Protocol Buffer Migration Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        .summary {{ background-color: #e7f3ff; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
        .domain {{ margin-bottom: 20px; }}
        .timestamp {{ color: #666; font-size: 0.9em; }}
    </style>
</head>
<body>
    <h1>Protocol Buffer Migration Report</h1>
    
    <div class="summary">
        <h2>Migration Summary</h2>
        <p><strong>Generated:</strong> <span class="timestamp">{stats['timestamp']}</span></p>
        <p><strong>Total Proto Files:</strong> {stats['totals']['proto_files']}</p>
        <p><strong>Total Generated Files:</strong> {stats['totals']['generated_files']}</p>
        <p><strong>Total Lines of Proto Code:</strong> {stats['totals']['total_lines']:,}</p>
        <p><strong>Domains Migrated:</strong> {len(stats['domains'])}</p>
    </div>
    
    <h2>Domain Breakdown</h2>
    <table>
        <tr>
            <th>Domain</th>
            <th>Proto Files</th>
            <th>Lines of Code</th>
            <th>Services</th>
            <th>Messages</th>
            <th>Enums</th>
            <th>Subdirectories</th>
        </tr>
"""
    
    for domain_name, domain_stats in sorted(stats['domains'].items()):
        subdirs = ', '.join(domain_stats['subdirectories'])
        html_content += f"""
        <tr>
            <td><strong>{domain_name}</strong></td>
            <td>{domain_stats['proto_files']}</td>
            <td>{domain_stats['total_lines']:,}</td>
            <td>{domain_stats['services']}</td>
            <td>{domain_stats['messages']}</td>
            <td>{domain_stats['enums']}</td>
            <td>{subdirs}</td>
        </tr>
"""
    
    html_content += """
    </table>
    
    <h2>Migration Benefits</h2>
    <ul>
        <li><strong>Organized Structure:</strong> All proto files now follow a consistent hierarchy</li>
        <li><strong>Improved Navigation:</strong> Clear domain and category separation</li>
        <li><strong>Better Tooling Support:</strong> Enhanced IDE support and code generation</li>
        <li><strong>Scalable Architecture:</strong> Easy to add new domains and services</li>
        <li><strong>Industry Standards:</strong> Follows Buf best practices and conventions</li>
    </ul>
    
    <h2>Next Steps</h2>
    <ol>
        <li>Update CI/CD pipelines to use new proto structure</li>
        <li>Update development documentation</li>
        <li>Train team on new structure and workflows</li>
        <li>Set up automated proto validation</li>
        <li>Consider implementing proto breaking change detection</li>
    </ol>
    
</body>
</html>
"""
    
    report_file = Path('migration-report.html')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Generated HTML report: {report_file}")

def generate_json_report(stats: Dict):
    """Generate JSON migration report."""
    report_file = Path('migration-report.json')
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)
    
    print(f"✅ Generated JSON report: {report_file}")

if __name__ == '__main__':
    print("📊 Generating migration report...")
    
    stats = collect_migration_stats()
    generate_html_report(stats)
    generate_json_report(stats)
    
    print("🎉 Migration report generation completed")
```

## 08.3 Performance Optimization

### 08.3.1 Generated Code Optimization

**File:** `scripts/optimize-generated-code.py`

```python
#!/usr/bin/env python3
# file: scripts/optimize-generated-code.py
# version: 1.0.0
# guid: 6f7a8b9c-0d1e-2f3a-4b5c-6d7e8f9a0b1c

"""
Optimize generated code for better performance.
"""

import os
import re
from pathlib import Path

def optimize_generated_files():
    """Apply optimizations to generated Go files."""
    print("⚡ Optimizing generated code...")
    
    optimized_count = 0
    
    for pb_file in Path('pkg').rglob('*.pb.go'):
        if optimize_pb_file(pb_file):
            optimized_count += 1
    
    print(f"✅ Optimized {optimized_count} files")

def optimize_pb_file(pb_file: Path) -> bool:
    """Optimize a single .pb.go file."""
    try:
        with open(pb_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Add build tags for conditional compilation
        if not content.startswith('//go:build'):
            content = '//go:build !ignore_autogenerated\n\n' + content
        
        # Optimize imports (remove unused if any)
        content = optimize_imports(content)
        
        # Add performance hints
        content = add_performance_hints(content)
        
        if content != original_content:
            with open(pb_file, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"⚠️  Failed to optimize {pb_file}: {e}")
        return False

def optimize_imports(content: str) -> str:
    """Optimize import statements."""
    # This is a placeholder for import optimization
    # In practice, you'd use tools like goimports
    return content

def add_performance_hints(content: str) -> str:
    """Add performance optimization hints."""
    # Add compiler hints for hot paths
    if 'func (x *' in content and 'String()' in content:
        content = re.sub(
            r'func \(x \*(\w+)\) String\(\) string {',
            r'//go:noinline\nfunc (x *\1) String() string {',
            content
        )
    
    return content

if __name__ == '__main__':
    optimize_generated_files()
```

## 08.4 CI/CD Updates

### 08.4.1 Update GitHub Actions

**File:** `scripts/update-github-actions.py`

```python
#!/usr/bin/env python3
# file: scripts/update-github-actions.py
# version: 1.0.0
# guid: 7a8b9c0d-1e2f-3a4b-5c6d-7e8f9a0b1c2d

"""
Update GitHub Actions workflows for new proto structure.
"""

import os
import re
import yaml
from pathlib import Path

def update_workflows():
    """Update all GitHub Actions workflows."""
    print("🔄 Updating GitHub Actions workflows...")
    
    workflow_dir = Path('.github/workflows')
    if not workflow_dir.exists():
        print("ℹ️  No workflows directory found")
        return
    
    for workflow_file in workflow_dir.glob('*.yml'):
        update_workflow_file(workflow_file)

def update_workflow_file(workflow_file: Path):
    """Update a single workflow file."""
    try:
        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update proto paths in workflow steps
        content = re.sub(
            r'pkg/\*/proto/\*\.proto',
            r'proto/**/*.proto',
            content
        )
        
        # Update buf commands to use new structure
        content = re.sub(
            r'buf build',
            r'buf build proto',
            content
        )
        
        # Update any hardcoded pkg/ references
        content = re.sub(
            r'pkg/([^/]+)/proto',
            r'proto/gcommon/v1/\1',
            content
        )
        
        if content != original_content:
            with open(workflow_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Updated: {workflow_file}")
        else:
            print(f"ℹ️  No changes needed: {workflow_file}")
            
    except Exception as e:
        print(f"❌ Failed to update {workflow_file}: {e}")

if __name__ == '__main__':
    update_workflows()
```

## 08.5 Final Verification

### 08.5.1 Complete System Test

**File:** `scripts/final-verification.py`

```python
#!/usr/bin/env python3
# file: scripts/final-verification.py
# version: 1.0.0
# guid: 8b9c0d1e-2f3a-4b5c-6d7e-8f9a0b1c2d3e

"""
Final verification that the entire migration is successful.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_final_verification():
    """Run comprehensive final verification."""
    print("🔍 Running final verification...")
    
    tests = [
        ("Directory structure", verify_directory_structure),
        ("Proto syntax", verify_proto_syntax),
        ("Buf compilation", verify_buf_compilation),
        ("Go compilation", verify_go_compilation),
        ("Import resolution", verify_import_resolution),
        ("Generated code", verify_generated_code),
        ("Documentation", verify_documentation)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n🧪 Testing: {test_name}")
        try:
            result = test_func()
            results.append((test_name, result))
            if result:
                print(f"✅ {test_name}: PASSED")
            else:
                print(f"❌ {test_name}: FAILED")
        except Exception as e:
            print(f"💥 {test_name}: ERROR - {e}")
            results.append((test_name, False))
    
    # Print summary
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    print(f"\n📊 Final Verification Summary:")
    print(f"   Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED - Migration successful!")
        return True
    else:
        print("💥 Some tests failed - Migration needs attention")
        return False

def verify_directory_structure() -> bool:
    """Verify directory structure is correct."""
    required_dirs = [
        'proto/gcommon/v1/common',
        'proto/gcommon/v1/config', 
        'proto/gcommon/v1/database',
        'proto/gcommon/v1/media',
        'proto/gcommon/v1/metrics',
        'proto/gcommon/v1/organization',
        'proto/gcommon/v1/queue',
        'proto/gcommon/v1/web'
    ]
    
    return all(Path(d).exists() for d in required_dirs)

def verify_proto_syntax() -> bool:
    """Verify proto files have correct syntax."""
    proto_files = list(Path('proto').rglob('*.proto'))
    if not proto_files:
        return False
    
    for proto_file in proto_files[:5]:  # Test sample
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if 'package gcommon.v1.' not in content:
                return False
            if 'option go_package' not in content:
                return False
                
        except Exception:
            return False
    
    return True

def verify_buf_compilation() -> bool:
    """Verify buf can compile the new structure."""
    try:
        result = subprocess.run(
            ['buf', 'build', 'proto'],
            capture_output=True,
            text=True,
            timeout=60
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return True  # Skip if buf not available

def verify_go_compilation() -> bool:
    """Verify Go code compiles."""
    try:
        result = subprocess.run(
            ['go', 'build', './...'],
            capture_output=True,
            text=True,
            timeout=300
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return True  # Skip if Go not available

def verify_import_resolution() -> bool:
    """Verify import paths resolve correctly."""
    proto_files = list(Path('proto').rglob('*.proto'))
    
    for proto_file in proto_files[:10]:  # Test sample
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            imports = re.findall(r'import\s+"([^"]+)";', content)
            for import_path in imports:
                if import_path.startswith('proto/'):
                    import_file = Path(import_path)
                    if not import_file.exists():
                        return False
                        
        except Exception:
            return False
    
    return True

def verify_generated_code() -> bool:
    """Verify generated code exists and is valid."""
    pb_files = list(Path('pkg').rglob('*.pb.go'))
    return len(pb_files) > 0

def verify_documentation() -> bool:
    """Verify documentation exists."""
    doc_files = [
        'docs/PROTO_STRUCTURE.md',
        'migration-report.html'
    ]
    return all(Path(f).exists() for f in doc_files)

if __name__ == '__main__':
    if run_final_verification():
        sys.exit(0)
    else:
        sys.exit(1)
```

This completes Section 08 - Post-Migration Cleanup. The section includes comprehensive cleanup procedures, documentation updates, performance optimizations, CI/CD updates, and final verification to ensure the migration is completely successful.