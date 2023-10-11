import os
from dotenv import load_dotenv
from sayari import Connection, get_all_data

# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables


# Create a client that is authed against the API
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# Traversal
entity = client.search.search_entity(q="David Konigsberg", limit=1)
all_traversals = get_all_data(client.traversal.traversal, entity.data[0].id, limit=1)
print("Total:",len(all_traversals))

# Entities
all_entities = get_all_data(client.search.search_entity, q="David Konigsberg", limit=5)
print("Total:", len(all_entities))

all_entities = get_all_data(client.search.search_entity, q="David John Smith")
print("Total:", len(all_entities))

# Records
all_record = get_all_data(client.search.search_record, q="David Konigsberg")
print("Total:", len(all_record))
