import asyncio
import logging
import math
from typing import Final

import numpy as np

from async_market_sim.common.constants import SECONDS_PER_DAY
from async_market_sim.common.protocol import EventBus
from async_market_sim.common.types import (
    StochasticProcess, StochasticProcessConfig)
from async_market_sim.simulation.config import (
    GbmConfig, OrnsteinUhlenbeckConfig)

logger = logging.getLogger(__name__)


class MarketSimulation:

    def __init__(
            self,
            event_bus: EventBus,
            asset_name: str,
            stoch_proc: StochasticProcess,
            stoch_proc_config: StochasticProcessConfig
    ):
        self._event_bus: EventBus = event_bus
        self._asset_name: Final[str] = asset_name
        self._stoch_proc: Final[StochasticProcess] = stoch_proc
        self._stoch_proc_config: Final[StochasticProcessConfig] = (
            stoch_proc_config)

    async def start(self):
        logger.info(f"")
        pass

    async def _gbm(self, config: GbmConfig):

        value: float = config.start_value

        value_rng = np.random.default_rng(config.value_seed)
        arrival_time_rng = np.random.default_rng(config.arrival_time_seed)

        while True:

            d_time = float(
                arrival_time_rng.exponential(
                    scale=config.lambda_arrival_time, size=1
                )[0]
            )
            await asyncio.sleep(d_time)

            value = (
                value +
                config.mu_daily * (d_time / SECONDS_PER_DAY) +
                config.sigma_daily *
                math.sqrt(d_time / SECONDS_PER_DAY) *
                float(value_rng.normal(size=1)[0])
            )

    async def _ornstein_uhlenbeck(self):
        pass
