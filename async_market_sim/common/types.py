from typing import Final, Literal, TypeAlias, Union

from async_market_sim.simulation.config import (
    GbmConfig, OrnsteinUhlenbeckConfig)


StochasticProcess = Literal["gbm", "ou"]

StochasticProcessConfig: TypeAlias = Union[
    GbmConfig, OrnsteinUhlenbeckConfig
]
