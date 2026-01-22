from typing import Literal, TypeAlias, Union

from async_market_sim.publisher.config import (
    GbmConfig, OUConfig)


StochasticProcess = Literal["gbm", "ou"]

StochasticProcessConfig: TypeAlias = Union[
    GbmConfig, OUConfig
]
