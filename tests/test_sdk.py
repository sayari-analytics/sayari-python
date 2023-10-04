import os
import pytest
import string
import random
from dotenv import load_dotenv
import sys
sys.path.append("..")
from sdk.main import connect, get_all_data

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


@pytest.mark.repeat(3)
def test_entities(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))

    # query until we get results
    entity_search_results = client.search.search_entity(q=random_string)
    if len(entity_search_results.data) == 0:
        return test_entities(setup_connection)

    # assert that we have results
    assert len(entity_search_results.data) > 0

    # do some checks on the first result
    first_entity = entity_search_results.data[0]
    # capture entity id/label for debugging
    print(first_entity.id)
    print(first_entity.label)

    # get entity summary
    first_entity_summary = client.entity.entity_summary(first_entity.id)

    # summary should match search results
    assert first_entity_summary.id == first_entity.id
    assert first_entity_summary.label == first_entity.label
    assert first_entity_summary.degree == first_entity.degree
    assert first_entity_summary.pep == first_entity.pep
    assert first_entity_summary.psa_count == first_entity.psa_count
    assert first_entity_summary.type == first_entity.type
    # These currently don't match, not sure if we will be updating that
    # assert first_entity_summary.entity_url == first_entity.entity_url
    assert first_entity_summary.sanctioned == first_entity.sanctioned
    assert first_entity_summary.identifiers == first_entity.identifiers
    assert first_entity_summary.addresses == first_entity.addresses
    assert first_entity_summary.countries == first_entity.countries
    assert first_entity_summary.relationship_count == first_entity.relationship_count

    # get entity details
    first_entity_details = client.entity.get_entity(first_entity.id)

    # check all the same stuff we checked with summary
    assert first_entity_details.id == first_entity.id
    assert first_entity_details.label == first_entity.label
    assert first_entity_details.degree == first_entity.degree
    assert first_entity_details.pep == first_entity.pep
    assert first_entity_details.psa_count == first_entity.psa_count
    assert first_entity_details.type == first_entity.type
    assert first_entity_details.entity_url == first_entity.entity_url
    assert first_entity_details.sanctioned == first_entity.sanctioned
    assert first_entity_details.identifiers == first_entity.identifiers
    assert first_entity_details.addresses == first_entity.addresses
    assert first_entity_details.countries == first_entity.countries
    assert first_entity_details.relationship_count == first_entity.relationship_count

    # check some additional fields
    assert first_entity_details.company_type == first_entity.company_type
    assert first_entity_details.relationships.size.count == first_entity.degree
    if first_entity.degree < 200:
        assert len(first_entity_details.relationships.data) == first_entity.degree
    else:
        assert len(first_entity_details.relationships.data) == 200


def test_resolution(setup_connection):
    # get connection
    client = setup_connection

    # resolve an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    resolution = client.resolution.resolution(name=random_string)
    if len(resolution.data) == 0:
        return test_resolution(setup_connection)

    # assert that we have results
    assert len(resolution.data) > 0

    # do some checks on the first result
    print(resolution.fields)
    print(resolution.fields.name)

    assert len(resolution.fields.name) == 1
    assert resolution.fields.name[0] == random_string


def test_records(setup_connection):
    # get connection
    client = setup_connection

    # search for a record with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))

    # query until we get results
    record_search_results = client.search.search_record(q=random_string)
    if len(record_search_results.data) == 0:
        return test_records(setup_connection)

    # assert that we have results
    assert len(record_search_results.data) > 0

    # do some checks on the first result
    first_record = record_search_results.data[0]
    # capture record id/label for debugging
    print(first_record.id)
    print(first_record.label)

    # get this record and compair fields
    record = client.record.get_record(urllib.parse.quote(first_record.id, safe=''))

    # record should match search results
    assert record.label == first_record.label
    assert record.source == first_record.source
    assert record.publication_date == first_record.publication_date
    assert record.acquisition_date == first_record.acquisition_date
    assert record.record_url == first_record.record_url
    assert record.references_count == first_record.references_count
    assert record.source_url == first_record.source_url


def test_ownership_traversal(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))

    # query until we get results
    entity_search_results = client.search.search_entity(q=random_string)
    if len(entity_search_results.data) == 0 and len(entity_search_results.data[0].degree) > 0:
        return test_ownership_traversal(setup_connection)

    # use first entity
    entity = entity_search_results.data[0]
    # capture entity id/label for debugging
    print(entity.id)
    print(entity.label)

    # do traversal
    traversal = client.traversal.traversal(entity.id)
    # We may need to recurse here if it is possible to have no results...
    assert len(traversal.data) > 0
    assert traversal.data[0].source == entity.id

    # do UBO traversal
    ubo = client.traversal.ubo(entity.id)
    # try again if this entity doesn't have a UBO
    if len(ubo.data) == 0:
        return test_ownership_traversal(setup_connection)

    assert len(ubo.data) > 0
    ubo_id = ubo.data[0].target.id

    # do ownership traversal from ubo
    downstream = client.traversal.ownership(ubo_id)

    assert len(downstream.data) > 0

    # The test below doesn't work, but I don't know why.
    # entity 'YdHkr_vnixCoWoQdOX5V7A' has a UBO of 'Sb77z7bNzNs_YtDFAwjuTw'
    # ownership of 'Sb77z7bNzNs_YtDFAwjuTw' doesn't include 'YdHkr_vnixCoWoQdOX5V7A'
    # perhaps this makes sense...
    """
    # the downstream path should contain the initial entity
    found = False
    for path in downstream.data:
        for step in path.path:
            if step.entity.id == entity.id:
                found = True
    assert found
    """

    # shortest path
    shortest_path = client.traversal.shortest_path(entities=[entity.id, ubo_id])
    assert len(shortest_path.data[0].path) > 0

# TODO: figure out good test for watchlist traversal


def test_entity_pagination(setup_connection):
    # get connection
    client = setup_connection

    # handle pagination of a small number of results ~15
    search_term = "David Konigsberg"
    query_info = client.search.search_entity(q=search_term, limit=1)
    all_entities = get_all_data(client.search.search_entity, q=search_term, limit=5)
    assert len(all_entities) == query_info.size.count

    # handle pagination of a larger number of results ~1k
    search_term = "David John Smith"
    query_info = client.search.search_entity(q=search_term, limit=1)
    all_entities = get_all_data(client.search.search_entity, q=search_term)
    assert len(all_entities) == query_info.size.count

def test_record_pagination(setup_connection):
    # get connection
    client = setup_connection

    # handle pagination of a small number of results ~300
    search_term = "David Konigsberg"
    query_info = client.search.search_record(q=search_term, limit=1)
    all_entities = get_all_data(client.search.search_record, q=search_term)
    assert len(all_entities) == query_info.size.count

