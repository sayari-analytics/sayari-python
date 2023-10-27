from .python.client import SayariAnalyticsApi
import threading
import csv

client_header = "sayari-python"

# resolution attributes
Name = "name"
Identifier = "identifier"
Country = "country"
Address = "address"
DOB = "dateofbirth"
Contact = "contact"
Type = "type"

# CSV Headers
csvDict = {
    Name: "The name of the entity",
    Identifier: "...",
    Country: "Must be from the enum set",
    Address: "...",
    DOB: "...",
    Contact: "...",
    Type: "Must be from the enum set",
}

# Too much data requested error
max_results = 10000
err_too_much_data_requested = ValueError('this request returns {} or more objects. please request individual pages of results, or narrow your request to return fewer objects'.format(max_results))


class Connection(SayariAnalyticsApi):
    def __init__(self, client_id, client_secret):
        resp = get_token(client_id, client_secret)
        SayariAnalyticsApi.__init__(self, token=resp.access_token, client=client_header)
        self.client_id = client_id
        self.client_secret = client_secret

        # refresh 1 hr before the token expires
        refresh_in = resp.expires_in - 3600
        if refresh_in < 0:
            refresh_in = 0
        self.timer = threading.Timer(refresh_in, self.update_token)
        self.timer.daemon = True
        self.timer.start()

    def update_token(self):
        resp = get_token(self.client_id, self.client_secret)
        SayariAnalyticsApi.__init__(self, token=resp.access_token, client=client_header)
        refresh_in = resp.expires_in - 3600
        if refresh_in < 0:
            refresh_in = 0
        self.timer = threading.Timer(refresh_in, self.update_token, daemon=True)
        self.timer.daemon = True
        self.timer.start()

    # TODO: introduce concurrency
    def screen_csv(self, path_to_csv):
        # create empty result lists
        risky_entities = []
        non_risky_entities = []
        unresolved = []

        # Open csv
        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file)
            i = 0
            for row in csv_reader:
                i += 1
                # map the headers
                if i == 1:
                    column_map = map_csv(row)
                    continue

                # attempt to resolve entity
                entity_id = resolve_entity(self, column_map, row)

                # track unresolved rows
                if entity_id is None:
                    unresolved.append(row)
                    continue

                # Get entity summary
                entity_summary = self.entity.entity_summary(entity_id)

                if len(entity_summary.risk) > 0:
                    risky_entities.append(entity_summary)
                else:
                    non_risky_entities.append(entity_summary)

        return risky_entities, non_risky_entities, unresolved


def map_csv(row):
    column_map = {}
    # for each column of the CSV
    i = 0
    for col in row:
        # Remove all spaces from the column name and convert to lowercase
        col_name = col.lower().replace(' ', '')
        # check if it corresponds to one of our resolution fields
        if col_name in csvDict:
            # if so, check if we have mapped that column yet
            if col_name not in column_map:
                # if not, create it in the map
                column_map[col_name] = []
            # add column index to dict
            column_map[col_name].append(i)
        else:
            raise Exception("One or more of the CSV columns does not map to a resolution field")
        i += 1
    return column_map


def resolve_entity(client, column_map, row):
    name = None
    if Name in column_map:
        name = []
        for name_col in column_map[Name]:
            name.append(row[name_col])

    identifier = None
    if Identifier in column_map:
        identifier = []
        for id_col in column_map[Identifier]:
            identifier.append(row[id_col])

    country = None
    if Country in column_map:
        country = []
        for country_col in column_map[Country]:
            country.append(row[country_col])

    address = None
    if Address in column_map:
        address = []
        for address_col in column_map[Address]:
            address.append(row[address_col])

    dob = None
    if DOB in column_map:
        dob = []
        for dob_col in column_map[DOB]:
            dob.append(row[dob_col])

    contact = None
    if Contact in column_map:
        contact = []
        for contact_col in column_map[Contact]:
            contact.append(row[contact_col])

    ent_type = None
    if Type in column_map:
        ent_type = []
        for type_col in column_map[Type]:
            ent_type.append(row[type_col])

    entity = client.resolution.resolution(name=name, identifier=identifier, country=country, address=address,
                                          date_of_birth=dob, contact=contact, type=ent_type)

    if len(entity.data) == 0:
        return None
    return entity.data[0].entity_id


def get_token(client_id, client_secret):
    auth_client = SayariAnalyticsApi(client=client_header)
    return auth_client.auth.get_token(client_id=client_id,
                                      client_secret=client_secret,
                                      audience="sayari.com",
                                      grant_type="client_credentials")


# takes in a function and its args, will automatically page through the data and return all the results
def get_all_data(func, *args, **kwargs):
    resp = func(*args, **kwargs)
    if resp.size.count >= max_results:
        raise err_too_much_data_requested
    all_data = resp.data
    while resp.next:
        resp = func(*args, **kwargs, offset=resp.offset + resp.limit)
        all_data.extend(resp.data)

    return all_data
