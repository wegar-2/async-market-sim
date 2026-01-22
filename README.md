# async-market-sim

![Flake8 Lint Check](https://github.com/wegar-2/async-market-sim/actions/workflows/flake8-lint.yml/badge.svg)
![Pylint Check](https://github.com/wegar-2/async-market-sim/actions/workflows/pylint.yml/badge.svg)

Various async tools for market simulations. 

### Package Structure
The subpackages are consistent with pub/sub pattern. Key remarks about 
subpackages:

* [*publisher*](./async_market_sim/publisher) - contains the class 
responsible for stochastic process simulation i.e. *MarketSimulationPublisher*
* [*subscriber*](./async_market_sim/subscriber) - contains just a most
basic subscriber that prints data on price update
* [*event_bus*](./async_market_sim/event_bus) - usable class implementing
event bus pattern


### Examples

You can run price simulation for a single asset with (this is just the 
script [here](./async_market_sim/example/one_asset_market.py)):

```python
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
```
