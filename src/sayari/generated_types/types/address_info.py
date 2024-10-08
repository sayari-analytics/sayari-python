# This file was auto-generated by Fern from our API Definition.

from ...base_types.types.paginated_response import PaginatedResponse
import typing
from .address_data import AddressData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class AddressInfo(PaginatedResponse):
    """
    A physical location description. Addresses may exist as a simple string ("123 South Main St., South Bend, IN 46556"), or may be in smaller chunks with separate fields ("Number: 123", "Street name: South Main ..."). Where possible, these fields will be parsed using the [Libpostal ontology](https://github.com/openvenues/libpostal#parser-labels), which facilitates more robust address analysis and comparison.
    """

    data: typing.List[AddressData]
    next: typing.Optional[typing.Optional[typing.Any]] = None
    offset: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
