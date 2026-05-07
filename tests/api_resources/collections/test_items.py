# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from bem import Bem, AsyncBem
from bem.types import Collection
from tests.utils import assert_matches_type
from bem.types.collections import (
    ItemAddResponse,
    ItemUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Bem) -> None:
        item = client.collections.items.retrieve(
            collection_name="collectionName",
        )
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Bem) -> None:
        item = client.collections.items.retrieve(
            collection_name="collectionName",
            include_subcollections=True,
            limit=1,
            page=1,
        )
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Bem) -> None:
        response = client.collections.items.with_raw_response.retrieve(
            collection_name="collectionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Bem) -> None:
        with client.collections.items.with_streaming_response.retrieve(
            collection_name="collectionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(Collection, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Bem) -> None:
        item = client.collections.items.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Bem) -> None:
        response = client.collections.items.with_raw_response.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Bem) -> None:
        with client.collections.items.with_streaming_response.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Bem) -> None:
        item = client.collections.items.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Bem) -> None:
        response = client.collections.items.with_raw_response.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Bem) -> None:
        with client.collections.items.with_streaming_response.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add(self, client: Bem) -> None:
        item = client.collections.items.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Bem) -> None:
        response = client.collections.items.with_raw_response.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = response.parse()
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Bem) -> None:
        with client.collections.items.with_streaming_response.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = response.parse()
            assert_matches_type(ItemAddResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBem) -> None:
        item = await async_client.collections.items.retrieve(
            collection_name="collectionName",
        )
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBem) -> None:
        item = await async_client.collections.items.retrieve(
            collection_name="collectionName",
            include_subcollections=True,
            limit=1,
            page=1,
        )
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBem) -> None:
        response = await async_client.collections.items.with_raw_response.retrieve(
            collection_name="collectionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(Collection, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBem) -> None:
        async with async_client.collections.items.with_streaming_response.retrieve(
            collection_name="collectionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(Collection, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncBem) -> None:
        item = await async_client.collections.items.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        )
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncBem) -> None:
        response = await async_client.collections.items.with_raw_response.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemUpdateResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncBem) -> None:
        async with async_client.collections.items.with_streaming_response.update(
            collection_name="product_catalog",
            items=[
                {
                    "collection_item_id": "clitm_2N6gH8ZKCmvb6BnFcGqhKJ98VzP",
                    "data": "SKU-12345: Updated Industrial Widget - Premium Edition",
                },
                {
                    "collection_item_id": "clitm_3M7hI9ALDnwc7CoGdHriLK09WaQ",
                    "data": {
                        "sku": "SKU-67890",
                        "name": "Updated Premium Gear",
                        "category": "Hardware",
                        "price": 399.99,
                    },
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemUpdateResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncBem) -> None:
        item = await async_client.collections.items.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        )
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncBem) -> None:
        response = await async_client.collections.items.with_raw_response.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert item is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncBem) -> None:
        async with async_client.collections.items.with_streaming_response.delete(
            collection_item_id="collectionItemID",
            collection_name="collectionName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert item is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncBem) -> None:
        item = await async_client.collections.items.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        )
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncBem) -> None:
        response = await async_client.collections.items.with_raw_response.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        item = await response.parse()
        assert_matches_type(ItemAddResponse, item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncBem) -> None:
        async with async_client.collections.items.with_streaming_response.add(
            collection_name="product_catalog",
            items=[
                {
                    "data": {
                        "sku": "SKU-11111",
                        "name": "Deluxe Component",
                        "category": "Hardware",
                        "price": 299.99,
                    }
                },
                {
                    "data": {
                        "sku": "SKU-22222",
                        "name": "Standard Part",
                        "category": "Tools",
                        "price": 49.99,
                    }
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            item = await response.parse()
            assert_matches_type(ItemAddResponse, item, path=["response"])

        assert cast(Any, response.is_closed) is True
