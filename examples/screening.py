import os
import sys
from dotenv import load_dotenv # type: ignore
from sayari.client import Sayari

# NOTE: To connect you must provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables
# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()


client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
if client_id is None or client_secret is None:
    print("The CLIENT_ID and CLIENT_SECRET environment variables are required to run this example.")
    sys.exit(1)

# Create a client that is authed against the API
client = Sayari(
    client_id=client_id,
    client_secret=client_secret,
)

# Do screening
risky_entities, non_risky_entities, unresolved = client.screen_csv("examples/entities_to_screen.csv")

print("Found {} entities with risks.".format(len(risky_entities)))
print("Found {} entities without risks.".format(len(non_risky_entities)))
print("{} records could not be resolved to entities.".format(len(unresolved)))
