# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["WorkflowCopyResponse", "CopiedFunction"]


class CopiedFunction(BaseModel):
    source_function_id: str = FieldInfo(alias="sourceFunctionID")
    """ID of the source function that was copied."""

    source_function_name: str = FieldInfo(alias="sourceFunctionName")
    """Name of the source function that was copied."""

    source_version_num: int = FieldInfo(alias="sourceVersionNum")
    """Version number of the source function that was copied."""

    target_function_id: str = FieldInfo(alias="targetFunctionID")
    """ID of the newly created function in the target environment."""

    target_function_name: str = FieldInfo(alias="targetFunctionName")
    """Name of the newly created function in the target environment."""

    target_version_num: int = FieldInfo(alias="targetVersionNum")
    """Version number of the newly created function in the target environment."""


class WorkflowCopyResponse(BaseModel):
    copied_functions: Optional[List[CopiedFunction]] = FieldInfo(alias="copiedFunctions", default=None)
    """
    Functions that were copied when copying to a different environment. Empty when
    copying within the same environment.
    """

    environment: Optional[str] = None
    """The environment the workflow was copied to."""

    error: Optional[str] = None
    """Error message if the workflow copy failed."""

    workflow: Optional[Workflow] = None
    """V3 read representation of a workflow version."""
