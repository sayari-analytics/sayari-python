# This file was auto-generated by Fern from our API Definition.

from ...base_types.types.paginated_response import PaginatedResponse
from ...shared_types.types.entity_details import EntityDetails
from ...shared_types.types.entity_relationships import EntityRelationships
from ...shared_types.types.relationship_data import RelationshipData
import typing
from .search_results import SearchResults
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class EntitySearchResponse(PaginatedResponse):
    """
    OK

    Examples
    --------
    from sayari.base_types import QualifiedCount
    from sayari.search import Coordinates, EntitySearchResponse, SearchResults
    from sayari.shared_types import Identifier, RiskData, SourceCountInfo, Status

    EntitySearchResponse(
        offset=0,
        limit=1,
        size=QualifiedCount(
            count=41,
            qualifier="eq",
        ),
        next=True,
        data=[
            SearchResults(
                id="mGq1lpuqKssNWTjIokuPeA",
                label="VICTORIA BECKHAM LIMITED",
                degree=114,
                entity_url="/v1/entity/mGq1lpuqKssNWTjIokuPeA",
                pep=False,
                psa_id="65455301594691",
                psa_count=4,
                sanctioned=False,
                closed=False,
                company_type="LADIES FASHION",
                registration_date="Incorporated 2008-02-28",
                latest_status=Status(
                    status="active",
                    date="2023-08-29",
                ),
                trade_count={"sent": 82, "received": 2},
                type="company",
                identifiers=[
                    Identifier(
                        value="06517802",
                        type="uk_company_number",
                        label="Uk Company Number",
                    ),
                    Identifier(
                        value="6517802",
                        type="unknown",
                        label="Unknown",
                    ),
                    Identifier(
                        value="04781466",
                        type="ca_corporate_id_num",
                        label="Ca Corporate Id Num",
                    ),
                ],
                addresses=[
                    "202 HAMMERSMITH ROAD , LONDON , , UNITED KINGDOM , W6 7DN , GB",
                    "Unit 33, Ransomes Dock Business Centre, 35-37 Parkgate Road, London SW11 4NP",
                    "Hammersmith Road, London, W6 7DN",
                ],
                countries=["GBR", "USA"],
                relationship_count={
                    "linked_to": 3,
                    "has_officer": 2,
                    "shareholder_of": 1,
                    "has_shareholder": 2,
                    "has_registered_agent": 5,
                    "has_director": 11,
                    "owner_of": 3,
                    "has_founder": 1,
                    "ships_to": 5,
                    "receives_from": 1,
                },
                source_count={
                    "2b618f1996252fe537a6d998ae14c9b2": SourceCountInfo(
                        count=1,
                        label="UK Corporate Registry Confirmation Statements",
                    ),
                    "2b788dbdf9194ed5a5c309386a6516b1": SourceCountInfo(
                        count=37,
                        label="UK HM Revenue & Customs Traders Database",
                    ),
                    "a447a7b622c4ead6e1caf94983dc2337": SourceCountInfo(
                        count=8,
                        label="USA California Secretary of State",
                    ),
                    "a7829d9c8999fcaa78af55886da9be06": SourceCountInfo(
                        count=43,
                        label="Turkey Imports & Exports (January 2024 - Present)",
                    ),
                    "ecdfb3f2ecc8c3797e77d5795a8066ef": SourceCountInfo(
                        count=40,
                        label="UK Corporate Registry",
                    ),
                    "e5de7b52cc88ef4cd1a10e201bdf46ee": SourceCountInfo(
                        count=41,
                        label="Vietnam Imports & Exports (January 2023 - Present)",
                    ),
                    "2a4fe9a14e332c8f9ded1f8a457c2b89": SourceCountInfo(
                        count=42,
                        label="UK Land Commercial and Corporate Ownership Data (CCOD)",
                    ),
                    "4ea8bac1bed868e1510ffd21842e9551": SourceCountInfo(
                        count=86,
                        label="UK Persons with Significant Control",
                    ),
                },
                risk={
                    "basel_aml": RiskData(
                        value=4.28,
                        metadata={"country": ["USA"]},
                        level="relevant",
                    ),
                    "cpi_score": RiskData(
                        value=69.0,
                        metadata={"country": ["USA"]},
                        level="relevant",
                    ),
                },
                user_attribute_counts={},
                user_attribute_count={},
                user_record_count=0,
                user_related_entities_count=0,
                user_relationship_count={},
                related_entities_count=114,
                attribute_counts={
                    "company_type": 3,
                    "name": 2,
                    "business_purpose": 4,
                    "identifier": 3,
                    "additional_information": 106,
                    "country": 7,
                    "status": 5,
                    "address": 6,
                },
                attribute_count={
                    "company_type": 3,
                    "name": 2,
                    "business_purpose": 4,
                    "identifier": 3,
                    "additional_information": 106,
                    "country": 7,
                    "status": 5,
                    "address": 6,
                },
                reference_id="ecdfb3f2ecc8c3797e77d5795a8066ef/06517802/1540252800000:4a34442eccf1622995130b194a5d50e7",
                coordinates=[
                    Coordinates(
                        lat=51.49322001798694,
                        lng=-0.2220315859755715,
                        address="202 HAMMERSMITH ROAD , LONDON , , UNITED KINGDOM , W6 7DN , GB",
                    ),
                    Coordinates(
                        lat=51.47911101182882,
                        lng=-0.16811097048599777,
                        address="Unit 33, Ransomes Dock Business Centre, 35-37 Parkgate Road, London SW11 4NP",
                    ),
                    Coordinates(
                        lat=51.493835014595135,
                        lng=-0.21932487497451175,
                        address="Hammersmith Road, London, W6 7DN",
                    ),
                    Coordinates(
                        lat=53.06030545100003,
                        lng=-1.4104778399999418,
                        address="202 HAMMERSMITH ROAD UNITED KINGDOM",
                    ),
                    Coordinates(
                        address="202 HAMMERSMITH ROAD",
                    ),
                    Coordinates(
                        lat=51.490490045109766,
                        lng=-0.2455951217808129,
                        address="202 HAMMERSMITH ROAD BRITISH ISLES",
                    ),
                ],
                matches={
                    "name": [
                        "<em>VICTORIA</em> <em>BECKHAM</em> <em>LIMITED</em>",
                        "<em>BECKHAM</em> VENTURES <em>LIMITED</em>",
                        "<em>VICTORIA</em> <em>BECKHAM</em> LIMITED",
                        "<em>BECKHAM</em> VENTURES LIMITED",
                    ]
                },
            )
        ],
    )
    """

    offset: int
    next: bool
    data: typing.List[SearchResults]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
