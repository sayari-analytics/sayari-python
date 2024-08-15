# This file was auto-generated by Fern from our API Definition.

from ...base_types.types.paginated_response import PaginatedResponse
import typing
from .position_data import PositionData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PositionInfo(PaginatedResponse):
    """
    An attribute used for many different relationship types that allows for the inclusion of a title or designation (e.g., member_of_the_board_of, Position: "Secretary of the Board" or shareholder_of, Position: "Minority shareholder")
    """

    data: typing.List[PositionData]
    next: typing.Optional[typing.Optional[typing.Any]] = None
    offset: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
