#!/usr/bin/env python3
# file: sdks/python/tests/test_client.py
# version: 1.1.0
# guid: 8b4e833a-be6d-461a-8587-dd427a680f37
"""Tests for Python client."""
from __future__ import annotations

import pytest

from sdks.python.client.client import Client
from sdks.python.models.model import ExampleModel
from sdks.python.services.service import ExampleService


@pytest.mark.asyncio
async def test_client_call_unary_returns_response() -> None:
    """Client.call_unary returns response from registered handler."""

    async with Client().lifespan() as client:
        service = ExampleService(client)
        model = ExampleModel(identifier="1", name="demo")
        resp = await service.call(model)
        assert resp["status"] == "ok"


@pytest.mark.asyncio
async def test_client_requires_connection() -> None:
    """Calling without connection raises error."""

    client = Client()
    with pytest.raises(RuntimeError):
        await client.call_unary("Example/Call", {})
