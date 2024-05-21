# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.buyer_search_response import BuyerSearchResponse
from .types.shipment_search_response import ShipmentSearchResponse
from .types.supplier_search_response import SupplierSearchResponse
from .types.trade_filter_list import TradeFilterList

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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_shipments(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/shipments"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ShipmentSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_suppliers(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/suppliers"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(SupplierSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.trade.search_buyers(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/buyers"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BuyerSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.trade.search_shipments(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/shipments"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ShipmentSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.trade.search_suppliers(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/suppliers"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(SupplierSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
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
            A limit on the number of objects to be returned with a range between 1 and 100. Defaults to 100.

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
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.trade.search_buyers(
            limit=1,
            q="rum",
        )
        """
        _request: typing.Dict[str, typing.Any] = {"q": q}
        if filter is not OMIT:
            _request["filter"] = filter
        if facets is not OMIT:
            _request["facets"] = facets
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/trade/search/buyers"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "limit": limit,
                            "offset": offset,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BuyerSearchResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise RateLimitExceeded(pydantic_v1.parse_obj_as(RateLimitResponse, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(
                pydantic_v1.parse_obj_as(InternalServerErrorResponse, _response.json())  # type: ignore
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
