import os
from dotenv import load_dotenv
from datetime import date, timedelta
from sayari import Connection, encode_record_id

# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables

# Create a client that is authed against the API
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# list sources
sources = client.source.list_sources()
print("Found", len(sources.data), "sources")

# get the first source
firstSource = client.source.get_source(sources.data[0].id)
print("First source is:", firstSource.label)

# search for an entity
search_term = "victoria beckham limited"
entitySearchResults = client.search.search_entity(q=search_term)
print("Found", len(entitySearchResults.data), "entity results for ", search_term)

firstEntityResult = entitySearchResults.data[0].id

# get entity summary
entitySummary = client.entity.entity_summary(firstEntityResult)
print("Has address:", entitySummary.addresses[0])

# get the full entity
entityDetails = client.entity.get_entity(firstEntityResult)
print("Is referenced by", len(entityDetails.referenced_by.data), "sources")

# resolve
resolution = client.resolution.resolution(name=search_term)
print("Resolved to", len(resolution.data), "entities")

# search for record
recordSearch = client.search.search_record(q=search_term)
print("Found", len(recordSearch.data), "records.")

# get record
record = client.record.get_record(encode_record_id(recordSearch.data[0].id))
print("Found record:", record.label)

# do traversal
traversal = client.traversal.traversal(firstEntityResult)
print("Did traversal of entity", firstEntityResult, "Found", len(traversal.data), "related things.")

# do UBO traversal
ubo = client.traversal.ubo(firstEntityResult)
print("Found", len(ubo.data), "beneficial owners")

# ownership
downstream = client.traversal.ownership(ubo.data[0].target.id)
print("Found", len(downstream.data), "downstream things owned by the first UBO of", search_term)

# Fetch an entity likely to be associated with watch lists
putinResult = client.search.search_entity(q="putin")
# Check watchlist
watchlist = client.traversal.watchlist(putinResult.data[0].id)
print("Found", len(watchlist.data), "watchlist results for entity", putinResult.data[0].id)

# shortest path
shortestPath = client.traversal.shortest_path(entities=[firstEntityResult, ubo.data[0].target.id])
print("Found path with", len(shortestPath.data[0].path), "hops")

# Usage
usage = client.info.get_usage()
print("Entity summary usage: ", usage.usage.entity_summary)

# History
today = date.today()
history = client.info.get_history(size=10000, from_=today-timedelta(days=2), to=today-timedelta(days=1))
print("Found", len(history.events), "events from", today-timedelta(days=2), "to", today-timedelta(days=1))

