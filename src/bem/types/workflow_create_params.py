# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .function_version_identifier_param import FunctionVersionIdentifierParam
from .workflow_request_relationship_param import WorkflowRequestRelationshipParam

__all__ = ["WorkflowCreateParams"]


class WorkflowCreateParams(TypedDict, total=False):
    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """Display name of workflow."""

    main_function: Annotated[FunctionVersionIdentifierParam, PropertyInfo(alias="mainFunction")]
    """Main function for the workflow.

    The `mainFunction` and `relationships` fields act as a unit and must be provided
    together, or neither provided.

    - If `mainFunction` is provided without `relationships`, relationships will
      default to an empty array.
    - If `relationships` is provided, `mainFunction` must also be provided
      (validation error if missing).
    - If neither is provided, both mainFunction and relationships remain unchanged
      from the current workflow version.
    """

    name: str
    """Name of workflow.

    Can be updated to rename the workflow. Must be unique within the environment and
    match the pattern ^[a-zA-Z0-9_-]{1,128}$.
    """

    relationships: Iterable[WorkflowRequestRelationshipParam]
    """Relationships between functions in the workflow.

    The `mainFunction` and `relationships` fields act as a unit and must be provided
    together, or neither provided.

    - If `relationships` is provided, `mainFunction` must also be provided
      (validation error if missing).
    - If `mainFunction` is provided without `relationships`, relationships will
      default to an empty array.
    - If neither is provided, both mainFunction and relationships remain unchanged
      from the current workflow version.
    """

    tags: SequenceNotStr[str]
    """Array of tags to categorize and organize workflows."""
