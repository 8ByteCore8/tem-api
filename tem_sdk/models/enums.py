from enum import IntEnum, StrEnum


class Resource(IntEnum):
    Energy = 0
    Bandwidth = 1


class OrderStatus(StrEnum):
    Pending = "Pending"
    Completed = "Completed"


class OrderType(StrEnum):
    Public = "Public"
    Internal = "Internal"


class MarketType(StrEnum):
    Open = "Open"
    Fast = "Fast"
