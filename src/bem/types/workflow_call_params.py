# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkflowCallParams"]


class WorkflowCallParams(TypedDict, total=False):
    call_reference_id: Annotated[str, PropertyInfo(alias="callReferenceID")]
    """Your reference ID for tracking this call."""

    file: object
    """Single input file (for transform, analyze, route, and split functions)."""

    files: Iterable[object]
    """Multiple input files (for join functions)."""

    wait: str
    """
    When `true`, the endpoint blocks until the call completes (up to 30 seconds) and
    returns the finished call object. Default: `false`.
    """
