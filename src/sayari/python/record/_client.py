# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.remove_none_from_dict import remove_none_from_dict
from ..shared_errors.bad_request import BadRequest
from ..shared_errors.bad_request_response import BadRequestResponse
from ..shared_errors.internal_server_error import InternalServerError
from ..shared_errors.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.not_found import NotFound
from ..shared_errors.not_found_response import NotFoundResponse
from ..shared_errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.rate_limit_response import RateLimitResponse
from ..shared_errors.unauthorized import Unauthorized
from ..shared_errors.unauthorized_response import UnauthorizedResponse
from ..shared_types.record_id import RecordId
from .get_record_response import GetRecordResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RecordClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_record(
        self,
        id: RecordId,
        *,
        references_limit: typing.Optional[int] = None,
        references_offset: typing.Optional[int] = None,
    ) -> GetRecordResponse:
        """
        Retrieve a record from the database based on the ID

        Parameters:
            - id: RecordId.

            - references_limit: typing.Optional[int]. A limit on the number of references to be returned. Defaults to 100.

            - references_offset: typing.Optional[int]. Number of references to skip before returning response. Defaults to 0.
        ---
        from sayari-analytics.client import SayariAnalyticsApi

        client = SayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        client.record.get_record(id="74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254", )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/record/{id}"),
            params=remove_none_from_dict(
                {"references.limit": references_limit, "references.offset": references_offset}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetRecordResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRecordClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_record(
        self,
        id: RecordId,
        *,
        references_limit: typing.Optional[int] = None,
        references_offset: typing.Optional[int] = None,
    ) -> GetRecordResponse:
        """
        Retrieve a record from the database based on the ID

        Parameters:
            - id: RecordId.

            - references_limit: typing.Optional[int]. A limit on the number of references to be returned. Defaults to 100.

            - references_offset: typing.Optional[int]. Number of references to skip before returning response. Defaults to 0.
        ---
        from sayari-analytics.client import AsyncSayariAnalyticsApi

        client = AsyncSayariAnalyticsApi(client_name="YOUR_CLIENT_NAME", token="YOUR_TOKEN", )
        await client.record.get_record(id="74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254", )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/record/{id}"),
            params=remove_none_from_dict(
                {"references.limit": references_limit, "references.offset": references_offset}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(GetRecordResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
