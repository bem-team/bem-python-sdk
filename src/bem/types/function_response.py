# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .function import Function

__all__ = ["FunctionResponse"]


class FunctionResponse(BaseModel):
    """
    Single-function response wrapper used by V3 function endpoints.
    V3 wraps individual function responses in a `{"function": ...}` envelope
    for consistency with other V3 resource endpoints.
    """

    function: Function
    """
    A function that transforms and customizes input payloads using JMESPath
    expressions. Payload shaping allows you to extract specific data, perform
    calculations, and reshape complex input structures into simplified, standardized
    output formats tailored to your downstream systems or business requirements.
    """
