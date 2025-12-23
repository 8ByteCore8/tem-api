from pydantic import BaseModel, Field


class AvailableByPriceInfo(BaseModel):
    price: int = Field(...)
    value: float = Field(...)


class MarketInfo(BaseModel):
    availableEnergy: float = Field(...)
    availableFastEnergy: float = Field(...)
    availableEnergyByPrice: list[AvailableByPriceInfo] = Field(default_factory=list)
    totalEnergy: int = Field(...)
    nextReleaseEnergy: int = Field(...)
    availableBandwidth: float = Field(...)
    availableFastBandwidth: float = Field(...)
    availableBandwidthByPrice: list[AvailableByPriceInfo] = Field(default_factory=list)
    totalBandwidth: int = Field(...)
    nextReleaseBandwidth: int = Field(...)
    energyPerTrxFrozen: float = Field(...)
    bandwidthPerTrxFrozen: float = Field(...)
    trxPerEnergyFee: float = Field(...)
    trxPerBandwidthFee: float = Field(...)


class PriceInfo(BaseModel):
    minDuration: int = Field(...)
    basePrice: int = Field(...)
    minPoolPrice: int = Field(...)
    suggestedPrice: int = Field(...)


class PricesInfo(BaseModel):
    openEnergy: list[PriceInfo] = Field(default_factory=list)
    fastEnergy: list[PriceInfo] = Field(default_factory=list)
    openBandwidth: list[PriceInfo] = Field(default_factory=list)
    fastBandwidth: list[PriceInfo] = Field(default_factory=list)


class OrderInfo(BaseModel):
    minEnergy: int = Field(...)
    suggestedEnergy: int = Field(...)
    minBandwidth: int = Field(...)
    suggestedBandwidth: int = Field(...)
    minFillEnergy: int = Field(...)
    minFillBandwidth: int = Field(...)
    openDurations: list[int] = Field(default_factory=list)
    openSuggestedDuration: int = Field(...)
    fastDurations: list[int] = Field(default_factory=list)
    fastSuggestedDuration: int = Field(...)
    publicTime: int = Field(...)
    fillOrderAward: float = Field(...)
    cancellationFee: int = Field(...)


class PoolInfo(BaseModel):
    pass


class CreditInfo(BaseModel):
    minAmount: int = Field(...)
    minTimeToWithdraw: int = Field(...)


class ReferralInfo(BaseModel):
    reward: float = Field(...)


class RewardInfo(BaseModel):
    tokenId: str = Field(...)
    exchangeId: int = Field(...)
    exchangeTokenAmount: int = Field(...)
    exchangeTrxAmount: int = Field(...)


class TronInfo(BaseModel):
    node: str = Field(...)
    tronscan: str = Field(...)
    tronscanApi: str = Field(...)


class Info(BaseModel):
    address: str = Field(...)
    market: MarketInfo = Field(...)
    price: PricesInfo = Field(...)
    order: OrderInfo = Field(...)
    pool: PoolInfo = Field(...)
    credit: CreditInfo = Field(...)
    referral: ReferralInfo = Field(...)
    reward: RewardInfo = Field(...)
    tron: TronInfo = Field(...)
