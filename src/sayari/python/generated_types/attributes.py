# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Attributes(str, enum.Enum):
    ADDRESS = "address"
    MEASUREMENT = "measurement"
    WEAK_IDENTIFIER = "weak_identifier"
    COUNTRY = "country"
    GENDER = "gender"
    GENERIC = "generic"
    SHARES = "shares"
    IDENTIFIER = "identifier"
    STATUS = "status"
    DATE_OF_BIRTH = "date_of_birth"
    FINANCES = "finances"
    ADDITIONAL_INFORMATION = "additional_information"
    POSITION = "position"
    CONTACT = "contact"
    BUSINESS_PURPOSE = "business_purpose"
    RISK_INTELLIGENCE = "risk_intelligence"
    TRANSLATED_NAME = "translated_name"
    NAME = "name"
    PERSON_STATUS = "person_status"
    MONETARY_VALUE = "monetary_value"
    COMPANY_TYPE = "company_type"
    FINANCIALS = "financials"

    def visit(
        self,
        address: typing.Callable[[], T_Result],
        measurement: typing.Callable[[], T_Result],
        weak_identifier: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        gender: typing.Callable[[], T_Result],
        generic: typing.Callable[[], T_Result],
        shares: typing.Callable[[], T_Result],
        identifier: typing.Callable[[], T_Result],
        status: typing.Callable[[], T_Result],
        date_of_birth: typing.Callable[[], T_Result],
        finances: typing.Callable[[], T_Result],
        additional_information: typing.Callable[[], T_Result],
        position: typing.Callable[[], T_Result],
        contact: typing.Callable[[], T_Result],
        business_purpose: typing.Callable[[], T_Result],
        risk_intelligence: typing.Callable[[], T_Result],
        translated_name: typing.Callable[[], T_Result],
        name: typing.Callable[[], T_Result],
        person_status: typing.Callable[[], T_Result],
        monetary_value: typing.Callable[[], T_Result],
        company_type: typing.Callable[[], T_Result],
        financials: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Attributes.ADDRESS:
            return address()
        if self is Attributes.MEASUREMENT:
            return measurement()
        if self is Attributes.WEAK_IDENTIFIER:
            return weak_identifier()
        if self is Attributes.COUNTRY:
            return country()
        if self is Attributes.GENDER:
            return gender()
        if self is Attributes.GENERIC:
            return generic()
        if self is Attributes.SHARES:
            return shares()
        if self is Attributes.IDENTIFIER:
            return identifier()
        if self is Attributes.STATUS:
            return status()
        if self is Attributes.DATE_OF_BIRTH:
            return date_of_birth()
        if self is Attributes.FINANCES:
            return finances()
        if self is Attributes.ADDITIONAL_INFORMATION:
            return additional_information()
        if self is Attributes.POSITION:
            return position()
        if self is Attributes.CONTACT:
            return contact()
        if self is Attributes.BUSINESS_PURPOSE:
            return business_purpose()
        if self is Attributes.RISK_INTELLIGENCE:
            return risk_intelligence()
        if self is Attributes.TRANSLATED_NAME:
            return translated_name()
        if self is Attributes.NAME:
            return name()
        if self is Attributes.PERSON_STATUS:
            return person_status()
        if self is Attributes.MONETARY_VALUE:
            return monetary_value()
        if self is Attributes.COMPANY_TYPE:
            return company_type()
        if self is Attributes.FINANCIALS:
            return financials()
