import logging
from typing import Optional, Any


def init_logger(logger_name: str = "") -> logging.Logger:
    """
    initialize logger 

    Args:
        logger_name (str): logger name
        log_save_path (str): save path

    Returns:
        _type_: None
    """
    logger = logging.getLogger(logger_name)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s:%(lineno)-4s:%(name)-12s: %(levelname)-8s %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.propagate = False
    return logger
