# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rat_limit_exceeded import RatLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.error_response import ErrorResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from ..shared_types.types.record_details import RecordDetails
from ..shared_types.types.record_id import RecordId


class RecordClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_record(
        self,
        id: RecordId,
        *,
        references_limit: typing.Optional[int] = None,
        references_offset: typing.Optional[int] = None,
    ) -> RecordDetails:
        """
        Retrieve a record from the database based on the ID

        Parameters:
            - id: RecordId.

            - references_limit: typing.Optional[int]. A limit on the number of references to be returned. Defaults to 100.

            - references_offset: typing.Optional[int]. Number of references to skip before returning response. Defaults to 0.
        """
        _response = self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/record/{id}"),
            params=remove_none_from_dict(
                {"references.limit": references_limit, "references.offset": references_offset}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RatLimitExceeded()
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
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
    ) -> RecordDetails:
        """
        Retrieve a record from the database based on the ID

        Parameters:
            - id: RecordId.

            - references_limit: typing.Optional[int]. A limit on the number of references to be returned. Defaults to 100.

            - references_offset: typing.Optional[int]. Number of references to skip before returning response. Defaults to 0.
        """
        _response = await self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/record/{id}"),
            params=remove_none_from_dict(
                {"references.limit": references_limit, "references.offset": references_offset}
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RecordDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic.parse_obj_as(ErrorResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RatLimitExceeded()
        if _response.status_code == 401:
            raise Unauthorized(pydantic.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
