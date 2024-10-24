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

    # Define search queries and corresponding entity names
    queries = [
        (client.trade.search_shipments(q="microcenter"), "shipments"),
        (client.trade.search_suppliers(q="microcenter"), "suppliers"),
        (client.trade.search_buyers(q="microcenter"), "buyers"),
    ]

    # Search and print results
    for entity, entity_name in queries:
        print(f"Found {len(entity.data)} {entity_name}.")


if __name__ == "__main__":
    main()
