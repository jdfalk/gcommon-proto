#!/usr/bin/env python3
# file: scripts/setup-python-sdk.py
# version: 1.1.0
# guid: a1b2c3d4-e5f6-789a-bcde-f012345678ab

"""
Post-generation script to ensure Python SDK __init__.py files exist.

This script:
1. Ensures all Python SDK directories have proper __init__.py files
2. Creates package structure for generated protobuf Python code
3. Maintains version information in package files
4. Creates setup.py file if missing (e.g., after make clean)
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
            if package_dir.is_dir() and not package_dir.name.startswith("."):
                package_init_content = f'''"""
gcommon.v1.{package_dir.name} package

Generated protobuf definitions for {package_dir.name}.
"""
'''
                ensure_init_py_exists(package_dir, package_init_content)

    # Ensure setup.py exists
    setup_py = python_sdk_dir / "setup.py"
    if setup_py.exists():
        print(f"✅ setup.py found: {setup_py}")
    else:
        print(f"⚠️  setup.py not found: {setup_py}")
        print("   Creating setup.py for Python package installation")
        
        # Create setup.py content
        setup_py_content = '''#!/usr/bin/env python3
# file: sdks/python/setup.py
# version: 1.1.0
# guid: 9a8b7c6d-5e4f-3a2b-1c9d-8e7f6a5b4c3d

"""
Setup configuration for gcommon Python SDK.

This package provides Python bindings for gcommon protobuf definitions.
Install with: pip install -e .
"""

from setuptools import setup, find_packages

setup(
    name="gcommon",
    version="1.0.0",
    description="Python SDK for gcommon protobuf definitions",
    long_description="""
    gcommon Python SDK provides Python bindings for protocol buffer definitions
    used across gcommon services. This package includes generated protobuf classes
    for common data structures, metrics, queues, configurations, and more.
    """,
    long_description_content_type="text/plain",
    author="gcommon team",
    author_email="dev@gcommon.com",
    url="https://github.com/jdfalk/gcommon",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "protobuf>=3.20.0",
        "grpcio>=1.50.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Distributed Computing",
    ],
    keywords="protobuf grpc gcommon sdk api",
    project_urls={
        "Bug Reports": "https://github.com/jdfalk/gcommon/issues",
        "Source": "https://github.com/jdfalk/gcommon",
        "Documentation": "https://github.com/jdfalk/gcommon/blob/main/sdks/README.md",
    },
)
'''
        
        with open(setup_py, "w") as f:
            f.write(setup_py_content)
        print(f"✅ Created setup.py: {setup_py}")

    print("✅ Python SDK setup complete!")
    print("   - Package structure created with __init__.py files")
    print("   - Ready for 'pip install -e .' from sdks/python/")

    return 0


if __name__ == "__main__":
    sys.exit(main())
