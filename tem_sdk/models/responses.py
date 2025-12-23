from decimal import Decimal

from pydantic import BaseModel, Field

from tem_sdk.models.info import Info
from tem_sdk.models.orders import Order


class GetBalanceResponse(BaseModel):
    value: Decimal = Field(..., decimal_places=0)


class GetMarketInfoResponse(Info):
    pass


class GetOrdersResponse(BaseModel):
    list: "list[Order]" = Field(default_factory=list)
    total: int = Field(...)


class GetOrderResponse(Order):
    pass


class CreateOrderResponse(BaseModel):
    order: int = Field(...)
