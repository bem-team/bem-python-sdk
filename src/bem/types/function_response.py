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
    A function that delivers workflow outputs to an external destination. Send
    functions receive the output of an upstream workflow node and forward it to a
    webhook, S3 bucket, or Google Drive folder.
    """
