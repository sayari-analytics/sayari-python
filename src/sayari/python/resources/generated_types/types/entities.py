# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Entities(str, enum.Enum):
    """
    This represents which type of entity is being returned.
    """

    UNKNOWN = "unknown"
    """
    An unknown placeholder entity. Rarely used. An unknown entity has insufficient information to be grouped by an existing entity type.
    """

    COMPANY = "company"
    """
    A legal entity or organization
    """

    PROPERTY = "property"
    """
    Land, real estate, real property, or personal property not categorized under another entity type
    """

    LEGAL_MATTER = "legal_matter"
    """
    A civil or criminal legal case or similar type of proceeding
    """

    PERSON = "person"
    """
    A natural person (human being)
    """

    AIRCRAFT = "aircraft"
    """
    An airplane, helicopter, or other vehicle that travels by flight
    """

    INTELLECTUAL_PROPERTY = "intellectual_property"
    """
    A trademark, patent, copyright, or similar type of intangible property
    """

    SECURITY = "security"
    """
    A tradable financial asset
    """

    GENERIC = "generic"
    """
    A generic placeholder entity. Rarely used. A generic entity typically does not fit any other entity type.
    """

    VESSEL = "vessel"
    """
    A cargo ship, oil tanker, fishing trawler, or other type of watercraft
    """

    TRADENAME = "tradename"
    """
    A discretely registered name used by a person or company not operating under its legal name. This includes doing-business-as (DBA) names, fictitious names, etc. in jurisdictions that treat them as registered objects distinct from the person/company using them.
    """

    SHIPMENT = "shipment"
    """
    A shipment between two entities
    """

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        company: typing.Callable[[], T_Result],
        property: typing.Callable[[], T_Result],
        legal_matter: typing.Callable[[], T_Result],
        person: typing.Callable[[], T_Result],
        aircraft: typing.Callable[[], T_Result],
        intellectual_property: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        generic: typing.Callable[[], T_Result],
        vessel: typing.Callable[[], T_Result],
        tradename: typing.Callable[[], T_Result],
        shipment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Entities.UNKNOWN:
            return unknown()
        if self is Entities.COMPANY:
            return company()
        if self is Entities.PROPERTY:
            return property()
        if self is Entities.LEGAL_MATTER:
            return legal_matter()
        if self is Entities.PERSON:
            return person()
        if self is Entities.AIRCRAFT:
            return aircraft()
        if self is Entities.INTELLECTUAL_PROPERTY:
            return intellectual_property()
        if self is Entities.SECURITY:
            return security()
        if self is Entities.GENERIC:
            return generic()
        if self is Entities.VESSEL:
            return vessel()
        if self is Entities.TRADENAME:
            return tradename()
        if self is Entities.SHIPMENT:
            return shipment()
