# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..shared_errors.errors.bad_gateway import BadGateway
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.connection_error import ConnectionError
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_gateway_response import BadGatewayResponse
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.connection_error_response import ConnectionErrorResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.add_attribute import AddAttribute
from .types.attribute_response import AttributeResponse
from .types.update_attribute import UpdateAttribute

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AttributesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_attribute(
        self, *, request: AddAttribute, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Adds a new Attribute

        Parameters
        ----------
        request : AddAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        from sayari import AddAttribute
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.attributes.post_attribute(
            request=AddAttribute(
                entity="zq04axX2dLn9tE6W6Q8Qhg",
                type="address",
                value={
                    "street1": "1600 Pennsylvania Avenue NW",
                    "city": "Washington DC",
                    "state": "Washington DC",
                    "postalCode": "20500",
                    "country": "US",
                },
                to_date="2024-04-30",
                from_date="2024-01-01",
                date="2024-02-15",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/attribute", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def patch_attribute(
        self, attribute_id: str, *, request: UpdateAttribute, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Updates an existing Attribute

        Parameters
        ----------
        attribute_id : str

        request : UpdateAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        from sayari import UpdateAttribute
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.attributes.patch_attribute(
            attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
            request=UpdateAttribute(
                value={
                    "street1": "1600 Pennsylvania Avenue NW",
                    "city": "Washington DC",
                    "state": "Washington DC",
                    "postalCode": "20500",
                    "country": "US",
                },
                to_date="2024-04-30",
                from_date="2024-01-01",
                date="2024-02-15",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/attribute/{jsonable_encoder(attribute_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_attribute(
        self, attribute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Delete an existing Attribute

        Parameters
        ----------
        attribute_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.attributes.delete_attribute(
            attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/attribute/{jsonable_encoder(attribute_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAttributesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_attribute(
        self, *, request: AddAttribute, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Adds a new Attribute

        Parameters
        ----------
        request : AddAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        import asyncio

        from sayari import AddAttribute
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.attributes.post_attribute(
                request=AddAttribute(
                    entity="zq04axX2dLn9tE6W6Q8Qhg",
                    type="address",
                    value={
                        "street1": "1600 Pennsylvania Avenue NW",
                        "city": "Washington DC",
                        "state": "Washington DC",
                        "postalCode": "20500",
                        "country": "US",
                    },
                    to_date="2024-04-30",
                    from_date="2024-01-01",
                    date="2024-02-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/attribute", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def patch_attribute(
        self, attribute_id: str, *, request: UpdateAttribute, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Updates an existing Attribute

        Parameters
        ----------
        attribute_id : str

        request : UpdateAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        import asyncio

        from sayari import UpdateAttribute
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.attributes.patch_attribute(
                attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
                request=UpdateAttribute(
                    value={
                        "street1": "1600 Pennsylvania Avenue NW",
                        "city": "Washington DC",
                        "state": "Washington DC",
                        "postalCode": "20500",
                        "country": "US",
                    },
                    to_date="2024-04-30",
                    from_date="2024-01-01",
                    date="2024-02-15",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/attribute/{jsonable_encoder(attribute_id)}",
            method="PATCH",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_attribute(
        self, attribute_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AttributeResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Delete an existing Attribute

        Parameters
        ----------
        attribute_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AttributeResponse

        Examples
        --------
        import asyncio

        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.attributes.delete_attribute(
                attribute_id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/attribute/{jsonable_encoder(attribute_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(AttributeResponse, _response.json())  # type: ignore
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
            if _response.status_code == 502:
                raise BadGateway(pydantic_v1.parse_obj_as(BadGatewayResponse, _response.json()))  # type: ignore
            if _response.status_code == 520:
                raise ConnectionError(
                    pydantic_v1.parse_obj_as(ConnectionErrorResponse, _response.json())  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
