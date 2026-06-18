# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ReviewerAssignParams"]


class ReviewerAssignParams(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userID")]]
    """Public ID (`usr_...`) of the user to assign. Must belong to the account."""
