from typing import Callable, Protocol, Type


class EventBus(Protocol):

    def subscribe(self, event_type: Type, handler: Callable, **kwargs):
        pass

    async def publish(self, event, **kwargs):
        pass
