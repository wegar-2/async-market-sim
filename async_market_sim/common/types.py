from typing import Literal, TypeAlias, Union

from async_market_sim.simulation.config import (
    GbmConfig, OrnsteinUhlenbeckConfig)


StochasticProcess = Literal["gbm", "ornstein-uhlenbeck"]

StochasticProcessConfig: TypeAlias = Union[
    GbmConfig, OrnsteinUhlenbeckConfig
]
