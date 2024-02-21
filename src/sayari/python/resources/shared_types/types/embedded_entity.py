# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.country import Country
from ...generated_types.types.entities import Entities
from ...generated_types.types.relationships import Relationships
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

    id: str = pydantic.Field(description="Unique identifier of the entity")
    label: str = pydantic.Field(description="Display name of the entity")
    degree: int = pydantic.Field(description="Number of outgoing relationships")
    closed: bool = pydantic.Field(
        description="True if the entity existed in the past but not at the present time, otherwise false. Always false for data curation."
    )
    entity_url: str = pydantic.Field(description="Convenience URL to the entity in the API.")
    pep: bool = pydantic.Field(
        description='True if the entity has the ["Politically Exposed Person (PEP)" risk factor](/sayari-library/ontology/risk-factors#politically-exposed-person-pep-), otherwise false.'
    )
    psa_id: typing.Optional[str]
    psa_count: int = pydantic.Field(description="Number of entities that are Possibly the Same As (PSA) the entity.")
    sanctioned: bool = pydantic.Field(
        description='True if the entity has the ["Sanctioned" risk factor](/sayari-library/ontology/risk-factors#sanctioned), otherwise false.'
    )
    type: Entities = pydantic.Field(
        description="The entity type. See detailed explanations [here](/sayari-library/ontology/entities)."
    )
    identifiers: typing.List[Identifier]
    countries: typing.List[Country] = pydantic.Field(
        description="Entity [country](/sayari-library/ontology/enumerated-types#country)"
    )
    source_count: typing.Dict[str, SourceCountInfo] = pydantic.Field(
        description="Number of records associated with the entity, grouped by source."
    )
    addresses: typing.List[str] = pydantic.Field(
        description="List of physical addresses associated with the entity. See more [here](/sayari-library/ontology/attributes#address)"
    )
    date_of_birth: typing.Optional[str] = pydantic.Field(
        description="Birth date of a person. See more [here](/sayari-library/ontology/attributes#date-of-birth)"
    )
    relationship_count: typing.Dict[Relationships, int] = pydantic.Field(
        description="Count of related entities for a given relationship type."
    )
    user_relationship_count: typing.Dict[Relationships, int] = pydantic.Field(
        description="Count of related entities for a given relationship type."
    )
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
