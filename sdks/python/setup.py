#!/usr/bin/env python3
# file: sdks/python/setup.py
# version: 1.0.0
# guid: 12345678-1234-5678-9abc-123456789012

"""
Setup configuration for gcommon Python SDK
Generated protobuf packages for Python applications
"""

from setuptools import setup, find_packages

setup(
    name="gcommon",
    version="0.1.0",
    description="Common protobuf packages for Go applications - Python SDK",
    author="JD Falk",
    author_email="jd@jdfalk.com",
    url="https://github.com/jdfalk/gcommon",
    packages=find_packages(),
    install_requires=[
        "protobuf>=3.20.0",
        "grpcio>=1.50.0",
        "grpcio-tools>=1.50.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    package_data={
        "gcommon": ["**/*.py", "**/*.pyi"],
    },
    include_package_data=True,
)
