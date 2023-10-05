from .python.client import SayariAnalyticsApi


def connect(client_id, client_secret):
    auth_client = SayariAnalyticsApi()
    result = auth_client.auth.get_token(client_id=client_id,
                                        client_secret=client_secret,
                                        audience="sayari.com",
                                        grant_type="client_credentials")

    # TODO: add error checking?
    return SayariAnalyticsApi(token=result.access_token)


# takes in a function and its args, will automatically page through the data and return all the results
def get_all_data(func, *args, **kwargs):
    resp = func(*args, **kwargs)
    all_data = resp.data
    while resp.next:
        resp = func(*args, **kwargs, offset=resp.offset+resp.limit)
        all_data.extend(resp.data)

    return all_data
