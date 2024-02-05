# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .country import Country
from .country_context import CountryContext

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CountryProperties(pydantic.BaseModel):
    context: typing.Optional[CountryContext] = pydantic.Field(description="The type of affiliation")
    date: typing.Optional[str] = pydantic.Field(description="as-of date")
    from_date: typing.Optional[str] = pydantic.Field(description="start date")
    state: typing.Optional[str] = pydantic.Field(description="Subnational state, province, region, etc.")
    to_date: typing.Optional[str] = pydantic.Field(description="end date")
    value: Country = pydantic.Field(description="The country, ideally normalized to an ISO trigram")

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
