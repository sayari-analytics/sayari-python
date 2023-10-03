import sys
sys.path.append("..")

from generated.python.client import SayariAnalyticsApi

def Connect(id, secret):
    auth_client = SayariAnalyticsApi()
    result = auth_client.auth.get_token(client_id=id,
                                  client_secret=secret,
                                  audience="sayari.com",
                                  grant_type="client_credentials"
                                  )

    #TODO: add error checking?
    return SayariAnalyticsApi(token=result.access_token)

