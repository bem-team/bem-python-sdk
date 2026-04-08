# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import (
    Function,
    FunctionResponse,
)
from tests.utils import assert_matches_type
from bem.pagination import SyncFunctionsPage, AsyncFunctionsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="transform",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="transform",
            display_name="displayName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tabular_chunking_enabled=True,
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="transform",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="transform",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="analyze",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="analyze",
            display_name="displayName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="analyze",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="analyze",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="route",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="route",
            description="description",
            display_name="displayName",
            routes=[
                {
                    "name": "name",
                    "description": "description",
                    "function_id": "functionID",
                    "function_name": "functionName",
                    "is_error_fallback": True,
                    "origin": {"email": {"patterns": ["string"]}},
                    "regex": {"patterns": ["string"]},
                }
            ],
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="send",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="send",
            destination_type="webhook",
            display_name="displayName",
            google_drive_folder_id="googleDriveFolderId",
            s3_bucket="s3Bucket",
            s3_prefix="s3Prefix",
            tags=["string"],
            webhook_signing_enabled=True,
            webhook_url="webhookUrl",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="send",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="send",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="split",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="split",
            display_name="displayName",
            print_page_split_config={
                "next_function_id": "nextFunctionID",
                "next_function_name": "nextFunctionName",
            },
            semantic_page_split_config={
                "item_classes": [
                    {
                        "name": "name",
                        "description": "description",
                        "next_function_id": "nextFunctionID",
                        "next_function_name": "nextFunctionName",
                    }
                ]
            },
            split_type="print_page",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="split",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="split",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_6(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="join",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="join",
            description="description",
            display_name="displayName",
            join_type="standard",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_6(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="join",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="join",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_7(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="payload_shaping",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="payload_shaping",
            display_name="displayName",
            shaping_schema="shapingSchema",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_7(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="payload_shaping",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="payload_shaping",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_overload_8(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="enrich",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: Bem) -> None:
        function = client.functions.create(
            function_name="functionName",
            type="enrich",
            config={
                "steps": [
                    {
                        "collection_name": "collectionName",
                        "source_field": "sourceField",
                        "target_field": "targetField",
                        "include_cosine_distance": True,
                        "include_subcollections": True,
                        "score_threshold": 0,
                        "search_mode": "semantic",
                        "top_k": 1,
                    }
                ]
            },
            display_name="displayName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_overload_8(self, client: Bem) -> None:
        response = client.functions.with_raw_response.create(
            function_name="functionName",
            type="enrich",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: Bem) -> None:
        with client.functions.with_streaming_response.create(
            function_name="functionName",
            type="enrich",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        function = client.functions.retrieve(
            "functionName",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.functions.with_raw_response.retrieve(
            "functionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.functions.with_streaming_response.retrieve(
            "functionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="transform",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="transform",
            display_name="displayName",
            function_name="functionName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tabular_chunking_enabled=True,
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="transform",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="transform",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="transform",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="analyze",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="analyze",
            display_name="displayName",
            function_name="functionName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="analyze",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="analyze",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="analyze",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="route",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="route",
            description="description",
            display_name="displayName",
            function_name="functionName",
            routes=[
                {
                    "name": "name",
                    "description": "description",
                    "function_id": "functionID",
                    "function_name": "functionName",
                    "is_error_fallback": True,
                    "origin": {"email": {"patterns": ["string"]}},
                    "regex": {"patterns": ["string"]},
                }
            ],
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="route",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="send",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="send",
            destination_type="webhook",
            display_name="displayName",
            function_name="functionName",
            google_drive_folder_id="googleDriveFolderId",
            s3_bucket="s3Bucket",
            s3_prefix="s3Prefix",
            tags=["string"],
            webhook_signing_enabled=True,
            webhook_url="webhookUrl",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="send",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="send",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="send",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="split",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="split",
            display_name="displayName",
            function_name="functionName",
            print_page_split_config={
                "next_function_id": "nextFunctionID",
                "next_function_name": "nextFunctionName",
            },
            semantic_page_split_config={
                "item_classes": [
                    {
                        "name": "name",
                        "description": "description",
                        "next_function_id": "nextFunctionID",
                        "next_function_name": "nextFunctionName",
                    }
                ]
            },
            split_type="print_page",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="split",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="split",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_5(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="split",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_6(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="join",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="join",
            description="description",
            display_name="displayName",
            function_name="functionName",
            join_type="standard",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_6(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="join",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="join",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_6(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="join",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_7(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="payload_shaping",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="payload_shaping",
            display_name="displayName",
            function_name="functionName",
            shaping_schema="shapingSchema",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_7(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="payload_shaping",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="payload_shaping",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_7(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="payload_shaping",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_overload_8(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="enrich",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: Bem) -> None:
        function = client.functions.update(
            path_function_name="functionName",
            type="enrich",
            config={
                "steps": [
                    {
                        "collection_name": "collectionName",
                        "source_field": "sourceField",
                        "target_field": "targetField",
                        "include_cosine_distance": True,
                        "include_subcollections": True,
                        "score_threshold": 0,
                        "search_mode": "semantic",
                        "top_k": 1,
                    }
                ]
            },
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_overload_8(self, client: Bem) -> None:
        response = client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="enrich",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: Bem) -> None:
        with client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="enrich",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_overload_8(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            client.functions.with_raw_response.update(
                path_function_name="",
                type="enrich",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        function = client.functions.list()
        assert_matches_type(SyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        function = client.functions.list(
            display_name="displayName",
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            tags=["string"],
            types=["transform"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(SyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert_matches_type(SyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert_matches_type(SyncFunctionsPage[Function], function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Bem) -> None:
        function = client.functions.delete(
            "functionName",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Bem) -> None:
        response = client.functions.with_raw_response.delete(
            "functionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Bem) -> None:
        with client.functions.with_streaming_response.delete(
            "functionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            client.functions.with_raw_response.delete(
                "",
            )


class TestAsyncFunctions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="transform",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="transform",
            display_name="displayName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tabular_chunking_enabled=True,
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="transform",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="transform",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="analyze",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="analyze",
            display_name="displayName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="analyze",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="analyze",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="route",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="route",
            description="description",
            display_name="displayName",
            routes=[
                {
                    "name": "name",
                    "description": "description",
                    "function_id": "functionID",
                    "function_name": "functionName",
                    "is_error_fallback": True,
                    "origin": {"email": {"patterns": ["string"]}},
                    "regex": {"patterns": ["string"]},
                }
            ],
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="send",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="send",
            destination_type="webhook",
            display_name="displayName",
            google_drive_folder_id="googleDriveFolderId",
            s3_bucket="s3Bucket",
            s3_prefix="s3Prefix",
            tags=["string"],
            webhook_signing_enabled=True,
            webhook_url="webhookUrl",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="send",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="send",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="split",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="split",
            display_name="displayName",
            print_page_split_config={
                "next_function_id": "nextFunctionID",
                "next_function_name": "nextFunctionName",
            },
            semantic_page_split_config={
                "item_classes": [
                    {
                        "name": "name",
                        "description": "description",
                        "next_function_id": "nextFunctionID",
                        "next_function_name": "nextFunctionName",
                    }
                ]
            },
            split_type="print_page",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="split",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="split",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="join",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="join",
            description="description",
            display_name="displayName",
            join_type="standard",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="join",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="join",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="payload_shaping",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="payload_shaping",
            display_name="displayName",
            shaping_schema="shapingSchema",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="payload_shaping",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="payload_shaping",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="enrich",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.create(
            function_name="functionName",
            type="enrich",
            config={
                "steps": [
                    {
                        "collection_name": "collectionName",
                        "source_field": "sourceField",
                        "target_field": "targetField",
                        "include_cosine_distance": True,
                        "include_subcollections": True,
                        "score_threshold": 0,
                        "search_mode": "semantic",
                        "top_k": 1,
                    }
                ]
            },
            display_name="displayName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.create(
            function_name="functionName",
            type="enrich",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.create(
            function_name="functionName",
            type="enrich",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.retrieve(
            "functionName",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.retrieve(
            "functionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.retrieve(
            "functionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.functions.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="transform",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="transform",
            display_name="displayName",
            function_name="functionName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tabular_chunking_enabled=True,
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="transform",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="transform",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="transform",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="analyze",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="analyze",
            display_name="displayName",
            function_name="functionName",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="analyze",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="analyze",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="analyze",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="route",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="route",
            description="description",
            display_name="displayName",
            function_name="functionName",
            routes=[
                {
                    "name": "name",
                    "description": "description",
                    "function_id": "functionID",
                    "function_name": "functionName",
                    "is_error_fallback": True,
                    "origin": {"email": {"patterns": ["string"]}},
                    "regex": {"patterns": ["string"]},
                }
            ],
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="route",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="route",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="route",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="send",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="send",
            destination_type="webhook",
            display_name="displayName",
            function_name="functionName",
            google_drive_folder_id="googleDriveFolderId",
            s3_bucket="s3Bucket",
            s3_prefix="s3Prefix",
            tags=["string"],
            webhook_signing_enabled=True,
            webhook_url="webhookUrl",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="send",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="send",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="send",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="split",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="split",
            display_name="displayName",
            function_name="functionName",
            print_page_split_config={
                "next_function_id": "nextFunctionID",
                "next_function_name": "nextFunctionName",
            },
            semantic_page_split_config={
                "item_classes": [
                    {
                        "name": "name",
                        "description": "description",
                        "next_function_id": "nextFunctionID",
                        "next_function_name": "nextFunctionName",
                    }
                ]
            },
            split_type="print_page",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="split",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="split",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="split",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="join",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="join",
            description="description",
            display_name="displayName",
            function_name="functionName",
            join_type="standard",
            output_schema={},
            output_schema_name="outputSchemaName",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="join",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="join",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="join",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="payload_shaping",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="payload_shaping",
            display_name="displayName",
            function_name="functionName",
            shaping_schema="shapingSchema",
            tags=["string"],
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="payload_shaping",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="payload_shaping",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="payload_shaping",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="enrich",
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.update(
            path_function_name="functionName",
            type="enrich",
            config={
                "steps": [
                    {
                        "collection_name": "collectionName",
                        "source_field": "sourceField",
                        "target_field": "targetField",
                        "include_cosine_distance": True,
                        "include_subcollections": True,
                        "score_threshold": 0,
                        "search_mode": "semantic",
                        "top_k": 1,
                    }
                ]
            },
        )
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.update(
            path_function_name="functionName",
            type="enrich",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(FunctionResponse, function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.update(
            path_function_name="functionName",
            type="enrich",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(FunctionResponse, function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_function_name` but received ''"):
            await async_client.functions.with_raw_response.update(
                path_function_name="",
                type="enrich",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.list()
        assert_matches_type(AsyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.list(
            display_name="displayName",
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            tags=["string"],
            types=["transform"],
            workflow_ids=["string"],
            workflow_names=["string"],
        )
        assert_matches_type(AsyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert_matches_type(AsyncFunctionsPage[Function], function, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert_matches_type(AsyncFunctionsPage[Function], function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBem) -> None:
        function = await async_client.functions.delete(
            "functionName",
        )
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBem) -> None:
        response = await async_client.functions.with_raw_response.delete(
            "functionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        function = await response.parse()
        assert function is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBem) -> None:
        async with async_client.functions.with_streaming_response.delete(
            "functionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            function = await response.parse()
            assert function is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `function_name` but received ''"):
            await async_client.functions.with_raw_response.delete(
                "",
            )
