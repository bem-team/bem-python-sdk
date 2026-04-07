# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import (
    CallGetResponse,
    WorkflowCopyResponse,
    WorkflowListResponse,
    WorkflowCreateResponse,
    WorkflowUpdateResponse,
    WorkflowRetrieveResponse,
)
from tests.utils import assert_matches_type
from bem.pagination import SyncWorkflowsPage, AsyncWorkflowsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkflows:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        workflow = client.workflows.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        )
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Bem) -> None:
        workflow = client.workflows.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[
                {
                    "function": {
                        "id": "id",
                        "name": "name",
                        "version_num": 0,
                    },
                    "name": "name",
                }
            ],
            display_name="displayName",
            edges=[
                {
                    "destination_node_name": "destinationNodeName",
                    "source_node_name": "sourceNodeName",
                    "destination_name": "destinationName",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        workflow = client.workflows.retrieve(
            "workflowName",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.retrieve(
            "workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.retrieve(
            "workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Bem) -> None:
        workflow = client.workflows.update(
            workflow_name="workflowName",
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Bem) -> None:
        workflow = client.workflows.update(
            workflow_name="workflowName",
            display_name="displayName",
            edges=[
                {
                    "destination_node_name": "destinationNodeName",
                    "source_node_name": "sourceNodeName",
                    "destination_name": "destinationName",
                }
            ],
            main_node_name="mainNodeName",
            name="name",
            nodes=[
                {
                    "function": {
                        "id": "id",
                        "name": "name",
                        "version_num": 0,
                    },
                    "name": "name",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.update(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.update(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.update(
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        workflow = client.workflows.list()
        assert_matches_type(SyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        workflow = client.workflows.list(
            display_name="displayName",
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            tags=["string"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(SyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(SyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(SyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Bem) -> None:
        workflow = client.workflows.delete(
            "workflowName",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.delete(
            "workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.delete(
            "workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_call(self, client: Bem) -> None:
        workflow = client.workflows.call(
            workflow_name="workflowName",
        )
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_call_with_all_params(self, client: Bem) -> None:
        workflow = client.workflows.call(
            workflow_name="workflowName",
            call_reference_id="callReferenceID",
            file={},
            files=[{}],
            wait="wait",
        )
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_call(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.call(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_call(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.call(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(CallGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_call(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            client.workflows.with_raw_response.call(
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_copy(self, client: Bem) -> None:
        workflow = client.workflows.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        )
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_copy_with_all_params(self, client: Bem) -> None:
        workflow = client.workflows.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
            source_workflow_version_num=1,
            tags=["string"],
            target_display_name="targetDisplayName",
            target_environment="targetEnvironment",
        )
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_copy(self, client: Bem) -> None:
        response = client.workflows.with_raw_response.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = response.parse()
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_copy(self, client: Bem) -> None:
        with client.workflows.with_streaming_response.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = response.parse()
            assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkflows:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        )
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[
                {
                    "function": {
                        "id": "id",
                        "name": "name",
                        "version_num": 0,
                    },
                    "name": "name",
                }
            ],
            display_name="displayName",
            edges=[
                {
                    "destination_node_name": "destinationNodeName",
                    "source_node_name": "sourceNodeName",
                    "destination_name": "destinationName",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.create(
            main_node_name="mainNodeName",
            name="name",
            nodes=[{"function": {}}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowCreateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.retrieve(
            "workflowName",
        )
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.retrieve(
            "workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.retrieve(
            "workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowRetrieveResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.update(
            workflow_name="workflowName",
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.update(
            workflow_name="workflowName",
            display_name="displayName",
            edges=[
                {
                    "destination_node_name": "destinationNodeName",
                    "source_node_name": "sourceNodeName",
                    "destination_name": "destinationName",
                }
            ],
            main_node_name="mainNodeName",
            name="name",
            nodes=[
                {
                    "function": {
                        "id": "id",
                        "name": "name",
                        "version_num": 0,
                    },
                    "name": "name",
                }
            ],
            tags=["string"],
        )
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.update(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.update(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowUpdateResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.update(
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.list()
        assert_matches_type(AsyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.list(
            display_name="displayName",
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            tags=["string"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(AsyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(AsyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(AsyncWorkflowsPage[WorkflowListResponse], workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.delete(
            "workflowName",
        )
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.delete(
            "workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert workflow is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.delete(
            "workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert workflow is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_call(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.call(
            workflow_name="workflowName",
        )
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_call_with_all_params(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.call(
            workflow_name="workflowName",
            call_reference_id="callReferenceID",
            file={},
            files=[{}],
            wait="wait",
        )
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_call(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.call(
            workflow_name="workflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(CallGetResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_call(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.call(
            workflow_name="workflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(CallGetResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_call(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `workflow_name` but received ''"):
            await async_client.workflows.with_raw_response.call(
                workflow_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_copy(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        )
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncBem) -> None:
        workflow = await async_client.workflows.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
            source_workflow_version_num=1,
            tags=["string"],
            target_display_name="targetDisplayName",
            target_environment="targetEnvironment",
        )
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncBem) -> None:
        response = await async_client.workflows.with_raw_response.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workflow = await response.parse()
        assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncBem) -> None:
        async with async_client.workflows.with_streaming_response.copy(
            source_workflow_name="sourceWorkflowName",
            target_workflow_name="targetWorkflowName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workflow = await response.parse()
            assert_matches_type(WorkflowCopyResponse, workflow, path=["response"])

        assert cast(Any, response.is_closed) is True
