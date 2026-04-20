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
    """V3 read-side union.

    Same shape as the shared `Function` union but with `classify` in place of
    `route`. Legacy `transform` and `analyze` functions remain readable via V3.
    """
