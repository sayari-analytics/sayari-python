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

    # Search for shipments
    shipments = client.trade.search_shipments(q="microcenter")
    print("Found", len(shipments.data), "shipments.")

    # Search for suppliers
    suppliers = client.trade.search_suppliers(q="microcenter")
    print("Found", len(suppliers.data), "suppliers.")

    # Search for buyers
    buyers = client.trade.search_buyers(q="microcenter")
    print("Found", len(buyers.data), "buyers.")

if __name__ == "__main__":
    main()
