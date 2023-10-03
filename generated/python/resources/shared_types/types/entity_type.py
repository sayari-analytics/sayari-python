# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EntityType(str, enum.Enum):
    AIRCRAFT = "Aircraft"
    COMPANY = "Company"
    GENERIC = "Generic"
    INTELLECTUAL_PROPERTY = "Intellectual Property"
    LEGAL_MATTER = "Legal Matter"
    PERSON = "Person"
    PROPERTY = "Property"
    SECURITY = "Security"
    SHIPMENT = "Shipment"
    TRADENAME = "Tradename"
    UNKNOWN = "Unknown"
    VESSEL = "Vessel"

    def visit(
        self,
        aircraft: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        generic: typing.Callable[[], T_Result],
        intellectual_property: typing.Callable[[], T_Result],
        legal_matter: typing.Callable[[], T_Result],
        person: typing.Callable[[], T_Result],
        property: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        shipment: typing.Callable[[], T_Result],
        tradename: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        vessel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EntityType.AIRCRAFT:
            return aircraft()
        if self is EntityType.COMPANY:
            return company()
        if self is EntityType.GENERIC:
            return generic()
        if self is EntityType.INTELLECTUAL_PROPERTY:
            return intellectual_property()
        if self is EntityType.LEGAL_MATTER:
            return legal_matter()
        if self is EntityType.PERSON:
            return person()
        if self is EntityType.PROPERTY:
            return property()
        if self is EntityType.SECURITY:
            return security()
        if self is EntityType.SHIPMENT:
            return shipment()
        if self is EntityType.TRADENAME:
            return tradename()
        if self is EntityType.UNKNOWN:
            return unknown()
        if self is EntityType.VESSEL:
            return vessel()
