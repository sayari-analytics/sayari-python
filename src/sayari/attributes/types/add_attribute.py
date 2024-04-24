# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1


class AddAttribute(pydantic_v1.BaseModel):
    """
    from sayari import AddAttribute

    AddAttribute(
        entity="zq04axX2dLn9tE6W6Q8Qhg",
        type="address",
        value={
            "street1": "1600 Pennsylvania Avenue NW",
            "city": "Washington DC",
            "state": "Washington DC",
            "postalCode": "20500",
            "country": "US",
        },
        to_date="2024-04-30",
        from_date="2024-01-01",
        date="2024-02-15",
    )
    """

    entity: str = pydantic_v1.Field()
    """
    entity ID
    """

    type: str = pydantic_v1.Field()
    """
    type of additional information
    """

    value: typing.Any = pydantic_v1.Field()
    """
    value of additional information in JSON format
    """

    date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    as of date of the attribute
    """

    from_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    start date of the attribute
    """

    to_date: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    end date of the attribute
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
