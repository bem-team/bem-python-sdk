# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .function_version_identifier_param import FunctionVersionIdentifierParam

__all__ = ["WorkflowNodeParam"]


class WorkflowNodeParam(TypedDict, total=False):
    """A single function call-site node in a workflow DAG."""

    function: Required[FunctionVersionIdentifierParam]
    """The function (and version) to execute at this call site."""

    metadata: object
    """Opaque free-form JSON object attached to this node.

    Stored and returned verbatim; the server does not interpret it. Intended for
    client-side concerns such as canvas display properties (position, color,
    collapsed state, etc.).
    """

    name: str
    """Name for this call site.

    Must be unique within the workflow version. Defaults to the function's own name
    when omitted.
    """
