# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .language import Language
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class NameProperties(UniversalBaseModel):
    context: typing.Optional[str] = None
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

    language: typing.Optional[Language] = pydantic.Field(default=None)
    """
    The language that the name is in
    """

    to_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    end date of attribute
    """

    translated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name value translated to English
    """

    transliterated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name value transliterated to English
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
