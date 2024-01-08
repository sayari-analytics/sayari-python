# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..generated_types.country import Country
from ..generated_types.entities import Entities

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ResolutionResponseFields(pydantic.BaseModel):
    name: typing.Optional[typing.List[str]]
    identifier: typing.Optional[typing.List[str]]
    country: typing.Optional[typing.List[Country]]
    address: typing.Optional[typing.List[str]]
    date_of_birth: typing.Optional[typing.List[str]]
    contact: typing.Optional[typing.List[str]]
    type: typing.Optional[typing.List[Entities]]

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
