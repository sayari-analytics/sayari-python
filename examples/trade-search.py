import os
import sys
from dotenv import load_dotenv # type: ignore
from sayari.client import Sayari
from sayari.environment import SayariEnvironment

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

# Set ENV if provided
env = SayariEnvironment.PRODUCTION
if os.getenv('BASE_URL') is not None:
    env = os.getenv('BASE_URL')

# Create a client that is authed against the API
client = Sayari(
    client_id=client_id,
    client_secret=client_secret,
    environment=env
)

# Search for shipments
shipments = client.trade.search_shipments(q="microcenter")
print("Found", len(shipments.data), "shipments.")

# Search for suppliers
suppliers = client.trade.search_suppliers(q="microcenter")
print("Found", len(suppliers.data), "suppliers.")

# Search for buyers
buyers = client.trade.search_buyers(q="microcenter")
print("Found", len(buyers.data), "buyers.")
