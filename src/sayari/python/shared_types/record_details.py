# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .record_id import RecordId
from .source_id import SourceId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RecordDetails(pydantic.BaseModel):
    id: RecordId
    label: str
    source: SourceId
    publication_date: typing.Optional[str]
    acquisition_date: str
    references_count: int
    record_url: str
    source_url: typing.Optional[str]
    document_urls: typing.Optional[typing.List[str]]
    matches: typing.Optional[typing.Dict[str, typing.List[str]]]

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
