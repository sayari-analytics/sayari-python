# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .project import Project
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class DeleteProjectResponse(UniversalBaseModel):
    """
    Examples
    --------
    from sayari.project import DeleteProjectResponse, Project, ProjectCounts

    DeleteProjectResponse(
        data=Project(
            id="Gam5qG",
            label="Project Delta",
            archived=False,
            created="2024-04-24 13:43:56.546705+00",
            updated="2024-04-24 13:43:56.546705+00",
            counts=ProjectCounts(
                entity=2,
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
