# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .additional_information_info import AdditionalInformationInfo
from .address_info import AddressInfo
from .business_purpose_info import BusinessPurposeInfo
from .company_type_info import CompanyTypeInfo
from .contact_info import ContactInfo
from .country_info import CountryInfo
from .date_of_birth_info import DateOfBirthInfo
from .finances_info import FinancesInfo
from .financials_info import FinancialsInfo
from .gender_info import GenderInfo
from .generic_info import GenericInfo
from .identifier_info import IdentifierInfo
from .measurement_info import MeasurementInfo
from .monetary_value_info import MonetaryValueInfo
from .name_info import NameInfo
from .person_status_info import PersonStatusInfo
from .position_info import PositionInfo
from .risk_intelligence_info import RiskIntelligenceInfo
from .shares_info import SharesInfo
from .status_info import StatusInfo
from .translated_name_info import TranslatedNameInfo
from .weak_identifier_info import WeakIdentifierInfo


class AttributeDetails(pydantic_v1.BaseModel):
    additional_information: typing.Optional[AdditionalInformationInfo] = None
    address: typing.Optional[AddressInfo] = None
    business_purpose: typing.Optional[BusinessPurposeInfo] = None
    company_type: typing.Optional[CompanyTypeInfo] = None
    contact: typing.Optional[ContactInfo] = None
    country: typing.Optional[CountryInfo] = None
    date_of_birth: typing.Optional[DateOfBirthInfo] = None
    finances: typing.Optional[FinancesInfo] = None
    financials: typing.Optional[FinancialsInfo] = None
    gender: typing.Optional[GenderInfo] = None
    generic: typing.Optional[GenericInfo] = None
    identifier: typing.Optional[IdentifierInfo] = None
    measurement: typing.Optional[MeasurementInfo] = None
    monetary_value: typing.Optional[MonetaryValueInfo] = None
    name: typing.Optional[NameInfo] = None
    person_status: typing.Optional[PersonStatusInfo] = None
    position: typing.Optional[PositionInfo] = None
    risk_intelligence: typing.Optional[RiskIntelligenceInfo] = None
    shares: typing.Optional[SharesInfo] = None
    status: typing.Optional[StatusInfo] = None
    translated_name: typing.Optional[TranslatedNameInfo] = None
    weak_identifier: typing.Optional[WeakIdentifierInfo] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
