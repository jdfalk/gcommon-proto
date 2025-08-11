#!/usr/bin/env python3
# file: sdks/python/services/service.py
# version: 1.1.0
# guid: c9782c55-99c7-489f-b188-8eec742f46df
"""Service wrappers for the Python SDK."""
from __future__ import annotations

from typing import Any, Dict

from sdks.python.client.client import Client
from sdks.python.models.model import ExampleModel


class ExampleService:
    """High level wrapper around ``Example`` service methods."""

    def __init__(self, client: Client) -> None:
        self._client = client
        self._client.register_unary("Example/Call", self._call_rpc)

    # ------------------------------------------------------------------
    async def _call_rpc(self, payload: Any) -> Any:
        """Internal unary handler used for registration.

        The handler receives ``(request, metadata)`` so that the generic client
        can pass authentication headers.  The actual RPC invocation is simulated
        here because no backend service is available.  A real implementation
        would use a generated gRPC stub.
        """

        request, metadata = payload
        _ = metadata  # In this mock we simply ignore metadata
        model = ExampleModel.from_dict(request)
        model.validate()
        # Simulate server processing by echoing the model with a status field
        response: Dict[str, Any] = model.to_dict()
        response["status"] = "ok"
        return response

    # ------------------------------------------------------------------
    async def call(self, model: ExampleModel) -> Dict[str, Any]:
        """Invoke the ``Call`` RPC and return the response.

        The method validates the provided model, forwards it to the underlying
        client, and returns the server response.
        """

        model.validate()
        return await self._client.call_unary("Example/Call", model.to_dict())


__all__ = ["ExampleService"]
