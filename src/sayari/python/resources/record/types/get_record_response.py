# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...shared_types.types.record_details import RecordDetails
from .record_references import RecordReferences


class GetRecordResponse(RecordDetails):
    """
    OK
    ---
    from sayari-analytics import (CountQualifier, GetRecordResponse,
                                  QualifiedCount, RecordReferences)

    GetRecordResponse(id="74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254", label="Company Record from Hong Kong Companies Registry", source="74cf0fc2a62f9c8f4e88f8a0b3ffcca4", publication_date="2023-05-01", acquisition_date="2023-05-01", references_count=1, record_url="/v1/record/74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254", source_url="https://data.gov.hk/en-data/dataset/hk-cr-crdata-list-addr", document_urls=["/document/74cf0fc2a62f9c8f4e88f8a0b3ffcca4%2FF0000110%2F1682970471254/file/json%2FF0000110.json"], references=RecordReferences(next=False, offset=0, limit=100, size=QualifiedCount(count=1, qualifier=CountQualifier.EQ, ), data=[{"entity": {"id": "YUc8LtKFCpAbUIBGK8nQpw", "label": "\u4e2d\u56fd\u94f6\u884c\u80a1\u4efd\u6709\u9650\u516c\u53f8", "degree": 17908, "entity_url": "/v1/entity/YUc8LtKFCpAbUIBGK8nQpw", "pep": false, "psa_count": 0, "sanctioned": false, "closed": false, "translated_label": "Bank of China Limited", "company_type": "\u4f01\u4e1a\u6cd5\u4eba", "registration_date": "Incorporated 1983-10-31", "latest_status": {"status": "inactive"}, "type": "company", "identifiers": [{"value": "54930053HGCFWVHYZX42", "type": "lei", "label": "Lei"}, {"value": "911000001000013428", "type": "cn_unified_social_credit_code", "label": "Cn Unified Social Credit Code"}, {"value": "100000000001349", "type": "cn_registration_number", "label": "Cn Registration Number"}, {"value": "166044", "type": "xxx_edi_global_issuer_id", "label": "Xxx Edi Global Issuer Id"}, {"value": "3706001901616", "type": "unknown", "label": "Unknown"}], "addresses": ["No. 1 Fuxingmen Nei Dajie, Beijing 100818, China", "\u5317\u4eac\u5e02\u590d\u5174\u95e8\u5185\u5927\u88571\u53f7", "1 Fuxingmen Nei Dajie, Beijing, 100818, PRC"], "countries": ["CHN", "FRA", "MMR", "SGP", "HKG"], "relationship_count": {"linked_to": 20, "branch_of": 155, "has_branch": 11426, "beneficial_owner_of": 1, "party_to": 1, "has_manager": 4, "shareholder_of": 279, "has_shareholder": 102, "has_director": 87, "has_supervisor": 28, "owner_of": 3, "has_subsidiary": 103, "has_legal_representative": 7, "issuer_of": 6006}, "source_count": {"1fbdc8f3abdf32274f4c7657c048294a": {"count": 2, "label": "China CNinfo Shanghai/Shenzhen Stock Exchange Database"}, "fcfa3d1c6b5f9744188fc01d0999fb76": {"count": 404, "label": "China SAIC"}, "bf68c3a9a482c02f1f76342feb79af8d": {"count": 1, "label": "China Company Directory (Xin Gongshang Minglu)(Web Crawled Data)"}, "a025b3503797a9cd1e1964dec6943594": {"count": 764, "label": "Hong Kong Stock Exchange - Shareholding Disclosures"}, "78586b6984ecb00e81563ae3d31c9227": {"count": 1, "label": "Myanmar DICA"}, "db3416894cd5f0c4d2d6ecc79bdaf366": {"count": 21, "label": "EDI Publicly-Listed Global Security Issuers (3rd Party Data)"}, "b812677c0a32a1746b3ac741c7b97ae0": {"count": 59948, "label": "Legal Entity Identifier (LEI) Registry (3rd Party Data)"}, "0ff02c63234d4447c803acd7748b9afc": {"count": 15, "label": "China Company Directory (Shuidi)(Web Crawled Data)"}, "b6382672c6741fe1bca28d2668c1732b": {"count": 200, "label": "China LHNB MOFCOM Foreign Investment Directory"}, "2cd05c04774a433ce4d79e61ee105d08": {"count": 5, "label": "Hong Kong Judiciary Judgments"}, "0cf0044442daf17258e27a6ddd49770f": {"count": 223, "label": "China NECIPS"}, "148946e7e3e5b2ba031bfcefa28e4d83": {"count": 17, "label": "China Company Directory (Aiqicha)(Web Crawled Data)"}, "7e0b45866bdcca61b2cfd455e5403dc2": {"count": 9, "label": "China Central Government Procurement Center Enterprise Database"}, "74cf0fc2a62f9c8f4e88f8a0b3ffcca4": {"count": 2, "label": "Hong Kong Companies Registry"}, "8f21460f1cc54773b9672cb5efdb01cf": {"count": 7, "label": "China Ministry of Finance Government Procurement Announcements"}}, "risk": {"basel_aml": {"value": 6.81, "metadata": {"country": ["CHN"]}, "level": "relevant"}, "state_owned": {"value": true, "metadata": {}, "level": "high"}, "meu_list_contractors": {"value": true, "metadata": {"sources": ["China Central Government Procurement Center Enterprise Database", "China Ministry of Finance Government Procurement Announcements"]}, "level": "high"}, "cpi_score": {"value": 45, "metadata": {"country": ["CHN"]}, "level": "relevant"}, "owner_of_forced_labor_xinjiang_entity": {"value": 1, "metadata": {}, "level": "high"}, "owner_of_regulatory_action_entity": {"value": 1, "metadata": {}, "level": "high"}}}, "type": "about"}], ), )
    """

    references: RecordReferences

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
