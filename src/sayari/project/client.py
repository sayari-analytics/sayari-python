# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..generated_types.types.entities import Entities
from ..shared_errors.errors.bad_request import BadRequest
from ..shared_errors.errors.internal_server_error import InternalServerError
from ..shared_errors.errors.method_not_allowed import MethodNotAllowed
from ..shared_errors.errors.not_acceptable import NotAcceptable
from ..shared_errors.errors.not_found import NotFound
from ..shared_errors.errors.rate_limit_exceeded import RateLimitExceeded
from ..shared_errors.errors.unauthorized import Unauthorized
from ..shared_errors.types.bad_request_response import BadRequestResponse
from ..shared_errors.types.internal_server_error_response import InternalServerErrorResponse
from ..shared_errors.types.method_not_allowed_response import MethodNotAllowedResponse
from ..shared_errors.types.not_acceptable_response import NotAcceptableResponse
from ..shared_errors.types.not_found_response import NotFoundResponse
from ..shared_errors.types.rate_limit_response import RateLimitResponse
from ..shared_errors.types.unauthorized_response import UnauthorizedResponse
from .types.create_project_request import CreateProjectRequest
from .types.create_project_response import CreateProjectResponse
from .types.delete_project_response import DeleteProjectResponse
from .types.get_project_entities_accept_header import GetProjectEntitiesAcceptHeader
from .types.get_project_entities_response import GetProjectEntitiesResponse
from .types.get_projects_response import GetProjectsResponse
from .types.project_entities_aggs_definition import ProjectEntitiesAggsDefinition
from .types.project_entities_filter import ProjectEntitiesFilter
from .types.sort_field import SortField

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_project(
        self, *, request: CreateProjectRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateProjectResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Create a new project.

        Parameters:
            - request: CreateProjectRequest.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari import CreateProjectRequest
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.project.create_project(
            request=CreateProjectRequest(
                label="Project Alpha",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic_v1.parse_obj_as(CreateProjectResponse, _response.json())  # type: ignore
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

    def get_projects(
        self,
        *,
        next: typing.Optional[str] = None,
        prev: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectsResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Retrieve a list of projects including upload progress info.

        Parameters:
            - next: typing.Optional[str]. The pagination token for the next page of projects.

            - prev: typing.Optional[str]. The pagination token for the previous page of projects.

            - limit: typing.Optional[int]. Limit total values returned for projects. Defaults to 100. Max 100.

            - archived: typing.Optional[bool]. Toggle between projects that have been archived (true) or not (false). Defaults to false.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.project.get_projects(
            archived=False,
            limit=8,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "next": next,
                        "prev": prev,
                        "limit": limit,
                        "archived": archived,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
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
            return pydantic_v1.parse_obj_as(GetProjectsResponse, _response.json())  # type: ignore
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

    def get_project_entities(
        self,
        id: str,
        *,
        next: typing.Optional[str] = None,
        prev: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        entity_types: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        geo_facets: typing.Optional[bool] = None,
        hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        received_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        shipped_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        translation: typing.Optional[str] = None,
        sort: typing.Optional[SortField] = None,
        filters: typing.Optional[typing.Union[ProjectEntitiesFilter, typing.Sequence[ProjectEntitiesFilter]]] = None,
        aggregations: typing.Optional[
            typing.Union[ProjectEntitiesAggsDefinition, typing.Sequence[ProjectEntitiesAggsDefinition]]
        ] = None,
        accept: GetProjectEntitiesAcceptHeader,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectEntitiesResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Retrieve a list of entities in a project.

        Parameters:
            - id: str. The project identifier.

            - next: typing.Optional[str]. The pagination token for the next page of entities.

            - prev: typing.Optional[str]. The pagination token for the previous page of entities.

            - limit: typing.Optional[int]. Limit total entities returned. Defaults to 1,000. Max 10,000.

            - entity_types: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]. Only return entities of the specified [entity type(s)](/sayari-library/ontology/entities). Defaults to all types.

            - geo_facets: typing.Optional[bool]. Whether to include geo facets in the response. Defaults to false.

            - hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities with the specified HS code(s).

            - received_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities that received the specified HS code(s).

            - shipped_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities that shipped the specified HS code(s).

            - translation: typing.Optional[str]. The language code to translate the entity labels to. Defaults to the user's preferred language.

            - sort: typing.Optional[SortField].

            - filters: typing.Optional[typing.Union[ProjectEntitiesFilter, typing.Sequence[ProjectEntitiesFilter]]]. Only return entities that match the specified filters.

            - aggregations: typing.Optional[typing.Union[ProjectEntitiesAggsDefinition, typing.Sequence[ProjectEntitiesAggsDefinition]]]. Aggregations for entities in a project.

            - accept: GetProjectEntitiesAcceptHeader. The response format. Defaults to application/json.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.project.get_project_entities(
            id="gPq6EY",
            accept="application/json",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{jsonable_encoder(id)}/contents/entity"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "next": next,
                        "prev": prev,
                        "limit": limit,
                        "entity_types": entity_types,
                        "geo_facets": geo_facets,
                        "hs_codes": hs_codes,
                        "received_hs_codes": received_hs_codes,
                        "shipped_hs_codes": shipped_hs_codes,
                        "translation": translation,
                        "sort": sort,
                        "filters": filters,
                        "aggregations": aggregations,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Accept": str(accept) if accept is not None else None,
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
            return pydantic_v1.parse_obj_as(GetProjectEntitiesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    def delete_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProjectResponse:
        """
        Deletes an existing project.

        Parameters:
            - project_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import Sayari

        client = Sayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.project.delete_project(
            project_id="Gam5qG",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{jsonable_encoder(project_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic_v1.parse_obj_as(DeleteProjectResponse, _response.json())  # type: ignore
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


class AsyncProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_project(
        self, *, request: CreateProjectRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateProjectResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Create a new project.

        Parameters:
            - request: CreateProjectRequest.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari import CreateProjectRequest
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.project.create_project(
            request=CreateProjectRequest(
                label="Project Alpha",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return pydantic_v1.parse_obj_as(CreateProjectResponse, _response.json())  # type: ignore
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

    async def get_projects(
        self,
        *,
        next: typing.Optional[str] = None,
        prev: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectsResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Retrieve a list of projects including upload progress info.

        Parameters:
            - next: typing.Optional[str]. The pagination token for the next page of projects.

            - prev: typing.Optional[str]. The pagination token for the previous page of projects.

            - limit: typing.Optional[int]. Limit total values returned for projects. Defaults to 100. Max 100.

            - archived: typing.Optional[bool]. Toggle between projects that have been archived (true) or not (false). Defaults to false.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.project.get_projects(
            archived=False,
            limit=8,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v1/projects"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "next": next,
                        "prev": prev,
                        "limit": limit,
                        "archived": archived,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
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
            return pydantic_v1.parse_obj_as(GetProjectsResponse, _response.json())  # type: ignore
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

    async def get_project_entities(
        self,
        id: str,
        *,
        next: typing.Optional[str] = None,
        prev: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        entity_types: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]] = None,
        geo_facets: typing.Optional[bool] = None,
        hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        received_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        shipped_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        translation: typing.Optional[str] = None,
        sort: typing.Optional[SortField] = None,
        filters: typing.Optional[typing.Union[ProjectEntitiesFilter, typing.Sequence[ProjectEntitiesFilter]]] = None,
        aggregations: typing.Optional[
            typing.Union[ProjectEntitiesAggsDefinition, typing.Sequence[ProjectEntitiesAggsDefinition]]
        ] = None,
        accept: GetProjectEntitiesAcceptHeader,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetProjectEntitiesResponse:
        """
        <Callout intent="warning">This endpoint is in beta and is subject to change. It is provided for early access and testing purposes only.</Callout> Retrieve a list of entities in a project.

        Parameters:
            - id: str. The project identifier.

            - next: typing.Optional[str]. The pagination token for the next page of entities.

            - prev: typing.Optional[str]. The pagination token for the previous page of entities.

            - limit: typing.Optional[int]. Limit total entities returned. Defaults to 1,000. Max 10,000.

            - entity_types: typing.Optional[typing.Union[Entities, typing.Sequence[Entities]]]. Only return entities of the specified [entity type(s)](/sayari-library/ontology/entities). Defaults to all types.

            - geo_facets: typing.Optional[bool]. Whether to include geo facets in the response. Defaults to false.

            - hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities with the specified HS code(s).

            - received_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities that received the specified HS code(s).

            - shipped_hs_codes: typing.Optional[typing.Union[str, typing.Sequence[str]]]. Only return entities that shipped the specified HS code(s).

            - translation: typing.Optional[str]. The language code to translate the entity labels to. Defaults to the user's preferred language.

            - sort: typing.Optional[SortField].

            - filters: typing.Optional[typing.Union[ProjectEntitiesFilter, typing.Sequence[ProjectEntitiesFilter]]]. Only return entities that match the specified filters.

            - aggregations: typing.Optional[typing.Union[ProjectEntitiesAggsDefinition, typing.Sequence[ProjectEntitiesAggsDefinition]]]. Aggregations for entities in a project.

            - accept: GetProjectEntitiesAcceptHeader. The response format. Defaults to application/json.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.project.get_project_entities(
            id="gPq6EY",
            accept="application/json",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{jsonable_encoder(id)}/contents/entity"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "next": next,
                        "prev": prev,
                        "limit": limit,
                        "entity_types": entity_types,
                        "geo_facets": geo_facets,
                        "hs_codes": hs_codes,
                        "received_hs_codes": received_hs_codes,
                        "shipped_hs_codes": shipped_hs_codes,
                        "translation": translation,
                        "sort": sort,
                        "filters": filters,
                        "aggregations": aggregations,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        "Accept": str(accept) if accept is not None else None,
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
            return pydantic_v1.parse_obj_as(GetProjectEntitiesResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequest(pydantic_v1.parse_obj_as(BadRequestResponse, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise Unauthorized(pydantic_v1.parse_obj_as(UnauthorizedResponse, _response.json()))  # type: ignore
        if _response.status_code == 405:
            raise MethodNotAllowed(pydantic_v1.parse_obj_as(MethodNotAllowedResponse, _response.json()))  # type: ignore
        if _response.status_code == 406:
            raise NotAcceptable(pydantic_v1.parse_obj_as(NotAcceptableResponse, _response.json()))  # type: ignore
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

    async def delete_project(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProjectResponse:
        """
        Deletes an existing project.

        Parameters:
            - project_id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from sayari.client import AsyncSayari

        client = AsyncSayari(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        await client.project.delete_project(
            project_id="Gam5qG",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/projects/{jsonable_encoder(project_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic_v1.parse_obj_as(DeleteProjectResponse, _response.json())  # type: ignore
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
