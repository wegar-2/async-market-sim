from typing import Final

from async_market_sim.common.types import StochasticProcess

__all__ = [
    "DEFAULT_DATETIME_FORMAT",
    "SECONDS_PER_DAY",
    "STOCH_PROC_SHORTNAME_TO_FULLNAME"
]


SECONDS_PER_DAY: Final[int] = 24 * 60 * 60


STOCH_PROC_SHORTNAME_TO_FULLNAME: Final[dict[StochasticProcess, str]] = {
    "gbm": "Geometric Brownian Motion",
    "ou": "Ornstein-Uhlenbeck (mean-reverting random walk)"
}


DEFAULT_DATETIME_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S.%f"
