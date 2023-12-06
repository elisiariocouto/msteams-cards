# 📮 msteams-cards

> ⚠️ This project is under development, and is not yet ready for production use.

Send [Adaptive Cards](https://adaptivecards.io) to Microsoft Teams using webhooks.

## Usage

You can use the `Connector` class to send adaptive cards to Microsoft Teams. Here's a basic example:

```python
from msteams_cards import AdaptiveCard, TeamsConnector
from msteams_cards.elements import TextBlock

connector = TeamsConnector("https://outlook.office.com/webhook/...")
card = AdaptiveCard(body=[TextBlock(text="Hello, world!")])
connector.send_message(card)
```

Replace `"https://outlook.office.com/webhook/..."` with your actual Teams webhook URL.
