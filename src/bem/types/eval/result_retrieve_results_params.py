# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResultRetrieveResultsParams"]


class ResultRetrieveResultsParams(TypedDict, total=False):
    transformation_ids: Required[Annotated[str, PropertyInfo(alias="transformationIDs")]]
    """
    Comma-separated list of transformation IDs to fetch results for. Between 1 and
    100 IDs per request.
    """

    evaluation_version: Annotated[str, PropertyInfo(alias="evaluationVersion")]
    """Optional evaluation version filter."""
