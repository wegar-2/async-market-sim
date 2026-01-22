from pydantic import BaseModel, field_validator


class GbmSimulationConfig(BaseModel):
    start_value: float = 100
    mu_daily: float = 0.005
    sigma_daily: float = 0.02
    value_seed: int = 654_321
    lambda_arrival_time: float = 5
    arrival_time_seed: int = 123_456

    @field_validator("sigma_daily")
    def _validate_sigma_daily(self, value):
        if value <= 0:
            raise ValueError(f"Received invalid value of sigma_daily: {value}")
        return value


class OrnsteinUhlenbeckConfig(BaseModel):
    pass
