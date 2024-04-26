import typing
import httpx

from .base_client import BaseClient, AsyncBaseClient
from .environment import ClientEnvironment


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
        environment: ClientEnvironment = ClientEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        client_id: str,
        client_secret: str
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            # TODO: capture version info here
            client_name="python_sdk",
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            client_id=client_id,
            client_secret=client_secret
        )


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
        environment: ClientEnvironment = ClientEnvironment.PRODUCTION,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        client_id: str,
        client_secret: str
    ):
        super().__init__(
            base_url=base_url,
            environment=environment,
            # TODO: capture version info here
            client_name="python_sdk",
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
            client_id=client_id,
            client_secret=client_secret
        )

