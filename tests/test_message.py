import os

import pytest

from msteams_cards import AdaptiveCard, TeamsConnector
from msteams_cards.elements import TextBlock


def test_send():
    url = os.getenv("TEAMS_WEBHOOK_URL")
    if not url:
        pytest.fail("TEAMS_WEBHOOK_URL environment variable not set")
    connector = TeamsConnector(url)
    card = AdaptiveCard(body=[TextBlock(text="Hello, world!")])
    connector.send_message(card)
