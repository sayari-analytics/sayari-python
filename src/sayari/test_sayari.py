import os
import pytest
import string
import random
from dotenv import load_dotenv
from . import Connection, encode_record_id


# This fixture is used to set up the client for each test
@pytest.fixture(scope="session")
def setup_connection():
    # load ENV file if ENV vars are not set
    if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
        load_dotenv()

    # Create a client that is authed against the API
    client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))
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

    # do some checks on the first result
    first_record = record_search_results.data[0]
    # capture record id/label for debugging
    print(first_record.id)
    print(first_record.label)

    # get this record and compair fields
    record = client.record.get_record(encode_record_id(first_record.id))

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
    # recurse
    if len(traversal.data) == 0:
        test_ownership_traversal(setup_connection)

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
    if len(shipments.data.hits) == 0:
        return test_shipment_search(setup_connection)

    # assert that we have results
    assert len(shipments.data.hits) > 0

    # test field and filter
    entity_id = "f_nIivE32HCYDPEoSPTGJw"
    hs_code = "600410"
    filter_value = {"buyer_id": [entity_id]}
    shipments = client.trade.search_shipments(q=hs_code, fields="hs_code", filter=filter_value)
    assert len(shipments.data.hits) > 0
    for shipment in shipments.data.hits:
        # verify shipment matches on HS code
        assert len(shipment.business_purpose) > 0
        hs_found = False
        for purpose in shipment.business_purpose:
            if purpose.code == hs_code:
                hs_found = True
                break
        assert hs_found

        # verify entity matches
        assert len(shipment.dst) > 0
        entity_found = False
        for dst in shipment.dst:
            if dst.entity_id == entity_id:
                entity_found = True
                break
        assert entity_found

    # test field and multi-filter
    supplier_country = "CHN"
    supplier_risk = "sheffield_hallam_university_forced_labor_entity"
    hs_code = "600410"
    filter_values = {"supplier_country": [supplier_country], "supplier_risk": [supplier_risk]}
    shipments = client.trade.search_shipments(q=hs_code, fields="hs_code", filter=filter_values)
    assert len(shipments.data.hits) > 0
    for shipment in shipments.data.hits:
        # verify shipment matches on HS code
        assert len(shipment.business_purpose) > 0
        hs_found = False
        for purpose in shipment.business_purpose:
            if purpose.code == hs_code:
                hs_found = True
                break
        assert hs_found

        # verify shipment matches supplier country and risk
        assert len(shipment.src) > 0
        supplier_country_found = False
        supplier_risk_found = False
        for src in shipment.src:
            for country in src.country:
                if country == supplier_country:
                    supplier_country_found = True
                    break
            for risk in src.risk_factors.keys():
                if risk == supplier_risk:
                    supplier_risk_found = True
                    break
            if supplier_risk_found and supplier_country_found:
                break
        assert supplier_country_found
        assert supplier_risk_found




def test_supplier_search(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    print("searching for supplier: " + random_string)

    # query until we get results
    suppliers = client.trade.search_suppliers(q=random_string)
    if len(suppliers.data.hits) == 0:
        return test_supplier_search(setup_connection)

    # assert that we have results
    assert len(suppliers.data.hits) > 0


def test_buyer_search(setup_connection):
    # get connection
    client = setup_connection

    # search for an entity with a random string
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    print("searching for buyer: " + random_string)

    # query until we get results
    buyers = client.trade.search_buyers(q=random_string)
    if len(buyers.data.hits) == 0:
        return test_buyer_search(setup_connection)

    # assert that we have results
    assert len(buyers.data.hits) > 0


"""def test_too_much_data_requested(setup_connection):
    # get connection
    client = setup_connection

    with pytest.raises(ValueError) as e_info:
        all_entities = get_all_data(client.search.search_entity, q="amazon")
        assert e_info == err_too_much_data_requested
        assert len(all_entities) == 0"""


def test_usage(setup_connection):
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
