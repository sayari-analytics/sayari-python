# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .project import Project
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class CreateProjectResponse(UniversalBaseModel):
    """
    Examples
    --------
    from sayari.project import CreateProjectResponse, Project, ProjectCounts

    CreateProjectResponse(
        data=Project(
            id="YVMBRg",
            label="Project Alpha",
            archived=False,
            created="2024-03-15 20:31:06.08855+00",
            updated="2024-03-15 20:31:06.08855+00",
            counts=ProjectCounts(
                entity=0,
                graph=0,
                record=0,
                search=0,
            ),
        ),
    )
    """

    data: Project

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
