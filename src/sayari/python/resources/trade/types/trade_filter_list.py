# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TradeFilterList(pydantic.BaseModel):
    """
    Filter your search on the following attributes.
    """

    buyer_id: typing.Optional[str]
    supplier_id: typing.Optional[str]
    buyer_name: typing.Optional[str]
    supplier_name: typing.Optional[str]
    buyer_risk: typing.Optional[str]
    supplier_risk: typing.Optional[str]
    buyer_country: typing.Optional[str]
    supplier_country: typing.Optional[str]
    departure_country: typing.Optional[str]
    departure_state: typing.Optional[str]
    departure_city: typing.Optional[str]
    arrival_country: typing.Optional[str]
    arrival_state: typing.Optional[str]
    arrival_city: typing.Optional[str]
    hs_code: typing.Optional[str]
    hs_description: typing.Optional[str]
    supplier_purpose: typing.Optional[str]
    buyer_purpose: typing.Optional[str]
    arrival_date: typing.Optional[str]
    weight: typing.Optional[str]
    sources: typing.Optional[str]

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
