# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities
from ...generated_types.types.relationships import Relationships
from .company_type import CompanyType
from .entity_hs_code import EntityHsCode
from .entity_registration_date import EntityRegistrationDate
from .entity_risk import EntityRisk
from .entity_summary import EntitySummary
from .entity_translated_label import EntityTranslatedLabel
from .identifier import Identifier
from .psa import Psa
from .shipment_arrival import ShipmentArrival
from .shipment_departure import ShipmentDeparture
from .source_count_info import SourceCountInfo
from .status import Status

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CoreEntity(EntitySummary):
    """
    The attributes fields common to most entities.
    """

    id: str = pydantic.Field(description="Unique identifier of the entity")
    owner: typing.Optional[str] = pydantic.Field(
        default=None, description="User or group that created the entity, if applicable. Undefined for Sayari entities."
    )
    type: Entities = pydantic.Field(description="The [entity type](/sayari-library/ontology/entities).")
    label: str = pydantic.Field(description="Display name of the entity")
    names: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None, description="Name variations of the entity."
    )
    company_type: typing.Optional[CompanyType] = None
    registration_date: typing.Optional[EntityRegistrationDate] = None
    latest_status: typing.Optional[Status] = None
    shipment_arrival: typing.Optional[ShipmentArrival] = None
    shipment_departure: typing.Optional[ShipmentDeparture] = None
    hs_code: typing.Optional[EntityHsCode] = None
    translated_label: typing.Optional[EntityTranslatedLabel] = None
    short_label: typing.Optional[str] = None
    identifiers: typing.List[Identifier]
    addresses: typing.Optional[typing.List[str]] = pydantic.Field(
        default=None,
        description="List of physical addresses associated with the entity. See more [here](/sayari-library/ontology/attributes#address)",
    )
    date_of_birth: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Birth date of a person. See more [here](/sayari-library/ontology/attributes#date-of-birth)",
    )
    countries: typing.List[Country] = pydantic.Field(
        description="Entity [country](/sayari-library/ontology/enumerated-types#country)"
    )
    closed: typing.Optional[bool] = pydantic.Field(
        default=None,
        description="True if the entity existed in the past but not at the present time, otherwise false. Always false for data curation.",
    )
    related_entities_count: int
    user_related_entities_count: int
    relationship_counts: typing.Dict[Relationships, int] = pydantic.Field(
        description="Count of related entities for a given [relationship type](/sayari-library/ontology/relationships)."
    )
    user_relationship_counts: typing.Dict[Relationships, int] = pydantic.Field(
        description="Count of related entities for a given [relationship type](/sayari-library/ontology/relationships)."
    )
    attribute_counts: typing.Any
    user_attribute_counts: typing.Any
    trade_counts: typing.Dict[str, int]
    record_count: int
    user_record_count: int
    source_counts: typing.Dict[str, SourceCountInfo] = pydantic.Field(
        description="Number of records associated with the entity, grouped by source."
    )
    psa: typing.Optional[Psa] = None
    risk: EntityRisk = pydantic.Field(
        description="[Risk factors](/sayari-library/ontology/risk-factors) associated with the entity."
    )
    created: typing.Optional[str] = None
    updated: typing.Optional[str] = None
    edited_by: typing.Optional[str] = None
    editable: typing.Optional[bool] = None
    upload: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}