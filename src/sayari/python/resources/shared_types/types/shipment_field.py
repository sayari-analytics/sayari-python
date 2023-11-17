# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ShipmentField(str, enum.Enum):
    BUYER_NAME = "buyer_name"
    SUPPLIER_NAME = "supplier_name"
    BUYER_RISK = "buyer_risk"
    SUPPLIER_RISK = "supplier_risk"
    BUYER_COUNTRY = "buyer_country"
    SUPPLIER_COUNTRY = "supplier_country"
    DEPARTURE_COUNTRY = "departure_country"
    DEPARTURE_STATE = "departure_state"
    DEPARTURE_CITY = "departure_city"
    ARRIVAL_COUNTRY = "arrival_country"
    ARRIVAL_STATE = "arrival_state"
    ARRIVAL_CITY = "arrival_city"
    HS_CODE = "hs_code"
    HS_DESCRIPTION = "hs_description"
    SUPPLIER_PURPOSE = "supplier_purpose"
    BUYER_PURPOSE = "buyer_purpose"
    ARRIVAL_DATE = "arrival_date"
    WEIGHT = "weight"

    def visit(
        self,
        buyer_name: typing.Callable[[], T_Result],
        supplier_name: typing.Callable[[], T_Result],
        buyer_risk: typing.Callable[[], T_Result],
        supplier_risk: typing.Callable[[], T_Result],
        buyer_country: typing.Callable[[], T_Result],
        supplier_country: typing.Callable[[], T_Result],
        departure_country: typing.Callable[[], T_Result],
        departure_state: typing.Callable[[], T_Result],
        departure_city: typing.Callable[[], T_Result],
        arrival_country: typing.Callable[[], T_Result],
        arrival_state: typing.Callable[[], T_Result],
        arrival_city: typing.Callable[[], T_Result],
        hs_code: typing.Callable[[], T_Result],
        hs_description: typing.Callable[[], T_Result],
        supplier_purpose: typing.Callable[[], T_Result],
        buyer_purpose: typing.Callable[[], T_Result],
        arrival_date: typing.Callable[[], T_Result],
        weight: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ShipmentField.BUYER_NAME:
            return buyer_name()
        if self is ShipmentField.SUPPLIER_NAME:
            return supplier_name()
        if self is ShipmentField.BUYER_RISK:
            return buyer_risk()
        if self is ShipmentField.SUPPLIER_RISK:
            return supplier_risk()
        if self is ShipmentField.BUYER_COUNTRY:
            return buyer_country()
        if self is ShipmentField.SUPPLIER_COUNTRY:
            return supplier_country()
        if self is ShipmentField.DEPARTURE_COUNTRY:
            return departure_country()
        if self is ShipmentField.DEPARTURE_STATE:
            return departure_state()
        if self is ShipmentField.DEPARTURE_CITY:
            return departure_city()
        if self is ShipmentField.ARRIVAL_COUNTRY:
            return arrival_country()
        if self is ShipmentField.ARRIVAL_STATE:
            return arrival_state()
        if self is ShipmentField.ARRIVAL_CITY:
            return arrival_city()
        if self is ShipmentField.HS_CODE:
            return hs_code()
        if self is ShipmentField.HS_DESCRIPTION:
            return hs_description()
        if self is ShipmentField.SUPPLIER_PURPOSE:
            return supplier_purpose()
        if self is ShipmentField.BUYER_PURPOSE:
            return buyer_purpose()
        if self is ShipmentField.ARRIVAL_DATE:
            return arrival_date()
        if self is ShipmentField.WEIGHT:
            return weight()