# Functions

Types:

```python
from bem.types import (
    CreateFunction,
    EnrichConfig,
    EnrichStep,
    Function,
    FunctionAudit,
    FunctionResponse,
    FunctionType,
    ListFunctionsResponse,
    RouteListItem,
    SplitFunctionSemanticPageItemClass,
    UpdateFunction,
    UserActionSummary,
    WorkflowUsageInfo,
)
```

Methods:

- <code title="post /v3/functions">client.functions.<a href="./src/bem/resources/functions/functions.py">create</a>(\*\*<a href="src/bem/types/function_create_params.py">params</a>) -> <a href="./src/bem/types/function_response.py">FunctionResponse</a></code>
- <code title="get /v3/functions/{functionName}">client.functions.<a href="./src/bem/resources/functions/functions.py">retrieve</a>(function_name) -> <a href="./src/bem/types/function_response.py">FunctionResponse</a></code>
- <code title="patch /v3/functions/{functionName}">client.functions.<a href="./src/bem/resources/functions/functions.py">update</a>(path_function_name, \*\*<a href="src/bem/types/function_update_params.py">params</a>) -> <a href="./src/bem/types/function_response.py">FunctionResponse</a></code>
- <code title="get /v3/functions">client.functions.<a href="./src/bem/resources/functions/functions.py">list</a>(\*\*<a href="src/bem/types/function_list_params.py">params</a>) -> <a href="./src/bem/types/function.py">SyncFunctionsPage[Function]</a></code>
- <code title="delete /v3/functions/{functionName}">client.functions.<a href="./src/bem/resources/functions/functions.py">delete</a>(function_name) -> None</code>

## Copy

Types:

```python
from bem.types.functions import FunctionCopyRequest
```

Methods:

- <code title="post /v3/functions/copy">client.functions.copy.<a href="./src/bem/resources/functions/copy.py">create</a>(\*\*<a href="src/bem/types/functions/copy_create_params.py">params</a>) -> <a href="./src/bem/types/function_response.py">FunctionResponse</a></code>

## Versions

Types:

```python
from bem.types.functions import (
    FunctionVersion,
    ListFunctionVersionsResponse,
    VersionRetrieveResponse,
)
```

Methods:

- <code title="get /v3/functions/{functionName}/versions/{versionNum}">client.functions.versions.<a href="./src/bem/resources/functions/versions.py">retrieve</a>(version_num, \*, function_name) -> <a href="./src/bem/types/functions/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="get /v3/functions/{functionName}/versions">client.functions.versions.<a href="./src/bem/resources/functions/versions.py">list</a>(function_name) -> <a href="./src/bem/types/functions/list_function_versions_response.py">ListFunctionVersionsResponse</a></code>

# Calls

Types:

```python
from bem.types import Call, CallGetResponse
```

Methods:

- <code title="get /v3/calls/{callID}">client.calls.<a href="./src/bem/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/bem/types/call_get_response.py">CallGetResponse</a></code>
- <code title="get /v3/calls">client.calls.<a href="./src/bem/resources/calls.py">list</a>(\*\*<a href="src/bem/types/call_list_params.py">params</a>) -> <a href="./src/bem/types/call.py">SyncCallsPage[Call]</a></code>

# Errors

Types:

```python
from bem.types import ErrorEvent, InboundEmailEvent, ErrorRetrieveResponse
```

Methods:

- <code title="get /v3/errors/{eventID}">client.errors.<a href="./src/bem/resources/errors.py">retrieve</a>(event_id) -> <a href="./src/bem/types/error_retrieve_response.py">ErrorRetrieveResponse</a></code>
- <code title="get /v3/errors">client.errors.<a href="./src/bem/resources/errors.py">list</a>(\*\*<a href="src/bem/types/error_list_params.py">params</a>) -> <a href="./src/bem/types/error_event.py">SyncErrorsPage[ErrorEvent]</a></code>

# Outputs

Types:

```python
from bem.types import AnyType, Event, OutputRetrieveResponse
```

Methods:

- <code title="get /v3/outputs/{eventID}">client.outputs.<a href="./src/bem/resources/outputs.py">retrieve</a>(event_id) -> <a href="./src/bem/types/output_retrieve_response.py">OutputRetrieveResponse</a></code>
- <code title="get /v3/outputs">client.outputs.<a href="./src/bem/resources/outputs.py">list</a>(\*\*<a href="src/bem/types/output_list_params.py">params</a>) -> <a href="./src/bem/types/event.py">SyncOutputsPage[Event]</a></code>

# Workflows

Types:

```python
from bem.types import (
    FunctionVersionIdentifier,
    Workflow,
    WorkflowRequestRelationship,
    WorkflowCreateResponse,
    WorkflowRetrieveResponse,
    WorkflowUpdateResponse,
    WorkflowCopyResponse,
)
```

Methods:

- <code title="post /v3/workflows">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">create</a>(\*\*<a href="src/bem/types/workflow_create_params.py">params</a>) -> <a href="./src/bem/types/workflow_create_response.py">WorkflowCreateResponse</a></code>
- <code title="get /v3/workflows/{workflowName}">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">retrieve</a>(workflow_name) -> <a href="./src/bem/types/workflow_retrieve_response.py">WorkflowRetrieveResponse</a></code>
- <code title="patch /v3/workflows/{workflowName}">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">update</a>(workflow_name, \*\*<a href="src/bem/types/workflow_update_params.py">params</a>) -> <a href="./src/bem/types/workflow_update_response.py">WorkflowUpdateResponse</a></code>
- <code title="get /v3/workflows">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">list</a>(\*\*<a href="src/bem/types/workflow_list_params.py">params</a>) -> <a href="./src/bem/types/workflow.py">SyncWorkflowsPage[Workflow]</a></code>
- <code title="delete /v3/workflows/{workflowName}">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">delete</a>(workflow_name) -> None</code>
- <code title="post /v3/workflows/{workflowName}/call">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">call</a>(workflow_name, \*\*<a href="src/bem/types/workflow_call_params.py">params</a>) -> <a href="./src/bem/types/call_get_response.py">CallGetResponse</a></code>
- <code title="post /v3/workflows/copy">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">copy</a>(\*\*<a href="src/bem/types/workflow_copy_params.py">params</a>) -> <a href="./src/bem/types/workflow_copy_response.py">WorkflowCopyResponse</a></code>

## Versions

Types:

```python
from bem.types.workflows import VersionRetrieveResponse
```

Methods:

- <code title="get /v3/workflows/{workflowName}/versions/{versionNum}">client.workflows.versions.<a href="./src/bem/resources/workflows/versions.py">retrieve</a>(version_num, \*, workflow_name) -> <a href="./src/bem/types/workflows/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="get /v3/workflows/{workflowName}/versions">client.workflows.versions.<a href="./src/bem/resources/workflows/versions.py">list</a>(workflow_name, \*\*<a href="src/bem/types/workflows/version_list_params.py">params</a>) -> <a href="./src/bem/types/workflow.py">SyncWorkflowVersionsPage[Workflow]</a></code>
