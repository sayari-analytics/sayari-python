# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from ...generated_types.types.both_identifier_types import BothIdentifierTypes
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities
from .profile_enum import ProfileEnum


class ResolutionBody(pydantic_v1.BaseModel):
    name: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Entity name
    """

    identifier: typing.Optional[typing.List[BothIdentifierTypes]] = pydantic_v1.Field(default=None)
    """
    Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.
    """

    country: typing.Optional[typing.List[Country]] = pydantic_v1.Field(default=None)
    """
    Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)
    """

    address: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Entity address
    """

    date_of_birth: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Entity date of birth
    """

    contact: typing.Optional[typing.List[str]] = pydantic_v1.Field(default=None)
    """
    Entity contact
    """

    type: typing.Optional[typing.List[Entities]] = pydantic_v1.Field(default=None)
    """
    [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.
    """

    profile: typing.Optional[ProfileEnum] = pydantic_v1.Field(default=None)
    """
    Profile can be used to switch between search algorithms. The default profile `corporate` is optimized for accurate entity attribute matching and is ideal for business verification and matching entities with corporate data. The `supplier` profile is optimized for matching entities with extensive trade data. Ideal for supply chain and trade-related use cases.
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
