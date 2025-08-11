#!/usr/bin/env python3
# file: sdks/python/tests/test_auth.py
# version: 1.0.0
# guid: 939f0202-56e1-4cb8-a948-b2468d0cd347
"""Tests for TokenProvider."""
from __future__ import annotations

import asyncio
import datetime as _dt

import pytest

from sdks.python.auth.auth import TokenProvider


@pytest.mark.asyncio
async def test_token_provider_api_key() -> None:
    """Static API key is returned without refresh."""

    provider = TokenProvider(api_key="abc")
    assert await provider.token() == "abc"


@pytest.mark.asyncio
async def test_token_provider_custom_fetcher() -> None:
    """Custom coroutine is used for refresh."""

    calls: list[_dt.datetime] = []

    async def fetcher() -> str:
        calls.append(_dt.datetime.utcnow())
        return "fetched"

    provider = TokenProvider(token_fetcher=fetcher)
    assert await provider.token() == "fetched"
    assert len(calls) == 1

    # Token should be cached; second call does not trigger fetcher
    assert await provider.token() == "fetched"
    assert len(calls) == 1


@pytest.mark.asyncio
async def test_token_provider_oauth2_refresh() -> None:
    """OAuth2 configuration refreshes token."""

    provider = TokenProvider(
        token_endpoint="https://example.com/token",
        client_id="id",
        client_secret="secret",
    )
    token = await provider.token()
    assert token.startswith("oauth2-id")
