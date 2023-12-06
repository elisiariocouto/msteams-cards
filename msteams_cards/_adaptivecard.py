from pydantic import BaseModel, Field


class AdaptiveCard(BaseModel):
    type: str = "AdaptiveCard"
    version: str = "1.5"
    body: list = []
    actions: list = []
    schema: str = Field(
        default="http://adaptivecards.io/schemas/adaptive-card.json", alias="$schema"
    )

    def add_element(self, element):
        self.body.append(element)

    def json_dump(self) -> str:
        return self.model_dump_json()

    def dump(self) -> dict:
        return self.model_dump()
