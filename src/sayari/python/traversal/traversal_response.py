# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from ..generated_types.country import Country
from ..generated_types.relationships import Relationships
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
                                  Identifier, RelationshipAttributeValue,
                                  RelationshipInfo, Relationships, Risk, RiskData,
                                  RiskLevel, SourceCountInfo, TraversalData,
                                  TraversalPath, TraversalRelationshipData,
                                  TraversalResponse)

    TraversalResponse(min_depth=1, max_depth=6, relationships=[], countries=[], types=[], name="", watchlist=False, psa=False, offset=0, limit=1, next=True, explored_count=9999999, data=[TraversalData(source="mGq1lpuqKssNWTjIokuPeA", target=EntityDetails(id="ZzmU1uMYUuaVqQ4HVgO-tA", label="DAVID ROBERT JOSEPH BECKHAM", degree=16, entity_url="/v1/entity/ZzmU1uMYUuaVqQ4HVgO-tA", pep=False, psa_id="14078902799196", psa_count=2, sanctioned=False, closed=False, type=Entities.PERSON, identifiers=[Identifier(value="048137290006", type="uk_person_number", label="Uk Person Number", ), Identifier(value="256782810001", type="uk_person_number", label="Uk Person Number", ), Identifier(value="048137290009", type="uk_person_number", label="Uk Person Number", ), Identifier(value="048137290004", type="uk_person_number", label="Uk Person Number", ), Identifier(value="244456180001", type="uk_person_number", label="Uk Person Number", )], addresses=["C/O SRLV ACCOUNTANTS, 89 NEW BOND STREET, W1S 1DA, ENGLAND", "20-22 Great Titchfield Street, London, W1W 8BE", "7 SAVOY COURT, WC2R 0EX, UNITED KINGDOM"], date_of_birth="1975-05", countries=[Country.GBR], relationship_count={Relationships.DIRECTOR_OF: 16, Relationships.SHAREHOLDER_OF: 6, Relationships.LINKED_TO: 6}, source_count={"4ea8bac1bed868e1510ffd21842e9551": SourceCountInfo(count=99, label="UK Persons with Significant Control", ), "ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=215, label="UK Corporate Registry", )}, risk={Risk.BASEL_AML: RiskData(value=3.99, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, ), Risk.CPI_SCORE: RiskData(value=78, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, )}, ), path=[TraversalPath(field="has_director", entity=EntityDetails(id="ZzmU1uMYUuaVqQ4HVgO-tA", label="DAVID ROBERT JOSEPH BECKHAM", degree=16, entity_url="/v1/entity/ZzmU1uMYUuaVqQ4HVgO-tA", pep=False, psa_id="14078902799196", psa_count=2, sanctioned=False, closed=False, type=Entities.PERSON, identifiers=[Identifier(value="048137290006", type="uk_person_number", label="Uk Person Number", ), Identifier(value="256782810001", type="uk_person_number", label="Uk Person Number", ), Identifier(value="048137290009", type="uk_person_number", label="Uk Person Number", ), Identifier(value="048137290004", type="uk_person_number", label="Uk Person Number", ), Identifier(value="244456180001", type="uk_person_number", label="Uk Person Number", )], addresses=["C/O SRLV ACCOUNTANTS, 89 NEW BOND STREET, W1S 1DA, ENGLAND", "20-22 Great Titchfield Street, London, W1W 8BE", "7 SAVOY COURT, WC2R 0EX, UNITED KINGDOM"], date_of_birth="1975-05", countries=[Country.GBR], relationship_count={Relationships.DIRECTOR_OF: 16, Relationships.SHAREHOLDER_OF: 6, Relationships.LINKED_TO: 6}, source_count={"4ea8bac1bed868e1510ffd21842e9551": SourceCountInfo(count=99, label="UK Persons with Significant Control", ), "ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=215, label="UK Corporate Registry", )}, risk={Risk.BASEL_AML: RiskData(value=3.99, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, ), Risk.CPI_SCORE: RiskData(value=78, metadata={"country": ["GBR"]}, level=RiskLevel.RELEVANT, )}, ), relationships={Relationships.HAS_DIRECTOR: TraversalRelationshipData(values=[RelationshipInfo(record="ecdfb3f2ecc8c3797e77d5795a8066ef/06517802/1682985600000", from_date="2008-07-10", to_date="2014-12-10", acquisition_date="2023-05-02", publication_date="2023-05-02", former=True, attributes={Attributes.POSITION: [RelationshipAttributeValue(value="Director", )]}, ), RelationshipInfo(record="ecdfb3f2ecc8c3797e77d5795a8066ef/06517802/1686009600000", from_date="2008-07-10", to_date="2014-12-10", acquisition_date="2023-06-06", publication_date="2023-06-06", former=True, attributes={}, )], former=True, start_date="2008-07-10", end_date="2014-12-10", last_observed="2014-12-10", )}, )], )], )
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
    sanctioned: typing.Optional[bool]
    pep: typing.Optional[bool]
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