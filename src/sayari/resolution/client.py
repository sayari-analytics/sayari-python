# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..generated_types.types.both_identifier_types import BothIdentifierTypes
from ..generated_types.types.country import Country
from ..generated_types.types.entities import Entities
from .types.profile_enum import ProfileEnum
from ..core.request_options import RequestOptions
from .types.resolution_response import ResolutionResponse
from ..core.pydantic_utilities import parse_obj_as
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.errors.not_acceptable import NotAcceptable
from ..shared_errors.types.not_acceptable_response import NotAcceptableResponse
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.resolution_body import ResolutionBody
from .types.resolution_persisted_response import ResolutionPersistedResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ResolutionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def resolution(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        profile: typing.Optional[ProfileEnum] = None,
        name_min_percentage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity name

        identifier : typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]
            Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

        country : typing.Optional[typing.Union[Country, typing.Sequence[Country]]]
            Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

        address : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity address

        date_of_birth : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity date of birth

        contact : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity contact

        type : typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]
            [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

        profile : typing.Optional[ProfileEnum]
            Profile can be used to switch between search algorithms. The default profile `corporate` is optimized for accurate entity attribute matching and is ideal for business verification and matching entities with corporate data. The `suppliers` profile is optimized for matching entities with extensive trade data. Ideal for supply chain and trade-related use cases.

        name_min_percentage : typing.Optional[int]
            Adding this param enable an alternative matching logic. It will set a minimum percentage of tokens needed to match with user input to be considered a "hit". Accepts integers from 0 to 100 inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionResponse

        Examples
        --------
        from sayari import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resolution.resolution(
            name="victoria beckham limited",
            limit=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/resolution",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
                "identifier": identifier,
                "country": country,
                "address": address,
                "date_of_birth": date_of_birth,
                "contact": contact,
                "type": type,
                "profile": profile,
                "name_min_percentage": name_min_percentage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionResponse,
                    parse_obj_as(
                        type_=ResolutionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def resolution_post(
        self,
        *,
        request: ResolutionBody,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters
        ----------
        request : ResolutionBody

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionResponse

        Examples
        --------
        from sayari import Sayari
        from sayari.resolution import ResolutionBody

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resolution.resolution_post(
            limit=1,
            request=ResolutionBody(
                name=["victoria beckham limited"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/resolution",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionResponse,
                    parse_obj_as(
                        type_=ResolutionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def resolution_persisted(
        self,
        project_id: str,
        *,
        request: ResolutionBody,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionPersistedResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> The persisted resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the resolution endpoint, except it also stores matched entities into user's project.

        Parameters
        ----------
        project_id : str
            Unique identifier of the project

        request : ResolutionBody

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionPersistedResponse

        Examples
        --------
        from sayari import Sayari
        from sayari.resolution import ResolutionBody

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.resolution.resolution_persisted(
            project_id="V03eYM",
            limit=1,
            request=ResolutionBody(
                name=["victoria beckham limited"],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/resolution/persisted/{jsonable_encoder(project_id)}",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionPersistedResponse,
                    parse_obj_as(
                        type_=ResolutionPersistedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
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
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        profile: typing.Optional[ProfileEnum] = None,
        name_min_percentage: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        name : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity name

        identifier : typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]
            Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

        country : typing.Optional[typing.Union[Country, typing.Sequence[Country]]]
            Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

        address : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity address

        date_of_birth : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity date of birth

        contact : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity contact

        type : typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]
            [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

        profile : typing.Optional[ProfileEnum]
            Profile can be used to switch between search algorithms. The default profile `corporate` is optimized for accurate entity attribute matching and is ideal for business verification and matching entities with corporate data. The `suppliers` profile is optimized for matching entities with extensive trade data. Ideal for supply chain and trade-related use cases.

        name_min_percentage : typing.Optional[int]
            Adding this param enable an alternative matching logic. It will set a minimum percentage of tokens needed to match with user input to be considered a "hit". Accepts integers from 0 to 100 inclusive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.resolution.resolution(
                name="victoria beckham limited",
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/resolution",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
                "identifier": identifier,
                "country": country,
                "address": address,
                "date_of_birth": date_of_birth,
                "contact": contact,
                "type": type,
                "profile": profile,
                "name_min_percentage": name_min_percentage,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionResponse,
                    parse_obj_as(
                        type_=ResolutionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def resolution_post(
        self,
        *,
        request: ResolutionBody,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionResponse:
        """
        The resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the search endpoint, except it's tuned to only return the best match so the client doesn't need to do as much or any post-processing work to filter down results.

        Parameters
        ----------
        request : ResolutionBody

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari
        from sayari.resolution import ResolutionBody

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.resolution.resolution_post(
                limit=1,
                request=ResolutionBody(
                    name=["victoria beckham limited"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/resolution",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionResponse,
                    parse_obj_as(
                        type_=ResolutionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def resolution_persisted(
        self,
        project_id: str,
        *,
        request: ResolutionBody,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ResolutionPersistedResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> The persisted resolution endpoints allow users to search for matching entities against a provided list of attributes. The endpoint is similar to the resolution endpoint, except it also stores matched entities into user's project.

        Parameters
        ----------
        project_id : str
            Unique identifier of the project

        request : ResolutionBody

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10 inclusive. Defaults to 10.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ResolutionPersistedResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari
        from sayari.resolution import ResolutionBody

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.resolution.resolution_persisted(
                project_id="V03eYM",
                limit=1,
                request=ResolutionBody(
                    name=["victoria beckham limited"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/resolution/persisted/{jsonable_encoder(project_id)}",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ResolutionPersistedResponse,
                    parse_obj_as(
                        type_=ResolutionPersistedResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 400:
                raise BadRequest(
                    typing.cast(
                        BadRequestResponse,
                        parse_obj_as(
                            type_=BadRequestResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 401:
                raise Unauthorized(
                    typing.cast(
                        UnauthorizedResponse,
                        parse_obj_as(
                            type_=UnauthorizedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    typing.cast(
                        MethodNotAllowedResponse,
                        parse_obj_as(
                            type_=MethodNotAllowedResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 406:
                raise NotAcceptable(
                    typing.cast(
                        NotAcceptableResponse,
                        parse_obj_as(
                            type_=NotAcceptableResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 429:
                raise RateLimitExceeded(
                    typing.cast(
                        RateLimitResponse,
                        parse_obj_as(
                            type_=RateLimitResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    typing.cast(
                        InternalServerErrorResponse,
                        parse_obj_as(
                            type_=InternalServerErrorResponse,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
