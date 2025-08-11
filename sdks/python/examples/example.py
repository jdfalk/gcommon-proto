#!/usr/bin/env python3
# file: sdks/python/examples/example.py
# version: 1.1.0
# guid: 123ebb6a-9965-4e86-b3e2-d660c184b64f
"""Example usage for gcommon Python SDK."""
from __future__ import annotations

import asyncio

from sdks.python.client.client import Client
from sdks.python.models.model import ExampleModel
from sdks.python.services.service import ExampleService


async def basic_example() -> None:
    """Run a basic example."""
    async with Client().lifespan() as client:
        service = ExampleService(client)
        model = ExampleModel(identifier="1", name="demo")
        response = await service.call(model)
        print(response)


if __name__ == "__main__":
    asyncio.run(basic_example())
