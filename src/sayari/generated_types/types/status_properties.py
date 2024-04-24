# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .company_status import CompanyStatus
from .status_context import StatusContext


class StatusProperties(pydantic_v1.BaseModel):
    context: typing.Optional[StatusContext] = pydantic_v1.Field(default=None)
    """
    The type of status, such as license or partnership type
    """

    date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    as-of date
    """

    from_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    start date
    """

    text: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    The raw status text
    """

    to_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    end date
    """

    value: typing.Optional[CompanyStatus] = pydantic_v1.Field(default=None)
    """
    The status, normalized to one of the status enums
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
