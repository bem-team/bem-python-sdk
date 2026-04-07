# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import InferSchemaCreateResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInferSchema:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        infer_schema = client.infer_schema.create(
            file={},
        )
        assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.infer_schema.with_raw_response.create(
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infer_schema = response.parse()
        assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.infer_schema.with_streaming_response.create(
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infer_schema = response.parse()
            assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInferSchema:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        infer_schema = await async_client.infer_schema.create(
            file={},
        )
        assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.infer_schema.with_raw_response.create(
            file={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        infer_schema = await response.parse()
        assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.infer_schema.with_streaming_response.create(
            file={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            infer_schema = await response.parse()
            assert_matches_type(InferSchemaCreateResponse, infer_schema, path=["response"])

        assert cast(Any, response.is_closed) is True
