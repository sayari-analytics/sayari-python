# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...generated_types.types.country import Country
from ...generated_types.types.risk import Risk


class TradeFilterList(pydantic_v1.BaseModel):
    """
    Filter your search on the following attributes.
    """

    buyer_id: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Exact match against the entity_id of the buyer. The buyer is the receiver_of shipments.
    """

    supplier_id: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Exact match against the entity_id of the supplier. The supplier is the shipper_of shipments.
    """

    buyer_name: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Buyers whose name contains the provided string.
    """

    supplier_name: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Shipper whose name contains the provided string.
    """

    buyer_risk: typing.Optional[typing.List[Risk]] = pydantic_v1.Field(default=None)
    """
    Buyer with an exact match for the provided [risk factor](/sayari-library/ontology/risk-factors).
    """

    supplier_risk: typing.Optional[typing.List[Risk]] = pydantic_v1.Field(default=None)
    """
    Shipper with an exact match for the provided [risk factor](/sayari-library/ontology/risk-factors).
    """

    buyer_country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Buyer with an exact match for the provided [country code](/sayari-library/ontology/enumerated-types#country).
    """

    supplier_country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Supplier with an exact match for the provided [country code](/sayari-library/ontology/enumerated-types#country).
    """

    departure_country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Shipment departs from a country with an exact match for the provided [country code](/sayari-library/ontology/enumerated-types#country).
    """

    departure_state: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Shipment departs from a state that contains the provided state name.
    """

    departure_city: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Shipment departs from a city that contains the provided city name.
    """

    arrival_country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Shipment arrives at a country with an exact match for the provided [country code](/sayari-library/ontology/enumerated-types#country).
    """

    arrival_state: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Shipment arrives at a state that contains the provided state name.
    """

    arrival_city: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Shipment arrives at a city that contains the provided city name.
    """

    hs_code: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The shipment HS code starts with the provided HS code.
    """

    hs_description: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The HS description contains the provided string.
    """

    supplier_purpose: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The supplier purpose contains the provided string.
    """

    buyer_purpose: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The buyer purpose contains the provided string.
    """

    arrival_date: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The arrival date is within the provided range.
    """

    departure_date: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The departure date is within the provided range.
    """

    shipment_identifier: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The shipment identifier starts with the provided string.
    """

    weight: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    The shipment weight is within the provided range.
    """

    sources: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    An exact match for the provided sources.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}