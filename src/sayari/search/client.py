# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_acceptable import NotAcceptable
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_acceptable_response import NotAcceptableResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from ..shared_types.types.search_field import SearchField
from .types.entity_search_response import EntitySearchResponse
from .types.filter_list import FilterList
from .types.record_search_response import RecordSearchResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_entity(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Sequence[SearchField]] = OMIT,
        filter: typing.Optional[FilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySearchResponse:
        """
        Search for an entity. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Sequence[SearchField]]
            Record or entity fields to search against.

        filter : typing.Optional[FilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        geo_facets : typing.Optional[bool]
            Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitySearchResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.search.search_entity(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/entity",
            method="POST",
            params={"limit": limit, "offset": offset},
            json={
                "q": q,
                "fields": fields,
                "filter": filter,
                "facets": facets,
                "geo_facets": geo_facets,
                "advanced": advanced,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntitySearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    def search_entity_get(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]] = None,
        facets: typing.Optional[bool] = None,
        geo_facets: typing.Optional[bool] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySearchResponse:
        """
        Search for an entity. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]
            Record or entity fields to search against.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        geo_facets : typing.Optional[bool]
            Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitySearchResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.search.search_entity_get(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/entity",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "q": q,
                "fields": fields,
                "facets": facets,
                "geo_facets": geo_facets,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntitySearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    def search_record(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Sequence[SearchField]] = OMIT,
        filter: typing.Optional[FilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RecordSearchResponse:
        """
        Search for a record. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Sequence[SearchField]]
            Record or entity fields to search against.

        filter : typing.Optional[FilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordSearchResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.search.search_record(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/record",
            method="POST",
            params={"limit": limit, "offset": offset},
            json={"q": q, "fields": fields, "filter": filter, "facets": facets, "advanced": advanced},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RecordSearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    def search_record_get(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]] = None,
        facets: typing.Optional[bool] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RecordSearchResponse:
        """
        Search for a record. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]
            Record or entity fields to search against.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordSearchResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.search.search_record_get(
            q="victoria beckham limited",
            limit=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/search/record",
            method="GET",
            params={"limit": limit, "offset": offset, "q": q, "fields": fields, "facets": facets, "advanced": advanced},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RecordSearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_entity(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Sequence[SearchField]] = OMIT,
        filter: typing.Optional[FilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        geo_facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySearchResponse:
        """
        Search for an entity. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Sequence[SearchField]]
            Record or entity fields to search against.

        filter : typing.Optional[FilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        geo_facets : typing.Optional[bool]
            Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitySearchResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.search.search_entity(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/entity",
            method="POST",
            params={"limit": limit, "offset": offset},
            json={
                "q": q,
                "fields": fields,
                "filter": filter,
                "facets": facets,
                "geo_facets": geo_facets,
                "advanced": advanced,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntitySearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    async def search_entity_get(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]] = None,
        facets: typing.Optional[bool] = None,
        geo_facets: typing.Optional[bool] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> EntitySearchResponse:
        """
        Search for an entity. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]
            Record or entity fields to search against.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        geo_facets : typing.Optional[bool]
            Whether or not to return search geo bound facets in results giving counts by geo tile. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitySearchResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.search.search_entity_get(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/entity",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "q": q,
                "fields": fields,
                "facets": facets,
                "geo_facets": geo_facets,
                "advanced": advanced,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(EntitySearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    async def search_record(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Sequence[SearchField]] = OMIT,
        filter: typing.Optional[FilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        advanced: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RecordSearchResponse:
        """
        Search for a record. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Sequence[SearchField]]
            Record or entity fields to search against.

        filter : typing.Optional[FilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordSearchResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.search.search_record(
            limit=1,
            q="victoria beckham limited",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/record",
            method="POST",
            params={"limit": limit, "offset": offset},
            json={"q": q, "fields": fields, "filter": filter, "facets": facets, "advanced": advanced},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RecordSearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    async def search_record_get(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        fields: typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]] = None,
        facets: typing.Optional[bool] = None,
        advanced: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> RecordSearchResponse:
        """
        Search for a record. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        fields : typing.Optional[typing.Union[SearchField, typing.Sequence[SearchField]]]
            Record or entity fields to search against.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        advanced : typing.Optional[bool]
            Set to true to enable full elasticsearch query string syntax which allows for fielded search and more complex operators. Note that the syntax is more strict and can result in empty result-sets. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RecordSearchResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.search.search_record_get(
            q="victoria beckham limited",
            limit=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/search/record",
            method="GET",
            params={"limit": limit, "offset": offset, "q": q, "fields": fields, "facets": facets, "advanced": advanced},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(RecordSearchResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 405:
                raise MethodNotAllowed(
                    pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json())  # type: ignore
                )
            if _response.status_code == 406:
                raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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
