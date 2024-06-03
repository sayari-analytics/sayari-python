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
from ..generated_types.types.country import Country
from ..generated_types.types.risk import Risk
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
from .types.upstream_trade_traversal_response import UpstreamTradeTraversalResponse


class SupplyChainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upstream_trade_traversal(
        self,
        id: str,
        *,
        countries: typing.Optional[typing.Sequence[Country]] = None,
        not_countries: typing.Optional[typing.Sequence[Country]] = None,
        risks: typing.Optional[typing.Sequence[Risk]] = None,
        not_risk: typing.Optional[typing.Sequence[Risk]] = None,
        hs_code: typing.Optional[typing.Sequence[str]] = None,
        not_hs_code: typing.Optional[typing.Sequence[str]] = None,
        components: typing.Optional[typing.Sequence[str]] = None,
        not_components: typing.Optional[typing.Sequence[str]] = None,
        max_depth: typing.Optional[int] = None,
        date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpstreamTradeTraversalResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Execute a traversal of the upstream trade network (supply chain) of an entity, returning a set of entities and edges between them.

        Parameters
        ----------
        id : str
            The root entity identifier.

        countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in 1+ of the specified countries.

        not_countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in none of the specified countries.

        risks : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has 1+ of the specified risk factors.

        not_risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has none of the specified risk factors.

        hs_code : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has 1+ of the specified HS codes.

        not_hs_code : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has none of the specified HS codes.

        components : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain at least one edge with 1+ of the specified HS codes.

        not_components : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain no edges with any of the specified HS codes.

        max_depth : typing.Optional[int]
            The maximum depth of the traversal, from 1 to 4 inclusive. Default is 4. Reduce if query is timing out.

        date : typing.Optional[str]
            The date range to filter the supply chain by by only considering shipments within the specified date range, inclusive. The date range is formatted as "YYYY-MM-DD|YYYY-MM-DD", where the first date is the start date and the second date is the end date. Both dates are optional, e.g. "|2022-01-01" will return all shipments up to and including 2022-01-01.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpstreamTradeTraversalResponse

        Examples
        --------
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.supply_chain.upstream_trade_traversal(
            id="ESkH7J-UCRfY5t0_JXIH3w",
            date="2023-06-01",
            hs_code=["3206"],
            components=["3204"],
            max_depth=2,
            risks=["forced_labor_uflpa_origin_subtier"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/upstream/{jsonable_encoder(id)}"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "countries": jsonable_encoder(countries),
                            "-countries": jsonable_encoder(not_countries),
                            "risks": jsonable_encoder(risks),
                            "-risks": jsonable_encoder(not_risk),
                            "hs_code": jsonable_encoder(hs_code),
                            "-hs_code": jsonable_encoder(not_hs_code),
                            "components": jsonable_encoder(components),
                            "-components": jsonable_encoder(not_components),
                            "max_depth": max_depth,
                            "date": date,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
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
            return pydantic_v1.parse_obj_as(UpstreamTradeTraversalResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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


class AsyncSupplyChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upstream_trade_traversal(
        self,
        id: str,
        *,
        countries: typing.Optional[typing.Sequence[Country]] = None,
        not_countries: typing.Optional[typing.Sequence[Country]] = None,
        risks: typing.Optional[typing.Sequence[Risk]] = None,
        not_risk: typing.Optional[typing.Sequence[Risk]] = None,
        hs_code: typing.Optional[typing.Sequence[str]] = None,
        not_hs_code: typing.Optional[typing.Sequence[str]] = None,
        components: typing.Optional[typing.Sequence[str]] = None,
        not_components: typing.Optional[typing.Sequence[str]] = None,
        max_depth: typing.Optional[int] = None,
        date: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpstreamTradeTraversalResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Execute a traversal of the upstream trade network (supply chain) of an entity, returning a set of entities and edges between them.

        Parameters
        ----------
        id : str
            The root entity identifier.

        countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in 1+ of the specified countries.

        not_countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in none of the specified countries.

        risks : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has 1+ of the specified risk factors.

        not_risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has none of the specified risk factors.

        hs_code : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has 1+ of the specified HS codes.

        not_hs_code : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has none of the specified HS codes.

        components : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain at least one edge with 1+ of the specified HS codes.

        not_components : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain no edges with any of the specified HS codes.

        max_depth : typing.Optional[int]
            The maximum depth of the traversal, from 1 to 4 inclusive. Default is 4. Reduce if query is timing out.

        date : typing.Optional[str]
            The date range to filter the supply chain by by only considering shipments within the specified date range, inclusive. The date range is formatted as "YYYY-MM-DD|YYYY-MM-DD", where the first date is the start date and the second date is the end date. Both dates are optional, e.g. "|2022-01-01" will return all shipments up to and including 2022-01-01.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpstreamTradeTraversalResponse

        Examples
        --------
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.supply_chain.upstream_trade_traversal(
            id="ESkH7J-UCRfY5t0_JXIH3w",
            date="2023-06-01",
            hs_code=["3206"],
            components=["3204"],
            max_depth=2,
            risks=["forced_labor_uflpa_origin_subtier"],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/upstream/{jsonable_encoder(id)}"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "countries": jsonable_encoder(countries),
                            "-countries": jsonable_encoder(not_countries),
                            "risks": jsonable_encoder(risks),
                            "-risks": jsonable_encoder(not_risk),
                            "hs_code": jsonable_encoder(hs_code),
                            "-hs_code": jsonable_encoder(not_hs_code),
                            "components": jsonable_encoder(components),
                            "-components": jsonable_encoder(not_components),
                            "max_depth": max_depth,
                            "date": date,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
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
            return pydantic_v1.parse_obj_as(UpstreamTradeTraversalResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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