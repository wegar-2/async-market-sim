from typing import Optional

from pydantic import BaseModel, field_validator


class GbmConfig(BaseModel):
    start: float = 100
    mu_daily: float = 0.005
    sigma_daily: float = 0.02
    seed: int = 654_321

    @field_validator("sigma_daily")
    def _validate_sigma_daily(self, value):
        if value <= 0:
            raise ValueError(f"Received invalid value of sigma_daily: {value}")
        return value


class OUConfig(BaseModel):
    pass


class TickIntensityConfig(BaseModel):
    """
    By default the arrival times will be randomized - generated using
    exponential dist.
    If seed is set to None - arrivals will be deterministic, with the frequency
    given by arrivals_per_sec
    """
    arrivals_per_sec: float = 1 / 5
    seed: Optional[int] = 123
