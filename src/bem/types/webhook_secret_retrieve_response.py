# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["WebhookSecretRetrieveResponse"]


class WebhookSecretRetrieveResponse(BaseModel):
    """
    Webhook signing secret used to verify `bem-signature` headers on delivered webhooks.
    """

    secret: str
    """The signing secret value.

    Store this securely — it is shown in full only on generation.
    """
