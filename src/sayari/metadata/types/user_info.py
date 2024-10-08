# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class UserInfo(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Currently logged in user ID
    """

    group_display_names: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="groupDisplayNames")] = (
        pydantic.Field(default=None)
    )
    """
    Name of the sayari organization tied to credentials
    """

    roles: typing.Optional[str] = pydantic.Field(default=None)
    """
    Licenses associated with the organization
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
