# This file was auto-generated by Fern from our API Definition.

from ...shared_types.types.entity_details import EntityDetails
from ...shared_types.types.entity_relationships import EntityRelationships
from ...shared_types.types.relationship_data import RelationshipData
import typing
from .coordinates import Coordinates
from ...shared_types.types.entity_matches import EntityMatches
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class SearchResults(EntityDetails):
    coordinates: typing.List[Coordinates]
    matches: EntityMatches

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
