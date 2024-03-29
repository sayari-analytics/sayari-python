# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..generated_types.attribute_details import AttributeDetails
from .company_type import CompanyType
from .embedded_entity import EmbeddedEntity
from .entity_hs_code import EntityHsCode
from .entity_registration_date import EntityRegistrationDate
from .entity_risk import EntityRisk
from .entity_translated_label import EntityTranslatedLabel
from .possibly_same_as import PossiblySameAs
from .referenced_by import ReferencedBy
from .shipment_arrival import ShipmentArrival
from .shipment_departue import ShipmentDepartue
from .status import Status


class EntityDetails(EmbeddedEntity):
    """
    Additional fields providing more details about an entity
    """

    registration_date: typing.Optional[EntityRegistrationDate]
    translated_label: typing.Optional[EntityTranslatedLabel]
    hs_code: typing.Optional[EntityHsCode]
    shipment_arrival: typing.Optional[ShipmentArrival]
    shipment_departure: typing.Optional[ShipmentDepartue]
    company_type: typing.Optional[CompanyType]
    latest_status: typing.Optional[Status]
    risk: EntityRisk
    attributes: typing.Optional[AttributeDetails]
    relationships: typing.Optional[EntityRelationships]
    possibly_same_as: typing.Optional[PossiblySameAs]
    referenced_by: typing.Optional[ReferencedBy]

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


from .entity_relationships import EntityRelationships  # noqa: E402

EntityDetails.update_forward_refs()
