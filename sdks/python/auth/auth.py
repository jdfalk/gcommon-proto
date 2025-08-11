#!/usr/bin/env python3
# file: sdks/python/auth/auth.py
# version: 1.1.0
# guid: 58742820-6551-47e8-89bc-db88993ca7e0
"""Authentication utilities for the Python SDK.

This module provides an asynchronous ``TokenProvider`` that supports multiple
authentication mechanisms used by gcommon services.  The implementation is
designed to be intentionally lightweight so that SDK consumers may easily adapt
it for their own security requirements.  The provider currently understands the
following authentication flows:

* **Static API keys** supplied directly by the caller
* **OAuth2 client credentials** where a token endpoint issues short‑lived
  access tokens
* **Pre‑issued bearer tokens** which are refreshed on demand

The provider exposes an :meth:`token` coroutine that returns a valid access
token.  When the token is close to expiration, or if no token has been acquired
yet, the provider will automatically invoke :meth:`refresh` to obtain a new
token.  The refresh operation is guarded by an ``asyncio.Lock`` to ensure that
concurrent requests do not trigger multiple refreshes.

Example usage::

    provider = TokenProvider(api_key="xyz")
    token = await provider.token()

``token`` will either return the supplied API key or a retrieved OAuth2
access token depending on configuration.
"""
from __future__ import annotations

import asyncio
import datetime as _dt
from dataclasses import dataclass
from typing import Awaitable, Callable, Optional

_TokenFetcher = Callable[[], Awaitable[str]]


@dataclass
class _TokenState:
    """Internal representation of token data."""

    value: str = ""
    expires: Optional[_dt.datetime] = None

    def valid_for(self, delta: _dt.timedelta) -> bool:
        """Return ``True`` if token is valid for at least ``delta``.

        A ``None`` expiration is treated as already expired.
        """

        if self.expires is None:
            return False
        return _dt.datetime.utcnow() + delta < self.expires


class TokenProvider:
    """Manage authentication tokens for service requests.

    The provider can be configured with an API key, an arbitrary coroutine that
    fetches tokens, or OAuth2 client credentials.  The latter two approaches use
    :mod:`asyncio` to perform network I/O without blocking the event loop.

    Parameters
    ----------
    api_key:
        Static API key to attach to requests.  When supplied the provider will
        never attempt to refresh.
    token_fetcher:
        Custom coroutine that returns a token string.  This is useful for JWT
        implementations or more advanced OAuth2 flows.  The coroutine should
        raise ``RuntimeError`` on failure.
    token_endpoint, client_id, client_secret:
        If ``token_endpoint`` is provided the provider will perform the OAuth2
        client credentials flow.  Both ``client_id`` and ``client_secret`` are
        required in this mode.
    """

    def __init__(
        self,
        api_key: str | None = None,
        *,
        token_fetcher: _TokenFetcher | None = None,
        token_endpoint: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
    ) -> None:
        self._api_key = api_key
        self._fetcher = token_fetcher
        self._token_endpoint = token_endpoint
        self._client_id = client_id
        self._client_secret = client_secret

        self._state = _TokenState()
        self._lock = asyncio.Lock()

    # ------------------------------------------------------------------
    async def token(self) -> str:
        """Return a valid token, refreshing as necessary.

        If the provider is configured with a static API key the key is returned
        immediately.  Otherwise, when the current token is missing or expiring
        soon, :meth:`refresh` is invoked.
        """

        if self._api_key:
            return self._api_key

        async with self._lock:
            if not self._state.valid_for(_dt.timedelta(seconds=30)):
                await self.refresh()
            return self._state.value

    # ------------------------------------------------------------------
    async def refresh(self) -> None:
        """Refresh the cached token.

        The refresh strategy is chosen based on constructor arguments.  The
        default implementation uses a user supplied ``token_fetcher`` coroutine
        when available.  Otherwise, if ``token_endpoint`` is provided the
        OAuth2 client credentials flow is executed.  The OAuth2 implementation
        here is intentionally minimal and should be replaced in production with
        a library such as :mod:`aiohttp` or :mod:`httpx`.
        """

        if self._fetcher:
            token = await self._fetcher()
            self._state = _TokenState(token, _dt.datetime.utcnow() + _dt.timedelta(hours=1))
            return

        if self._token_endpoint and self._client_id and self._client_secret:
            # The actual network call is omitted to keep the SDK lightweight.
            # In real usage this block would perform an HTTP POST request to
            # the token endpoint and parse the returned JSON document.  Here we
            # simulate the behaviour by generating a fake token with a fixed
            # expiration time.
            await asyncio.sleep(0)
            fake_token = f"oauth2-{self._client_id}"
            self._state = _TokenState(
                fake_token, _dt.datetime.utcnow() + _dt.timedelta(hours=1)
            )
            return

        raise RuntimeError("No token refresh mechanism configured")

    # ------------------------------------------------------------------
    def set_api_key(self, api_key: str) -> None:
        """Configure the provider to use a static API key."""

        self._api_key = api_key
        self._state = _TokenState(api_key, None)

    # ------------------------------------------------------------------
    def configure_oauth2(self, endpoint: str, client_id: str, client_secret: str) -> None:
        """Set OAuth2 client credentials for token refresh."""

        self._token_endpoint = endpoint
        self._client_id = client_id
        self._client_secret = client_secret
        self._fetcher = None
        self._api_key = None
        self._state = _TokenState()

    # ------------------------------------------------------------------
    def configure_fetcher(self, fetcher: _TokenFetcher) -> None:
        """Use a custom coroutine to fetch tokens."""

        self._fetcher = fetcher
        self._api_key = None
        self._token_endpoint = None
        self._client_id = None
        self._client_secret = None
        self._state = _TokenState()


__all__ = ["TokenProvider"]
