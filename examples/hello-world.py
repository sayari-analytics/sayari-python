import json
import os
from sys import exit
from dotenv import load_dotenv
from sayari.client import Sayari


class SayariCustomEncoder(json.JSONEncoder):
    """
    Custom encoder to handle non-serializable objects from the Sayari client.
    This encoder handles objects with a __dict__ attribute and Sayari Identifier types.
    """

    def default(self, obj):
        if hasattr(obj, "__dict__"):
            return obj.__dict__
        if isinstance(obj, Sayari.Identifier):
            return str(obj)
        return super().default(obj)


def main():
    """Main function to load environment variables, create the Sayari client,
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

    # Create the Sayari client
    client = Sayari(client_id=client_id, client_secret=client_secret)

    # Resolve entity by name and retrieve entity details
    resolution_data = client.resolution.resolution(name="Victoria Beckham").data
    if not resolution_data:
        exit("No entities resolved for 'Victoria Beckham'")

    entity_id = resolution_data[0].entity_id
    entity_details = client.entity.get_entity(entity_id)

    # Print and format the entity details
    formatted_entity_details = json.dumps(
        entity_details, indent=2, cls=SayariCustomEncoder
    )
    print(formatted_entity_details)


if __name__ == "__main__":
    main()
