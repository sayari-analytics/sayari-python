# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities


class ResolutionResponseFields(pydantic_v1.BaseModel):
    name: typing.Optional[typing.List[str]] = None
    identifier: typing.Optional[typing.List[str]] = None
    profile: typing.Optional[typing.List[str]] = None
    country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Entity country - must be ISO (3166) Trigram i.e., USA. See complete list [here](/sayari-library/ontology/enumerated-types#country)
    """

    address: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    List of physical addresses associated with the entity.
    """

    date_of_birth: typing.Optional[typing.List[str]] = None
    contact: typing.Optional[typing.List[str]] = None
    type: typing.Optional[typing.List[Entities]] = pydantic_v1.Field(default=None)
    """
    [Entity type](/sayari-library/ontology/entities)
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
