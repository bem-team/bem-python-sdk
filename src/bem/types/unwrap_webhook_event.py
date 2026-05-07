# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .error_event import ErrorEvent
from .join_webhook_event import JoinWebhookEvent
from .send_webhook_event import SendWebhookEvent
from .parse_webhook_event import ParseWebhookEvent
from .enrich_webhook_event import EnrichWebhookEvent
from .extract_webhook_event import ExtractWebhookEvent
from .classify_webhook_event import ClassifyWebhookEvent
from .evaluation_webhook_event import EvaluationWebhookEvent
from .split_item_webhook_event import SplitItemWebhookEvent
from .payload_shaping_webhook_event import PayloadShapingWebhookEvent
from .split_collection_webhook_event import SplitCollectionWebhookEvent
from .collection_processing_webhook_event import CollectionProcessingWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        ExtractWebhookEvent,
        ClassifyWebhookEvent,
        ParseWebhookEvent,
        SplitCollectionWebhookEvent,
        SplitItemWebhookEvent,
        JoinWebhookEvent,
        EnrichWebhookEvent,
        PayloadShapingWebhookEvent,
        SendWebhookEvent,
        EvaluationWebhookEvent,
        CollectionProcessingWebhookEvent,
        ErrorEvent,
    ],
    PropertyInfo(discriminator="event_type"),
]
