# This file was auto-generated by Fern from our API Definition.

import time
import typing

import httpx

from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import SayariAnalyticsApiEnvironment
from .resources.auth.client import AsyncAuthClient, AuthClient
from .resources.entity.client import AsyncEntityClient, EntityClient
from .resources.info.client import AsyncInfoClient, InfoClient
from .resources.record.client import AsyncRecordClient, RecordClient
from .resources.resolution.client import AsyncResolutionClient, ResolutionClient
from .resources.search.client import AsyncSearchClient, SearchClient
from .resources.source.client import AsyncSourceClient, SourceClient
from .resources.trade.client import AsyncTradeClient, TradeClient
from .resources.traversal.client import AsyncTraversalClient, TraversalClient

# Because this rate limiter doesn't block all requests, we need a relatively high limit to cope with racing threads.
retry_limit = 10


class Retry(httpx.HTTPTransport):
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        retry = 0
        resp = None
        while retry < retry_limit:
            retry += 1
            try:
                if resp is not None:
                    resp.close()
                resp = super().handle_request(request)
            # Retry on request exception
            except Exception as e:
                print("httpx {} exception {} caught - retrying".format(request.url, e))
                time.sleep(1)
                continue
            # Retry on 429
            if resp.status_code == 429:
                retry_delay = resp.headers.get("Retry-After")
                print("httpx {} 429 response - retrying after {}s".format(request.url, retry_delay))
                # Sleep for the requested amount of time
                time.sleep(int(retry_delay))
                continue
            # Retry on 502
            if resp.status_code == 502:
                print("httpx {} 502 response - retrying after 30s".format(request.url))
                time.sleep(30)
                continue
            content_type = resp.headers.get("Content-Type")
            if content_type is not None:
                mime_type, _, _ = content_type.partition(";")
                if mime_type == "application/json":
                    try:
                        resp.read()
                        resp.json()
                    except Exception as e:
                        print("httpx {} response not valid json '{}' - retrying".format(request.url, e))
                        continue
            break
        return resp


class SayariAnalyticsApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SayariAnalyticsApiEnvironment. The environment to use for requests from the client. from .environment import SayariAnalyticsApiEnvironment

                                                      Defaults to SayariAnalyticsApiEnvironment.PRODUCTION

        - client_name: str.

        - token: typing.Optional[typing.Union[str, typing.Callable[[], str]]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.Client]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from sayari-analytics.client import SayariAnalyticsApi

    client = SayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariAnalyticsApiEnvironment = SayariAnalyticsApiEnvironment.PRODUCTION,
        client_name: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            client_name=client_name,
            token=token,
            httpx_client=httpx.Client(timeout=timeout, transport=Retry()) if httpx_client is None else httpx_client,
        )
        self.auth = AuthClient(client_wrapper=self._client_wrapper)
        self.entity = EntityClient(client_wrapper=self._client_wrapper)
        self.info = InfoClient(client_wrapper=self._client_wrapper)
        self.record = RecordClient(client_wrapper=self._client_wrapper)
        self.resolution = ResolutionClient(client_wrapper=self._client_wrapper)
        self.search = SearchClient(client_wrapper=self._client_wrapper)
        self.source = SourceClient(client_wrapper=self._client_wrapper)
        self.trade = TradeClient(client_wrapper=self._client_wrapper)
        self.traversal = TraversalClient(client_wrapper=self._client_wrapper)


class AsyncSayariAnalyticsApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propogate to these functions.

    Parameters:
        - base_url: typing.Optional[str]. The base url to use for requests from the client.

        - environment: SayariAnalyticsApiEnvironment. The environment to use for requests from the client. from .environment import SayariAnalyticsApiEnvironment

                                                      Defaults to SayariAnalyticsApiEnvironment.PRODUCTION

        - client_name: str.

        - token: typing.Optional[typing.Union[str, typing.Callable[[], str]]].

        - timeout: typing.Optional[float]. The timeout to be used, in seconds, for requests by default the timeout is 60 seconds.

        - httpx_client: typing.Optional[httpx.AsyncClient]. The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.
    ---
    from sayari-analytics.client import AsyncSayariAnalyticsApi

    client = AsyncSayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: SayariAnalyticsApiEnvironment = SayariAnalyticsApiEnvironment.PRODUCTION,
        client_name: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            client_name=client_name,
            token=token,
            httpx_client=httpx.AsyncClient(timeout=timeout, transport=Retry())
            if httpx_client is None
            else httpx_client,
        )
        self.auth = AsyncAuthClient(client_wrapper=self._client_wrapper)
        self.entity = AsyncEntityClient(client_wrapper=self._client_wrapper)
        self.info = AsyncInfoClient(client_wrapper=self._client_wrapper)
        self.record = AsyncRecordClient(client_wrapper=self._client_wrapper)
        self.resolution = AsyncResolutionClient(client_wrapper=self._client_wrapper)
        self.search = AsyncSearchClient(client_wrapper=self._client_wrapper)
        self.source = AsyncSourceClient(client_wrapper=self._client_wrapper)
        self.trade = AsyncTradeClient(client_wrapper=self._client_wrapper)
        self.traversal = AsyncTraversalClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: SayariAnalyticsApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
