# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UsageInfo(pydantic.BaseModel):
    entity: typing.Optional[int] = None
    entity_summary: typing.Optional[int] = None
    record: typing.Optional[int] = None
    resolve: typing.Optional[int] = None
    search_entities: typing.Optional[int] = None
    search_records: typing.Optional[int] = None
    search_trade: typing.Optional[int] = None
    traversal: typing.Optional[int] = None

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
