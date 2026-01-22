from collections import defaultdict
from typing import Any, Callable, Type

from async_market_sim.common.abcs import ABCEventBus


class EventBus(ABCEventBus):

    def __init__(self):
        self._event_type_to_subscribers_map: dict[Type, list[Callable]] = (
            defaultdict(list))

    def subscribe(
            self,
            event_type: Type,
            handler: Callable,
            **kwargs
    ):
        self._event_type_to_subscribers_map[event_type].append(handler)

    async def publish(self, event: Any, **kwargs):
        subscribers: list[Callable] = (
            self._event_type_to_subscribers_map[type(event)]
        )
        for subscriber in subscribers:
            subscriber(event)
