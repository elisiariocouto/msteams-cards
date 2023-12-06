from typing import Literal

from pydantic import BaseModel


class Container(BaseModel):
    type: str = "Container"


class Column(BaseModel):
    type: str = "Column"
    width: Literal["auto", "stretch"] = "auto"


class ColumnSet(BaseModel):
    type: str = "ColumnSet"
    columns: list[Column] = []
