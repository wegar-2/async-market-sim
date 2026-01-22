from collections import defaultdict
from typing import Callable, Type


class EventBus:

    def __init__(self):
        self._event_type_to_subscribers_map: dict[Type, Callable] = (
            defaultdict())

    def subscribe(
            self,
            event_type: Type,
            handler: Callable
    ):
        self._event_type_to_subscribers_map[event_type].append(handler)

    async def publish(self):
        pass
