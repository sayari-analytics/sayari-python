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
from ..shared_types.types.source_id import SourceId
from .types.source import Source
from .types.source_list import SourceList


class SourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_sources(self, *, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None) -> SourceList:
        """
        Returns metadata for all sources that Sayari collects data from

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.
        """
        _response = self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/sources"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SourceList, _response.json())  # type: ignore
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

    def get_source(self, id: SourceId) -> Source:
        """
        Returns metadata for a source that Sayari collects data from

        Parameters:
            - id: SourceId.
        """
        _response = self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/source/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Source, _response.json())  # type: ignore
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


class AsyncSourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_sources(
        self, *, limit: typing.Optional[int] = None, offset: typing.Optional[int] = None
    ) -> SourceList:
        """
        Returns metadata for all sources that Sayari collects data from

        Parameters:
            - limit: typing.Optional[int]. A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

            - offset: typing.Optional[int]. Number of results to skip before returning response. Defaults to 0.
        """
        _response = await self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/sources"),
            params=remove_none_from_dict({"limit": limit, "offset": offset}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SourceList, _response.json())  # type: ignore
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

    async def get_source(self, id: SourceId) -> Source:
        """
        Returns metadata for a source that Sayari collects data from

        Parameters:
            - id: SourceId.
        """
        _response = await self._client_wrapper.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/source/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(Source, _response.json())  # type: ignore
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
