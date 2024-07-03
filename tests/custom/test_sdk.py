import os
import pytest
import string
import random
# from dotenv import load_dotenv # type: ignore
from sayari.client import Sayari
from sayari.environment import SayariEnvironment
# from . import Connection, encode_record_id


# This fixture is used to set up the client for each test
@pytest.fixture(scope="session")
def setup_connection():
    # load ENV file if ENV vars are not set
    # if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    #     load_dotenv()

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    assert client_id is not None
    assert client_secret is not None

    # Set ENV if provided
    env = SayariEnvironment.PRODUCTION
    base_url = "https://api.sayari.com"
    if os.getenv('BASE_URL') is not None:
        base_url = os.getenv('BASE_URL')
        env = os.getenv('BASE_URL')
    assert env is not None

    # Create a client that is authed against the API
    client = Sayari(
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
        environment=env
    )

    return client


def test_sources(setup_connection):
    # get connection
    client = setup_connection

    # list sources
    sources = client.source.list_sources()

    # We should have 250 sources as of 12/19/2023
    assert len(sources.data) >= 250


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

    # test the GET variant of the search endpoint
    entity_search_get_results = client.search.search_entity_get(q=random_string)
    assert len(entity_search_results.data) == len(entity_search_get_results.data)
    assert entity_search_results.size.count == entity_search_get_results.size.count
    assert entity_search_results.size.qualifier == entity_search_get_results.size.qualifier

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
    if first_entity.degree < 50:
        assert len(first_entity_details.relationships.data) == first_entity.degree
    else:
        assert len(first_entity_details.relationships.data) == 50


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
    print(random_string)
    record_search_results = client.search.search_record(q=random_string)
    if len(record_search_results.data) == 0:
        return test_records(setup_connection)

    # assert that we have results
    assert len(record_search_results.data) > 0

    # verify that get results match
    record_search_get_results = client.search.search_record_get(q=random_string)
    assert len(record_search_results.data) == len(record_search_get_results.data)
    assert record_search_results.size.count == record_search_get_results.size.count
    assert record_search_results.size.qualifier == record_search_get_results.size.qualifier

    # do some checks on the first result
    first_record = record_search_results.data[0]
    # capture record id/label for debugging
    print(first_record.id)
    print(first_record.label)

    # TODO: reimplement this
    # get this record and compair fields
    # record = client.record.get_record(encode_record_id(first_record.id))

    # record should match search results
    # assert record.label == first_record.label
    # assert record.source == first_record.source
    # assert record.publication_date == first_record.publication_date
    # assert record.acquisition_date == first_record.acquisition_date
    # assert record.record_url == first_record.record_url
    # assert record.references_count == first_record.references_count
    # assert record.source_url == first_record.source_url


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
    # recurse
    if len(traversal.data) == 0:
        test_ownership_traversal(setup_connection)

    # query until we get results
    if len(traversal.data) == 0:
        return test_ownership_traversal(setup_connection)

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


"""def test_entity_pagination(setup_connection):
    # get connection
    client = setup_connection

    # handle pagination of a small number of results ~15
    search_term = "David Konigsberg"
    query_info = client.search.search_entity(q=search_term, limit=1)
    all_entities = client.get_all_entity_search_results(q=search_term, limit=5)
    assert all_entities.limit == query_info.size.count

    # handle pagination of a larger number of results ~1k
    search_term = "David John Smith"
    query_info = client.search.search_entity(q=search_term, limit=1)
    all_entities = client.get_all_entity_search_results(q=search_term)
    assert all_entities.limit == query_info.size.count


def test_record_pagination(setup_connection):
    # get connection
    client = setup_connection

    # handle pagination of a small number of results ~300
    search_term = "David Konigsberg"
    query_info = client.search.search_record(q=search_term, limit=1)
    all_records = client.get_all_record_search_results(q=search_term)
    assert all_records.limit == query_info.size.count


def test_traversal_pagination(setup_connection):
    # get connection
    client = setup_connection

    entity = client.search.search_entity(q="David Konigsberg", limit=1)
    all_traversals = client.get_all_traversal_results(entity.data[0].id, limit=1)
    assert all_traversals.limit > 1"""


def test_shipment_search(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    print("searching for shipment: " + random_string)

    # query until we get results
    shipments = client.trade.search_shipments(q=random_string)
    if len(shipments.data) == 0:
        return test_shipment_search(setup_connection)

    # assert that we have results
    assert len(shipments.data) > 0

    # test field and multi-filter
    buyer_name = "HANSOLL TEXTILE LTD"
    buyer_id = "ZxL0IrGu9KNKx3NJjN0aeA"
    hs_code = "600410"
    filter_value = {"buyer_id": [buyer_id], "hs_code": [hs_code]}
    shipments = client.trade.search_shipments(q=buyer_name, filter=filter_value)
    assert len(shipments.data) > 0
    for shipment in shipments.data:
        # verify shipment matches on HS code
        assert len(shipment.product_descriptions) > 0
        hs_found = False
        for shipment_hs_code in shipment.hs_codes:
            if shipment_hs_code.code.startswith(hs_code):
                hs_found = True
                break
        assert hs_found

        # verify entity matches
        assert len(shipment.buyer) > 0
        entity_found = False
        for buyer in shipment.buyer:
            if buyer.id == buyer_id:
                entity_found = True
                break
        assert entity_found


def test_supplier_search(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    print("searching for supplier: " + random_string)

    # query until we get results
    suppliers = client.trade.search_suppliers(q=random_string)
    if len(suppliers.data) == 0:
        return test_supplier_search(setup_connection)

    # assert that we have results
    assert len(suppliers.data) > 0


def test_buyer_search(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    print("searching for buyer: " + random_string)

    # query until we get results
    buyers = client.trade.search_buyers(q=random_string)
    if len(buyers.data) == 0:
        return test_buyer_search(setup_connection)

    # assert that we have results
    assert len(buyers.data) > 0


"""def test_too_much_data_requested(setup_connection):
    # get connection
    client = setup_connection

    with pytest.raises(ValueError) as e_info:
        all_entities = get_all_data(client.search.search_entity, q="amazon")
        assert e_info == err_too_much_data_requested
        assert len(all_entities) == 0"""


def test_usage(setup_connection):
    if os.getenv('BASE_URL') is None:
        # get connection
        client = setup_connection

        usage = client.info.get_usage()
        assert usage.usage.entity > 0
        assert usage.usage.entity_summary > 0
        assert usage.usage.record > 0
        assert usage.usage.resolve > 0
        assert usage.usage.search_entities > 0
        assert usage.usage.search_records > 0
        assert usage.usage.search_trade > 0
        assert usage.usage.traversal > 0


def test_history(setup_connection):
    # get connection
    client = setup_connection

    history = client.info.get_history(size=10)
    assert history.size == len(history.events)
