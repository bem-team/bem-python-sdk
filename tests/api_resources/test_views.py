# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import (
    ViewListResponse,
    ViewCreateResponse,
    ViewUpdateResponse,
    ViewRetrieveResponse,
    ViewGenerateTableDataResponse,
    ViewGenerateAggregationDataResponse,
)
from bem._utils import parse_datetime
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestViews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        view = client.views.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.views.with_raw_response.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.views.with_streaming_response.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewCreateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        view = client.views.retrieve(
            "view_id",
        )
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.views.with_raw_response.retrieve(
            "view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.views.with_streaming_response.retrieve(
            "view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewRetrieveResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Bem) -> None:
        view = client.views.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Bem) -> None:
        response = client.views.with_raw_response.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Bem) -> None:
        with client.views.with_streaming_response.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewUpdateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.update(
                view_id="",
                aggregations=[
                    {
                        "function": "count",
                        "name": "name",
                    }
                ],
                columns=[
                    {
                        "display_order_index": 0,
                        "name": "name",
                        "value_schema_path": ["string"],
                    }
                ],
                filters=[
                    {
                        "column_name": "columnName",
                        "filter_type": "equals_string",
                    }
                ],
                functions=[{}],
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        view = client.views.list()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        view = client.views.list(
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            view_ids=["string"],
            view_name_substring="viewNameSubstring",
        )
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewListResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Bem) -> None:
        view = client.views.delete(
            "view_id",
        )
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Bem) -> None:
        response = client.views.with_raw_response.delete(
            "view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Bem) -> None:
        with client.views.with_streaming_response.delete(
            "view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.views.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_aggregation_data(self, client: Bem) -> None:
        view = client.views.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_aggregation_data(self, client: Bem) -> None:
        response = client.views.with_raw_response.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_aggregation_data(self, client: Bem) -> None:
        with client.views.with_streaming_response.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_table_data(self, client: Bem) -> None:
        view = client.views.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_table_data_with_all_params(self, client: Bem) -> None:
        view = client.views.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                    "aggregate_column_name": "aggregateColumnName",
                    "group_by_column_name": "groupByColumnName",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                    "number": 0,
                    "string": "string",
                }
            ],
            functions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            offset=0,
        )
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_table_data(self, client: Bem) -> None:
        response = client.views.with_raw_response.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = response.parse()
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_table_data(self, client: Bem) -> None:
        with client.views.with_streaming_response.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = response.parse()
            assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncViews:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        view = await async_client.views.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewCreateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.create(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewCreateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        view = await async_client.views.retrieve(
            "view_id",
        )
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.retrieve(
            "view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewRetrieveResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.retrieve(
            "view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewRetrieveResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBem) -> None:
        view = await async_client.views.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewUpdateResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.update(
            view_id="view_id",
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewUpdateResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.update(
                view_id="",
                aggregations=[
                    {
                        "function": "count",
                        "name": "name",
                    }
                ],
                columns=[
                    {
                        "display_order_index": 0,
                        "name": "name",
                        "value_schema_path": ["string"],
                    }
                ],
                filters=[
                    {
                        "column_name": "columnName",
                        "filter_type": "equals_string",
                    }
                ],
                functions=[{}],
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        view = await async_client.views.list()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        view = await async_client.views.list(
            ending_before="endingBefore",
            function_ids=["string"],
            function_names=["string"],
            limit=1,
            sort_order="asc",
            starting_after="startingAfter",
            view_ids=["string"],
            view_name_substring="viewNameSubstring",
        )
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewListResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewListResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBem) -> None:
        view = await async_client.views.delete(
            "view_id",
        )
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.delete(
            "view_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert view is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.delete(
            "view_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert view is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.views.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_aggregation_data(self, async_client: AsyncBem) -> None:
        view = await async_client.views.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_aggregation_data(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_aggregation_data(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.generate_aggregation_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewGenerateAggregationDataResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_table_data(self, async_client: AsyncBem) -> None:
        view = await async_client.views.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_table_data_with_all_params(self, async_client: AsyncBem) -> None:
        view = await async_client.views.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                    "aggregate_column_name": "aggregateColumnName",
                    "group_by_column_name": "groupByColumnName",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                    "number": 0,
                    "string": "string",
                }
            ],
            functions=[
                {
                    "id": "id",
                    "name": "name",
                }
            ],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            limit=1,
            offset=0,
        )
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_table_data(self, async_client: AsyncBem) -> None:
        response = await async_client.views.with_raw_response.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        view = await response.parse()
        assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_table_data(self, async_client: AsyncBem) -> None:
        async with async_client.views.with_streaming_response.generate_table_data(
            aggregations=[
                {
                    "function": "count",
                    "name": "name",
                }
            ],
            columns=[
                {
                    "display_order_index": 0,
                    "name": "name",
                    "value_schema_path": ["string"],
                }
            ],
            filters=[
                {
                    "column_name": "columnName",
                    "filter_type": "equals_string",
                }
            ],
            functions=[{}],
            name="name",
            time_window={
                "end": parse_datetime("2019-12-27T18:11:19.117Z"),
                "start": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            view = await response.parse()
            assert_matches_type(ViewGenerateTableDataResponse, view, path=["response"])

        assert cast(Any, response.is_closed) is True
