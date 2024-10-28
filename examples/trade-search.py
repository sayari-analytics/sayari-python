import os
from sayari.environment import SayariEnvironment
from env_loader import load_env_vars_and_authenticate


def main():
    """
    Main function to search for shipments, suppliers, and buyers related to 'microcenter'.
    Default environment is set to PRODUCTION unless BASE_URL is set.
    """
    # Set environment, default to PRODUCTION unless BASE_URL is set
    base_url = os.getenv("BASE_URL", SayariEnvironment.PRODUCTION)
    env = SayariEnvironment(base_url)

    # Load environment variables and authenticate
    client = load_env_vars_and_authenticate(env)

    resolution = client.resolution.resolution(name="microcenter")
    entity_details = client.entity.get_entity(resolution.data[0].entity_id)
    print(
        f"**********************************************************************\n"
        f"Name of Company : {entity_details.label}\n"               # Display the company name
        f"Address         : {entity_details.addresses}\n"           # Display the company address
        f"Company Type    : {entity_details.company_type}\n"        # Display the company type
        f"**********************************************************************"
    )

    # Define the search queries and corresponding entity names.
    # Each tuple in `queries` consists of:
    # 1. A search call using `client.trade` API for different entities (shipments, suppliers, buyers).
    # 2. A string that represents the entity name, which is used to label the search result.

    queries = [
        (client.trade.search_shipments(q="microcenter"), "shipments"),  # Search for shipments containing 'microcenter'
        (client.trade.search_suppliers(q="microcenter"), "suppliers"),  # Search for suppliers containing 'microcenter'
        (client.trade.search_buyers(q="microcenter"), "buyers"),        # Search for buyers containing 'microcenter'
    ]

    # Loop through each entity search, process the search results, and print the count.
    # `entity` represents the search result object, and `search_type` is the name label.

    for entity, search_type in queries:
        # `entity.data` holds the list of results for each query (e.g., all shipments matching "microcenter")
        # Print the total count of found entities for each search_type (shipments, suppliers, or buyers).
        print(f"Found {len(entity.data)} {search_type}.")


if __name__ == "__main__":
    main()
