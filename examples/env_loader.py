import os
from sys import exit, version_info
from dotenv import load_dotenv
from sayari.client import Sayari


def load_env_vars_and_authenticate(environment=None):
    """
    Loads environment variables, checks if CLIENT_ID and CLIENT_SECRET are set,
    and authenticates the Sayari client. If an environment is provided, it is
    used; otherwise, the default environment is used. Additionally, ensures that
    Python version 3.9 or higher is used.

    Parameters:
    - environment (optional): A `SayariEnvironment` object to set the desired
      API environment. Defaults to None.

    Returns:
    - client: An authenticated `Sayari` client.
    """
    # Check Python version (must be 3.9 or higher)
    if version_info < (3, 9):
        exit(
            "Python 3.9.x or higher is required to run this script. Please upgrade your Python version."
        )

    # Load environment variables from .env file
    load_dotenv()

    # Get CLIENT_ID and check if it's present
    client_id = os.getenv("CLIENT_ID")
    if not client_id:
        exit("CLIENT_ID is required - Please refer to Sayari documentation")

    # Get CLIENT_SECRET and check if it's present
    client_secret = os.getenv("CLIENT_SECRET")
    if not client_secret:
        exit("CLIENT_SECRET is required - Please refer to Sayari documentation")

    # Create the Sayari client using the provided environment or default settings
    client = (
        Sayari(
            client_id=client_id, client_secret=client_secret, environment=environment
        )
        if environment
        else Sayari(client_id=client_id, client_secret=client_secret)
    )

    return client
