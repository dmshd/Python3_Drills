"""
This script shows how to use requests to get the list of protocols from the
defiLlama API and handle exceptions.
"""

import logging

import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

try:
    response = requests.get("https://api.llama.fi/protocols")
except ConnectionError as e:
    logger.error(f"(Connection) Could not get the list of protocols from the defiLlama API : {e}")
except HTTPError as e:
    logger.error(f"(HTTP) Could not get the list of protocols from the defiLlama API : {e}")
except Timeout as e:
    logger.error(f"(Timeout) Could not get the list of protocols from the defiLlama API : {e}")
