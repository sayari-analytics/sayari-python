# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .translation_context import TranslationContext
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class TranslatedNameProperties(UniversalBaseModel):
    context: typing.Optional[TranslationContext] = pydantic.Field(default=None)
    """
    The type of translation
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    as-of date
    """

    from_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    start date
    """

    original: typing.Optional[str] = pydantic.Field(default=None)
    """
    The original name
    """

    to_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    end date
    """

    value: str = pydantic.Field()
    """
    The name, as text
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
