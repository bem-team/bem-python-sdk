# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .function_version import FunctionVersion

__all__ = ["VersionRetrieveResponse"]


class VersionRetrieveResponse(BaseModel):
    """Single-function-version response wrapper used by V3 endpoints."""

    function: FunctionVersion
    """
    A version of a payload shaping function that transforms and customizes input
    payloads using JMESPath expressions. Payload shaping allows you to extract
    specific data, perform calculations, and reshape complex input structures into
    simplified, standardized output formats tailored to your downstream systems or
    business requirements.
    """
