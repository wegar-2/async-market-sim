from pydantic import BaseModel


class PriceTickEvent(BaseModel):
    asset_name: str
    price: float
    timestamp: str
