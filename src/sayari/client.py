import typing
import httpx
import urllib.parse
import csv
import queue
import time
from multiprocessing import Process, Queue, set_start_method
from .base_client import BaseClient, AsyncBaseClient
from .environment import SayariEnvironment

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


class Sayari(BaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: ClientEnvironment. The environment to use for requests from the client. from .environment import ClientEnvironment

                                          Defaults to ClientEnvironment.PRODUCTION

        - client_name: str.

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - follow_redirects: typing.Optional[bool]. Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

        - client_id: str.

        - client_secret: str.
    ---
    from sayari.client import Client

    client = Client(
        client_name="YOUR_CLIENT_NAME",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariEnvironment = SayariEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        client_id: str,
        client_secret: str
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            client_id=client_id,
            client_secret=client_secret
        )

    def screen_csv(self, path_to_csv):
        # create empty result lists
        risky_entities = []
        non_risky_entities = []
        unresolved = []

        # setup multiprocessing
        set_start_method('fork')
        rows_to_process = Queue()
        results = Queue()
        # this can be scaled up to allow for more concurrent processes
        # it was reduced from 3 -> 1 to cope with rate limiting
        num_processes = 1
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


class AsyncSayari(AsyncBaseClient):
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: ClientEnvironment. The environment to use for requests from the client. from .environment import ClientEnvironment

                                          Defaults to ClientEnvironment.PRODUCTION

        - client_name: str.

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

        - follow_redirects: typing.Optional[bool]. Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

        - client_id: str.

        - client_secret: str.
    ---
    from sayari.client import AsyncClient

    client = AsyncClient(
        client_name="YOUR_CLIENT_NAME",
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
    )
    """
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariEnvironment = SayariEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        client_id: str,
        client_secret: str
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            client_id=client_id,
            client_secret=client_secret
        )


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


def encode_record_id(record_id):
    return urllib.parse.quote(record_id, safe='')
