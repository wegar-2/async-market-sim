import asyncio

from async_market_sim.event_bus.event_bus import EventBus
from async_market_sim.publisher.market_simulation_publisher import (
    MarketSimulationPublisher)
from async_market_sim.publisher.config import GbmConfig, TickIntensityConfig
from async_market_sim.subscriber.log_tick_subscriber import LogTickSubscriber
from async_market_sim.publisher.event import PriceTickEvent


async def one_asset_market():

    bus = EventBus()
    xyz_publisher = MarketSimulationPublisher(
        event_bus=bus,
        asset_name="XYZ",
        stoch_proc="gbm",
        stoch_proc_config=GbmConfig(),
        tick_freq_config=TickIntensityConfig()
    )
    log_tick_subscriber = LogTickSubscriber()
    bus.subscribe(
        event_type=PriceTickEvent,
        handler=log_tick_subscriber.log
    )

    await xyz_publisher.start()


if __name__ == '__main__':
    asyncio.run(one_asset_market())
