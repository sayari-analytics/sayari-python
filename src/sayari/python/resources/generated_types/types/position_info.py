# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...base_types.types.paginated_response import PaginatedResponse
from .position_data import PositionData


class PositionInfo(PaginatedResponse):
    """
    An attribute used for many different relationship types that allows for the inclusion of a title or designation (e.g., member_of_the_board_of, Position: "Secretary of the Board" or shareholder_of, Position: "Minority shareholder")
    """

    data: typing.List[PositionData]
    next: typing.Optional[typing.Any] = None
    offset: typing.Optional[int] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
