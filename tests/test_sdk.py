import os
import pytest
import string
import random
from dotenv import load_dotenv
import sys
sys.path.append("..")
from sdk.main import connect

import urllib.parse

# This fixture is used to set up the client for each test
@pytest.fixture(scope="session")
def setup_connection():
    # load ENV file
    load_dotenv()

    # Create a client that is authed against the API
    client = connect(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
    return client


def test_sources(setup_connection):
    # get connection
    client = setup_connection

    # list sources
    sources = client.source.list_sources()

    # We should have 249 sources as of 10/4/2023
    assert len(sources.data) == 249

    # The first of these should be "Abu Dhabi Registration Authority Online Registry" as of 10/4/2023
    assert sources.data[0].label == "Abu Dhabi Registration Authority Online Registry"

    """ 
    Commented out b/c this check is slow (~20s)
    # We should be able to describer all of these without an error
    idx = 0
    for source in sources.data:
        result = client.source.get_source(source.id)
        assert result.label == sources.data[idx].label
        idx += 1
    """

def test_entities(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random word
    random_string = ''.join(random.choices(string.ascii_letters, k=3))

    # query until we get results
    entitySearchResults = client.search.search_entity(q=random_string)
    if len(entitySearchResults.data) == 0:
        return test_entities(setup_connection)

    # assert that we have results
    assert len(entitySearchResults.data) > 0

    # do some checks on the first result
    first_entity = entitySearchResults.data[0]
    # capture entity id/label for debugging
    print(entitySearchResults.data[0].id)
    print(entitySearchResults.data[0].label)

    # get entity summary
    first_entity_summary = client.entity.entity_summary(first_entity.id)

    # summary should match search results
    assert first_entity_summary.id == first_entity.id
    assert first_entity_summary.label == first_entity.label
    assert first_entity_summary.degree == first_entity.degree
    assert first_entity_summary.pep == first_entity.pep
    assert first_entity_summary.psa_count == first_entity.psa_count
    assert first_entity_summary.type == first_entity.type

    # get entity details
    first_entity_details = client.entity.get_entity(first_entity.id)

    assert first_entity_details.company_type == first_entity.company_type


"""
# search for an entity


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
record = client.record.get_record(urllib.parse.quote(recordSearch.data[0].id, safe=''))
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
"""
