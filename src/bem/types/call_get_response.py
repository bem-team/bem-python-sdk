# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .call import Call
from .._models import BaseModel

__all__ = ["CallGetResponse"]


class CallGetResponse(BaseModel):
    call: Optional[Call] = None
    """A call returned by the V3 API.

    Compared to the V2 `Call` model:

    - Terminal outputs are split into `outputs` (non-error events) and `errors`
      (error events)
    - The deprecated `functionCalls` field is removed (use
      `GET /v3/calls/{callID}/trace`)
    - `url` and `traceUrl` hint fields are included for resource discovery

    Most calls are workflow calls, and `POST /v3/workflows/{workflowName}/call` only
    ever creates those. `GET /v3/calls` and `GET /v3/calls/{callID}` also return
    direct and adhoc function calls, which carry the function-scoped fields instead
    of the workflow-scoped ones — read `callType` to tell them apart.
    """

    error: Optional[str] = None
    """
    Error message if the call retrieval failed, or if the call itself failed when
    using `wait=true`.
    """
