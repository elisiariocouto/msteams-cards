from pydantic import BaseModel, Field

from msteams_cards.styles import TextSize


class TextBlock(BaseModel):
    type: str = "TextBlock"
    text: str
    wrap: bool = True
    size: TextSize = TextSize.DEFAULT
    subtle: bool = Field(default=False, alias="isSubtle")
