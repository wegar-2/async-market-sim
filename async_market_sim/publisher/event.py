from datetime import datetime

from pydantic import BaseModel

from async_market_sim.common.constants import DEFAULT_DATETIME_FORMAT


class PriceTickEvent(BaseModel):
    asset_name: str
    price: float
    timestamp: datetime

    def __str__(self):
        return (f"Price tick on asset {self.asset_name} "
                f"at {self.timestamp.strftime(DEFAULT_DATETIME_FORMAT)}, "
                f"new price: {self.price:_.10f}")
