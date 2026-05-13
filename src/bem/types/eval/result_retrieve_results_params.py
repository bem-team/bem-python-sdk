# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResultRetrieveResultsParams"]


class ResultRetrieveResultsParams(TypedDict, total=False):
    evaluation_version: Annotated[str, PropertyInfo(alias="evaluationVersion")]
    """Optional evaluation version filter."""

    event_ids: Annotated[str, PropertyInfo(alias="eventIDs")]
    """Comma-separated list of event KSUIDs to fetch results for.

    Between 1 and 100 IDs per request. Mutually exclusive with `transformationIDs`.
    """

    transformation_ids: Annotated[str, PropertyInfo(alias="transformationIDs")]
    """
    Comma-separated list of transformation IDs to fetch results for. Between 1 and
    100 IDs per request. Mutually exclusive with `eventIDs`. Prefer `eventIDs` for
    new integrations.
    """
