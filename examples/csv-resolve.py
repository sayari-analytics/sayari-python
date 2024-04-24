import os
import sys
import csv
from dotenv import load_dotenv # type: ignore
from sayari.client import Sayari


# NOTE: To connect you must provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables
# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()


client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
if client_id is None or client_secret is None:
    print("The CLIENT_ID and CLIENT_SECRET environment variables are required to run this example.")
    sys.exit(1)

# Create a client that is authed against the API
client = Sayari(
    client_name="test",
    client_id=client_id,
    client_secret=client_secret,
)

# Do screening
path_to_csv = "examples/entities_to_screen.csv"

# Open csv
with open(path_to_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    header_skipped = False

    # refer to the various fields by their index in the CSV
    # in this CSV, the columns are name, address, address, address, country
    # to map these columns automatically, see the code for the screen_csv function
    for row in csv_reader:
        # skip header
        if not header_skipped:
            header_skipped = True
            continue

        name = []
        name.append(row[0])

        country = []
        country.append(row[4])

        address = []
        address.append(row[1])
        address.append(row[2])
        address.append(row[3])

        # use the resolve function to attempt to resolve each entity
        entity = client.resolution.resolution(name=name, country=country, address=address)

        # print the label of the first result
        print(entity.data[0].label)
