# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..shared_errors.errors.not_found_error import NotFoundError
from .types.resolution_response import ResolutionResponse


class ResolutionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def resolution(
        self,
        *,
        name: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        identifier: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        country: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        address: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        date_of_birth: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        contact: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        type: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters:
            - name: typing.Union[typing.Optional[str], typing.List[str]]. Entity name

            - identifier: typing.Union[typing.Optional[str], typing.List[str]]. Entity identifier

            - country: typing.Union[typing.Optional[str], typing.List[str]]. Entity country

            - address: typing.Union[typing.Optional[str], typing.List[str]]. Entity address

            - date_of_birth: typing.Union[typing.Optional[str], typing.List[str]]. Entity date of birth

            - contact: typing.Union[typing.Optional[str], typing.List[str]]. Entity contact

            - type: typing.Union[typing.Optional[str], typing.List[str]]. Entity type. If multiple values are passed for any field, the endpoint will match entities with ANY of the values.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/resolution"),
            params=remove_none_from_dict(
                {
                    "name": name,
                    "identifier": identifier,
                    "country": country,
                    "address": address,
                    "date_of_birth": date_of_birth,
                    "contact": contact,
                    "type": type,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ResolutionResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncResolutionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def resolution(
        self,
        *,
        name: typing.Union[typing.Optional[str], typing.List[str]],
        identifier: typing.Union[typing.Optional[str], typing.List[str]],
        country: typing.Union[typing.Optional[str], typing.List[str]],
        address: typing.Union[typing.Optional[str], typing.List[str]],
        date_of_birth: typing.Union[typing.Optional[str], typing.List[str]],
        contact: typing.Union[typing.Optional[str], typing.List[str]],
        type: typing.Union[typing.Optional[str], typing.List[str]],
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters:
            - name: typing.Union[typing.Optional[str], typing.List[str]]. Entity name

            - identifier: typing.Union[typing.Optional[str], typing.List[str]]. Entity identifier

            - country: typing.Union[typing.Optional[str], typing.List[str]]. Entity country

            - address: typing.Union[typing.Optional[str], typing.List[str]]. Entity address

            - date_of_birth: typing.Union[typing.Optional[str], typing.List[str]]. Entity date of birth

            - contact: typing.Union[typing.Optional[str], typing.List[str]]. Entity contact

            - type: typing.Union[typing.Optional[str], typing.List[str]]. Entity type. If multiple values are passed for any field, the endpoint will match entities with ANY of the values.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/resolution"),
            params=remove_none_from_dict(
                {
                    "name": name,
                    "identifier": identifier,
                    "country": country,
                    "address": address,
                    "date_of_birth": date_of_birth,
                    "contact": contact,
                    "type": type,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ResolutionResponse, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
