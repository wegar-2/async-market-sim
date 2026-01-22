from abc import abstractmethod, ABC
from typing import Any, Callable, Type


class ABCEventBus(ABC):

    @abstractmethod
    def subscribe(
            self,
            event_type: Type,
            handler: Callable,
            **kwargs
    ):
        pass

    @abstractmethod
    async def publish(self, event: Any, **kwargs):
        pass
