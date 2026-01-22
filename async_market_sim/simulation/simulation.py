import asyncio
import logging
import math
from typing import Final, Optional

import numpy as np

from async_market_sim.common.constants import SECONDS_PER_DAY
from async_market_sim.common.protocol import EventBusProtocol
from async_market_sim.common.types import (
    StochasticProcess, StochasticProcessConfig)
from async_market_sim.simulation.config import (
    GbmConfig, OrnsteinUhlenbeckConfig, TickIntensityConfig)

logger = logging.getLogger(__name__)


class MarketSimulation:

    def __init__(
            self,
            event_bus: EventBusProtocol,
            asset_name: str,
            stoch_proc: StochasticProcess,
            stoch_proc_config: StochasticProcessConfig,
            tick_freq_config: TickIntensityConfig
    ):
        self._event_bus: EventBusProtocol = event_bus
        self._asset_name: Final[str] = asset_name
        if stoch_proc == "ou":
            raise ValueError("OU stochastic process not implemented yet! ")
        self._stoch_proc: Final[StochasticProcess] = stoch_proc
        self._stoch_proc_config: Final[StochasticProcessConfig] = (
            stoch_proc_config)
        self._tick_freq_config: Final[TickIntensityConfig] = tick_freq_config

        self._sleep_time_rng: Optional = None
        if (seed := self._tick_freq_config.seed) is not None:
            self._sleep_time_rng = np.random.default_rng(seed=seed)


    async def start(self):
        logger.info(
            f"Starting simulation for asset {self._asset_name}! "
            f"Underlying stochastic process: "
            f"with parameters:"
        )

    def _get_sleep_time(self) -> float:
        if self._tick_freq_config.seed is None:
            return 1 / self._tick_freq_config.arrivals_per_sec
        else:
            return float(
                self._sleep_time_rng.exponential(
                    scale=self._tick_freq_config.arrivals_per_sec,
                    size=1
                )[0]
            )

    async def _gbm(self, config: GbmConfig):
        value: float = config.start
        value_rng = np.random.default_rng(config.seed)

        while True:
            d_time = self._get_sleep_time()
            await asyncio.sleep(d_time)
            value = (
                value +
                (
                        config.mu_daily * (d_time / SECONDS_PER_DAY)
                ) +
                (
                        config.sigma_daily *
                        math.sqrt(d_time / SECONDS_PER_DAY) *
                        float(value_rng.normal(size=1)[0])
                )
            )

    async def _ou(self, config: OrnsteinUhlenbeckConfig):
        raise ValueError("Unhandled case! ")
