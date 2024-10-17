# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...base_types.types.paginated_response import PaginatedResponse
from ...shared_types.types.entity_details import EntityDetails
from ...shared_types.types.entity_relationships import EntityRelationships
from ...shared_types.types.relationship_data import RelationshipData
import typing
from .supplier_or_buyer import SupplierOrBuyer
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...core.pydantic_utilities import update_forward_refs


class BuyerSearchResponse(PaginatedResponse):
    """
    OK

    Examples
    --------
    from sayari.base_types import QualifiedCount
    from sayari.shared_types import Identifier, RiskData, SourceCountInfo
    from sayari.trade import (
        BuyerSearchResponse,
        HsCode,
        SupplierMetadata,
        SupplierOrBuyer,
    )

    BuyerSearchResponse(
        offset=0,
        limit=1,
        size=QualifiedCount(
            count=3,
            qualifier="eq",
        ),
        next=True,
        data=[
            SupplierOrBuyer(
                id="uWNWgzX-Kvp1j-WeXKmLQw",
                label='ООО "ЭРБЭ ЭЛЕКТРОМЕДИЦИН"',
                degree=195,
                entity_url="/v1/entity/uWNWgzX-Kvp1j-WeXKmLQw",
                pep=False,
                psa_id="4398046624552",
                psa_count=1,
                sanctioned=False,
                closed=False,
                translated_label='GESELLSCHAFT MIT BESCHRANKTER HAFTUNG "ERBE ELEKTROMEDIZIN"',
                registration_date="Registered 2008-09-08",
                trade_count={"sent": 0, "received": 192},
                type="company",
                identifiers=[
                    Identifier(
                        value="7705856072",
                        type="ru_inn",
                        label="Ru Inn",
                    ),
                    Identifier(
                        value="5087746065578",
                        type="ru_ogrn",
                        label="Ru Ogrn",
                    ),
                    Identifier(
                        value="770401001",
                        type="ru_kpp",
                        label="Ru Kpp",
                    ),
                    Identifier(
                        value="ФС-99-04-005763",
                        type="ru_license_number",
                        label="Ru License Number",
                    ),
                    Identifier(
                        value="Л016-00110-77/00565584",
                        type="ru_license_number",
                        label="Ru License Number",
                    ),
                ],
                addresses=[
                    "119270, , Г.МОСКВА, УЛ.ХАМОВНИЧЕСКИЙ ВАЛ,Д.12,ЭТ.2,ПОМ.Х,КОМ.15,",
                    "119270, , Г.МОСКВА, УЛ.ХАМОВНИЧЕСКИЙ ВАЛ,Д.12,ЭТ12,ПОМ.Х,КОМ.15,",
                    "119270, ГОРОД МОСКВА, УЛ. ХАМОВНИЧЕСКИЙ ВАЛ, Д. 12, ЭТАЖ 2 ПОМ Х КОМ 15",
                ],
                countries=["RUS"],
                relationship_count={
                    "has_shareholder": 1,
                    "notify_party_of": 133,
                    "has_director": 1,
                    "receives_from": 1,
                    "has_legal_representative": 1,
                },
                source_count={
                    "a9a18eeb901e4376c912e95dc05ceb78": SourceCountInfo(
                        count=9,
                        label="Russia Federal Tax Registry",
                    ),
                    "66dfefb726ae00fde8f09f34c5578d35": SourceCountInfo(
                        count=360,
                        label="Russia Imports & Exports (January 2023 - Present)",
                    ),
                    "e61c3b3478534c110b46cd64c7746e82": SourceCountInfo(
                        count=2,
                        label="Russia Federal Tax Service Financial Statements",
                    ),
                    "56bce0e008204712e302271ddd7b4fb1": SourceCountInfo(
                        count=1,
                        label="Russia Federal Tax Registry (2018)",
                    ),
                },
                risk={
                    "imports_bis_high_priority_items": RiskData(
                        value=1.0,
                        metadata={"origin_shipment_product": ["853669"]},
                        level="elevated",
                    ),
                    "imports_bis_high_priority_items_critical_components": RiskData(
                        value=1.0,
                        metadata={"origin_shipment_product": ["854231"]},
                        level="high",
                    ),
                },
                user_attribute_counts={},
                user_attribute_count={},
                user_record_count=0,
                user_related_entities_count=0,
                user_relationship_count={},
                related_entities_count=195,
                attribute_counts={
                    "name": 3,
                    "business_purpose": 10,
                    "identifier": 7,
                    "additional_information": 2,
                    "country": 2,
                    "shares": 1,
                    "status": 1,
                    "address": 4,
                    "financials": 3,
                },
                attribute_count={
                    "name": 3,
                    "business_purpose": 10,
                    "identifier": 7,
                    "additional_information": 2,
                    "country": 2,
                    "shares": 1,
                    "status": 1,
                    "address": 4,
                    "financials": 3,
                },
                reference_id="56bce0e008204712e302271ddd7b4fb1/5087746065578_7705856072_OOO-ERBE-ELEKTROMEDICIN.html/1552661755844:e39b6745ba02f2a46afdd7ffbd700920",
                metadata=SupplierMetadata(
                    latest_shipment_date="2024-07-10",
                    shipments=6,
                    hs_codes=[
                        HsCode(
                            key="854231",
                            doc_count=6,
                            value="Electronic integrated circuits; processors and controllers, whether or not combined with memories, converters, logic circuits, amplifiers, clock and timing circuits, or other circuits",
                            value_simple="Integrated Circuits",
                        )
                    ],
                ),
            )
        ],
    )
    """

    offset: int
    next: bool
    data: typing.List[SupplierOrBuyer]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EntityDetails, BuyerSearchResponse=BuyerSearchResponse)
update_forward_refs(EntityRelationships, BuyerSearchResponse=BuyerSearchResponse)
update_forward_refs(RelationshipData, BuyerSearchResponse=BuyerSearchResponse)
