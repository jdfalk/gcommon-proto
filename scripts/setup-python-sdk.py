#!/usr/bin/env python3
# file: scripts/setup-python-sdk.py
# version: 1.0.0
# guid: a1b2c3d4-e5f6-789a-bcde-f012345678ab

"""
Post-generation script to ensure Python SDK __init__.py files exist.

This script:
1. Ensures all Python SDK directories have proper __init__.py files
2. Creates package structure for generated protobuf Python code
3. Maintains version information in package files
"""

import sys
from pathlib import Path


def ensure_init_py_exists(directory, content=""):
    """Ensure __init__.py file exists in directory with given content."""
    init_file = directory / "__init__.py"
    
    if init_file.exists():
        print(f"✅ __init__.py already exists: {init_file}")
        return
    
    with open(init_file, "w") as f:
        f.write(content)
    print(f"Created __init__.py: {init_file}")


def main():
    # Get script directory and project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    python_sdk_dir = project_root / "sdks" / "python"

    print("Setting up Python SDK package structure")
    print(f"Working in: {python_sdk_dir}")

    # Ensure the python sdk directory exists
    python_sdk_dir.mkdir(parents=True, exist_ok=True)

    # Create root __init__.py for python SDK
    root_init_content = '''"""
gcommon Python SDK

This package provides Python bindings for gcommon protobuf definitions.
"""

__version__ = "1.0.0"
__author__ = "gcommon team"
'''
    ensure_init_py_exists(python_sdk_dir, root_init_content)

    # Create gcommon package __init__.py
    gcommon_dir = python_sdk_dir / "gcommon"
    gcommon_dir.mkdir(exist_ok=True)
    gcommon_init_content = '''"""
gcommon package

Core gcommon protobuf definitions and types.
"""
'''
    ensure_init_py_exists(gcommon_dir, gcommon_init_content)

    # Create v1 package __init__.py
    v1_dir = gcommon_dir / "v1"
    v1_dir.mkdir(exist_ok=True)
    v1_init_content = '''"""
gcommon v1 API

Version 1 of the gcommon protobuf API definitions.
"""
'''
    ensure_init_py_exists(v1_dir, v1_init_content)

    # Create __init__.py files for all generated package directories
    if v1_dir.exists():
        for package_dir in v1_dir.iterdir():
            if package_dir.is_dir() and not package_dir.name.startswith('.'):
                package_init_content = f'''"""
gcommon.v1.{package_dir.name} package

Generated protobuf definitions for {package_dir.name}.
"""
'''
                ensure_init_py_exists(package_dir, package_init_content)

    # Check for setup.py
    setup_py = python_sdk_dir / "setup.py"
    if setup_py.exists():
        print(f"✅ setup.py found: {setup_py}")
    else:
        print(f"⚠️  setup.py not found: {setup_py}")
        print("   Python package won't be installable without setup.py")

    print("✅ Python SDK setup complete!")
    print("   - Package structure created with __init__.py files")
    print("   - Ready for 'pip install -e .' from sdks/python/")

    return 0


if __name__ == "__main__":
    sys.exit(main())
