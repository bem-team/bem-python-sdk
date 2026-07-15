# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import (
    EntityType,
    EntityTypeListResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntityTypes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Bem) -> None:
        entity_type = client.entity_types.create(
            name="Drug",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Bem) -> None:
        entity_type = client.entity_types.create(
            name="Drug",
            attribute_schema={},
            description="A pharmaceutical compound",
            parent_type_id="parentTypeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Bem) -> None:
        response = client.entity_types.with_raw_response.create(
            name="Drug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Bem) -> None:
        with client.entity_types.with_streaming_response.create(
            name="Drug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        entity_type = client.entity_types.retrieve(
            "typeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.entity_types.with_raw_response.retrieve(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.entity_types.with_streaming_response.retrieve(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Bem) -> None:
        entity_type = client.entity_types.update(
            type_id="typeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Bem) -> None:
        entity_type = client.entity_types.update(
            type_id="typeID",
            attribute_schema={},
            description="description",
            parent_type_id="parentTypeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Bem) -> None:
        response = client.entity_types.with_raw_response.update(
            type_id="typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Bem) -> None:
        with client.entity_types.with_streaming_response.update(
            type_id="typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.with_raw_response.update(
                type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Bem) -> None:
        entity_type = client.entity_types.list()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Bem) -> None:
        entity_type = client.entity_types.list(
            ending_before="endingBefore",
            limit=0,
            parent_type_id="parentTypeId",
            starting_after="startingAfter",
        )
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Bem) -> None:
        response = client.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Bem) -> None:
        with client.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Bem) -> None:
        entity_type = client.entity_types.delete(
            "typeID",
        )
        assert entity_type is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Bem) -> None:
        response = client.entity_types.with_raw_response.delete(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = response.parse()
        assert entity_type is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Bem) -> None:
        with client.entity_types.with_streaming_response.delete(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = response.parse()
            assert entity_type is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Bem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            client.entity_types.with_raw_response.delete(
                "",
            )


class TestAsyncEntityTypes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.create(
            name="Drug",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.create(
            name="Drug",
            attribute_schema={},
            description="A pharmaceutical compound",
            parent_type_id="parentTypeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.with_raw_response.create(
            name="Drug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.with_streaming_response.create(
            name="Drug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.retrieve(
            "typeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.with_raw_response.retrieve(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.with_streaming_response.retrieve(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.update(
            type_id="typeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.update(
            type_id="typeID",
            attribute_schema={},
            description="description",
            parent_type_id="parentTypeID",
        )
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.with_raw_response.update(
            type_id="typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityType, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.with_streaming_response.update(
            type_id="typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityType, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.with_raw_response.update(
                type_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.list()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.list(
            ending_before="endingBefore",
            limit=0,
            parent_type_id="parentTypeId",
            starting_after="startingAfter",
        )
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert_matches_type(EntityTypeListResponse, entity_type, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBem) -> None:
        entity_type = await async_client.entity_types.delete(
            "typeID",
        )
        assert entity_type is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBem) -> None:
        response = await async_client.entity_types.with_raw_response.delete(
            "typeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity_type = await response.parse()
        assert entity_type is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBem) -> None:
        async with async_client.entity_types.with_streaming_response.delete(
            "typeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity_type = await response.parse()
            assert entity_type is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncBem) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `type_id` but received ''"):
            await async_client.entity_types.with_raw_response.delete(
                "",
            )
