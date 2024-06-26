# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.history_response import HistoryResponse
from .types.usage_response import UsageResponse


class InfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_usage(
        self,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> UsageResponse:
        """
        The usage endpoint provides a simple interface to retrieve information on usage made by your API account. This includes both views per API path and credits consumed. The time period for the usage query is also specified in the response and whether or not this includes total usage.

        Parameters
        ----------
        from_ : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the starting time period to obtain usage stats. In the format YYYY-MM-DD

        to : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the ending time period to obtain usage stats. In the format YYYY-MM-DD

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageResponse
            OK

        Examples
        --------
        import datetime

        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.info.get_usage(
            from_=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            to=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/usage",
            method="GET",
            params={"from": str(from_) if from_ is not None else None, "to": str(to) if to is not None else None},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(UsageResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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

    def get_history(
        self,
        *,
        events: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        size: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> HistoryResponse:
        """
        The history endpoint return a user's event history.

        Parameters
        ----------
        events : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The type of events to filter on.

        from_ : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the starting time period for the events. In the format YYYY-MM-DD

        to : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the ending time period for the events. In the format YYYY-MM-DD

        size : typing.Optional[int]
            Size to limit number of events returned

        token : typing.Optional[str]
            Pagination token to retrieve the next page of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryResponse
            OK

        Examples
        --------
        import datetime

        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.info.get_history(
            events="string",
            from_=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            to=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            size=1,
            token="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/history",
            method="GET",
            params={
                "events": events,
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "size": size,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(HistoryResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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


class AsyncInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_usage(
        self,
        *,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> UsageResponse:
        """
        The usage endpoint provides a simple interface to retrieve information on usage made by your API account. This includes both views per API path and credits consumed. The time period for the usage query is also specified in the response and whether or not this includes total usage.

        Parameters
        ----------
        from_ : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the starting time period to obtain usage stats. In the format YYYY-MM-DD

        to : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the ending time period to obtain usage stats. In the format YYYY-MM-DD

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsageResponse
            OK

        Examples
        --------
        import datetime

        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.info.get_usage(
            from_=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            to=datetime.date.fromisoformat(
                "2023-01-15",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/usage",
            method="GET",
            params={"from": str(from_) if from_ is not None else None, "to": str(to) if to is not None else None},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(UsageResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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

    async def get_history(
        self,
        *,
        events: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_: typing.Optional[dt.date] = None,
        to: typing.Optional[dt.date] = None,
        size: typing.Optional[int] = None,
        token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None
    ) -> HistoryResponse:
        """
        The history endpoint return a user's event history.

        Parameters
        ----------
        events : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The type of events to filter on.

        from_ : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the starting time period for the events. In the format YYYY-MM-DD

        to : typing.Optional[dt.date]
            An ISO 8601 encoded date string indicating the ending time period for the events. In the format YYYY-MM-DD

        size : typing.Optional[int]
            Size to limit number of events returned

        token : typing.Optional[str]
            Pagination token to retrieve the next page of results

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HistoryResponse
            OK

        Examples
        --------
        import datetime

        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.info.get_history(
            events="string",
            from_=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            to=datetime.date.fromisoformat(
                "2023-01-15",
            ),
            size=1,
            token="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/history",
            method="GET",
            params={
                "events": events,
                "from": str(from_) if from_ is not None else None,
                "to": str(to) if to is not None else None,
                "size": size,
                "token": token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return pydantic_v1.parse_obj_as(HistoryResponse, _response.json())  # type: ignore
            if _response.status_code == 400:
                raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
            if _response.status_code == 401:
                raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
            if _response.status_code == 404:
                raise NotFound(pydantic_v1.parse_obj_as(NotFoundResponse, _response.json()))  # type: ignore
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
