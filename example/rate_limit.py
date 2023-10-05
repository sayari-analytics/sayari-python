import os
import urllib.parse
import sys
from dotenv import load_dotenv
sys.path.append("..")
from sdk.main import connect

# load ENV file
load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables


# Create a client that is authed against the API
client = connect(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))


# query until we get results
entity_search_results = client.search.search_entity(q="DAKLabb")

# assert that we have results
assert len(entity_search_results.data) > 0

# do some checks on the first result
first_entity = entity_search_results.data[0]

limit_hit = False
while not limit_hit:
    # call UBO a bunch of time
    ubo = client.traversal.traversal(first_entity.id)
    print(ubo)
    if len(ubo.data) == 0:
        limit_hit = True
        print ("limit hit")
        assert False
