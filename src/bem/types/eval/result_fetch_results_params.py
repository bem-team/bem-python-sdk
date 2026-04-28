# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ResultFetchResultsParams"]


class ResultFetchResultsParams(TypedDict, total=False):
    transformation_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="transformationIDs")]]
    """Transformation IDs to fetch results for. Up to 100 per request."""

    evaluation_version: Annotated[str, PropertyInfo(alias="evaluationVersion")]
    """Optional evaluation version filter."""
