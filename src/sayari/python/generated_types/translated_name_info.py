# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..base_types.paginated_response import PaginatedResponse
from ..core.datetime_utils import serialize_datetime
from .translated_name_data import TranslatedNameData


class TranslatedNameInfo(PaginatedResponse):
    """
    A name that has been translated to English
    """

    data: typing.List[TranslatedNameData]
    next: typing.Optional[typing.Any]
    offset: typing.Optional[int]

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
