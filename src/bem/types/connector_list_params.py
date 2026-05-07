# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ConnectorListParams"]


class ConnectorListParams(TypedDict, total=False):
    workflow_id: Annotated[str, PropertyInfo(alias="workflowID")]
    """Filter connectors by workflow API ID (e.g. `wf_...`).

    If both `workflowID` and `workflowName` are provided, results must match both.
    """

    workflow_name: Annotated[str, PropertyInfo(alias="workflowName")]
    """Filter connectors by workflow name (exact match).

    If both `workflowID` and `workflowName` are provided, results must match both.
    """
