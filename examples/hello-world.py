import os
from dotenv import load_dotenv # type: ignore
from sayari.client import Sayari


# NOTE: To connect you must provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables
# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()

# Create a client that is authed against the API
client = Sayari(
    client_name="test",
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
)

# resolve by name
resolution = client.resolution.resolution(name="Victoria Beckham")

# get the entity details for the resolved entity
entity_details = client.entity.get_entity(resolution.data[0].entity_id)
print(entity_details)
