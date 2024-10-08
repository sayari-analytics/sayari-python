# This file was auto-generated by Fern from our API Definition.

from ...base_types.types.paginated_response import PaginatedResponse
import typing
from .identifier_data import IdentifierData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class IdentifierInfo(PaginatedResponse):
    """
    An ID number that uniquely identifies one entity when value and type are taken into account.
    """

    data: typing.List[IdentifierData]
    next: typing.Optional[typing.Optional[typing.Any]] = None
    offset: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
