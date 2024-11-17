from enum import IntEnum, StrEnum

from pydantic import Field


class Resource(IntEnum):
    Energy = 0
    Bandwidth = 1


class OrderStatus(StrEnum):
    Pending = "Pending"
    Completed = "Completed"


class OrderType(StrEnum):
    Public = "Public"


class MarketType(StrEnum):
    Open = "Open"
    Fast = "Fast"


class SignedMS:
    message: str = Field(..., pattern=r"^te_\w+$")
    signature: str = Field(...)
