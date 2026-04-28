# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.types.eval import (
    ResultFetchResultsResponse,
    ResultRetrieveResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch_results(self, client: Bem) -> None:
        result = client.eval.results.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_fetch_results_with_all_params(self, client: Bem) -> None:
        result = client.eval.results.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
            evaluation_version="0.1.0-gemini",
        )
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_fetch_results(self, client: Bem) -> None:
        response = client.eval.results.with_raw_response.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_fetch_results(self, client: Bem) -> None:
        with client.eval.results.with_streaming_response.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_results(self, client: Bem) -> None:
        result = client.eval.results.retrieve_results(
            transformation_ids="transformationIDs",
        )
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_results_with_all_params(self, client: Bem) -> None:
        result = client.eval.results.retrieve_results(
            transformation_ids="transformationIDs",
            evaluation_version="evaluationVersion",
        )
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_results(self, client: Bem) -> None:
        response = client.eval.results.with_raw_response.retrieve_results(
            transformation_ids="transformationIDs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = response.parse()
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_results(self, client: Bem) -> None:
        with client.eval.results.with_streaming_response.retrieve_results(
            transformation_ids="transformationIDs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = response.parse()
            assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResults:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch_results(self, async_client: AsyncBem) -> None:
        result = await async_client.eval.results.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_fetch_results_with_all_params(self, async_client: AsyncBem) -> None:
        result = await async_client.eval.results.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
            evaluation_version="0.1.0-gemini",
        )
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_fetch_results(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.results.with_raw_response.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_fetch_results(self, async_client: AsyncBem) -> None:
        async with async_client.eval.results.with_streaming_response.fetch_results(
            transformation_ids=["tr_01HXAB...", "tr_01HXCD..."],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultFetchResultsResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_results(self, async_client: AsyncBem) -> None:
        result = await async_client.eval.results.retrieve_results(
            transformation_ids="transformationIDs",
        )
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_results_with_all_params(self, async_client: AsyncBem) -> None:
        result = await async_client.eval.results.retrieve_results(
            transformation_ids="transformationIDs",
            evaluation_version="evaluationVersion",
        )
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_results(self, async_client: AsyncBem) -> None:
        response = await async_client.eval.results.with_raw_response.retrieve_results(
            transformation_ids="transformationIDs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        result = await response.parse()
        assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_results(self, async_client: AsyncBem) -> None:
        async with async_client.eval.results.with_streaming_response.retrieve_results(
            transformation_ids="transformationIDs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            result = await response.parse()
            assert_matches_type(ResultRetrieveResultsResponse, result, path=["response"])

        assert cast(Any, response.is_closed) is True
