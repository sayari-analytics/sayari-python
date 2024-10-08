# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import pydantic
from .project_counts import ProjectCounts
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Project(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique project identifier.
    """

    label: str = pydantic.Field()
    """
    Most recently set name for the project.
    """

    archived: bool = pydantic.Field()
    """
    Whether the project is archived. Archival is a soft delete.
    """

    created: str
    updated: str
    counts: ProjectCounts

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
