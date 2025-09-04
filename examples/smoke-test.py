from datetime import date, timedelta
from sayari.client import encode_record_id
from env_loader import load_env_vars_and_authenticate


def main():
    # Load environment variables and authenticate
    client = load_env_vars_and_authenticate()

    # List and fetch sources
    sources = client.ontology.get_sources().data
    print(f"Found {len(sources)} sources")

    # Get first two sources by ID (using multiple IDs works correctly)
    filtered_sources = client.ontology.get_sources(id=[sources[0].id, sources[1].id])
    first_source = filtered_sources.data[0]
    print(f"First source is: {first_source.label}")
    print(f"Retrieved {len(filtered_sources.data)} sources via filtered API call")

    # Search for an entity
    search_term = "victoria beckham limited"
    entity_results = client.search.search_entity(q=search_term).data
    print(f"Found {len(entity_results)} entity results for {search_term}")

    first_entity = entity_results[0].id

    # Get entity summary and details
    entity_summary = client.entity.entity_summary(first_entity)
    if entity_summary.addresses:
        print(f"Has address: {entity_summary.addresses[0]}")

    entity_details = client.entity.get_entity(first_entity)
    print(f"Is referenced by {len(entity_details.referenced_by.data)} sources")

    # Entity resolution
    resolution = client.resolution.resolution(name=search_term)
    print(f"Resolved to {len(resolution.data)} entities")

    # Record search and retrieval
    record_results = client.search.search_record(q=search_term).data
    print(f"Found {len(record_results)} records")

    record = client.record.get_record(encode_record_id(record_results[0].id))
    print(f"Found record: {record.label}")

    # Traversal, UBO, and ownership
    traversal = client.traversal.traversal(first_entity)
    print(
        f"Did traversal of entity {first_entity}, found {len(traversal.data)} related things"
    )

    ubo = client.traversal.ubo(first_entity).data
    print(f"Found {len(ubo)} beneficial owners")

    downstream = client.traversal.ownership(ubo[0].target.id)
    print(
        f"Found {len(downstream.data)} downstream things owned by the first UBO of {search_term}"
    )

    # Watchlist check for Putin
    putin_result = client.search.search_entity(q="putin").data
    watchlist = client.traversal.watchlist(putin_result[0].id)
    print(
        f"Found {len(watchlist.data)} watchlist results for entity {putin_result[0].id}"
    )

    # Shortest path traversal
    # TODO: revert reversal of query once bug is fixed
    shortest_path = client.traversal.shortest_path(
        entities=[ubo[0].target.id, first_entity]
    )
    print(f"Found path with {len(shortest_path.data[0].path)} hops")

    # Usage and history
    usage = client.info.get_usage()
    print(f"Entity summary usage: {usage.usage.entity}")

    today = date.today()
    history = client.info.get_history(
        size=10000, from_=today - timedelta(days=2), to=today - timedelta(days=1)
    )
    print(
        f"Found {len(history.events)} events from {today - timedelta(days=2)} to {today - timedelta(days=1)}"
    )


if __name__ == "__main__":
    main()
