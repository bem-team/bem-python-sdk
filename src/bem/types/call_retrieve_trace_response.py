# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .function_type import FunctionType

__all__ = [
    "CallRetrieveTraceResponse",
    "Trace",
    "TraceFunctionCall",
    "TraceFunctionCallActivity",
    "TraceFunctionCallInput",
]


class TraceFunctionCallActivity(BaseModel):
    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    status: Optional[Literal["pending", "running", "completed", "failed"]] = None


class TraceFunctionCallInput(BaseModel):
    input_type: Optional[str] = FieldInfo(alias="inputType", default=None)
    """Input type of the file"""

    item_reference_id: Optional[str] = FieldInfo(alias="itemReferenceID", default=None)
    """Item reference ID for batch inputs"""

    s3_url: Optional[str] = FieldInfo(alias="s3URL", default=None)
    """Presigned S3 URL for the file input"""


class TraceFunctionCall(BaseModel):
    function_call_id: str = FieldInfo(alias="functionCallID")
    """Unique identifier for this function call"""

    function_id: str = FieldInfo(alias="functionID")
    """ID of the function that was called"""

    function_name: str = FieldInfo(alias="functionName")
    """Name of the function that was called"""

    reference_id: str = FieldInfo(alias="referenceID")
    """User-provided reference ID for tracking"""

    started_at: datetime = FieldInfo(alias="startedAt")
    """The date and time this function call started."""

    status: Literal["pending", "running", "completed", "failed"]
    """The status of the action."""

    type: FunctionType
    """The type of the function."""

    activity: Optional[List[TraceFunctionCallActivity]] = None
    """Array of activity steps for this function call"""

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)
    """The date and time this function call finished. Absent while still running."""

    function_version_num: Optional[int] = FieldInfo(alias="functionVersionNum", default=None)
    """Version number of the function"""

    incoming_destination_name: Optional[str] = FieldInfo(alias="incomingDestinationName", default=None)
    """The labelled outlet on the upstream node that routed execution to this call.

    Absent for root calls, unlabelled edges, and pre-migration rows.
    """

    inputs: Optional[List[TraceFunctionCallInput]] = None
    """Array of all file inputs with their S3 URLs"""

    input_type: Optional[str] = FieldInfo(alias="inputType", default=None)
    """Input type for single file input (set when there's exactly one file input)"""

    s3_url: Optional[str] = FieldInfo(alias="s3URL", default=None)
    """
    Presigned S3 URL for single file input (set when there's exactly one file input)
    """

    source_event_id: Optional[str] = FieldInfo(alias="sourceEventID", default=None)
    """ID of the event that spawned this function call (for DAG reconstruction).

    Nil for the root function call.
    """

    source_function_call_id: Optional[str] = FieldInfo(alias="sourceFunctionCallID", default=None)
    """
    ID of the function call that spawned this function call (for DAG reconstruction)
    """

    workflow_call_id: Optional[str] = FieldInfo(alias="workflowCallID", default=None)
    """
    ID of the workflow call this function call belongs to (top-level execution
    context)
    """

    workflow_node_name: Optional[str] = FieldInfo(alias="workflowNodeName", default=None)
    """Name of the workflow DAG call-site node this function call is executing.

    Absent for non-workflow calls and pre-migration rows.
    """


class Trace(BaseModel):
    """Full execution DAG of a call as flat arrays.

    Reconstruct the graph using
    FunctionCallResponseBase.sourceEventID and each event's functionCallID.
    """

    events: List[object]
    """All events emitted within this call, polymorphic by eventType."""

    function_calls: List[TraceFunctionCall] = FieldInfo(alias="functionCalls")
    """All function calls executed within this call."""


class CallRetrieveTraceResponse(BaseModel):
    """Response from `GET /v3/calls/{callID}/trace`.

    Contains the full execution DAG as flat arrays of function calls and events. Reconstruct the
    graph using `FunctionCallResponseBase.sourceEventID` (the event that spawned each function call)
    and each event's `functionCallID` (the function call that emitted it).
    """

    error: Optional[str] = None
    """Error message if trace retrieval failed."""

    trace: Optional[Trace] = None
    """Full execution DAG of a call as flat arrays.

    Reconstruct the graph using FunctionCallResponseBase.sourceEventID and each
    event's functionCallID.
    """
