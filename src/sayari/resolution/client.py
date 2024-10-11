# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..generated_types.types.country import Country
from ..generated_types.types.both_identifier_types import BothIdentifierTypes
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
from ..core.serialization import convert_and_respect_annotation_metadata
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
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        profile: typing.Optional[ProfileEnum] = None,
        name_min_percentage: typing.Optional[int] = None,
        name_min_tokens: typing.Optional[int] = None,
        minimum_score_threshold: typing.Optional[int] = None,
        search_fallback: typing.Optional[bool] = None,
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

        address : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity address. For optimal matching results, it's recommended to concatenate the full address string (street, city, state, postal code).

        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity city that contains the provided city name.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity state that contains the provided state name.

        country : typing.Optional[typing.Union[Country, typing.Sequence[Country]]]
            Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

        identifier : typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]
            Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

        date_of_birth : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity date of birth

        contact : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity contact

        type : typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]
            [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

        profile : typing.Optional[ProfileEnum]
            Specifies the search algorithm to use. `corporate` (default) is optimized for accurate entity attribute matching, ideal for business verification. `suppliers` is tailored for matching entities with trade data, suitable for supply chain use cases. `search` mimics /search/entity behavior, best for name-only matches.

        name_min_percentage : typing.Optional[int]
            Adding this param enables an alternative matching logic. It will set a minimum percentage of tokens needed to match with user input to be considered a "hit". Accepts integers from 0 to 100 inclusive.

        name_min_tokens : typing.Optional[int]
            Adding this param enables an alternative matching logic. It sets the minimum number of matching tokens the resolved hits need to have in common with the user input to be considered a "hit". Accepts non-negative integers.

        minimum_score_threshold : typing.Optional[int]
            Specifies the minimum score required to pass, which controls the strictness of the matching threshold. The default value is 77, and tuned for general use-case accuracy. Increase the value for stricter matching, reduce to loosen.

        search_fallback : typing.Optional[bool]
            Enables a name search fallback when either the corporate or supplier profiles fails to find a match. When invoked, the fallback will make a call similar to /search/entity on name only. By default set to true.

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
            name="Thomas Bangalter",
            address="8 AVENUE RACHEL",
            country="FRA",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/resolution",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "name": name,
                "address": address,
                "city": city,
                "state": state,
                "country": country,
                "identifier": identifier,
                "date_of_birth": date_of_birth,
                "contact": contact,
                "type": type,
                "profile": profile,
                "name_min_percentage": name_min_percentage,
                "name_min_tokens": name_min_tokens,
                "minimum_score_threshold": minimum_score_threshold,
                "search_fallback": search_fallback,
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
            json=convert_and_respect_annotation_metadata(object_=request, annotation=ResolutionBody, direction="write"),
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


class AsyncResolutionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def resolution(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        name: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        address: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        city: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        state: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        country: typing.Optional[typing.Union[Country, typing.Sequence[Country]]] = None,
        identifier: typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]] = None,
        date_of_birth: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contact: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        type: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        profile: typing.Optional[ProfileEnum] = None,
        name_min_percentage: typing.Optional[int] = None,
        name_min_tokens: typing.Optional[int] = None,
        minimum_score_threshold: typing.Optional[int] = None,
        search_fallback: typing.Optional[bool] = None,
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

        address : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity address. For optimal matching results, it's recommended to concatenate the full address string (street, city, state, postal code).

        city : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity city that contains the provided city name.

        state : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity state that contains the provided state name.

        country : typing.Optional[typing.Union[Country, typing.Sequence[Country]]]
            Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)

        identifier : typing.Optional[typing.Union[BothIdentifierTypes, typing.Sequence[BothIdentifierTypes]]]
            Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.

        date_of_birth : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity date of birth

        contact : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Entity contact

        type : typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]
            [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.

        profile : typing.Optional[ProfileEnum]
            Specifies the search algorithm to use. `corporate` (default) is optimized for accurate entity attribute matching, ideal for business verification. `suppliers` is tailored for matching entities with trade data, suitable for supply chain use cases. `search` mimics /search/entity behavior, best for name-only matches.

        name_min_percentage : typing.Optional[int]
            Adding this param enables an alternative matching logic. It will set a minimum percentage of tokens needed to match with user input to be considered a "hit". Accepts integers from 0 to 100 inclusive.

        name_min_tokens : typing.Optional[int]
            Adding this param enables an alternative matching logic. It sets the minimum number of matching tokens the resolved hits need to have in common with the user input to be considered a "hit". Accepts non-negative integers.

        minimum_score_threshold : typing.Optional[int]
            Specifies the minimum score required to pass, which controls the strictness of the matching threshold. The default value is 77, and tuned for general use-case accuracy. Increase the value for stricter matching, reduce to loosen.

        search_fallback : typing.Optional[bool]
            Enables a name search fallback when either the corporate or supplier profiles fails to find a match. When invoked, the fallback will make a call similar to /search/entity on name only. By default set to true.

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
                name="Thomas Bangalter",
                address="8 AVENUE RACHEL",
                country="FRA",
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
                "address": address,
                "city": city,
                "state": state,
                "country": country,
                "identifier": identifier,
                "date_of_birth": date_of_birth,
                "contact": contact,
                "type": type,
                "profile": profile,
                "name_min_percentage": name_min_percentage,
                "name_min_tokens": name_min_tokens,
                "minimum_score_threshold": minimum_score_threshold,
                "search_fallback": search_fallback,
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
            json=convert_and_respect_annotation_metadata(object_=request, annotation=ResolutionBody, direction="write"),
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
