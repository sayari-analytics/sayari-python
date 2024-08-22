# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from .types.trade_filter_list import TradeFilterList
from ..core.request_options import RequestOptions
from .types.shipment_search_response import ShipmentSearchResponse
from ..core.pydantic_utilities import parse_obj_as
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.supplier_search_response import SupplierSearchResponse
from .types.buyer_search_response import BuyerSearchResponse
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TradeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_shipments(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShipmentSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a shipment. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShipmentSearchResponse

        Examples
        --------
        from sayari import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_shipments(
            limit=1,
            q="rum",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trade/search/shipments",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ShipmentSearchResponse,
                    parse_obj_as(
                        type_=ShipmentSearchResponse,  # type: ignore
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

    def search_suppliers(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SupplierSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a supplier. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SupplierSearchResponse

        Examples
        --------
        from sayari import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_suppliers(
            limit=1,
            q="rum",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trade/search/suppliers",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SupplierSearchResponse,
                    parse_obj_as(
                        type_=SupplierSearchResponse,  # type: ignore
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

    def search_buyers(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuyerSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a buyer. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuyerSearchResponse

        Examples
        --------
        from sayari import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_buyers(
            limit=1,
            q="rum",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/trade/search/buyers",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BuyerSearchResponse,
                    parse_obj_as(
                        type_=BuyerSearchResponse,  # type: ignore
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


class AsyncTradeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_shipments(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ShipmentSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a shipment. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ShipmentSearchResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.trade.search_shipments(
                limit=1,
                q="rum",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trade/search/shipments",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    ShipmentSearchResponse,
                    parse_obj_as(
                        type_=ShipmentSearchResponse,  # type: ignore
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

    async def search_suppliers(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SupplierSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a supplier. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SupplierSearchResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.trade.search_suppliers(
                limit=1,
                q="rum",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trade/search/suppliers",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SupplierSearchResponse,
                    parse_obj_as(
                        type_=SupplierSearchResponse,  # type: ignore
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

    async def search_buyers(
        self,
        *,
        q: str,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter: typing.Optional[TradeFilterList] = OMIT,
        facets: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuyerSearchResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Search for a buyer. Please note, searches are limited to a maximum of 10,000 results.

        Parameters
        ----------
        q : str
            Query term. The syntax for the query parameter follows elasticsearch simple query string syntax. The includes the ability to use search operators and to perform nested queries. Must be url encoded.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned with a range between 1 and 10000. Defaults to 100.

        offset : typing.Optional[int]
            Number of results to skip before returning response. Defaults to 0.

        filter : typing.Optional[TradeFilterList]
            Filters to be applied to search query to limit the result-set.

        facets : typing.Optional[bool]
            Whether or not to return search facets in results giving counts by field. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuyerSearchResponse

        Examples
        --------
        import asyncio

        from sayari import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.trade.search_buyers(
                limit=1,
                q="rum",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/trade/search/buyers",
            method="POST",
            params={
                "limit": limit,
                "offset": offset,
            },
            json={
                "q": q,
                "filter": filter,
                "facets": facets,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    BuyerSearchResponse,
                    parse_obj_as(
                        type_=BuyerSearchResponse,  # type: ignore
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
