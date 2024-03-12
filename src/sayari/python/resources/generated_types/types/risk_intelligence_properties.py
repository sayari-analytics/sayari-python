# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .tag import Tag

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RiskIntelligenceProperties(pydantic.BaseModel):
    authority: typing.Optional[str] = pydantic.Field(
        default=None, description="Government authority issuing the enforcement or risk intelligence action"
    )
    date: typing.Optional[str] = pydantic.Field(default=None, description="as-of date")
    from_date: typing.Optional[str] = pydantic.Field(default=None, description="start date")
    list_: typing.Optional[str] = pydantic.Field(
        alias="list",
        default=None,
        description="Official list where the entity's risk information or enforcement action is recorded",
    )
    program: typing.Optional[str] = pydantic.Field(
        default=None, description="Specific to sanctions risk. Sanctions program under which the entity is designated."
    )
    reason: typing.Optional[str] = pydantic.Field(
        default=None, description="Explanation or legal basis for the risk intelligence"
    )
    to_date: typing.Optional[str] = pydantic.Field(default=None, description="end date")
    type: Tag = pydantic.Field(description="Type of risk intelligence")

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
