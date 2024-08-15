# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .finance_type import FinanceType
import pydantic
from .currency import Currency
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class FinancesProperties(UniversalBaseModel):
    context: typing.Optional[FinanceType] = pydantic.Field(default=None)
    """
    The type of figure
    """

    currency: typing.Optional[Currency] = pydantic.Field(default=None)
    """
    The currency, if applicable
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    as-of date
    """

    from_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    start date
    """

    to_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    end date
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    A free-text definition of the type
    """

    value: float = pydantic.Field()
    """
    The numerical amount
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
