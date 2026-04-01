# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .function_version_identifier_param import FunctionVersionIdentifierParam

__all__ = ["WorkflowRequestRelationshipParam"]


class WorkflowRequestRelationshipParam(TypedDict, total=False):
    destination_function: Required[Annotated[FunctionVersionIdentifierParam, PropertyInfo(alias="destinationFunction")]]

    source_function: Required[Annotated[FunctionVersionIdentifierParam, PropertyInfo(alias="sourceFunction")]]

    destination_name: Annotated[str, PropertyInfo(alias="destinationName")]
    """Name of destination."""
