# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InferSchemaCreateParams"]


class InferSchemaCreateParams(TypedDict, total=False):
    file: Required[object]
    """The file to analyze and infer a JSON schema from."""
