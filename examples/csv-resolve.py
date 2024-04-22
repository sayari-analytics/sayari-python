import os
from dotenv import load_dotenv
from sayari import Connection
import csv

# load ENV file if ENV vars are not set
if os.getenv('CLIENT_ID') is None or os.getenv('CLIENT_SECRET') is None:
    load_dotenv()

# To connect you most provide your client ID and client secret. To avoid accidentally checking these into git,
# it is recommended to use ENV variables

# Create a client that is authed against the API
client = Connection(os.getenv('CLIENT_ID'), os.getenv('CLIENT_SECRET'))

# Do screening
path_to_csv = "examples/entities_to_screen.csv"

# Open csv
with open(path_to_csv) as csv_file:
    csv_reader = csv.reader(csv_file)
    header_skipped = False
    for row in csv_reader:
        # skip header
        if not header_skipped:
            header_skipped = True
            continue

        # refer to the various fields by their index in the CSV
        # in this CSV, the columns are name, address, address, address, country
        # to map these columns automatically, see the code for the screen_csv function
        name = []
        name.append(row[0])

        country = []
        country.append(row[4])

        address = []
        address.append(row[1])
        address.append(row[2])
        address.append(row[3])

        entity = client.resolution.resolution(name=name, country=country, address=address)

        # print the label of the first result
        print(entity.data[0].label)
