# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from tests.utils import assert_matches_type
from bem.pagination import SyncWorkflowVersionsPage, AsyncWorkflowVersionsPage
from bem.types.workflows import VersionListResponse, VersionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        version = client.workflows.versions.retrieve(
            version_num=0,
            workflow_name="workflowName",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.workflows.versions.with_raw_response.retrieve(
            version_num=0,
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.workflows.versions.with_streaming_response.retrieve(
            version_num=0,
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.versions.with_raw_response.retrieve(
                version_num=0,
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        version = client.workflows.versions.list(
            workflow_name="workflowName",
        )
        assert_matches_type(SyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        version = client.workflows.versions.list(
            workflow_name="workflowName",
            ending_before=0,
            limit=1,
            sort_order="asc",
            starting_after=0,
        )
        assert_matches_type(SyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.workflows.versions.with_raw_response.list(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.workflows.versions.with_streaming_response.list(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.versions.with_raw_response.list(
                workflow_name="",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        version = await async_client.workflows.versions.retrieve(
            version_num=0,
            workflow_name="workflowName",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.versions.with_raw_response.retrieve(
            version_num=0,
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.versions.with_streaming_response.retrieve(
            version_num=0,
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.versions.with_raw_response.retrieve(
                version_num=0,
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        version = await async_client.workflows.versions.list(
            workflow_name="workflowName",
        )
        assert_matches_type(AsyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        version = await async_client.workflows.versions.list(
            workflow_name="workflowName",
            ending_before=0,
            limit=1,
            sort_order="asc",
            starting_after=0,
        )
        assert_matches_type(AsyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.versions.with_raw_response.list(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.versions.with_streaming_response.list(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncWorkflowVersionsPage[VersionListResponse], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.versions.with_raw_response.list(
                workflow_name="",
            )
