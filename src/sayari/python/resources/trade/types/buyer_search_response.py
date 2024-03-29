# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...base_types.types.paginated_response import PaginatedResponse
from .supplier_or_buyer import SupplierOrBuyer


class BuyerSearchResponse(PaginatedResponse):
    """
    OK
    ---
    from sayari-analytics import (BuyerSearchResponse, CountQualifier, Country,
                                  Entities, HsCode, Identifier, QualifiedCount,
                                  Relationships, SourceCountInfo, SupplierMetadata,
                                  SupplierOrBuyer)

    BuyerSearchResponse(offset=0, limit=1, size=QualifiedCount(count=5974, qualifier=CountQualifier.EQ, ), next=True, data=[SupplierOrBuyer(id="VRttegVx-TLCsNHKfNe1Cw", label='Товариство з обмеженою відповідальністю "ВЕСТ-СПРИНТ"', degree=4333, entity_url="/v1/entity/VRttegVx-TLCsNHKfNe1Cw", pep=False, psa_count=0, sanctioned=False, closed=False, translated_label="VOLYN LIMITED LIABILITY COMPANY VOLYN INSTITUTE OF INFORMATION TECHNOLOGIES", company_type="АДВОКАТСЬКЕ БЮРО", registration_date="Registered 2021-02-02", type=Entities.COMPANY, identifiers=[Identifier(value="44102648", label="Ukr Edrpou", ), Identifier(value="43994030", label="Ukr Edrpou", ), Identifier(value="43913941", label="Ukr Edrpou", ), Identifier(value="44154434", label="Ukr Edrpou", ), Identifier(value="10019810200000131", label="Ukr Reg Num", )], addresses=[".", "Україна, 43020, Волинська обл., місто Луцьк, вул.Рівненська, будинок 48", "Україна, 43020, Волинська обл., місто Луцьк, вул.Електроапаратна, будинок 17"], countries=[Country.UKR], relationship_count={Relationships.RECEIVER_OF: 4142, Relationships.HAS_BENEFICIAL_OWNER: 73, Relationships.HAS_OFFICER: 65, Relationships.HAS_SHAREHOLDER: 75, Relationships.HAS_FOUNDER: 78, Relationships.RECEIVES_FROM: 98, Relationships.HAS_LEGAL_REPRESENTATIVE: 4}, source_count={"96c06a5a03b61b91324c7e05b3114fb6": SourceCountInfo(count=4142, label="Ukraine Imports & Exports (January 2023 - Present)", ), "d1bce737c158efddbef5048d63aaf124": SourceCountInfo(count=241, label="Ukraine Ministry of Justice Registry of Companies", )}, risk={}, user_attribute_counts={}, user_record_count=0, user_related_entities_count=0, user_relationship_count={}, related_entities_count=4333, attribute_counts={"company_type": 6, "name": 77, "business_purpose": 100, "identifier": 70, "additional_information": 56, "country": 2, "contact": 27, "status": 70, "address": 14}, metadata=SupplierMetadata(latest_shipment_date="2023-10-28", shipments=4142, hs_codes=[HsCode(key="870323", doc_count=1492, value="Vehicles; with only spark-ignition internal combustion reciprocating piston engine, cylinder capacity over 1500 but not over 3000cc", value_simple="Cars & Passenger Vehicles", ), HsCode(key="8703239013", doc_count=1477, value="Vehicles; with only spark-ignition internal combustion reciprocating piston engine, cylinder capacity over 1500 but not over 3000cc", value_simple="Cars & Passenger Vehicles", ), HsCode(key="870332", doc_count=897, value="Vehicles; with only compression-ignition internal combustion piston engine (diesel or semi-diesel), cylinder capacity over 1500 but not over 2500cc", value_simple="Cars & Passenger Vehicles", ), HsCode(key="8703329030", doc_count=830, value="Vehicles; with only compression-ignition internal combustion piston engine (diesel or semi-diesel), cylinder capacity over 1500 but not over 2500cc", value_simple="Cars & Passenger Vehicles", ), HsCode(key="870322", doc_count=551, value="Vehicles; with only spark-ignition internal combustion piston engine, cylinder capacity over 1000 but not over 1500cc", value_simple="Cars & Passenger Vehicles", )], ), )], )
    """

    offset: int
    next: bool
    data: typing.List[SupplierOrBuyer]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
