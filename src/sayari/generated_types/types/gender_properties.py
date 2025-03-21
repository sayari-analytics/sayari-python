# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .gender import Gender
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class GenderProperties(UniversalBaseModel):
    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    as-of date of attribute
    """

    extra: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    extra information of attribute
    """

    from_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    start date of attribute
    """

    to_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    end date of attribute
    """

    value: Gender = pydantic.Field()
    """
    May be described as "female", "male", or "other"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
