from .python.client import SayariAnalyticsApi
import threading

client_header = "sayari-python"


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


def get_token(client_id, client_secret):
    auth_client = SayariAnalyticsApi(client=client_header)
    return auth_client.auth.get_token(client_id=client_id,
                                        client_secret=client_secret,
                                        audience="sayari.com",
                                        grant_type="client_credentials")


# takes in a function and its args, will automatically page through the data and return all the results
def get_all_data(func, *args, **kwargs):
    resp = func(*args, **kwargs)
    all_data = resp.data
    while resp.next:
        resp = func(*args, **kwargs, offset=resp.offset+resp.limit)
        all_data.extend(resp.data)

    return all_data
