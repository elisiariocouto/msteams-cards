from enum import Enum


class TextSize(str, Enum):
    SMALL = "small"
    DEFAULT = "default"
    MEDIUM = "medium"
    LARGE = "large"
    EXTRA_LARGE = "extraLarge"
