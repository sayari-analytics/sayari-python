# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..shared_errors.bad_request import BadRequest
from ..shared_errors.bad_request_response import BadRequestResponse
from ..shared_errors.internal_server_error import InternalServerError
from ..shared_errors.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.unauthorized import Unauthorized
from ..shared_errors.unauthorized_response import UnauthorizedResponse
from .audience import Audience
from .auth_response import AuthResponse
from .client_id import ClientId
from .client_secret import ClientSecret
from .grant_type import GrantType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_token(
        self, *, client_id: ClientId, client_secret: ClientSecret, audience: Audience, grant_type: GrantType
    ) -> AuthResponse:
        """
        Hit the auth endpoint to get a bearer token

        Parameters:
            - client_id: ClientId.

            - client_secret: ClientSecret.

            - audience: Audience.

            - grant_type: GrantType.
        ---
        from sayari-analytics import Audience, GrantType
        from sayari-analytics.client import SayariAnalyticsApi

        client = SayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        client.auth.get_token(client_id="your client_id here", client_secret="your client_secret here", audience=Audience.SAYARI_COM, grant_type=GrantType.CLIENT_CREDENTIALS, )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "oauth/token"),
            json=jsonable_encoder(
                {"client_id": client_id, "client_secret": client_secret, "audience": audience, "grant_type": grant_type}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AuthResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_token(
        self, *, client_id: ClientId, client_secret: ClientSecret, audience: Audience, grant_type: GrantType
    ) -> AuthResponse:
        """
        Hit the auth endpoint to get a bearer token

        Parameters:
            - client_id: ClientId.

            - client_secret: ClientSecret.

            - audience: Audience.

            - grant_type: GrantType.
        ---
        from sayari-analytics import Audience, GrantType
        from sayari-analytics.client import AsyncSayariAnalyticsApi

        client = AsyncSayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        await client.auth.get_token(client_id="your client_id here", client_secret="your client_secret here", audience=Audience.SAYARI_COM, grant_type=GrantType.CLIENT_CREDENTIALS, )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "oauth/token"),
            json=jsonable_encoder(
                {"client_id": client_id, "client_secret": client_secret, "audience": audience, "grant_type": grant_type}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(AuthResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
