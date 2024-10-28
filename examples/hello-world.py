import json
import os
from sys import exit
from dotenv import load_dotenv
from sayari.client import Sayari


def main():
    """
    Main function to load environment variables, create the Sayari client,
    resolve entity details, and print them in a formatted manner.
    """
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

    # Create the AUTH-enticated Sayari client
    client = Sayari(client_id=client_id, client_secret=client_secret)

    resolution_data = client.resolution.resolution(name="Victoria Beckham")
    if not resolution_data:
        exit("No entities resolved for 'Victoria Beckham'")

    entity_details = client.entity.get_entity(resolution_data.data[0].entity_id)
    # Print the entire output with proper labels
    print(
        f"**********************************************************************\n"
        f"Name of Company : {entity_details.label}\n"
        f"Address         : {entity_details.addresses}\n"
        f"Company Type    : {entity_details.company_type}\n"
        f"**********************************************************************"
    )


if __name__ == "__main__":
    main()
