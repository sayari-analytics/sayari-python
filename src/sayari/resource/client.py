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
from .types.delete_resource_response import DeleteResourceResponse
from .types.resource_type import ResourceType
from .types.save_entity_request import SaveEntityRequest
from .types.save_entity_response import SaveEntityResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def save_entity(
        self, *, request: SaveEntityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEntityResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Save an entity to a project.

        Parameters
        ----------
        request : SaveEntityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SaveEntityResponse

        Examples
        --------
        from sayari import SaveEntityRequest
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resource.save_entity(
            request=SaveEntityRequest(
                type="entity",
                project="GNJbkG",
                entity_id="Zk0qOaM2SSYg_ZhsljykMQ",
                custom_fields={"properties": {"custom_name": "Victoria Beckham"}},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/resource/entity", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SaveEntityResponse, _response.json())  # type: ignore
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

    def delete_resource(
        self, type: ResourceType, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResourceResponse:
        """
        Deletes an existing saved resource from a project.

        Parameters
        ----------
        type : ResourceType

        resource_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResourceResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resource.delete_resource(
            type="entity",
            resource_id="YWmNKV",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/resource/{jsonable_encoder(type)}/{jsonable_encoder(resource_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(DeleteResourceResponse, _response.json())  # type: ignore
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


class AsyncResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def save_entity(
        self, *, request: SaveEntityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> SaveEntityResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Save an entity to a project.

        Parameters
        ----------
        request : SaveEntityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SaveEntityResponse

        Examples
        --------
        from sayari import SaveEntityRequest
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.resource.save_entity(
            request=SaveEntityRequest(
                type="entity",
                project="GNJbkG",
                entity_id="Zk0qOaM2SSYg_ZhsljykMQ",
                custom_fields={"properties": {"custom_name": "Victoria Beckham"}},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/resource/entity", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(SaveEntityResponse, _response.json())  # type: ignore
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

    async def delete_resource(
        self, type: ResourceType, resource_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteResourceResponse:
        """
        Deletes an existing saved resource from a project.

        Parameters
        ----------
        type : ResourceType

        resource_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteResourceResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.resource.delete_resource(
            type="entity",
            resource_id="YWmNKV",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/resource/{jsonable_encoder(type)}/{jsonable_encoder(resource_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(DeleteResourceResponse, _response.json())  # type: ignore
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
