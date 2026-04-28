# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import OutputListResponse, OutputRetrieveResponse
from tests.utils import assert_matches_type
from bem.pagination import SyncOutputsPage, AsyncOutputsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOutputs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        output = client.outputs.retrieve(
            "eventID",
        )
        assert_matches_type(OutputRetrieveResponse, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.outputs.with_raw_response.retrieve(
            "eventID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(OutputRetrieveResponse, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.outputs.with_streaming_response.retrieve(
            "eventID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(OutputRetrieveResponse, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.outputs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        output = client.outputs.list()
        assert_matches_type(SyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        output = client.outputs.list(
            call_ids=["string"],
            ending_before="endingBefore",
            event_ids=["string"],
            function_ids=["string"],
            function_names=["string"],
            function_version_nums=[0],
            include_intermediate=True,
            is_labelled=True,
            is_regression=True,
            limit=1,
            reference_ids=["string"],
            reference_id_substring="referenceIDSubstring",
            sort_order="asc",
            starting_after="startingAfter",
            transformation_ids=["string"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(SyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.outputs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = response.parse()
        assert_matches_type(SyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.outputs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = response.parse()
            assert_matches_type(SyncOutputsPage[OutputListResponse], output, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOutputs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        output = await async_client.outputs.retrieve(
            "eventID",
        )
        assert_matches_type(OutputRetrieveResponse, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.outputs.with_raw_response.retrieve(
            "eventID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(OutputRetrieveResponse, output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.outputs.with_streaming_response.retrieve(
            "eventID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(OutputRetrieveResponse, output, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.outputs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        output = await async_client.outputs.list()
        assert_matches_type(AsyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        output = await async_client.outputs.list(
            call_ids=["string"],
            ending_before="endingBefore",
            event_ids=["string"],
            function_ids=["string"],
            function_names=["string"],
            function_version_nums=[0],
            include_intermediate=True,
            is_labelled=True,
            is_regression=True,
            limit=1,
            reference_ids=["string"],
            reference_id_substring="referenceIDSubstring",
            sort_order="asc",
            starting_after="startingAfter",
            transformation_ids=["string"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(AsyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.outputs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        output = await response.parse()
        assert_matches_type(AsyncOutputsPage[OutputListResponse], output, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.outputs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            output = await response.parse()
            assert_matches_type(AsyncOutputsPage[OutputListResponse], output, path=["response"])

        assert cast(Any, response.is_closed) is True
