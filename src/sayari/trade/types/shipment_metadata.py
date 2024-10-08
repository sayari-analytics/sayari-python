# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...generated_types.types.country import Country
import pydantic
from ...generated_types.types.address_properties import AddressProperties
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ShipmentMetadata(UniversalBaseModel):
    arrival_country: typing.List[Country]
    jurisdiction: typing.List[Country]
    reference_id: str
    entity_id: str = pydantic.Field()
    """
    Unique identifier of the entity
    """

    departure_address: typing.Optional[AddressProperties] = None
    type: str
    sources: typing.List[str]
    departure_country: typing.List[Country]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
