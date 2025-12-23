from datetime import datetime
from decimal import Decimal

from pydantic import AliasChoices, BaseModel, Field

from tem_sdk.models.enums import MarketType, OrderStatus, OrderType, Resource

"""
Pydantic models for order-related data structures.

This module defines the `Order` model used across the SDK to represent
orders returned by or sent to the TEM API.
"""


class Order(BaseModel):
    """
    Represents an order in the Tron Energy Market.

    This Pydantic model mirrors the JSON structure used by the TEM API for
    orders. Use this model to parse, validate, and serialize order data.

    Fields:
        id (Decimal): Unique identifier of the order (no fractional part).
        type (OrderType): The order type (e.g., Public, Internal).
        market (MarketType): The market type (e.g., Open, Fast).
        origin (str): Origin address (seller/creator).
        target (str): Target address (renter/recipient).
        price (Decimal): Price per unit (in SUN, no fractional part).
        amount (Decimal): Amount of resource requested (no fractional part).
        freeze (Decimal): Amount frozen for the order (no fractional part).
        frozen (Decimal): Amount already frozen/locked (no fractional part).
        resource (Resource): Resource type (e.g., Energy, Bandwidth).
        locked (bool): Whether the order is currently locked.
        duration (Decimal): Duration of the order (seconds, no fractional part).
        payment (Decimal): Total payment for the order (in SUN, no fractional part).
        partfill (bool): Whether partial fills are allowed.
        extend (bool): Whether the order can be extended.
        maxlock (int): Maximum lock time/value (implementation-specific).
        status (OrderStatus): Status of the order (e.g., Pending, Completed).
        archive (bool): Whether the order is archived.
        created_at (datetime): Timestamp when the order was created.
        updated_at (datetime): Timestamp when the order was last updated.
    """

    id: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "id",
            "Id",
        ),
    )
    type: OrderType = Field(
        ...,
        validation_alias=AliasChoices(
            "type",
            "Type",
        ),
    )
    market: MarketType = Field(
        MarketType.Open,
        validation_alias=AliasChoices(
            "market",
            "Market",
        ),
    )
    origin: str = Field(
        ...,
        validation_alias=AliasChoices(
            "origin",
            "Origin",
        ),
    )
    target: str | list[str] = Field(
        ...,
        validation_alias=AliasChoices(
            "target",
            "Target",
        ),
    )
    price: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "price",
            "Price",
        ),
    )
    amount: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "amount",
            "Amount",
        ),
    )
    freeze: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "freeze",
            "Freeze",
        ),
    )
    frozen: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "frozen",
            "Frozen",
        ),
    )
    resource: Resource = Field(
        ...,
        validation_alias=AliasChoices(
            "resource",
            "Resource",
        ),
    )
    locked: bool = Field(
        False,
        validation_alias=AliasChoices(
            "locked",
            "Locked",
        ),
    )
    duration: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "duration",
            "Duration",
        ),
    )
    payment: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "payment",
            "Payment",
        ),
    )
    partfill: bool = Field(
        False,
        validation_alias=AliasChoices(
            "partfill",
            "Partfill",
        ),
    )
    extend: bool = Field(
        False,
        validation_alias=AliasChoices(
            "extend",
            "Extend",
        ),
    )
    maxlock: int = Field(
        -1,
        validation_alias=AliasChoices(
            "maxlock",
            "Maxlock",
        ),
    )
    status: OrderStatus = Field(
        ...,
        validation_alias=AliasChoices(
            "status",
            "Status",
        ),
    )
    archive: bool = Field(
        ...,
        validation_alias=AliasChoices(
            "archive",
            "Archive",
        ),
    )
    created_at: datetime = Field(
        ...,
        validation_alias=AliasChoices(
            "created_at",
            "createdAt",
            "CreatedAt",
        ),
    )
    updated_at: datetime = Field(
        ...,
        validation_alias=AliasChoices(
            "updated_at",
            "updatedAt",
            "UpdatedAt",
        ),
    )

    def __hash__(self) -> int:
        """
        Return a hash value for the order.

        The hash is based on the order `id` to allow usage of `Order` instances
        in sets and as dictionary keys.

        Returns:
            int: Hash of the order identifier.
        """
        return hash(self.id)

    def __eq__(self, other: object):
        """
        Compare this order with another object for equality.

        Equality is defined by comparing the `id` field when the other object
        is also an `Order` instance.

        Args:
            other (object): The object to compare against.

        Returns:
            bool: True if `other` is an `Order` with the same `id`, False otherwise.
        """
        if not isinstance(other, Order):
            return False
        return self.id == other.id

    def __ne__(self, other: object):
        """
        Determine whether this order is not equal to another object.

        This is the logical inverse of `__eq__`.

        Args:
            other (object): The object to compare against.

        Returns:
            bool: True if objects are not equal, False if they are equal.
        """
        return not self.__eq__(other)
