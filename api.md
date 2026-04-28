# Functions

Types:

```python
from bem.types import (
    ClassificationListItem,
    CreateFunction,
    EnrichConfig,
    EnrichStep,
    Function,
    FunctionAudit,
    FunctionResponse,
    FunctionType,
    ListFunctionsResponse,
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
from bem.types import Call, CallGetResponse, CallRetrieveTraceResponse
```

Methods:

- <code title="get /v3/calls/{callID}">client.calls.<a href="./src/bem/resources/calls.py">retrieve</a>(call_id) -> <a href="./src/bem/types/call_get_response.py">CallGetResponse</a></code>
- <code title="get /v3/calls">client.calls.<a href="./src/bem/resources/calls.py">list</a>(\*\*<a href="src/bem/types/call_list_params.py">params</a>) -> <a href="./src/bem/types/call.py">SyncCallsPage[Call]</a></code>
- <code title="get /v3/calls/{callID}/trace">client.calls.<a href="./src/bem/resources/calls.py">retrieve_trace</a>(call_id) -> <a href="./src/bem/types/call_retrieve_trace_response.py">CallRetrieveTraceResponse</a></code>

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
from bem.types import AnyType, OutputRetrieveResponse, OutputListResponse
```

Methods:

- <code title="get /v3/outputs/{eventID}">client.outputs.<a href="./src/bem/resources/outputs.py">retrieve</a>(event_id) -> <a href="./src/bem/types/output_retrieve_response.py">OutputRetrieveResponse</a></code>
- <code title="get /v3/outputs">client.outputs.<a href="./src/bem/resources/outputs.py">list</a>(\*\*<a href="src/bem/types/output_list_params.py">params</a>) -> <a href="./src/bem/types/output_list_response.py">SyncOutputsPage[OutputListResponse]</a></code>

# Workflows

Types:

```python
from bem.types import (
    FunctionVersionIdentifier,
    Workflow,
    WorkflowAudit,
    WorkflowEdgeResponse,
    WorkflowNodeResponse,
    WorkflowRetrieveResponse,
    WorkflowUpdateResponse,
    WorkflowCopyResponse,
)
```

Methods:

- <code title="post /v3/workflows">client.workflows.<a href="./src/bem/resources/workflows/workflows.py">create</a>(\*\*<a href="src/bem/types/workflow_create_params.py">params</a>) -> <a href="./src/bem/types/workflow.py">Optional[Workflow]</a></code>
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

# InferSchema

Types:

```python
from bem.types import InferSchemaCreateResponse
```

Methods:

- <code title="post /v3/infer-schema">client.infer_schema.<a href="./src/bem/resources/infer_schema.py">create</a>(\*\*<a href="src/bem/types/infer_schema_create_params.py">params</a>) -> <a href="./src/bem/types/infer_schema_create_response.py">InferSchemaCreateResponse</a></code>

# Collections

Types:

```python
from bem.types import (
    CollectionCreateResponse,
    CollectionListResponse,
    CollectionCountTokensResponse,
)
```

Methods:

- <code title="post /v3/collections">client.collections.<a href="./src/bem/resources/collections/collections.py">create</a>(\*\*<a href="src/bem/types/collection_create_params.py">params</a>) -> <a href="./src/bem/types/collection_create_response.py">CollectionCreateResponse</a></code>
- <code title="get /v3/collections">client.collections.<a href="./src/bem/resources/collections/collections.py">list</a>(\*\*<a href="src/bem/types/collection_list_params.py">params</a>) -> <a href="./src/bem/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="delete /v3/collections">client.collections.<a href="./src/bem/resources/collections/collections.py">delete</a>(\*\*<a href="src/bem/types/collection_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/collections/token-count">client.collections.<a href="./src/bem/resources/collections/collections.py">count_tokens</a>(\*\*<a href="src/bem/types/collection_count_tokens_params.py">params</a>) -> <a href="./src/bem/types/collection_count_tokens_response.py">CollectionCountTokensResponse</a></code>

## Items

Types:

```python
from bem.types.collections import ItemRetrieveResponse, ItemUpdateResponse, ItemAddResponse
```

Methods:

- <code title="get /v3/collections/items">client.collections.items.<a href="./src/bem/resources/collections/items.py">retrieve</a>(\*\*<a href="src/bem/types/collections/item_retrieve_params.py">params</a>) -> <a href="./src/bem/types/collections/item_retrieve_response.py">ItemRetrieveResponse</a></code>
- <code title="put /v3/collections/items">client.collections.items.<a href="./src/bem/resources/collections/items.py">update</a>(\*\*<a href="src/bem/types/collections/item_update_params.py">params</a>) -> <a href="./src/bem/types/collections/item_update_response.py">ItemUpdateResponse</a></code>
- <code title="delete /v3/collections/items">client.collections.items.<a href="./src/bem/resources/collections/items.py">delete</a>(\*\*<a href="src/bem/types/collections/item_delete_params.py">params</a>) -> None</code>
- <code title="post /v3/collections/items">client.collections.items.<a href="./src/bem/resources/collections/items.py">add</a>(\*\*<a href="src/bem/types/collections/item_add_params.py">params</a>) -> <a href="./src/bem/types/collections/item_add_response.py">ItemAddResponse</a></code>

# Events

Types:

```python
from bem.types import EventSubmitFeedbackResponse
```

Methods:

- <code title="post /v3/events/{eventID}/feedback">client.events.<a href="./src/bem/resources/events.py">submit_feedback</a>(event_id, \*\*<a href="src/bem/types/event_submit_feedback_params.py">params</a>) -> <a href="./src/bem/types/event_submit_feedback_response.py">EventSubmitFeedbackResponse</a></code>

# WebhookSecret

Types:

```python
from bem.types import WebhookSecretCreateResponse, WebhookSecretRetrieveResponse
```

Methods:

- <code title="post /v3/webhook-secret">client.webhook_secret.<a href="./src/bem/resources/webhook_secret.py">create</a>() -> <a href="./src/bem/types/webhook_secret_create_response.py">WebhookSecretCreateResponse</a></code>
- <code title="get /v3/webhook-secret">client.webhook_secret.<a href="./src/bem/resources/webhook_secret.py">retrieve</a>() -> <a href="./src/bem/types/webhook_secret_retrieve_response.py">WebhookSecretRetrieveResponse</a></code>
- <code title="delete /v3/webhook-secret">client.webhook_secret.<a href="./src/bem/resources/webhook_secret.py">revoke</a>() -> None</code>
