import sys
from generated.python.client import SayariAnalyticsApi

sys.path.append("..")


def connect(client_id, client_secret):
    auth_client = SayariAnalyticsApi()
    result = auth_client.auth.get_token(client_id=client_id,
                                        client_secret=client_secret,
                                        audience="sayari.com",
                                        grant_type="client_credentials")

    # TODO: add error checking?
    return SayariAnalyticsApi(token=result.access_token)

