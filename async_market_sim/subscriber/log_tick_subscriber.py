import logging

from async_market_sim.publisher.event import PriceTickEvent

logger = logging.getLogger(__name__)


class LogTickSubscriber:

    @staticmethod
    def log(pt_event: PriceTickEvent):
        logger.info(str(pt_event))
