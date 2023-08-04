"""
This script will check that the Jenkins jobs
related to iA.Teleservices are fine. It will
do so by verifying the status via the Jenkins
Rest API. If that is not the case, it will print
report of failure with some details.

Author:
    Daniel Muyshond - 01.12.2022

Ideas of possible improvments:

    Adding a command-line interface (CLI) to the script using a library like argparse or click. This allows users to pass in arguments when running the script, such as the Jenkins URL or the endpoint URLs to check.

    Adding tests to the script to ensure that it is working as expected. This can help you catch any bugs or regressions early on and
"""


from os import environ

import requests

JENKINS_JOB_ENDPOINTS_FOR_URL = [
    "imio-townstreet/job/dev-test/",
    "imio-townstreet/job/main/",
    "imio-ts-aes/job/dev-test/",
    "imio-ts-aes/job/main/",
    "imio-ts-aes/job/odoo15/",
    "imio-ts-aes/job/odoo9/",
    "imio-ts-aes/job/wip%252F50391-indus/",
    "passerelle-imio-ts1-datasources/job/master/",
    "passerelle-imio-abiware/job/dev-test/",
    "passerelle-imio-abiware/job/main/",
    "passerelle-imio-abiware/job/wip_MTELELIEZ2-25/",
    "passerelle-imio-aes-health/job/dev-test/",
    "passerelle-imio-aes-health/job/main/",
    "passerelle-imio-aes-meal/job/dev-test/",
    "passerelle-imio-aes-meal/job/main/",
    "passerelle-imio-apims-baec/job/dev-test/",
    "passerelle-imio-apims-baec/job/main/",
    "passerelle-imio-ia-aes/job/dev-test/",
    "passerelle-imio-ia-aes/job/main/",
    "passerelle-imio-ia-aes/job/odoo15/",
    "passerelle-imio-ia-aes/job/odoo9/",
    "passerelle-imio-ia-delib/job/dev-test/",
    "passerelle-imio-ia-delib/job/main/",
    "passerelle-imio-ia-tech/job/dev-test/",
    "passerelle-imio-ia-tech/job/main/",
    "passerelle-imio-sso-agents/job/dev-test/",
    "passerelle-imio-sso-agents/job/main/",
    "passerelle-imio-wca/job/dev-test/",
    "passerelle-imio-wca/job/main/",
    "scripts-teleservices/job/dev-test/",
    "scripts-teleservices/job/main/",
    "teleservices-iacitizen/job/dev-test/",
    "teleservices-iacitizen/job/main/",
    "teleservices-package/job/dev-test/",
    "teleservices-package/job/main/",
    "teleservices-package-light/job/dev-test/",
    "teleservices-package-light/job/main/",
]

failed_jobs = []

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)
"""
This will use the Python logging module to log messages at various levels (e.g. ERROR, INFO) with timestamps and other information. The messages will be printed to the console by default, but you can also configure the logging module to write the messages to a file or send them to a logging service.

You can then use the logger to log messages at different levels throughout the script, such as logger.info for informative messages, logger.warning for warnings, and logger.error for errors. This will allow you to better track and debug the script, and will provide a more detailed and structured log
"""


def checkup_jenkins_jobs_status():
    """Will iterate through Téléservices Jenkins
    jobs URL via Jenkins Rest API and print out
    which Job has failed.
    It will print 'OK' if the job is 'success'.
    """
    logger.info("Checkup Jenkins jobs")
    try:
        with requests.Session() as session:
            for index, endpoint in enumerate(JENKINS_JOB_ENDPOINTS_FOR_URL, start=1):
                # for endpoint in JENKINS_JOB_ENDPOINTS_FOR_URL:
                # Make the request to the Jenkins API
                jenkins_url = f"{environ.get('IMIO_JENKINS_URL')}{endpoint}lastBuild/api/json"
                response = session.get(
                    jenkins_url,
                    auth=(
                        environ.get("IMIO_JENKINS_USERNAME"),
                        environ.get("IMIO_JENKINS_PASSWORD"),
                    ),
                )

                # Raise an exception if the request fails
                response.raise_for_status()

                # Process the response
                data = response.json()
                info = f"Jenkins job #{index}:"
                if data["result"] == "SUCCESS":
                    logger.info(f"{info} {endpoint} is OK")
                else:
                    logger.error(f"{info} {endpoint} is KO")
                    logger.error(f"{info} {endpoint} result: {data['result']}")
                    logger.error(f"{info} {endpoint} url: {data['url']}")
    except requests.exceptions.ConnectionError as e:
        # Handle connection errors
        logger.exception(f"An error occured while checking the status of {info} {endpoint}: {e}")
    except ValueError as e:
        # Handle JSON parsing errors
        logger.exception(f"An error occurred while parsing the response for {info} {endpoint}: {e}")
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (e.g. 404 status code)
        logger.exception(f"An error occurred while checking the status of {info} {endpoint}: {e}")


if __name__ == "__main__":
    checkup_jenkins_jobs_status()
