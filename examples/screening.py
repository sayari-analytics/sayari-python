from env_loader import load_env_vars_and_authenticate


def main():
    """
    Main function to load environment variables, authenticate, and perform
    entity screening from a CSV file.
    """
    # Load environment variables and authenticate
    client = load_env_vars_and_authenticate()

    # Perform screening and retrieve entities
    risky_entities, non_risky_entities, unresolved = client.screen_csv(
        "examples/entities_to_screen.csv"
    )

    # Output the screening results
    print(f"Found {len(risky_entities)} entities with risks.")
    print(f"Found {len(non_risky_entities)} entities without risks.")
    print(f"{len(unresolved)} records could not be resolved to entities.")


if __name__ == "__main__":
    main()
