# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.country import Country
from ...shared_types.types.relationship_type import RelationshipType
from .traversal_data import TraversalData


class TraversalResponse(pydantic.BaseModel):
    min_depth: int
    max_depth: int
    relationships: typing.List[RelationshipType]
    countries: typing.List[Country]
    types: typing.List[str]
    psa: bool
    offset: int
    limit: int
    next: bool
    data: typing.List[TraversalData]
    explored_count: int

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
