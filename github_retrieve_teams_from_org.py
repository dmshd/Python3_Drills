"""
This script retrieves the teams of a GitHub organization.
"""

import logging

import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# Set the URL for the GitHub API endpoint for retrieving the branches of a repository
url = "https://api.github.com/orgs/IMIO/teams"


# Set the authorization header with a personal access token
headers = {"Authorization": "TOKEN"}

# Send the GET request
try:
    # response = requests.get(url)
    response = requests.get(url, headers=headers)
    print(response)
except requests.exceptions.ConnectionError as e:
    # Handle connection errors
    logger.exception(f"A ConnectionError occured while checking the status: {e}")
except ValueError as e:
    # Handle JSON parsing errors
    logger.exception(f"A ValueError occurred while parsing the response: {e}")
except requests.exceptions.HTTPError as e:
    print(e.response.status_code)
    logger.exception(f"A HTTPError occurred while checking the status: {e}")
finally:
    # Check the status code of the response
    if response.status_code == 200:
        # The request was successful
        # The branches are returned in the response as a list of dictionaries
        branches = response.json()
        for branch in branches:
            print(branch["name"])
    else:
        # The request was unsuccessful
        logger.error("Failed to retrieve branches")
