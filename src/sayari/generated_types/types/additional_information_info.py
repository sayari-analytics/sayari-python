# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...base_types.types.paginated_response import PaginatedResponse
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .additional_information_data import AdditionalInformationData


class AdditionalInformationInfo(PaginatedResponse):
    """
    This is a generic attribute used to hold miscellaneous information not covered by any other attribute. Includes "value" (for the attribute itself), "type" (a name: e.g., "Real property description"), and "extra" (a miscellaneous field to hold any other details).
    """

    data: typing.List[AdditionalInformationData]
    next: typing.Optional[typing.Any] = None
    offset: typing.Optional[int] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
