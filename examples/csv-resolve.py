import csv
from env_loader import load_env_vars_and_authenticate

# Load environment variables and authenticate
client = load_env_vars_and_authenticate()

# Process CSV and resolve entities
with open("examples/entities_to_screen.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row

    for row in csv_reader:
        # Extract data from row
        name, address, country = [row[0]], row[1:4], [row[4]]

        # Resolve entity and handle empty results
        entity = client.resolution.resolution(
            name=name, country=country, address=address
        )

        if entity.data:  # Check if there is any data
            print(entity.data[0].label)
        else:
            print(f"No entity found for: {name}, {address}, {country}")
