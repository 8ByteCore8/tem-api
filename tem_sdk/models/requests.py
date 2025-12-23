from decimal import Decimal

from pydantic import BaseModel, Field, computed_field, model_validator

from tem_sdk.models.enums import MarketType, Resource
from tem_sdk.models.parts import SignedMS


class BalanceDepositRequest(BaseModel):
    address: str = Field(...)
    signed_tx: str = Field(...)


class BalanceWithdrawRequest(BaseModel):
    address: str = Field(...)
    signed_ms: SignedMS = Field(...)
    amount: Decimal | None = Field(..., decimal_places=0)


class CreateOrderRequest(BaseModel):
    market: MarketType = Field(...)
    """Market type"""
    address: str = Field(...)
    """Sender of TRX"""
    target: str | list[str] = Field(...)
    """Rent target"""
    payment: Decimal = Field(..., decimal_places=0)
    """Payment in sun"""
    resource: Resource = Field(...)
    """Rented resource"""
    duration: Decimal = Field(..., decimal_places=0)
    """Rent duration"""
    price: Decimal = Field(..., decimal_places=0)
    """Rent price"""
    partfill: bool = Field(...)
    """Allow particular order execution"""
    api_key: str | None = Field(None)
    """User API key"""
    signed_ms: SignedMS | None = Field(None)
    """Sing order"""
    signed_tx: str | None = Field(None)
    """Sing TRX transaction"""

    @computed_field()
    @property
    def bulk(self) -> bool:
        """Order is bulk"""
        return isinstance(self.target, list)

    @model_validator(mode="after")
    def validate_targets(self) -> "CreateOrderRequest":
        if isinstance(self.target, str):
            return self

        if isinstance(self.target, list):
            if len(self.target) == 1:
                self.target = self.target[0]
                return self

            if len(self.target) > 0:
                return self

            raise ValueError("Target list cannot be empty")

        raise ValueError("Invalid target type")

    @model_validator(mode="after")
    def validate_signature(self) -> "CreateOrderRequest":
        if self.api_key:
            self.signed_tx = None
            self.signed_ms = None
            return self

        if self.signed_tx and self.signed_ms:
            self.api_key = None
            return self

        raise ValueError("Invalid signature")


class FillOrderRequest(BaseModel):
    id: int = Field(...)
    origin_address: str | None = Field(None)
    address: str = Field(...)
    signed_tx: str = Field(...)


class CancelOrderRequest(BaseModel):
    order: int = Field(...)
    address: str = Field(...)
    signed_ms: SignedMS = Field(...)


# class ReclimeOrderRequest(BaseModel):
#    pass
