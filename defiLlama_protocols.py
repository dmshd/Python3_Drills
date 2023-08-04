"""
This script is used to get the list of protocols from the defiLlama API
"""

import logging
import os

from requests.exceptions import ConnectionError, HTTPError, Timeout

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

import hashlib
import json

import requests

# Open the JSON file locally stored if it exists
if os.path.exists("defiLlama_protocols.json"):
    with open("defiLlama_protocols.json", "r") as f:
        protocols = json.load(f)
        f.close()
        logger.info("Successfully loaded the list of protocols from the defiLlama API")
else:
    # Try to get the list of protocols from the defiLlama API
    try:
        response = requests.get("https://api.llama.fi/protocols")
    except ConnectionError as e:
        logger.error(f"(Connection) Could not get the list of protocols from the defiLlama API : {e}")
    except HTTPError as e:
        logger.error(f"(HTTP) Could not get the list of protocols from the defiLlama API : {e}")
    except Timeout as e:
        logger.error(f"(Timeout) Could not get the list of protocols from the defiLlama API : {e}")

# List all the protocols names
for protocol in protocols:
    print(protocol["name"])


# # Store the response in a JSON file if the file is not already present
# if not os.path.exists("defiLlama_protocols.json"):
#     with open("defiLlama_protocols.json", "+w") as f:
#         json.dump(response.json(), f)
#         f.close()
#         logger.info("Successfully stored the list of protocols from the defiLlama API in a JSON file")
# else:
#     logger.info("The list of protocols from the defiLlama API is already stored in a JSON file")
#     # Check if the JSON file is up to date comparing hashes
#     # Compute the hash value of the response
#     response_hash = hashlib.sha256(response.content).hexdigest()
#     # Compute the hash value of the local JSON file
#     with open("defiLlama_protocols.json", "r") as f:
#         local_file_hash = hashlib.sha256(f.read().encode("utf-8")).hexdigest()
#         breakpoint()
#         f.close()
#     # Compare the two hash values
#     if response_hash == local_file_hash:
#         logger.info("The list of protocols from the defiLlama API is up to date")
#     else:
#         logger.info("The list of protocols from the defiLlama API is not up to date")
#         # Update the JSON file
#         with open("defiLlama_protocols.json", "w") as f:
#             json.dump(response.json(), f)
#             f.close()
#             logger.info("Successfully updated the list of protocols from the defiLlama API in a JSON file")


# # Store response.content bytes in a binary file
# with open("defiLlama_protocols.bin", "wb") as f:
#     f.write(response.content)
#     # Compute hash value of the response.content and store it in a file
#     with open("defiLlama_protocols_hash.txt", "w") as f_hash:
#         f_hash.write(hashlib.sha256(response.content).hexdigest())
#         f_hash.close()
#     f.close()
#     logger.info("Successfully stored the list of protocols from the defiLlama API in a binary file")
