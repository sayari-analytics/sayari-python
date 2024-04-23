# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...generated_types.types.address_properties import AddressProperties
from ...generated_types.types.country import Country


class ShipmentMetadata(pydantic_v1.BaseModel):
    arrival_country: typing.List[Country]
    jurisdiction: typing.List[Country]
    reference_id: str
    entity_id: str = pydantic_v1.Field()
    """
    Unique identifier of the entity
    """

    departure_address: typing.Optional[AddressProperties] = None
    type: str
    sources: typing.List[str]
    departure_country: typing.List[Country]

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