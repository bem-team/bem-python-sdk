# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["VersionRetrieveParams"]


class VersionRetrieveParams(TypedDict, total=False):
    function_name: Required[Annotated[str, PropertyInfo(alias="functionName")]]

    include_extra_settings: Annotated[bool, PropertyInfo(alias="includeExtraSettings")]
    """Populate the version's `extraConfig` block.

    Omitted or `false` by default, in which case `extraConfig` is absent from the
    response.
    """
