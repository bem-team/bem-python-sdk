# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import ReviewQueueListResponse
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReviewQueue:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        review_queue = client.review_queue.list()
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        review_queue = client.review_queue.list(
            assigned_to="assignedTo",
            bucket="bucket",
            cursor="cursor",
            limit=1,
            since="since",
            status=["string"],
            type=["string"],
        )
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.review_queue.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review_queue = response.parse()
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.review_queue.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review_queue = response.parse()
            assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncReviewQueue:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        review_queue = await async_client.review_queue.list()
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        review_queue = await async_client.review_queue.list(
            assigned_to="assignedTo",
            bucket="bucket",
            cursor="cursor",
            limit=1,
            since="since",
            status=["string"],
            type=["string"],
        )
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.review_queue.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        review_queue = await response.parse()
        assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.review_queue.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            review_queue = await response.parse()
            assert_matches_type(ReviewQueueListResponse, review_queue, path=["response"])

        assert cast(Any, response.is_closed) is True
