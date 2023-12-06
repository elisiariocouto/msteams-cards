import requests
from pydantic import BaseModel

from msteams_cards._adaptivecard import AdaptiveCard


class _TeamsWebhookMessageAttachment(BaseModel):
    contentType: str = "application/vnd.microsoft.card.adaptive"
    content: AdaptiveCard


class _TeamsWebhookMessage(BaseModel):
    type: str = "message"
    attachments: list[_TeamsWebhookMessageAttachment] = []


class TeamsConnector:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def _wrap_adaptive_card(self, payload: AdaptiveCard) -> _TeamsWebhookMessage:
        return _TeamsWebhookMessage(
            type="message",
            attachments=[_TeamsWebhookMessageAttachment(content=payload)],
        )

    def send_message(self, card: AdaptiveCard):
        j = self._wrap_adaptive_card(card).model_dump()

        response = requests.post(self.webhook_url, json=j)
        response.raise_for_status()

        return response.status_code
