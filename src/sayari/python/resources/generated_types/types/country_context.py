# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CountryContext(str, enum.Enum):
    """
    Country context enums describe different ways an entity can be connected to a country.
    """

    CITIZENSHIP = "citizenship"
    """
    The reported citizenship of a person
    """

    INCORPORATION = "incorporation"
    """
    Rarely used. Converted to "domicile".
    """

    RESIDENCE = "residence"
    """
    The reported country of residence of a person
    """

    NATIONALITY = "nationality"
    """
    The reported nationality of a person
    """

    ADDRESS = "address"
    """
    The country of an entity address
    """

    VESSEL_FLAG = "vessel_flag"
    """
    The flag state of a vessel. Often changes over time.
    """

    DOMICILE = "domicile"
    """
    e.g., "Country of incorporation", "Jurisdiction of formation", "Organized under the laws of". A company can operate in multiple countries, but can only have one domicile at a time.
    """

    SHIPMENT_DEPARTURE = "shipment_departure"
    """
    The country a shipment starts in
    """

    SHIPMENT_ARRIVAL = "shipment_arrival"
    """
    The country of the consignee/recipient of a shipment
    """

    SHIPMENT_TRANSIT = "shipment_transit"
    """
    Any country a shipment moves through between its departure and arrival
    """

    ACTIVITY_IN = "activity_in"
    """
    The entity is the principal entity in a record originating from this country
    """

    MENTIONED_IN = "mentioned_in"
    """
    The entity is mentioned in a record originating from this country
    """

    def visit(
        self,
        citizenship: typing.Callable[[], T_Result],
        incorporation: typing.Callable[[], T_Result],
        residence: typing.Callable[[], T_Result],
        nationality: typing.Callable[[], T_Result],
        address: typing.Callable[[], T_Result],
        vessel_flag: typing.Callable[[], T_Result],
        domicile: typing.Callable[[], T_Result],
        shipment_departure: typing.Callable[[], T_Result],
        shipment_arrival: typing.Callable[[], T_Result],
        shipment_transit: typing.Callable[[], T_Result],
        activity_in: typing.Callable[[], T_Result],
        mentioned_in: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CountryContext.CITIZENSHIP:
            return citizenship()
        if self is CountryContext.INCORPORATION:
            return incorporation()
        if self is CountryContext.RESIDENCE:
            return residence()
        if self is CountryContext.NATIONALITY:
            return nationality()
        if self is CountryContext.ADDRESS:
            return address()
        if self is CountryContext.VESSEL_FLAG:
            return vessel_flag()
        if self is CountryContext.DOMICILE:
            return domicile()
        if self is CountryContext.SHIPMENT_DEPARTURE:
            return shipment_departure()
        if self is CountryContext.SHIPMENT_ARRIVAL:
            return shipment_arrival()
        if self is CountryContext.SHIPMENT_TRANSIT:
            return shipment_transit()
        if self is CountryContext.ACTIVITY_IN:
            return activity_in()
        if self is CountryContext.MENTIONED_IN:
            return mentioned_in()
