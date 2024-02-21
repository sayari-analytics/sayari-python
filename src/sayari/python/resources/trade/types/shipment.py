# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .data_source import DataSource
from .hs_code_info import HsCodeInfo
from .monetary_value import MonetaryValue
from .shipment_address import ShipmentAddress
from .shipment_identifier import ShipmentIdentifier
from .source_or_destination_entity import SourceOrDestinationEntity
from .weight import Weight

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Shipment(pydantic.BaseModel):
    id: str
    type: str
    buyer: typing.List[SourceOrDestinationEntity]
    supplier: typing.List[SourceOrDestinationEntity]
    arrival_date: typing.Optional[str]
    departure_date: typing.Optional[str]
    departure_address: typing.Optional[ShipmentAddress]
    arrival_address: typing.Optional[ShipmentAddress]
    monetary_value: typing.List[MonetaryValue]
    weight: typing.List[Weight]
    identifier: typing.List[ShipmentIdentifier]
    sources: typing.List[DataSource]
    hs_codes: typing.List[HsCodeInfo]
    product_descriptions: typing.List[str]
    record: str = pydantic.Field(description="The unique identifier for a record in the database")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
