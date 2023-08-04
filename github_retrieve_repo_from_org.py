"""
This script retrieves the repositories of an organization from GitHub using the GitHub API.
"""

import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

# Set the organization name
organization_name = "IMIO"


def retrieve_repositories_from_organization(organization_name):
    """
    Retrieve the repositories of an organization from GitHub using the GitHub API.
    """
    # Set the URL for the GitHub API endpoint for retrieving the repositories of an organization
    url = "https://api.github.com/orgs/{ORG}/repos"

    # Set the organization name in the URL
    url = url.format(ORG=organization_name)

    # Send the GET request
    try:
        response = requests.get(url)
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
            # The repositories are returned in the response as a list of dictionaries
            repositories = response.json()
            for repository in repositories:
                print(repository["name"])
        else:
            # The request was unsuccessful
            print("Failed to retrieve repositories")


if __name__ == "__main__":
    # Retrieve the repositories of the organization
    retrieve_repositories_from_organization(organization_name)
