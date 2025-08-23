#!/usr/bin/env python3
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
