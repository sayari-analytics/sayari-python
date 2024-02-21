# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .business_purpose_standard import BusinessPurposeStandard

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class BusinessPurposeProperties(pydantic.BaseModel):
    code: typing.Optional[str] = pydantic.Field(description="A code")
    date: typing.Optional[str] = pydantic.Field(description="as-of date")
    from_date: typing.Optional[str] = pydantic.Field(description="start date")
    standard: typing.Optional[BusinessPurposeStandard] = pydantic.Field(
        description='The type of code (e.g., "ISIC4", "NACE1")'
    )
    to_date: typing.Optional[str] = pydantic.Field(description="end date")
    value: typing.Optional[str] = pydantic.Field(description="A text description")

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
