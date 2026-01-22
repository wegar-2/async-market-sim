from typing import Final

from async_market_sim.common.types import StochasticProcess


SECONDS_PER_DAY: Final[int] = 24 * 60 * 60


STOCH_PROC_SHORTNAME_TO_FULLNAME: Final[dict[StochasticProcess, str]] = {
    "gbm": "Geometric Brownian Motion",
    "ou": "Ornstein-Uhlenbeck (mean-reverting random walk)"
}
