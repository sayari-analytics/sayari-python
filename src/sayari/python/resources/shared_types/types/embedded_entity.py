# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities
from .entity_addresses import EntityAddresses
from .entity_dob import EntityDob
from .entity_id import EntityId
from .entity_relationship_count import EntityRelationshipCount
from .identifier import Identifier
from .source_count_info import SourceCountInfo

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class EmbeddedEntity(pydantic.BaseModel):
    """
    The attributes fields common to most entities.
    """

    id: EntityId
    label: str = pydantic.Field(description="Display name of the entity")
    degree: int = pydantic.Field(description="Number of outgoing relationships")
    closed: bool = pydantic.Field(
        description="True if the entity existed in the past but not at the present time, otherwise false. Always false for data curation."
    )
    entity_url: str = pydantic.Field(description="Convenience URL to the entity in the API.")
    pep: bool = pydantic.Field(
        description='True if the entity has the "Politically Exposed Person (PEP)" risk factor, otherwise false. See https://docs.sayari.com/risk/#politically-exposed-person-pep'
    )
    psa_id: typing.Optional[str]
    psa_count: int = pydantic.Field(description="Number of entities that are Possibly the Same As (PSA) the entity.")
    sanctioned: bool = pydantic.Field(
        description='True if the entity has the "Sanctioned" risk factor, otherwise false. See https://docs.sayari.com/risk/#sanctioned'
    )
    type: Entities
    identifiers: typing.List[Identifier]
    countries: typing.List[Country]
    source_count: typing.Dict[str, SourceCountInfo] = pydantic.Field(
        description="Number of records associated with the entity, grouped by source."
    )
    addresses: typing.List[EntityAddresses]
    date_of_birth: typing.Optional[EntityDob]
    relationship_count: EntityRelationshipCount
    user_relationship_count: EntityRelationshipCount
    attribute_counts: typing.Any
    user_attribute_counts: typing.Any
    related_entities_count: int
    user_related_entities_count: int
    user_record_count: int

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
