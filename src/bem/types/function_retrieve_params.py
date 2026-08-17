# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FunctionRetrieveParams"]


class FunctionRetrieveParams(TypedDict, total=False):
    include_extra_settings: Annotated[bool, PropertyInfo(alias="includeExtraSettings")]
    """Populate the function's `extraConfig` block.

    Omitted or `false` by default, in which case `extraConfig` is absent from the
    response.
    """
