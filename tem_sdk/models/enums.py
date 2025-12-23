"""
Enum definitions used across tem_sdk models.

This module defines enums that represent resources, order status/type and market
types used by the Tron Energy Market API models. These enums are intentionally
simple, providing semantic names for values returned by or sent to the API.
"""

from enum import IntEnum, StrEnum


class Resource(IntEnum):
    """
    Resource types used in orders.

    This enum represents the discrete blockchain resources that can be rented or
    traded via the market API (for example, energy and bandwidth). Use these
    values when constructing requests or interpreting order/resource fields in
    API responses.
    """

    Energy = 0
    Bandwidth = 1


class OrderStatus(StrEnum):
    """
    Order lifecycle status values.

    These string-backed status names are used to indicate the current state of
    an order in the market (for example, whether it is pending or completed).
    """

    Pending = "Pending"
    Completed = "Completed"
    Cancelled = "Cancelled"


class OrderType(StrEnum):
    """
    Order origin/type classification.

    Indicates whether an order is a public market order or an internal/system
    order. Use these values to distinguish behavior or visibility when handling
    orders.
    """

    Public = "Public"
    Internal = "Internal"


class MarketType(StrEnum):
    """
    Market pricing/processing mode.

    Represents market modes the API supports (for example 'Open' vs 'Fast'),
    which typically affect pricing and how orders are matched/processed.
    """

    Open = "Open"
    Fast = "Fast"
