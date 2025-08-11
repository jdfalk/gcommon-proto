#!/usr/bin/env python3
# file: sdks/python/examples/example.py
# version: 1.0.0
# guid: 123ebb6a-9965-4e86-b3e2-d660c184b64f
"""Example usage for gcommon Python SDK."""
from __future__ import annotations

import asyncio

from sdks.python.client.client import Client


async def basic_example() -> None:
    """Run a basic example."""
    client = Client()
    await client.connect()
    try:
        # TODO: call service methods
        print("TODO: call service method")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(basic_example())
