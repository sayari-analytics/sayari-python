# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .shortest_path_data import ShortestPathData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ShortestPathResponse(pydantic.BaseModel):
    """
    OK
    ---
    from sayari-analytics import (Attributes, Country, Entities, EntityDetails,
                                  Identifier, RelationshipAttributeValue,
                                  RelationshipInfo, Relationships,
                                  ShortestPathData, ShortestPathResponse,
                                  SourceCountInfo, Status, TraversalPath,
                                  TraversalRelationshipData)

    ShortestPathResponse(entities=["mGq1lpuqKssNWTjIokuPeA", "ekPP386sHXHREr15-iVgvw"], data=[ShortestPathData(source="mGq1lpuqKssNWTjIokuPeA", target=EntityDetails(id="ekPP386sHXHREr15-iVgvw", label="BECKHAM RETAIL LIMITED", degree=6, entity_url="/v1/entity/ekPP386sHXHREr15-iVgvw", pep=False, psa_count=0, sanctioned=False, closed=False, company_type="Private Limited Company", registration_date="Incorporated 2013-08-22", latest_status=Status(status="active", ), type=Entities.COMPANY, identifiers=[Identifier(value="08661308", type="uk_company_number", label="Uk Company Number", )], addresses=["202 HAMMERSMITH ROAD, LONDON, W6 7DN"], countries=[Country.GBR], relationship_count={Relationships.HAS_SHAREHOLDER: 1, Relationships.HAS_REGISTERED_AGENT: 1, Relationships.HAS_DIRECTOR: 4, Relationships.LINKED_TO: 1}, source_count={"ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=32, label="UK Corporate Registry", ), "2b618f1996252fe537a6d998ae14c9b2": SourceCountInfo(count=1, label="UK Corporate Registry Confirmation Statements", ), "4ea8bac1bed868e1510ffd21842e9551": SourceCountInfo(count=18, label="UK Persons with Significant Control", )}, risk={}, ), path=[TraversalPath(field="linked_to", entity=EntityDetails(id="ekPP386sHXHREr15-iVgvw", label="BECKHAM RETAIL LIMITED", degree=6, entity_url="/v1/entity/ekPP386sHXHREr15-iVgvw", pep=False, psa_count=0, sanctioned=False, closed=False, company_type="Private Limited Company", registration_date="Incorporated 2013-08-22", latest_status=Status(status="active", ), type=Entities.COMPANY, identifiers=[Identifier(value="08661308", type="uk_company_number", label="Uk Company Number", )], addresses=["202 HAMMERSMITH ROAD, LONDON, W6 7DN"], countries=[Country.GBR], relationship_count={Relationships.HAS_SHAREHOLDER: 1, Relationships.HAS_REGISTERED_AGENT: 1, Relationships.HAS_DIRECTOR: 4, Relationships.LINKED_TO: 1}, source_count={"ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(count=32, label="UK Corporate Registry", ), "2b618f1996252fe537a6d998ae14c9b2": SourceCountInfo(count=1, label="UK Corporate Registry Confirmation Statements", ), "4ea8bac1bed868e1510ffd21842e9551": SourceCountInfo(count=18, label="UK Persons with Significant Control", )}, risk={}, ), relationships={Relationships.LINKED_TO: TraversalRelationshipData(values=[RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/08661308/1560176240192", acquisition_date="2019-06-10", attributes={Attributes.POSITION: [RelationshipAttributeValue(value="Has right to appoint and remove directors", )]}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1586822400000", acquisition_date="2020-04-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1601424000000", acquisition_date="2020-09-30", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1616630400000", acquisition_date="2021-03-25", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1634169600000", acquisition_date="2021-10-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1649894400000", acquisition_date="2022-04-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1667433600000", acquisition_date="2022-11-03", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1675123200000", acquisition_date="2023-01-31", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1676505600000", acquisition_date="2023-02-16", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1678320000000", acquisition_date="2023-03-09", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1680566400000", acquisition_date="2023-04-04", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1682899200000", acquisition_date="2023-05-01", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1685577600000", acquisition_date="2023-06-01", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1689033600000", acquisition_date="2023-07-11", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1692662400000", acquisition_date="2023-08-22", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1694476800000", acquisition_date="2023-09-12", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1696896000000", acquisition_date="2023-10-10", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1699488000000", acquisition_date="2023-11-09", attributes={}, )], ), Relationships.SHAREHOLDER_OF: TraversalRelationshipData(values=[RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/08661308/1560176240192", acquisition_date="2019-06-10", attributes={Attributes.POSITION: [RelationshipAttributeValue(value="Has right to appoint and remove directors", )]}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1586822400000", acquisition_date="2020-04-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1601424000000", acquisition_date="2020-09-30", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1616630400000", acquisition_date="2021-03-25", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1634169600000", acquisition_date="2021-10-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1649894400000", acquisition_date="2022-04-14", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1667433600000", acquisition_date="2022-11-03", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1675123200000", acquisition_date="2023-01-31", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1676505600000", acquisition_date="2023-02-16", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1678320000000", acquisition_date="2023-03-09", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1680566400000", acquisition_date="2023-04-04", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1682899200000", acquisition_date="2023-05-01", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1685577600000", acquisition_date="2023-06-01", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1689033600000", acquisition_date="2023-07-11", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1692662400000", acquisition_date="2023-08-22", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1694476800000", acquisition_date="2023-09-12", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1696896000000", acquisition_date="2023-10-10", attributes={}, ), RelationshipInfo(record="4ea8bac1bed868e1510ffd21842e9551/ef8cbb3fcc71d09f098f00728df231e8/1699488000000", acquisition_date="2023-11-09", attributes={}, )], )}, )], )], )
    """

    entities: typing.List[str]
    data: typing.List[ShortestPathData]

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
