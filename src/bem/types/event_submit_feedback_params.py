# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventSubmitFeedbackParams"]


class EventSubmitFeedbackParams(TypedDict, total=False):
    correction: Required[object]

    order_matching: Annotated[bool, PropertyInfo(alias="orderMatching")]
