# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CollectionCreateParams"]


class CollectionCreateParams(TypedDict, total=False):
    collection_name: Required[Annotated[str, PropertyInfo(alias="collectionName")]]
    """Unique name/path for the collection.

    Supports dot notation for hierarchical paths.

    - Only letters (a-z, A-Z), digits (0-9), underscores (\\__), and dots (.) are
      allowed
    - Each segment (between dots) must start with a letter or underscore (not a
      digit)
    - Segments cannot consist only of digits
    - Each segment must be 1-256 characters
    - No leading, trailing, or consecutive dots
    - Invalid names are rejected with a 400 Bad Request error

    **Valid Examples:**

    - 'product_catalog'
    - 'orders.line_items.sku'
    - 'customer_data'
    - 'price_v2'

    **Invalid Examples:**

    - 'product-catalog' (contains hyphen)
    - '123items' (starts with digit)
    - 'items..data' (consecutive dots)
    - 'order#123' (contains invalid character #)
    """
