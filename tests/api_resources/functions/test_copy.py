# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import FunctionResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCopy:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        copy = client.functions.copy.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        )
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Bem) -> None:
        copy = client.functions.copy.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
            tags=["string"],
            target_display_name="targetDisplayName",
            target_environment="targetEnvironment",
        )
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.functions.copy.with_raw_response.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = response.parse()
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.functions.copy.with_streaming_response.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = response.parse()
            assert_matches_type(FunctionResponse, copy, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCopy:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        copy = await async_client.functions.copy.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        )
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBem) -> None:
        copy = await async_client.functions.copy.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
            tags=["string"],
            target_display_name="targetDisplayName",
            target_environment="targetEnvironment",
        )
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.copy.with_raw_response.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        copy = await response.parse()
        assert_matches_type(FunctionResponse, copy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.functions.copy.with_streaming_response.create(
            source_function_name="sourceFunctionName",
            target_function_name="targetFunctionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            copy = await response.parse()
            assert_matches_type(FunctionResponse, copy, path=["response"])

        assert cast(Any, response.is_closed) is True
