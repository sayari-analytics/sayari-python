# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ResolutionUploadResponse(UniversalBaseModel):
    """
    Examples
    --------
    from sayari.resolution import ResolutionUploadResponse

    ResolutionUploadResponse(
        file="vbeck.json",
        uploaded="2024-10-02T20:53:24.007Z",
        count=7,
    )
    """

    file: str
    uploaded: str
    count: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
