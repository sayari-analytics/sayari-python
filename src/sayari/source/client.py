# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.get_source_response import GetSourceResponse
from .types.list_sources_response import ListSourcesResponse


class SourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourcesResponse:
        """
        Returns metadata for all sources that Sayari collects data from

        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSourcesResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.source.list_sources(
            limit=2,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/sources", method="GET", params={"limit": limit, "offset": offset}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListSourcesResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSourceResponse:
        """
        Returns metadata for a source that Sayari collects data from

        Parameters
        ----------
        id : str
            The unique identifier for a source in the database

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSourceResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.source.get_source(
            id="f4396e4b8a41d1fd9f09ea94d2ebedb9",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/source/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetSourceResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_sources(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListSourcesResponse:
        """
        Returns metadata for all sources that Sayari collects data from

        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListSourcesResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.source.list_sources(
            limit=2,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/sources", method="GET", params={"limit": limit, "offset": offset}, request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(ListSourcesResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSourceResponse:
        """
        Returns metadata for a source that Sayari collects data from

        Parameters
        ----------
        id : str
            The unique identifier for a source in the database

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSourceResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.source.get_source(
            id="f4396e4b8a41d1fd9f09ea94d2ebedb9",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/source/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(GetSourceResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
            if _response.status_code == 500:
                raise InternalServerError(
                    pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
