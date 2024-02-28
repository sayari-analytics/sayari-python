# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...generated_types.types.country import Country
from ...generated_types.types.relationships import Relationships
from .traversal_data import TraversalData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TraversalResponse(pydantic.BaseModel):
    """
    OK
    ---
    from sayari-analytics import (Attributes, Country, Entities, EntityDetails,
                                  RelationshipInfo, Relationships, Risk, RiskData,
                                  RiskLevel, SourceCountInfo, TraversalData,
                                  TraversalPath, TraversalRelationshipData,
                                  TraversalResponse)

    TraversalResponse(min_depth=1, max_depth=6, relationships=[], countries=[], types=[], name="", watchlist=False, psa=False, offset=0, limit=1, next=True, explored_count=9999999, data=[TraversalData(source="mGq1lpuqKssNWTjIokuPeA", target=EntityDetails(id="gm0zROLKqgX34AlFV4nw6w", label="HAL MANAGEMENT LIMITED", degree=1, entity_url="/v1/entity/gm0zROLKqgX34AlFV4nw6w", pep=False, psa_id="15753940187055", psa_count=1303, sanctioned=False, closed=False, type=Entities.COMPANY, identifiers=[], addresses=["HANOVER HOUSE, 14 HANOVER SQUARE, W1S 1HP"], countries=[Country.GBR], relationship_count={Relationships.REGISTERED_AGENT_OF: 1}, source_count={"ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=2, label="UK Corporate Registry", )}, risk={Risk.BASEL_AML: RiskData(value=3.99, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, ), Risk.CPI_SCORE: RiskData(value=78, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, )}, user_attribute_counts={}, user_record_count=0, user_related_entities_count=0, user_relationship_count={}, related_entities_count=1, attribute_counts={"address": 1, "name": 1, "country": 2}, ), path=[TraversalPath(field="has_registered_agent", entity=EntityDetails(id="gm0zROLKqgX34AlFV4nw6w", label="HAL MANAGEMENT LIMITED", degree=1, entity_url="/v1/entity/gm0zROLKqgX34AlFV4nw6w", pep=False, psa_id="15753940187055", psa_count=1303, sanctioned=False, closed=False, type=Entities.COMPANY, identifiers=[], addresses=["HANOVER HOUSE, 14 HANOVER SQUARE, W1S 1HP"], countries=[Country.GBR], relationship_count={Relationships.REGISTERED_AGENT_OF: 1}, source_count={"ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=2, label="UK Corporate Registry", )}, risk={Risk.BASEL_AML: RiskData(value=3.99, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, ), Risk.CPI_SCORE: RiskData(value=78, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, )}, user_attribute_counts={}, user_record_count=0, user_related_entities_count=0, user_relationship_count={}, related_entities_count=1, attribute_counts={"address": 1, "name": 1, "country": 2}, ), relationships={Relationships.HAS_REGISTERED_AGENT: TraversalRelationshipData(values=[RelationshipInfo(record="ecdfb3f2ecc8c3797e77d5795a8066ef/06517802/1682985600000", from_date="2008-02-28", to_date="2008-07-10", acquisition_date="2023-05-02", publication_date="2023-05-02", former=True, attributes={Attributes.POSITION: [{"value": "Secretary"}]}, ), RelationshipInfo(record="ecdfb3f2ecc8c3797e77d5795a8066ef/06517802/1686009600000", from_date="2008-02-28", to_date="2008-07-10", acquisition_date="2023-06-06", publication_date="2023-06-06", former=True, attributes={}, )], former=True, start_date="2008-02-28", end_date="2008-07-10", last_observed="2008-07-10", )}, )], )], )
    """

    min_depth: int
    max_depth: int
    relationships: typing.List[Relationships]
    countries: typing.List[Country]
    types: typing.List[str]
    name: str
    watchlist: bool
    psa: bool
    offset: int
    limit: int
    next: bool
    data: typing.List[TraversalData]
    sanctioned: typing.Optional[bool] = None
    pep: typing.Optional[bool] = None
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
