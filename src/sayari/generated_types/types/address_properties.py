# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .language import Language


class AddressProperties(pydantic_v1.BaseModel):
    building: typing.Optional[str] = None
    category: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    For category queries like "restaurants", etc.
    """

    city: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Any human settlement, including cities, towns, villages, hamlets, localities, etc.
    """

    city_district: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Boroughs or districts within a city that serve some official purpose (e.g., "Brooklyn", "Hackney", or "Bratislava IV")
    """

    country: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Sovereign nations and their dependent territories; anything with an ISO 3166 code
    """

    country_region: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Informal subdivision of a country without any political status
    """

    date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    as-of date
    """

    entrance: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Numbered/lettered entrance
    """

    from_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    start date
    """

    house: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Building/site name (e.g., "Brooklyn Academy of Music", "Empire State Building")
    """

    house_number: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Usually refers to the external (street-facing) building number. In some jurisdictions, this may be a compound number that also includes an apartment/block number.
    """

    island: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Named islands (e.g., "Maui")
    """

    language: typing.Optional[Language] = pydantic_v1.Field(default=None)
    """
    The language in which the address was provided in the record
    """

    level: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Expressions indicating a floor number (e.g., "3rd Floor", "Ground Floor")
    """

    metro_station: typing.Optional[str] = None
    near: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Phrases like "in", "near", etc. used after a category phrase, to help with parsing queries like "restaurants in Brooklyn"
    """

    normalized: str
    po_box: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Typically found in non-physical (mail-only) addresses
    """

    postcode: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Postal codes used for mail sorting
    """

    precision_code: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A code describing the precision of the X and Y coordinates
    """

    road: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Street name(s)
    """

    staircase: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Numbered/lettered staircase
    """

    state: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A first-level administrative division, including provinces and departments. Scotland, Northern Ireland, Wales, and England in the UK are also mapped to "state" (convention commonly used in geocoding tools).
    """

    state_district: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    A second-level administrative division or county
    """

    suburb: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Usually an unofficial neighborhood name, like "Harlem", "South Bronx", or "Crown Heights"
    """

    to_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    end date
    """

    translated: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The address value translated to English
    """

    transliterated: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The address value transliterated to English
    """

    type: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Indicates what the address is referring to. For example, it could be a physical address, mailing address, or other address type.
    """

    unit: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    An apartment, unit, office, lot, or other secondary unit designator
    """

    value: typing.Optional[str] = None
    world_region: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Currently only used for appending “West Indies” after the country name, a pattern frequently used in the English-speaking Caribbean (e.g., “Jamaica, West Indies”)
    """

    x: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The X coordinate (longitude) of the address
    """

    y: typing.Optional[float] = pydantic_v1.Field(default=None)
    """
    The Y coordinate (latitude) of the address
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
