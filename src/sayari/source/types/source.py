# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...generated_types.types.country import Country


class Source(pydantic_v1.BaseModel):
    id: str = pydantic_v1.Field()
    """
    The unique identifier of the source
    """

    label: str
    description: str
    country: Country = pydantic_v1.Field()
    """
    Source [country](/sayari-library/ontology/enumerated-types#country)
    """

    region: str
    date_added: str
    source_type: str
    record_type: str
    structure: str
    source_url: typing.Optional[str] = None
    pep: bool
    watchlist: bool

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