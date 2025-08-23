# file: sdks/python/setup.py
# version: 1.0.0
# guid: def01234-5678-9abc-def0-123456789abc

"""
Setup configuration for gcommon Python SDK.

This package provides Python bindings for gcommon protobuf definitions,
enabling easy integration with gcommon services and data structures.
"""

from setuptools import setup, find_packages

# Read long description from README if available
long_description = """
# gcommon Python SDK

Python SDK for gcommon protocol buffer definitions.

## Installation

```bash
pip install gcommon
```

## Usage

```python
from gcommon.v1.common import timestamp_pb2
from gcommon.v1.queue import message_pb2
```
"""

setup(
    name="gcommon",
    version="1.0.0",
    author="gcommon team",
    author_email="dev@gcommon.com",
    description="Python SDK for gcommon protocol buffer definitions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jdfalk/gcommon",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.8",
    install_requires=[
        "protobuf>=3.20.0",
        "grpcio>=1.50.0",
        "grpcio-tools>=1.50.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=22.0",
            "isort>=5.0",
            "mypy>=0.910",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
