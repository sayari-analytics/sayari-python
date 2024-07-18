# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
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
        risk: typing.Optional[typing.Sequence[Risk]] = None,
        not_risk: typing.Optional[typing.Sequence[Risk]] = None,
        countries: typing.Optional[typing.Sequence[Country]] = None,
        not_countries: typing.Optional[typing.Sequence[Country]] = None,
        product: typing.Optional[typing.Sequence[str]] = None,
        not_product: typing.Optional[typing.Sequence[str]] = None,
        component: typing.Optional[typing.Sequence[str]] = None,
        not_component: typing.Optional[typing.Sequence[str]] = None,
        min_date: typing.Optional[str] = None,
        max_date: typing.Optional[str] = None,
        max_depth: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpstreamTradeTraversalResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Execute a traversal of the upstream trade network (supply chain) of an entity, returning a set of entities and edges between them.

        Parameters
        ----------
        id : str
            The root entity identifier.

        risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has 1+ of the specified [risk factors](/sayari-library/ontology/risk-factors).

        not_risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has none of the specified [risk factors](/sayari-library/ontology/risk-factors).

        countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in 1+ of the specified countries.

        not_countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in none of the specified countries.

        product : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has 1+ of the specified HS codes.

        not_product : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has none of the specified HS codes.

        component : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain at least one edge with 1+ of the specified HS codes.

        not_component : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain no edges with any of the specified HS codes.

        min_date : typing.Optional[str]
            Minimum date edge filter. Only return supply chains with edge dates that are greater than or equal to this date.

        max_date : typing.Optional[str]
            Maximum date edge filter. Only return supply chains with edge dates that are less than or equal to this date.

        max_depth : typing.Optional[int]
            The maximum depth of the traversal, from 1 to 4 inclusive. Default is 4. Reduce if query is timing out.

        limit : typing.Optional[int]
            The maximum number of results to return. Default and maximum values are 25,000.

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
            min_date="2023-03-15",
            product=["3204"],
            risk=["forced_labor_xinjiang_origin_subtier"],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/supply_chain/upstream/{jsonable_encoder(id)}",
            method="GET",
            params={
                "risk": jsonable_encoder(risk),
                "-risk": jsonable_encoder(not_risk),
                "countries": jsonable_encoder(countries),
                "-countries": jsonable_encoder(not_countries),
                "product": jsonable_encoder(product),
                "-product": jsonable_encoder(not_product),
                "component": jsonable_encoder(component),
                "-component": jsonable_encoder(not_component),
                "min_date": min_date,
                "max_date": max_date,
                "max_depth": max_depth,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(UpstreamTradeTraversalResponse, _response.json())  # type: ignore
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


class AsyncSupplyChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upstream_trade_traversal(
        self,
        id: str,
        *,
        risk: typing.Optional[typing.Sequence[Risk]] = None,
        not_risk: typing.Optional[typing.Sequence[Risk]] = None,
        countries: typing.Optional[typing.Sequence[Country]] = None,
        not_countries: typing.Optional[typing.Sequence[Country]] = None,
        product: typing.Optional[typing.Sequence[str]] = None,
        not_product: typing.Optional[typing.Sequence[str]] = None,
        component: typing.Optional[typing.Sequence[str]] = None,
        not_component: typing.Optional[typing.Sequence[str]] = None,
        min_date: typing.Optional[str] = None,
        max_date: typing.Optional[str] = None,
        max_depth: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpstreamTradeTraversalResponse:
        """
        <Warning>This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> Execute a traversal of the upstream trade network (supply chain) of an entity, returning a set of entities and edges between them.

        Parameters
        ----------
        id : str
            The root entity identifier.

        risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has 1+ of the specified [risk factors](/sayari-library/ontology/risk-factors).

        not_risk : typing.Optional[typing.Sequence[Risk]]
            Risk leaf node filter. Only return supply chains that end with a supplier that has none of the specified [risk factors](/sayari-library/ontology/risk-factors).

        countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in 1+ of the specified countries.

        not_countries : typing.Optional[typing.Sequence[Country]]
            Country leaf node filter. Only return supply chains that end with a supplier in none of the specified countries.

        product : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has 1+ of the specified HS codes.

        not_product : typing.Optional[typing.Sequence[str]]
            Product root edge filter. Only return supply chains that start with an edge that has none of the specified HS codes.

        component : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain at least one edge with 1+ of the specified HS codes.

        not_component : typing.Optional[typing.Sequence[str]]
            Component node filter. Only return supply chains that contain no edges with any of the specified HS codes.

        min_date : typing.Optional[str]
            Minimum date edge filter. Only return supply chains with edge dates that are greater than or equal to this date.

        max_date : typing.Optional[str]
            Maximum date edge filter. Only return supply chains with edge dates that are less than or equal to this date.

        max_depth : typing.Optional[int]
            The maximum depth of the traversal, from 1 to 4 inclusive. Default is 4. Reduce if query is timing out.

        limit : typing.Optional[int]
            The maximum number of results to return. Default and maximum values are 25,000.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpstreamTradeTraversalResponse

        Examples
        --------
        import asyncio

        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.supply_chain.upstream_trade_traversal(
                id="ESkH7J-UCRfY5t0_JXIH3w",
                min_date="2023-03-15",
                product=["3204"],
                risk=["forced_labor_xinjiang_origin_subtier"],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/supply_chain/upstream/{jsonable_encoder(id)}",
            method="GET",
            params={
                "risk": jsonable_encoder(risk),
                "-risk": jsonable_encoder(not_risk),
                "countries": jsonable_encoder(countries),
                "-countries": jsonable_encoder(not_countries),
                "product": jsonable_encoder(product),
                "-product": jsonable_encoder(not_product),
                "component": jsonable_encoder(component),
                "-component": jsonable_encoder(not_component),
                "min_date": min_date,
                "max_date": max_date,
                "max_depth": max_depth,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(UpstreamTradeTraversalResponse, _response.json())  # type: ignore
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
