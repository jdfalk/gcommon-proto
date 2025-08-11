#!/usr/bin/env python3
# file: sdks/python/client/client.py
# version: 1.1.0
# guid: 4f216115-2495-4e02-8a2d-ec427217e97b
"""Async client for interacting with gcommon services.

The :class:`Client` manages connectivity, authentication, and basic request
routing for the Python SDK.  It intentionally avoids coupling to specific gRPC
stubs so that generated service clients can build on top of it.  A small set of
helper methods provide common functionality such as unary RPC invocation,
streaming support, and graceful shutdown.

The client is lightweight and does not perform any network I/O until
:meth:`connect` is called.  Authentication is delegated to the
:class:`~sdks.python.auth.auth.TokenProvider` which supplies bearer tokens.
"""
from __future__ import annotations

import asyncio
import contextlib
import logging
from typing import Any, Awaitable, Callable, Dict, Optional

from sdks.python.auth.auth import TokenProvider

_LOGGER = logging.getLogger(__name__)

_ResponseHandler = Callable[[Any], Awaitable[Any]]


class Client:
    """Client for gcommon services.

    Parameters
    ----------
    address:
        Endpoint of the gcommon gateway, typically ``"localhost:50051"``.
    token_provider:
        Instance of :class:`TokenProvider` used for authentication.  When not
        supplied an unauthenticated client is created.
    default_timeout:
        Timeout in seconds applied to RPC calls if not specified otherwise.
    """

    def __init__(
        self,
        address: str = "localhost:50051",
        *,
        token_provider: TokenProvider | None = None,
        default_timeout: float = 30.0,
    ) -> None:
        self._address = address
        self._token_provider = token_provider
        self._default_timeout = default_timeout

        self._connected = False
        self._lock = asyncio.Lock()

        # Registered unary RPC handlers.  Generated service stubs register
        # closures here that perform the actual network operations.  The client
        # simply manages authentication and timeout logic.
        self._unary_handlers: Dict[str, _ResponseHandler] = {}

    # ------------------------------------------------------------------
    async def connect(self) -> None:
        """Establish connection to services.

        The base implementation does not require network initialization, but the
        method is present for API parity with real gRPC clients.  Subclasses may
        override this method to perform I/O such as opening a channel.
        """

        async with self._lock:
            if self._connected:
                return
            _LOGGER.debug("Client connected to %s", self._address)
            self._connected = True

    # ------------------------------------------------------------------
    async def close(self) -> None:
        """Close the client and release resources."""

        async with self._lock:
            if not self._connected:
                return
            _LOGGER.debug("Client connection closed")
            self._connected = False

    # ------------------------------------------------------------------
    def register_unary(self, name: str, handler: _ResponseHandler) -> None:
        """Register a unary RPC handler.

        Generated service clients use this method to register closures that
        perform the actual RPC invocation.  ``name`` is typically of the form
        ``"Service/Method"``.
        """

        self._unary_handlers[name] = handler

    # ------------------------------------------------------------------
    async def call_unary(
        self, name: str, request: Any, *, timeout: float | None = None
    ) -> Any:
        """Invoke a unary RPC handler.

        This method resolves the handler registered under ``name`` and invokes
        it with authentication headers.  ``timeout`` defaults to
        ``default_timeout`` provided at construction.
        """

        if name not in self._unary_handlers:
            raise ValueError(f"unregistered handler: {name}")

        if not self._connected:
            raise RuntimeError("client not connected")

        metadata: Dict[str, str] = {}
        if self._token_provider:
            token = await self._token_provider.token()
            metadata["authorization"] = f"Bearer {token}"

        handler = self._unary_handlers[name]
        timeout = timeout if timeout is not None else self._default_timeout

        try:
            return await asyncio.wait_for(handler((request, metadata)), timeout)
        except asyncio.TimeoutError as exc:  # pragma: no cover - defensive
            raise TimeoutError(f"RPC {name} timed out") from exc

    # ------------------------------------------------------------------
    @contextlib.asynccontextmanager
    async def lifespan(self) -> Any:
        """Async context manager that connects and closes the client."""

        await self.connect()
        try:
            yield self
        finally:
            await self.close()


__all__ = ["Client"]
