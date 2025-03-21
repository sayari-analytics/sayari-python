# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .measurement_type import MeasurementType
from .unit import Unit
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class MeasurementProperties(UniversalBaseModel):
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

    type: MeasurementType = pydantic.Field()
    """
    Type of the measurement
    """

    unit: Unit = pydantic.Field()
    """
    The unit of the measurement
    """

    value: float = pydantic.Field()
    """
    The value of the measurement
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
