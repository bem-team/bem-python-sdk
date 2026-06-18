# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EntityBulkValidateParams"]


class EntityBulkValidateParams(TypedDict, total=False):
    entity_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="entityIDs")]]
    """The `ent_...` IDs to transition. Must be non-empty."""

    status: Required[Literal["approved", "rejected"]]
    """Terminal status to apply to every entity."""
