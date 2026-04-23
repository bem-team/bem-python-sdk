# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import WebhookSecretCreateResponse, WebhookSecretRetrieveResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhookSecret:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        webhook_secret = client.webhook_secret.create()
        assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.webhook_secret.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = response.parse()
        assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.webhook_secret.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = response.parse()
            assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        webhook_secret = client.webhook_secret.retrieve()
        assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.webhook_secret.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = response.parse()
        assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.webhook_secret.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = response.parse()
            assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_revoke(self, client: Bem) -> None:
        webhook_secret = client.webhook_secret.revoke()
        assert webhook_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_revoke(self, client: Bem) -> None:
        response = client.webhook_secret.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = response.parse()
        assert webhook_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_revoke(self, client: Bem) -> None:
        with client.webhook_secret.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = response.parse()
            assert webhook_secret is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWebhookSecret:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        webhook_secret = await async_client.webhook_secret.create()
        assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.webhook_secret.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = await response.parse()
        assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.webhook_secret.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = await response.parse()
            assert_matches_type(WebhookSecretCreateResponse, webhook_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        webhook_secret = await async_client.webhook_secret.retrieve()
        assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.webhook_secret.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = await response.parse()
        assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.webhook_secret.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = await response.parse()
            assert_matches_type(WebhookSecretRetrieveResponse, webhook_secret, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_revoke(self, async_client: AsyncBem) -> None:
        webhook_secret = await async_client.webhook_secret.revoke()
        assert webhook_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_revoke(self, async_client: AsyncBem) -> None:
        response = await async_client.webhook_secret.with_raw_response.revoke()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook_secret = await response.parse()
        assert webhook_secret is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_revoke(self, async_client: AsyncBem) -> None:
        async with async_client.webhook_secret.with_streaming_response.revoke() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook_secret = await response.parse()
            assert webhook_secret is None

        assert cast(Any, response.is_closed) is True
