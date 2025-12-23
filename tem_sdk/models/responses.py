from decimal import Decimal

from pydantic import AliasChoices, BaseModel, Field

from tem_sdk.models.info import Info
from tem_sdk.models.orders import Order


class GetBalanceResponse(BaseModel):
    """
    Response model for retrieving account balance.

    Fields:
        value (Decimal): Account balance in SUN (smallest TRX unit). This is an integer
            represented as a Decimal with zero decimal places.
    """

    value: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "value",
            "Value",
        ),
    )


class GetMarketInfoResponse(Info):
    """
    Response model for retrieving market information.

    This model extends `Info` and represents the full market information payload
    returned by the `/info` endpoint.

    Fields (inherited from `Info`):
        address (str): The market contract or service address.
        market (MarketInfo): Aggregated market metrics such as available energy/bandwidth,
            pools and release schedules.
        price (PricesInfo): Price-related configuration for open and fast markets and resources.
        order (OrderInfo): Order-related constraints and recommended values (limits, durations, fees).
        pool (PoolInfo): Pool-related information (may be empty or expand in the future).
        credit (CreditInfo): Information about credit-related constraints (min amount, withdrawal delay).
        referral (ReferralInfo): Referral program related configuration (reward rates).
        reward (RewardInfo): Reward token and exchange information.
        tron (TronInfo): Information about Tron network endpoints used by the service.
    """

    pass


class GetOrdersResponse(BaseModel):
    """
    Response model for retrieving a list of orders.

    Fields:
        orders (list[Order]): A list of `Order` instances representing orders returned
            by the `/order/list` endpoint. Defaults to an empty list when no orders are present.
        total (int): Total number of orders available for the given query (useful for pagination).
    """

    orders: list[Order] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "list",
            "List",
            "items",
            "Items",
            "orders",
            "Orders",
        ),
    )
    total: int = Field(
        ...,
        validation_alias=AliasChoices(
            "total",
            "Total",
        ),
    )


class GetOrderResponse(Order):
    """
    Response model for retrieving a single order's details.

    This model extends `Order` and contains the full set of order attributes returned
    by the `/order/info` endpoint.

    Fields (inherited from `Order`):
        id (Decimal): Unique order identifier (integer represented as Decimal).
        type (OrderType): Order type (e.g. Public, Internal).
        market (MarketType): Market type (e.g. Open, Fast).
        origin (str): Origin address (creator) of the order.
        target (str): Target address or identifier for the order.
        price (Decimal): Price per unit for the order (in SUN, integer Decimal).
        amount (Decimal): Amount of resource to be rented (integer Decimal).
        freeze (Decimal): Amount frozen for the order (integer Decimal).
        frozen (Decimal): Amount already frozen/consumed from the order (integer Decimal).
        resource (Resource): Resource type (Energy or Bandwidth).
        locked (bool): Whether the order is locked.
        duration (Decimal): Duration of the rent (integer Decimal, seconds).
        payment (Decimal): Total payment amount for the order (in SUN, integer Decimal).
        partfill (bool): Whether partial fills are allowed.
        extend (bool): Whether the order supports extension.
        maxlock (int): Maximum lock count or limit related to the order.
        status (OrderStatus): Current order status (e.g. Pending, Completed).
        archive (bool): Whether the order is archived.
        created_at (datetime): Creation timestamp of the order.
        updated_at (datetime): Last update timestamp of the order.
    """

    pass


class CreateOrderResponse(BaseModel):
    """
    Response model returned after successful order creation.

    Fields:
        order (int): The identifier of the newly created order.
    """

    order_id: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "order",
            "Order",
            "order_id",
            "orderId",
            "OrderId",
        ),
    )
