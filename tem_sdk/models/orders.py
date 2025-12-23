from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, Field

from tem_sdk.models.enums import MarketType, OrderStatus, OrderType, Resource


class Order(BaseModel):
    id: Decimal = Field(..., decimal_places=0)
    type: OrderType = Field(...)
    market: MarketType = Field(...)
    origin: str = Field(...)
    target: str = Field(...)
    price: Decimal = Field(..., decimal_places=0)
    amount: Decimal = Field(..., decimal_places=0)
    freeze: Decimal = Field(..., decimal_places=0)
    frozen: Decimal = Field(..., decimal_places=0)
    resource: Resource = Field(...)
    locked: bool = Field(...)
    duration: Decimal = Field(..., decimal_places=0)
    payment: Decimal = Field(..., decimal_places=0)
    partfill: bool = Field(...)
    extend: bool = Field(...)
    maxlock: int = Field(...)
    status: OrderStatus = Field(...)
    archive: bool = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime = Field(...)

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object):
        if not isinstance(other, Order):
            return False
        return self.id == other.id

    def __ne__(self, other: object):
        return not self.__eq__(other)
