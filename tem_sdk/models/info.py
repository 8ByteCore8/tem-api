from decimal import Decimal

from pydantic import AliasChoices, BaseModel, Field


class AvailableByPriceInfo(BaseModel):
    """
    Information about available resource quantity at a specific price.

    Attributes:
        price (int): The price tier (in SUN).
        value (float): The amount of resource available at this price.
    """

    price: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "price",
            "Price",
        ),
    )
    value: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "value",
            "Value",
        ),
    )


class MarketInfo(BaseModel):
    """
    Aggregated market statistics for energy and bandwidth resources.

    Attributes:
        availableEnergy (float): Currently available amount of regular energy.
        availableFastEnergy (float): Currently available amount of fast energy.
        availableEnergyByPrice (list[AvailableByPriceInfo]): List of available energy grouped by price tiers.
        totalEnergy (int): Total energy in the market.
        nextReleaseEnergy (int): Amount of energy scheduled for next release.
        availableBandwidth (float): Currently available amount of regular bandwidth.
        availableFastBandwidth (float): Currently available amount of fast bandwidth.
        availableBandwidthByPrice (list[AvailableByPriceInfo]): List of available bandwidth grouped by price tiers.
        totalBandwidth (int): Total bandwidth in the market.
        nextReleaseBandwidth (int): Amount of bandwidth scheduled for next release.
        energyPerTrxFrozen (float): Energy amount obtained per TRX frozen.
        bandwidthPerTrxFrozen (float): Bandwidth amount obtained per TRX frozen.
        trxPerEnergyFee (float): Transaction cost (TRX) per energy fee.
        trxPerBandwidthFee (float): Transaction cost (TRX) per bandwidth fee.
    """

    available_energy: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "available_energy",
            "availableEnergy",
            "AvailableEnergy",
        ),
    )
    available_fast_energy: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "available_fast_energy",
            "availableFastEnergy",
            "AvailableFastEnergy",
        ),
    )
    available_energy_by_price: list[AvailableByPriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "available_energy_by_price",
            "availableEnergyByPrice",
            "AvailableEnergyByPrice",
        ),
    )
    total_energy: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "total_energy",
            "totalEnergy",
            "TotalEnergy",
        ),
    )
    next_release_energy: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "next_release_energy",
            "nextReleaseEnergy",
            "NextReleaseEnergy",
        ),
    )
    available_bandwidth: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "available_bandwidth",
            "availableBandwidth",
            "AvailableBandwidth",
        ),
    )
    available_fast_bandwidth: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "available_fast_bandwidth",
            "availableFastBandwidth",
            "AvailableFastBandwidth",
        ),
    )
    available_bandwidth_by_price: list[AvailableByPriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "available_bandwidth_by_price",
            "availableBandwidthByPrice",
            "AvailableBandwidthByPrice",
        ),
    )
    total_bandwidth: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "total_bandwidth",
            "totalBandwidth",
            "TotalBandwidth",
        ),
    )
    next_release_bandwidth: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "next_release_bandwidth",
            "nextReleaseBandwidth",
            "NextReleaseBandwidth",
        ),
    )
    energy_per_trx_frozen: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "energy_per_trx_frozen",
            "energyPerTrxFrozen",
            "EnergyPerTrxFrozen",
        ),
    )
    bandwidth_per_trx_frozen: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "bandwidth_per_trx_frozen",
            "bandwidthPerTrxFrozen",
            "BandwidthPerTrxFrozen",
        ),
    )
    trx_per_energy_fee: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "trx_per_energy_fee",
            "trxPerEnergyFee",
            "TrxPerEnergyFee",
        ),
    )
    trx_per_bandwidth_fee: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "trx_per_bandwidth_fee",
            "trxPerBandwidthFee",
            "TrxPerBandwidthFee",
        ),
    )


class PriceInfo(BaseModel):
    """
    Price-related constraints and suggestions for a particular queue (open/fast, energy/bandwidth).

    Attributes:
        min_duration (Decimal): Minimum duration (in seconds) allowed for orders in this price tier.
        base_price (Decimal): Base price for this tier.
        min_pool_price (Decimal): Minimum pool price threshold.
        suggested_price (Decimal): Suggested price to use for this tier.
    """

    min_duration: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_duration",
            "minDuration",
            "MinDuration",
        ),
    )
    base_price: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "base_price",
            "basePrice",
            "BasePrice",
        ),
    )
    min_pool_price: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_pool_price",
            "minPoolPrice",
            "MinPoolPrice",
        ),
    )
    suggested_price: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "suggested_price",
            "suggestedPrice",
            "SuggestedPrice",
        ),
    )


class PricesInfo(BaseModel):
    """
    Price configurations for different resource queues.

    Attributes:
        openEnergy (list[PriceInfo]): Price information for open energy queue.
        fastEnergy (list[PriceInfo]): Price information for fast energy queue.
        openBandwidth (list[PriceInfo]): Price information for open bandwidth queue.
        fastBandwidth (list[PriceInfo]): Price information for fast bandwidth queue.
    """

    open_energy: list[PriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "open_energy",
            "openEnergy",
            "OpenEnergy",
        ),
    )
    fast_energy: list[PriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "fast_energy",
            "fastEnergy",
            "FastEnergy",
        ),
    )
    open_bandwidth: list[PriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "open_bandwidth",
            "openBandwidth",
            "OpenBandwidth",
        ),
    )
    fast_bandwidth: list[PriceInfo] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "fast_bandwidth",
            "fastBandwidth",
            "FastBandwidth",
        ),
    )


class OrderInfo(BaseModel):
    """
    Order and execution-related constraints and suggested values.

    Attributes:
        minEnergy (int): Minimum energy amount allowed in an order.
        suggestedEnergy (int): Suggested energy amount for order creation.
        minBandwidth (int): Minimum bandwidth amount allowed in an order.
        suggestedBandwidth (int): Suggested bandwidth amount for order creation.
        minFillEnergy (int): Minimum energy amount required to consider an order as filled.
        minFillBandwidth (int): Minimum bandwidth amount required to consider an order as filled.
        openDurations (list[int]): Allowed durations (in seconds) for open market orders.
        openSuggestedDuration (int): Suggested duration for open market orders.
        fastDurations (list[int]): Allowed durations (in seconds) for fast market orders.
        fastSuggestedDuration (int): Suggested duration for fast market orders.
        publicTime (int): Time a public order remains available (in seconds).
        fillOrderAward (float): Reward paid for filling an order.
        cancellationFee (int): Fee charged for canceling an order (in SUN).
    """

    min_energy: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_energy",
            "minEnergy",
            "MinEnergy",
        ),
    )
    suggested_energy: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "suggested_energy",
            "suggestedEnergy",
            "SuggestedEnergy",
        ),
    )
    min_bandwidth: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_bandwidth",
            "minBandwidth",
            "MinBandwidth",
        ),
    )
    suggested_bandwidth: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "suggested_bandwidth",
            "suggestedBandwidth",
            "SuggestedBandwidth",
        ),
    )
    min_fill_energy: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_fill_energy",
            "minFillEnergy",
            "MinFillEnergy",
        ),
    )
    min_fill_bandwidth: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_fill_bandwidth",
            "minFillBandwidth",
            "MinFillBandwidth",
        ),
    )
    open_durations: list[int] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "open_durations",
            "openDurations",
            "OpenDurations",
        ),
    )
    open_suggested_duration: int = Field(
        ...,
        validation_alias=AliasChoices(
            "open_suggested_duration",
            "openSuggestedDuration",
            "OpenSuggestedDuration",
        ),
    )
    fast_durations: list[int] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "fast_durations",
            "fastDurations",
            "FastDurations",
        ),
    )
    fast_suggested_duration: int = Field(
        ...,
        validation_alias=AliasChoices(
            "fast_suggested_duration",
            "fastSuggestedDuration",
            "FastSuggestedDuration",
        ),
    )
    public_time: int = Field(
        ...,
        validation_alias=AliasChoices(
            "public_time",
            "publicTime",
            "PublicTime",
        ),
    )
    fill_order_award: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "fill_order_award",
            "fillOrderAward",
            "FillOrderAward",
        ),
    )
    cancellation_fee: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "cancellation_fee",
            "cancellationFee",
            "CancellationFee",
        ),
    )


class PoolInfo(BaseModel):
    """
    Information about liquidity pools.

    Note:
        This model currently has no defined fields but exists to represent the pool
        section in the market info payload. Fields may be added in the future.
    """

    pass


class CreditInfo(BaseModel):
    """
    Configuration and constraints for credit (deposit/withdraw) operations.

    Attributes:
        min_amount (Decimal): Minimum amount (in SUN) that can be deposited/credited.
        min_time_to_withdraw (Decimal): Minimum time (in seconds) that must pass before a withdrawal is allowed.
    """

    min_amount: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_amount",
            "minAmount",
            "MinAmount",
        ),
    )
    min_time_to_withdraw: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "min_time_to_withdraw",
            "minTimeToWithdraw",
            "MinTimeToWithdraw",
        ),
    )


class ReferralInfo(BaseModel):
    """
    Referral program information.

    Attributes:
        reward (float): Reward percentage or amount provided by the referral program.
    """

    reward: Decimal = Field(
        ...,
        validation_alias=AliasChoices(
            "reward",
            "Reward",
        ),
    )


class RewardInfo(BaseModel):
    """
    Information about reward tokens and exchange configuration.

    Attributes:
        tokenId (str): Identifier of the reward token.
        exchangeId (int): ID of the exchange configuration.
        exchangeTokenAmount (int): Token amount available for exchange.
        exchangeTrxAmount (int): TRX amount corresponding to the exchangeTokenAmount.
    """

    token_id: str = Field(
        ...,
        validation_alias=AliasChoices(
            "token_id",
            "tokenId",
            "TokenId",
        ),
    )
    exchange_id: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "exchange_id",
            "exchangeId",
            "ExchangeId",
        ),
    )
    exchange_token_amount: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "exchange_token_amount",
            "exchangeTokenAmount",
            "ExchangeTokenAmount",
        ),
    )
    exchange_trx_amount: Decimal = Field(
        ...,
        decimal_places=0,
        validation_alias=AliasChoices(
            "exchange_trx_amount",
            "exchangeTrxAmount",
            "ExchangeTrxAmount",
        ),
    )


class TronInfo(BaseModel):
    """
    Tron network related endpoints and nodes.

    Attributes:
        node (str): RPC node URL used by the market backend.
        tronscan (str): Tronscan URL.
        tronscan_api (str): Tronscan API URL.
    """

    node: str = Field(
        ...,
        validation_alias=AliasChoices(
            "node",
            "Node",
        ),
    )
    tronscan: str = Field(
        ...,
        validation_alias=AliasChoices(
            "tronscan",
            "Tronscan",
        ),
    )
    tronscan_api: str = Field(
        ...,
        validation_alias=AliasChoices(
            "tronscan_api",
            "tronscanApi",
            "TronscanApi",
        ),
    )


class Info(BaseModel):
    """
    Root market information model returned by the `/info` endpoint.

    Attributes:
        address (str): Market/tron address associated with the market.
        market (MarketInfo): Aggregated market statistics for energy and bandwidth.
        price (PricesInfo): Price configurations and suggestions for queues.
        order (OrderInfo): Order-related constraints and suggestions.
        pool (PoolInfo): Liquidity pool information.
        credit (CreditInfo): Credit/deposit configuration and constraints.
        referral (ReferralInfo): Referral program configuration.
        reward (RewardInfo): Reward token and exchange configuration.
        tron (TronInfo): Tron network connection information used by the market.
    """

    address: str = Field(
        ...,
        validation_alias=AliasChoices(
            "address",
            "Address",
        ),
    )
    market: MarketInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "market",
            "Market",
        ),
    )
    price: PricesInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "price",
            "Price",
        ),
    )
    order: OrderInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "order",
            "Order",
        ),
    )
    pool: PoolInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "pool",
            "Pool",
        ),
    )
    credit: CreditInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "credit",
            "Credit",
        ),
    )
    referral: ReferralInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "referral",
            "Referral",
        ),
    )
    reward: RewardInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "reward",
            "Reward",
        ),
    )
    tron: TronInfo = Field(
        ...,
        validation_alias=AliasChoices(
            "tron",
            "Tron",
        ),
    )
