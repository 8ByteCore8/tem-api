from collections.abc import Coroutine
from decimal import ROUND_DOWN, ROUND_UP, Decimal
from types import TracebackType
from typing import Any

from httpx import AsyncClient, HTTPError

from tem_sdk.models.enums import MarketType, OrderStatus, Resource
from tem_sdk.models.info import Info
from tem_sdk.models.orders import Order
from tem_sdk.models.parts import SignedMS
from tem_sdk.models.requests import (
    BalanceDepositRequest,
    BalanceWithdrawRequest,
    CancelOrderRequest,
    CreateOrderRequest,
    FillOrderRequest,
)
from tem_sdk.models.responses import (
    CreateOrderResponse,
    GetBalanceResponse,
    GetMarketInfoResponse,
    GetOrderResponse,
    GetOrdersResponse,
)


class TemClient:
    __client__: AsyncClient

    async def __aenter__(self) -> "TemClient":
        await self.__client__.__aenter__()
        return self

    @staticmethod
    def calculate_order_payment(
        price: Decimal | int, amount: Decimal | int, duration: Decimal | int
    ) -> Decimal:
        """
        Calculate the total payment for an order based on price, amount, and duration.

        Args:
            price (int): The price per unit of resource.
            amount (int): The amount of resource being ordered.
            duration (int): The duration for which the resource is being ordered.

        Returns:
            int: The total payment required for the order.
        """
        day = Decimal(86400)
        price = Decimal(price)
        amount = Decimal(amount)
        duration = Decimal(duration) + day if duration < day else Decimal(duration)
        return ((price * amount * duration) / day).quantize(
            Decimal("1."), rounding=ROUND_UP
        )

    @staticmethod
    def convert_sun_to_trx(sun: Decimal | int) -> Decimal:
        return Decimal(sun) / Decimal(1_000_000)

    @staticmethod
    def convert_trx_to_sun(trx: Decimal | int | float) -> Decimal:
        return (Decimal(trx) * Decimal(1_000_000)).quantize(
            Decimal("1."), rounding=ROUND_DOWN
        )

    def __aexit__(
        self,
        exc_type: type[BaseException] | None = None,
        exc_value: BaseException | None = None,
        traceback: TracebackType | None = None,
    ) -> Coroutine[Any, Any, None]:
        return self.__client__.__aexit__(
            exc_type,
            exc_value,
            traceback,
        )

    def __init__(
        self,
        *,
        base_url: str = "https://api.tronenergy.market/",
    ) -> None:
        self.__client__ = AsyncClient(base_url=base_url)

    async def check_status(self):
        try:
            response = await self.__client__.get("/status")
            return response.is_success
        except HTTPError:
            return False

    async def get_market_info(self) -> Info:
        """Get market info"""
        response = await self.__client__.get("/info")
        response.raise_for_status()
        return Info(
            **(GetMarketInfoResponse.model_validate_json(response.content)).model_dump()
        )

    async def get_balance(self, account_address: str) -> Decimal:
        """Get account balance in SUN"""
        response = await self.__client__.get(
            "/credit", params={"address": account_address}
        )
        response.raise_for_status()
        return GetBalanceResponse.model_validate_json(response.content).value

    async def deposit_balance(
        self,
        account_address: str,
        signed_tx: str,
    ) -> None:
        response = await self.__client__.post(
            url="/credit/deposit",
            json=BalanceDepositRequest(
                address=account_address,
                signed_tx=signed_tx,
            ).model_dump(mode="json", exclude_none=True, exclude_unset=True),
        )
        response.raise_for_status()

    async def withdraw_balance(
        self,
        account_address: str,
        signed_ms: SignedMS,
        amount: int | Decimal | None = None,
    ) -> None:
        response = await self.__client__.post(
            url="/credit/withdraw",
            json=BalanceWithdrawRequest(
                address=account_address,
                amount=Decimal(amount) if amount else None,
                signed_ms=signed_ms,
            ).model_dump(mode="json", exclude_none=True, exclude_unset=True),
        )
        response.raise_for_status()

    async def get_orders(
        self,
        *,
        skip: int = 0,
        take: int = 1000,
        status: OrderStatus | None = None,
        account_address: str | None = None,
    ) -> list[Order]:
        params: dict[str, str] = {
            "skip": str(skip),
            "limit": str(take),
        }
        if status is not None:
            params["status"] = status.value
        if account_address is not None:
            params["address"] = account_address

        response = await self.__client__.get("/order/list", params=params)
        response.raise_for_status()
        return GetOrdersResponse.model_validate_json(response.content).list

    async def get_all_orders(
        self,
        *,
        status: OrderStatus | None = None,
        account_address: str | None = None,
    ) -> list[Order]:
        orders = set()
        skip = 0
        take = 1000

        while True:
            chunk = await self.get_orders(
                skip=skip,
                take=take,
                status=status,
                account_address=account_address,
            )
            orders.update(chunk)
            if len(chunk) < take:
                break
            skip += take

        return list(orders)

    async def get_order(self, order_id: int) -> Order:
        params = {
            "id": str(order_id),
        }

        response = await self.__client__.get("/order/info", params=params)
        response.raise_for_status()
        return Order(
            **(GetOrderResponse.model_validate_json(response.content).model_dump())
        )

    async def create_order(
        self,
        market: MarketType,
        account_address: str,
        target: str | list[str],
        resource: Resource,
        amount: Decimal | int,
        duration: Decimal | int,
        price: Decimal | int,
        partfill: bool = True,
        api_key: str | None = None,
        signed_ms: SignedMS | None = None,
        signed_tx: str | None = None,
    ) -> int:
        response = await self.__client__.post(
            "/order/new",
            json=CreateOrderRequest(
                market=market,
                address=account_address,
                target=target,
                payment=self.calculate_order_payment(price, amount, duration),
                resource=resource,
                price=Decimal(price),
                duration=Decimal(duration),
                partfill=partfill,
                api_key=api_key,
                signed_ms=signed_ms,
                signed_tx=signed_tx,
            ).model_dump(mode="json"),
        )
        response.raise_for_status()
        return CreateOrderResponse.model_validate_json(response.content).order

    async def fill_order(
        self,
        order_id: int,
        account_address: str,
        signed_tx: str,
        target: str | None = None,
    ) -> None:
        response = await self.__client__.post(
            "/order/fill",
            json=FillOrderRequest(
                id=order_id,
                address=account_address,
                signed_tx=signed_tx,
                origin_address=target,
            ).model_dump(mode="json", exclude_none=True, exclude_unset=True),
        )
        response.raise_for_status()

    async def cancel_order(
        self, order_id: int, account_address: str, signed_ms: SignedMS
    ) -> None:
        response = await self.__client__.post(
            "/order/cancel",
            json=CancelOrderRequest(
                order=order_id,
                address=account_address,
                signed_ms=signed_ms,
            ).model_dump(mode="json", exclude_none=True, exclude_unset=True),
        )
        response.raise_for_status()

    # No info about this method
    # async def reclaim_order(session: ClientSession, payload: CancelOrder):
    #     await session.post("/order/reclaim", json=payload.model_dump(mode="json"))
