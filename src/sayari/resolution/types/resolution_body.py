# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from ...generated_types.types.both_identifier_types import BothIdentifierTypes
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities
from .profile_enum import ProfileEnum
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ResolutionBody(UniversalBaseModel):
    name: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity name
    """

    identifier: typing.Optional[typing.List[BothIdentifierTypes]] = pydantic.Field(default=None)
    """
    Entity identifier. Can be from either the [Identifier Type](/sayari-library/ontology/enumerated-types#identifier-type) or [Weak Identifier Type](/sayari-library/ontology/enumerated-types#weak-identifier-type) enums.
    """

    country: typing.Optional[typing.List[Country]] = pydantic.Field(default=None)
    """
    Entity country - must be ISO (3166) Trigram i.e., `USA`. See complete list [here](/sayari-library/ontology/enumerated-types#country)
    """

    address: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity address
    """

    date_of_birth: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity date of birth
    """

    contact: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Entity contact
    """

    type: typing.Optional[typing.List[Entities]] = pydantic.Field(default=None)
    """
    [Entity type](/sayari-library/ontology/entities). If multiple values are passed for any field, the endpoint will match entities with ANY of the values.
    """

    profile: typing.Optional[ProfileEnum] = pydantic.Field(default=None)
    """
    Profile can be used to switch between search algorithms. The default profile `corporate` is optimized for accurate entity attribute matching and is ideal for business verification and matching entities with corporate data. The `suppliers` profile is optimized for matching entities with extensive trade data. Ideal for supply chain and trade-related use cases.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
