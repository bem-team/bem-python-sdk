# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .function_version import FunctionVersion

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    """Single-function-version response wrapper used by V3 endpoints."""

    function: FunctionVersion
    """V3 read-side union for function versions.

    Same shape as the shared `FunctionVersion` union but with `classify` in place of
    `route`.
    """
