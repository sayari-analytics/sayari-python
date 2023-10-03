# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..shared_errors.errors.not_found_error import NotFoundError
from ..shared_types.types.entity_details import EntityDetails
from ..shared_types.types.entity_id import EntityId


class EntityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_entity(
        self,
        id: EntityId,
        *,
        attributes_name_next: typing.Optional[str] = None,
        attributes_name_prev: typing.Optional[str] = None,
        attributes_name_limit: typing.Optional[int] = None,
        attributes_address_next: typing.Optional[str] = None,
        attributes_address_prev: typing.Optional[str] = None,
        attributes_address_limit: typing.Optional[int] = None,
        attributes_country_next: typing.Optional[str] = None,
        attributes_country_prev: typing.Optional[str] = None,
        attributes_country_limit: typing.Optional[int] = None,
        relationships_next: typing.Optional[str] = None,
        relationships_prev: typing.Optional[str] = None,
        relationships_limit: typing.Optional[int] = None,
        relationships_type: typing.Optional[str] = None,
        relationships_sort: typing.Optional[str] = None,
        relationships_start_date: typing.Optional[dt.date] = None,
        relationships_end_date: typing.Optional[dt.date] = None,
        relationships_min_shares: typing.Optional[int] = None,
        relationships_country: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        relationships_arrival_country: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        relationships_departure_country: typing.Optional[typing.Union[typing.Optional[str], typing.List[str]]] = None,
        relationships_hs_code: typing.Optional[str] = None,
        possibly_same_as_next: typing.Optional[str] = None,
        possibly_same_as_prev: typing.Optional[str] = None,
        possibly_same_as_limit: typing.Optional[int] = None,
        referenced_by_next: typing.Optional[str] = None,
        referenced_by_prev: typing.Optional[str] = None,
        referenced_by_limit: typing.Optional[int] = None,
    ) -> EntityDetails:
        """
        Retrieve an entity from the database based on the ID

        Parameters:
            - id: EntityId.

            - attributes_name_next: typing.Optional[str]. The pagination token for the next page of attribute `name`.

            - attributes_name_prev: typing.Optional[str]. The pagination token for the previous page of attribute `name`.

            - attributes_name_limit: typing.Optional[int]. Limit total values returned for attribute `name`. Defaults to 100.

            - attributes_address_next: typing.Optional[str]. The pagination token for the next page of attribute `address`.

            - attributes_address_prev: typing.Optional[str]. The pagination token for the previous page of attribute `address`.

            - attributes_address_limit: typing.Optional[int]. Limit total values returned for attribute `address`. Defaults to 100.

            - attributes_country_next: typing.Optional[str]. The pagination token for the next page of attribute `country`.

            - attributes_country_prev: typing.Optional[str]. The pagination token for the previous page of attribute `country`.

            - attributes_country_limit: typing.Optional[int]. Limit total values returned for attribute `country`. Defaults to 100.

            - relationships_next: typing.Optional[str]. The pagination token for the next page of relationship results

            - relationships_prev: typing.Optional[str]. The pagination token for the previous page of relationship results

            - relationships_limit: typing.Optional[int]. Limit total relationship values. Defaults to 100.

            - relationships_type: typing.Optional[str]. Filter relationships to relationship type, e.g. director_of or has_shareholder

            - relationships_sort: typing.Optional[str]. Sorts relationships by As Of date or Shareholder percentage, e.g. date or -shares

            - relationships_start_date: typing.Optional[dt.date]. Filters relationships to after a date

            - relationships_end_date: typing.Optional[dt.date]. Filters relationships to before a date

            - relationships_min_shares: typing.Optional[int]. Filters relationships to greater than or equal to a Shareholder percentage

            - relationships_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters relationships to a list of countries

            - relationships_arrival_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters shipment relationships to a list of arrival countries

            - relationships_departure_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters shipment relationships to a list of departure countries

            - relationships_hs_code: typing.Optional[str]. Filters shipment relationships to an HS code

            - possibly_same_as_next: typing.Optional[str]. The pagination token for the next page of possibly same entities.

            - possibly_same_as_prev: typing.Optional[str]. The pagination token for the previous page of possibly same entities.

            - possibly_same_as_limit: typing.Optional[int]. Limit total possibly same as entities. Defaults to 100.

            - referenced_by_next: typing.Optional[str]. The pagination token for the next page of the entity's referencing records

            - referenced_by_prev: typing.Optional[str]. The pagination token for the previous page of the entity's referencing records

            - referenced_by_limit: typing.Optional[int]. Limit totals values returned for entity's referencing records. Defaults to 100.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity/{id}"),
            params=remove_none_from_dict(
                {
                    "attributes.name.next": attributes_name_next,
                    "attributes.name.prev": attributes_name_prev,
                    "attributes.name.limit": attributes_name_limit,
                    "attributes.address.next": attributes_address_next,
                    "attributes.address.prev": attributes_address_prev,
                    "attributes.address.limit": attributes_address_limit,
                    "attributes.country.next": attributes_country_next,
                    "attributes.country.prev": attributes_country_prev,
                    "attributes.country.limit": attributes_country_limit,
                    "relationships.next": relationships_next,
                    "relationships.prev": relationships_prev,
                    "relationships.limit": relationships_limit,
                    "relationships.type": relationships_type,
                    "relationships.sort": relationships_sort,
                    "relationships.startDate": str(relationships_start_date)
                    if relationships_start_date is not None
                    else None,
                    "relationships.endDate": str(relationships_end_date)
                    if relationships_end_date is not None
                    else None,
                    "relationships.minShares": relationships_min_shares,
                    "relationships.country": relationships_country,
                    "relationships.arrivalCountry": relationships_arrival_country,
                    "relationships.departureCountry": relationships_departure_country,
                    "relationships.hsCode": relationships_hs_code,
                    "possibly_same_as.next": possibly_same_as_next,
                    "possibly_same_as.prev": possibly_same_as_prev,
                    "possibly_same_as.limit": possibly_same_as_limit,
                    "referenced_by.next": referenced_by_next,
                    "referenced_by.prev": referenced_by_prev,
                    "referenced_by.limit": referenced_by_limit,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntityDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def entity_summary(self, id: EntityId) -> EntityDetails:
        """
        The Entity Summary endpoint returns a smaller entity payload

        Parameters:
            - id: EntityId.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity_summary/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntityDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncEntityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_entity(
        self,
        id: EntityId,
        *,
        attributes_name_next: typing.Optional[str] = None,
        attributes_name_prev: typing.Optional[str] = None,
        attributes_name_limit: typing.Optional[int] = None,
        attributes_address_next: typing.Optional[str] = None,
        attributes_address_prev: typing.Optional[str] = None,
        attributes_address_limit: typing.Optional[int] = None,
        attributes_country_next: typing.Optional[str] = None,
        attributes_country_prev: typing.Optional[str] = None,
        attributes_country_limit: typing.Optional[int] = None,
        relationships_next: typing.Optional[str] = None,
        relationships_prev: typing.Optional[str] = None,
        relationships_limit: typing.Optional[int] = None,
        relationships_type: typing.Optional[str] = None,
        relationships_sort: typing.Optional[str] = None,
        relationships_start_date: typing.Optional[dt.date] = None,
        relationships_end_date: typing.Optional[dt.date] = None,
        relationships_min_shares: typing.Optional[int] = None,
        relationships_country: typing.Union[typing.Optional[str], typing.List[str]],
        relationships_arrival_country: typing.Union[typing.Optional[str], typing.List[str]],
        relationships_departure_country: typing.Union[typing.Optional[str], typing.List[str]],
        relationships_hs_code: typing.Optional[str] = None,
        possibly_same_as_next: typing.Optional[str] = None,
        possibly_same_as_prev: typing.Optional[str] = None,
        possibly_same_as_limit: typing.Optional[int] = None,
        referenced_by_next: typing.Optional[str] = None,
        referenced_by_prev: typing.Optional[str] = None,
        referenced_by_limit: typing.Optional[int] = None,
    ) -> EntityDetails:
        """
        Retrieve an entity from the database based on the ID

        Parameters:
            - id: EntityId.

            - attributes_name_next: typing.Optional[str]. The pagination token for the next page of attribute `name`.

            - attributes_name_prev: typing.Optional[str]. The pagination token for the previous page of attribute `name`.

            - attributes_name_limit: typing.Optional[int]. Limit total values returned for attribute `name`. Defaults to 100.

            - attributes_address_next: typing.Optional[str]. The pagination token for the next page of attribute `address`.

            - attributes_address_prev: typing.Optional[str]. The pagination token for the previous page of attribute `address`.

            - attributes_address_limit: typing.Optional[int]. Limit total values returned for attribute `address`. Defaults to 100.

            - attributes_country_next: typing.Optional[str]. The pagination token for the next page of attribute `country`.

            - attributes_country_prev: typing.Optional[str]. The pagination token for the previous page of attribute `country`.

            - attributes_country_limit: typing.Optional[int]. Limit total values returned for attribute `country`. Defaults to 100.

            - relationships_next: typing.Optional[str]. The pagination token for the next page of relationship results

            - relationships_prev: typing.Optional[str]. The pagination token for the previous page of relationship results

            - relationships_limit: typing.Optional[int]. Limit total relationship values. Defaults to 100.

            - relationships_type: typing.Optional[str]. Filter relationships to relationship type, e.g. director_of or has_shareholder

            - relationships_sort: typing.Optional[str]. Sorts relationships by As Of date or Shareholder percentage, e.g. date or -shares

            - relationships_start_date: typing.Optional[dt.date]. Filters relationships to after a date

            - relationships_end_date: typing.Optional[dt.date]. Filters relationships to before a date

            - relationships_min_shares: typing.Optional[int]. Filters relationships to greater than or equal to a Shareholder percentage

            - relationships_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters relationships to a list of countries

            - relationships_arrival_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters shipment relationships to a list of arrival countries

            - relationships_departure_country: typing.Union[typing.Optional[str], typing.List[str]]. Filters shipment relationships to a list of departure countries

            - relationships_hs_code: typing.Optional[str]. Filters shipment relationships to an HS code

            - possibly_same_as_next: typing.Optional[str]. The pagination token for the next page of possibly same entities.

            - possibly_same_as_prev: typing.Optional[str]. The pagination token for the previous page of possibly same entities.

            - possibly_same_as_limit: typing.Optional[int]. Limit total possibly same as entities. Defaults to 100.

            - referenced_by_next: typing.Optional[str]. The pagination token for the next page of the entity's referencing records

            - referenced_by_prev: typing.Optional[str]. The pagination token for the previous page of the entity's referencing records

            - referenced_by_limit: typing.Optional[int]. Limit totals values returned for entity's referencing records. Defaults to 100.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity/{id}"),
            params=remove_none_from_dict(
                {
                    "attributes.name.next": attributes_name_next,
                    "attributes.name.prev": attributes_name_prev,
                    "attributes.name.limit": attributes_name_limit,
                    "attributes.address.next": attributes_address_next,
                    "attributes.address.prev": attributes_address_prev,
                    "attributes.address.limit": attributes_address_limit,
                    "attributes.country.next": attributes_country_next,
                    "attributes.country.prev": attributes_country_prev,
                    "attributes.country.limit": attributes_country_limit,
                    "relationships.next": relationships_next,
                    "relationships.prev": relationships_prev,
                    "relationships.limit": relationships_limit,
                    "relationships.type": relationships_type,
                    "relationships.sort": relationships_sort,
                    "relationships.startDate": str(relationships_start_date)
                    if relationships_start_date is not None
                    else None,
                    "relationships.endDate": str(relationships_end_date)
                    if relationships_end_date is not None
                    else None,
                    "relationships.minShares": relationships_min_shares,
                    "relationships.country": relationships_country,
                    "relationships.arrivalCountry": relationships_arrival_country,
                    "relationships.departureCountry": relationships_departure_country,
                    "relationships.hsCode": relationships_hs_code,
                    "possibly_same_as.next": possibly_same_as_next,
                    "possibly_same_as.prev": possibly_same_as_prev,
                    "possibly_same_as.limit": possibly_same_as_limit,
                    "referenced_by.next": referenced_by_next,
                    "referenced_by.prev": referenced_by_prev,
                    "referenced_by.limit": referenced_by_limit,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntityDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def entity_summary(self, id: EntityId) -> EntityDetails:
        """
        The Entity Summary endpoint returns a smaller entity payload

        Parameters:
            - id: EntityId.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"v1/entity_summary/{id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(EntityDetails, _response.json())  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError()
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
