import asyncio
from datetime import datetime
import logging
import math

import numpy as np

from async_market_sim.common.constants import SECONDS_PER_DAY
from async_market_sim.simulation.config import GbmSimulationConfig
from async_market_sim.common.protocol import EventBus

DataQueue: asyncio.Queue = asyncio.Queue()

logger = logging.getLogger(__name__)


class MarketSimulation:

    def __init__(self, event_bus: EventBus):
        self._event_bus: EventBus = event_bus

    async def start(self):
        pass

async def gbm_simulation(config: GbmSimulationConfig):

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
