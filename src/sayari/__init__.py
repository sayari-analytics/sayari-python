import queue
import time

from .python.client import SayariAnalyticsApi
from .python.resources.traversal.client import TraversalResponse
from .python.resources.base_types import SizeInfo
from .python.resources.auth.types.audience import Audience
from .python.resources.auth.types.grant_type import GrantType
from .python.resources.shared_types.types.client_name import ClientName
import threading
import urllib.parse
import csv
from multiprocessing import Process, Queue, set_start_method

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
err_function_not_paginated = ValueError('this function is not paginated and cannot be used with "get_all_data"')


class Connection(SayariAnalyticsApi):
    def __init__(self, client_id, client_secret):
        resp = get_token(client_id, client_secret)
        SayariAnalyticsApi.__init__(self, token=resp.access_token, client_name=ClientName.PYTHON)
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
        SayariAnalyticsApi.__init__(self, token=resp.access_token, client_name=ClientName.PYTHON)
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

        # setup multiprocessing
        set_start_method('fork')
        rows_to_process = Queue()
        results = Queue()
        num_processes = 3
        processes = []

        # Open csv
        with open(path_to_csv) as csv_file:
            csv_reader = csv.reader(csv_file)
            column_map = map_csv(next(csv_reader))
            for row in csv_reader:
                # queue up row to process
                rows_to_process.put(row)

        # start processing rows
        for i in range(num_processes):
            p = Process(target=process_row, args=(self, column_map, rows_to_process, results))
            processes.append(p)
            p.start()

        # read results
        while any(p.is_alive() for p in processes):
            try:
                result = results.get_nowait()
            except queue.Empty:
                time.sleep(1)
            else:
                # check results
                if "risky" in result:
                    risky_entities.append(result["risky"])
                elif "non_risky" in result:
                    non_risky_entities.append(result["non_risky"])
                elif "unresolved" in result:
                    unresolved.append(result["unresolved"])

        # complete processes
        for p in processes:
            p.join()

        return risky_entities, non_risky_entities, unresolved


def process_row(client, column_map, rows_to_process, results):
    while True:
        try:
            row = rows_to_process.get_nowait()
        except queue.Empty:
            break
        else:
            # attempt to resolve entity
            entity_id = resolve_entity(client, column_map, row)

            # track unresolved rows
            if entity_id is None:
                # unresolved.append(row)
                results.put({"unresolved": row})
                continue

            # Get entity summary
            entity_summary = client.entity.entity_summary(entity_id)
            if len(entity_summary.risk) > 0:
                # risky_entities.append(entity_summary)
                results.put({"risky": entity_summary})
            else:
                # non_risky_entities.append(entity_summary)
                results.put({"non_risky": entity_summary})
    return True


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
    auth_client = SayariAnalyticsApi(client_name=ClientName.PYTHON)
    return auth_client.auth.get_token(client_id=client_id,
                                      client_secret=client_secret,
                                      audience=Audience.SAYARI,
                                      grant_type=GrantType.CLIENT_CREDENTIALS)


"""
# takes in a function and its args, will automatically page through the data and return all the results
def get_all_data(func, *args, **kwargs):
    # intercept requests for too much data
    resp = func(*args, **kwargs)
    if hasattr(resp, 'size') and resp.size.count >= max_results:
        raise err_too_much_data_requested

    # intercept request from non-paginated functions
    if not hasattr(resp, 'next'):
        raise err_function_not_paginated

    # get all data
    all_data = resp.data
    while resp.next:
        resp = func(*args, **kwargs, offset=resp.offset + resp.limit)
        all_data.extend(resp.data)

    return all_data, resp # capture the other data in the response
"""


def encode_record_id(record_id):
    return urllib.parse.quote(record_id, safe='')
