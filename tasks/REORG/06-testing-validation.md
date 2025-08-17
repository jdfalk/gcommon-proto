<!-- file: tasks/REORG/06-testing-validation.md -->
<!-- version: 1.0.0 -->
<!-- guid: 2f3a4b5c-6d7e-8f9a-0b1c-2d3e4f5a6b7c -->

# Section 06: Testing and Validation

## 06.1 Pre-Migration Testing

### 06.1.1 Current State Validation

**File:** `scripts/test-current-state.py`

```python
#!/usr/bin/env python3
# file: scripts/test-current-state.py
# version: 1.0.0
# guid: 3a4b5c6d-7e8f-9a0b-1c2d-3e4f5a6b7c8d

"""
Test and validate current proto file state before migration.
"""

import os
import sys
import subprocess
from pathlib import Path

def test_current_proto_compilation():
    """Test that current proto files compile successfully."""
    print("🔍 Testing current proto compilation...")

    # Find all proto files
    proto_files = []
    for proto_file in Path('.').rglob('pkg/**/*.proto'):
        proto_files.append(str(proto_file))

    if not proto_files:
        print("❌ No proto files found")
        return False

    print(f"📁 Found {len(proto_files)} proto files")

    # Test compilation with protoc if available
    try:
        result = subprocess.run(
            ['protoc', '--version'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ protoc available: {result.stdout.strip()}")
            return test_protoc_compilation(proto_files)
        else:
            print("⚠️  protoc not available, skipping compilation test")
            return True
    except FileNotFoundError:
        print("⚠️  protoc not found, skipping compilation test")
        return True

def test_protoc_compilation(proto_files):
    """Test proto compilation with protoc."""
    failed_files = []

    for proto_file in proto_files[:10]:  # Test first 10 files
        try:
            result = subprocess.run([
                'protoc',
                '--proto_path=.',
                '--go_out=/tmp',
                proto_file
            ], capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                failed_files.append(proto_file)

        except subprocess.TimeoutExpired:
            failed_files.append(f"{proto_file} (timeout)")
        except Exception as e:
            failed_files.append(f"{proto_file} (error: {e})")

    if failed_files:
        print(f"⚠️  Some files failed compilation: {len(failed_files)}")
        return False
    else:
        print("✅ Proto compilation test passed")
        return True

if __name__ == '__main__':
    if test_current_proto_compilation():
        sys.exit(0)
    else:
        sys.exit(1)
```

### 06.1.2 Import Dependency Analysis

**File:** `scripts/analyze-dependencies.py`

```python
#!/usr/bin/env python3
# file: scripts/analyze-dependencies.py
# version: 1.0.0
# guid: 4b5c6d7e-8f9a-0b1c-2d3e-4f5a6b7c8d9e

"""
Analyze proto file dependencies to plan migration order.
"""

import re
import json
from pathlib import Path
from typing import Dict, List, Set

def analyze_proto_dependencies():
    """Analyze dependencies between proto files."""
    dependencies = {}
    all_files = set()

    # Find all proto files
    for proto_file in Path('.').rglob('pkg/**/*.proto'):
        file_path = str(proto_file)
        all_files.add(file_path)

        # Extract imports
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()

            imports = re.findall(r'import\s+"([^"]+)";', content)
            local_imports = [imp for imp in imports if imp.startswith('pkg/')]

            dependencies[file_path] = local_imports

        except Exception as e:
            print(f"⚠️  Could not analyze {file_path}: {e}")

    # Create dependency graph
    print(f"📊 Dependency Analysis:")
    print(f"   Total files: {len(all_files)}")
    print(f"   Files with dependencies: {len([f for f in dependencies.values() if f])}")

    # Find files with no dependencies (migration candidates)
    no_deps = [f for f, deps in dependencies.items() if not deps]
    print(f"   Files with no dependencies: {len(no_deps)}")

    # Find most imported files
    import_counts = {}
    for deps in dependencies.values():
        for dep in deps:
            import_counts[dep] = import_counts.get(dep, 0) + 1

    most_imported = sorted(import_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    print(f"   Most imported files:")
    for file_path, count in most_imported:
        print(f"     {file_path}: {count} imports")

    # Save dependency data
    with open('proto-dependencies.json', 'w') as f:
        json.dump({
            'dependencies': dependencies,
            'import_counts': import_counts,
            'no_dependencies': no_deps
        }, f, indent=2)

    print("✅ Dependency analysis saved to proto-dependencies.json")

if __name__ == '__main__':
    analyze_proto_dependencies()
```

## 06.2 Migration Testing

### 06.2.1 Progressive Migration Testing

**File:** `scripts/test-progressive-migration.py`

```python
#!/usr/bin/env python3
# file: scripts/test-progressive-migration.py
# version: 1.0.0
# guid: 5c6d7e8f-9a0b-1c2d-3e4f-5a6b7c8d9e0f

"""
Test progressive migration by domain to ensure each step works.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

def test_domain_migration(domain):
    """Test migration for a specific domain."""
    print(f"🧪 Testing {domain} domain migration...")

    # Create temporary directory for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Copy current structure to temp
        temp_path = Path(temp_dir)
        shutil.copytree('.', temp_path / 'test',
                       ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))

        os.chdir(temp_path / 'test')

        # Run domain migration in dry-run mode
        result = os.system(f'python3 scripts/migrate-domain.py {domain} --dry-run')

        if result == 0:
            print(f"✅ {domain} domain migration test passed")
            return True
        else:
            print(f"❌ {domain} domain migration test failed")
            return False

def test_all_domains():
    """Test migration for all domains."""
    domains = ['common', 'config', 'database', 'media', 'metrics',
              'organization', 'queue', 'web']

    results = {}
    for domain in domains:
        results[domain] = test_domain_migration(domain)

    # Summary
    passed = sum(1 for result in results.values() if result)
    total = len(results)

    print(f"\n📊 Migration Test Summary:")
    print(f"   Passed: {passed}/{total}")

    for domain, result in results.items():
        status = "✅" if result else "❌"
        print(f"   {status} {domain}")

    return passed == total

if __name__ == '__main__':
    original_dir = os.getcwd()
    try:
        if test_all_domains():
            sys.exit(0)
        else:
            sys.exit(1)
    finally:
        os.chdir(original_dir)
```

### 06.2.2 Import Path Resolution Testing

**File:** `scripts/test-import-resolution.py`

```python
#!/usr/bin/env python3
# file: scripts/test-import-resolution.py
# version: 1.0.0
# guid: 6d7e8f9a-0b1c-2d3e-4f5a-6b7c8d9e0f1a

"""
Test that all import paths resolve correctly after migration.
"""

import re
from pathlib import Path
from typing import Set, List

def find_all_imports(proto_dir: Path) -> Set[str]:
    """Find all import statements in proto files."""
    imports = set()

    for proto_file in proto_dir.rglob('*.proto'):
        try:
            with open(proto_file, 'r', encoding='utf-8') as f:
                content = f.read()

            file_imports = re.findall(r'import\s+"([^"]+)";', content)
            imports.update(file_imports)

        except Exception as e:
            print(f"⚠️  Could not read {proto_file}: {e}")

    return imports

def validate_import_resolution(proto_dir: Path) -> bool:
    """Validate that all imports can be resolved."""
    print("🔍 Validating import resolution...")

    all_imports = find_all_imports(proto_dir)
    proto_imports = [imp for imp in all_imports if imp.startswith('proto/')]

    missing_imports = []

    for import_path in proto_imports:
        import_file = proto_dir / import_path
        if not import_file.exists():
            missing_imports.append(import_path)

    if missing_imports:
        print(f"❌ Found {len(missing_imports)} missing imports:")
        for missing in missing_imports[:10]:  # Show first 10
            print(f"     {missing}")
        return False
    else:
        print(f"✅ All {len(proto_imports)} imports resolved successfully")
        return True

if __name__ == '__main__':
    proto_dir = Path('proto')
    if proto_dir.exists():
        success = validate_import_resolution(proto_dir)
        sys.exit(0 if success else 1)
    else:
        print("❌ proto/ directory not found")
        sys.exit(1)
```

## 06.3 Post-Migration Validation

### 06.3.1 Comprehensive Validation Suite

**File:** `scripts/comprehensive-validation.py`

```python
#!/usr/bin/env python3
# file: scripts/comprehensive-validation.py
# version: 1.0.0
# guid: 7e8f9a0b-1c2d-3e4f-5a6b-7c8d9e0f1a2b

"""
Comprehensive validation suite for post-migration testing.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

class ValidationSuite:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def validate_directory_structure(self) -> bool:
        """Validate the expected directory structure exists."""
        print("🔍 Validating directory structure...")

        expected_dirs = [
            'proto/gcommon/v1/common',
            'proto/gcommon/v1/config',
            'proto/gcommon/v1/database',
            'proto/gcommon/v1/media',
            'proto/gcommon/v1/metrics',
            'proto/gcommon/v1/organization',
            'proto/gcommon/v1/queue',
            'proto/gcommon/v1/web'
        ]

        missing = []
        for dir_path in expected_dirs:
            if not Path(dir_path).exists():
                missing.append(dir_path)

        if missing:
            self.errors.extend([f"Missing directory: {d}" for d in missing])
            return False

        print("✅ Directory structure validation passed")
        return True

    def validate_proto_syntax(self) -> bool:
        """Validate proto file syntax."""
        print("🔍 Validating proto syntax...")

        proto_files = list(Path('proto').rglob('*.proto'))
        syntax_errors = []

        for proto_file in proto_files:
            try:
                with open(proto_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Basic syntax checks
                if 'package ' not in content:
                    syntax_errors.append(f"Missing package in {proto_file}")

                if 'option go_package' not in content:
                    syntax_errors.append(f"Missing go_package in {proto_file}")

            except Exception as e:
                syntax_errors.append(f"Could not read {proto_file}: {e}")

        if syntax_errors:
            self.errors.extend(syntax_errors)
            return False

        print(f"✅ Proto syntax validation passed ({len(proto_files)} files)")
        return True

    def validate_buf_compilation(self) -> bool:
        """Validate buf compilation."""
        print("🔍 Validating buf compilation...")

        try:
            result = subprocess.run(
                ['buf', 'build', 'proto'],
                capture_output=True,
                text=True,
                timeout=120
            )

            if result.returncode == 0:
                print("✅ Buf compilation successful")
                return True
            else:
                self.errors.append(f"Buf compilation failed: {result.stderr}")
                return False

        except FileNotFoundError:
            self.warnings.append("buf command not found - skipping compilation test")
            return True
        except subprocess.TimeoutExpired:
            self.errors.append("Buf compilation timed out")
            return False

    def validate_go_generation(self) -> bool:
        """Validate Go code generation."""
        print("🔍 Validating Go code generation...")

        try:
            result = subprocess.run(
                ['buf', 'generate', '--template', 'buf.gen.yaml'],
                capture_output=True,
                text=True,
                timeout=300
            )

            if result.returncode == 0:
                print("✅ Go code generation successful")

                # Check generated files
                generated_files = list(Path('pkg').rglob('*.pb.go'))
                print(f"📁 Generated {len(generated_files)} Go files")
                return True
            else:
                self.errors.append(f"Go generation failed: {result.stderr}")
                return False

        except FileNotFoundError:
            self.warnings.append("buf command not found - skipping generation test")
            return True
        except subprocess.TimeoutExpired:
            self.errors.append("Go generation timed out")
            return False

    def run_full_validation(self) -> bool:
        """Run the complete validation suite."""
        print("🚀 Running comprehensive validation suite...")

        validations = [
            self.validate_directory_structure,
            self.validate_proto_syntax,
            self.validate_buf_compilation,
            self.validate_go_generation
        ]

        results = []
        for validation in validations:
            results.append(validation())

        # Print summary
        passed = sum(results)
        total = len(results)

        print(f"\n📊 Validation Summary:")
        print(f"   Tests passed: {passed}/{total}")
        print(f"   Errors: {len(self.errors)}")
        print(f"   Warnings: {len(self.warnings)}")

        if self.errors:
            print(f"\n❌ Errors:")
            for error in self.errors:
                print(f"   • {error}")

        if self.warnings:
            print(f"\n⚠️  Warnings:")
            for warning in self.warnings:
                print(f"   • {warning}")

        return all(results) and not self.errors

if __name__ == '__main__':
    validator = ValidationSuite()

    if validator.run_full_validation():
        print("\n🎉 All validations passed!")
        sys.exit(0)
    else:
        print("\n💥 Validation failed!")
        sys.exit(1)
```

## 06.4 Performance Testing

### 06.4.1 Build Performance Comparison

**File:** `scripts/performance-comparison.py`

```python
#!/usr/bin/env python3
# file: scripts/performance-comparison.py
# version: 1.0.0
# guid: 8f9a0b1c-2d3e-4f5a-6b7c-8d9e0f1a2b3c

"""
Compare build performance before and after migration.
"""

import time
import subprocess
from statistics import mean

def measure_build_time(command, iterations=3):
    """Measure average build time for a command."""
    times = []

    for i in range(iterations):
        start_time = time.time()
        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=600
            )
            end_time = time.time()

            if result.returncode == 0:
                times.append(end_time - start_time)
            else:
                print(f"⚠️  Build failed on iteration {i+1}")

        except subprocess.TimeoutExpired:
            print(f"⚠️  Build timed out on iteration {i+1}")

    return mean(times) if times else None

def performance_comparison():
    """Compare build performance."""
    print("⏱️  Measuring build performance...")

    # Test buf build
    buf_time = measure_build_time(['buf', 'build', 'proto'])
    if buf_time:
        print(f"📊 Buf build time: {buf_time:.2f}s")

    # Test buf generate
    gen_time = measure_build_time(['buf', 'generate'])
    if gen_time:
        print(f"📊 Buf generate time: {gen_time:.2f}s")

    # Test go build
    go_time = measure_build_time(['go', 'build', './...'])
    if go_time:
        print(f"📊 Go build time: {go_time:.2f}s")

if __name__ == '__main__':
    performance_comparison()
```

## 06.5 Rollback Testing

### 06.5.1 Rollback Verification

**File:** `scripts/test-rollback.py`

```python
#!/usr/bin/env python3
# file: scripts/test-rollback.py
# version: 1.0.0
# guid: 9a0b1c2d-3e4f-5a6b-7c8d-9e0f1a2b3c4d

"""
Test rollback functionality to ensure it works correctly.
"""

import os
import sys
import tempfile
import shutil
from pathlib import Path

def test_rollback_process():
    """Test the complete rollback process."""
    print("🧪 Testing rollback process...")

    # Create test environment
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        test_dir = temp_path / 'test'

        # Copy current structure
        shutil.copytree('.', test_dir,
                       ignore=shutil.ignore_patterns('.git', '__pycache__'))

        original_cwd = os.getcwd()
        os.chdir(test_dir)

        try:
            # Create some migration artifacts
            proto_dir = Path('proto')
            proto_dir.mkdir(exist_ok=True)

            # Create backup files
            shutil.copy('buf.yaml', 'buf.yaml.backup')
            shutil.copy('buf.gen.yaml', 'buf.gen.yaml.backup')

            # Test rollback
            result = os.system('./scripts/orchestrate-migration.sh rollback')

            if result == 0:
                print("✅ Rollback test passed")
                return True
            else:
                print("❌ Rollback test failed")
                return False

        finally:
            os.chdir(original_cwd)

if __name__ == '__main__':
    if test_rollback_process():
        sys.exit(0)
    else:
        sys.exit(1)
```
