# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...generated_types.types.attributes import Attributes


class RelationshipInfo(pydantic_v1.BaseModel):
    editable: typing.Optional[bool] = None
    record: str
    attributes: typing.Dict[Attributes, typing.List[typing.Any]]
    date: typing.Optional[str] = None
    from_date: typing.Optional[str] = None
    to_date: typing.Optional[str] = None
    acquisition_date: str
    former: typing.Optional[bool] = None
    publication_date: typing.Optional[str] = None

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