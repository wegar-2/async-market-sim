import logging

COLORS = {
    'DEBUG': '\033[94m',  # Blue
    'INFO': '\033[92m',  # Green
    'WARNING': '\033[93m',  # Yellow
    'ERROR': '\033[91m',  # Red
    'CRITICAL': '\033[95m',  # Magenta
    'RESET': '\033[0m',  # Reset to default color
}


class ColoredFormatter(logging.Formatter):
    def format(self, record):
        log_color = COLORS.get(record.levelname, COLORS['RESET'])
        reset_color = COLORS['RESET']
        record.msg = f"{log_color}{record.msg}{reset_color}"
        return super().format(record)


def configure_logging():
    console_handler = logging.StreamHandler()

    formatter = ColoredFormatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(console_handler)


configure_logging()
