"""
This script shows how to configure logging.
"""

import logging


def configure_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logger = logging.getLogger(__name__)
    return logger
