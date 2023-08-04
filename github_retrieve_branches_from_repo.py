"""
This script retrieves the branches of a GitHub repository.
"""

import requests

# Set the URL for the GitHub API endpoint for retrieving the branches of a repository
url = "https://api.github.com/repos/{OWNER}/{REPO}/branches"

# Set the repository owner and repository name in the URL
url = url.format(OWNER="IMIO", REPO="scripts-teleservices")

# Set the authorization header with a personal access token
# headers = {"Authorization": "TOKEN"}

# Send the GET request
# response = requests.get(url, headers=headers)
response = requests.get(url)

# Check the status code of the response
if response.status_code == 200:
    # The request was successful
    # The branches are returned in the response as a list of dictionaries
    branches = response.json()
    for branch in branches:
        print(branch["name"])
else:
    # The request was unsuccessful
    print("Failed to retrieve branches")
