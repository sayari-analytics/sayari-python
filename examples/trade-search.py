import os
from dotenv import load_dotenv
from sayari import Connection

# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables

# Create a client that is authed against the API
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# Search for shipments
shipments = client.trade.search_shipments(q="microcenter")
print("Found", len(shipments.data.hits), "shipments.")

# Search for suppliers
suppliers = client.trade.search_suppliers(q="microcenter")
print("Found", len(suppliers.data.hits), "suppliers.")

# Search for buyers
buyers = client.trade.search_buyers(q="microcenter")
print("Found", len(buyers.data.hits), "buyers.")
