# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .project_counts import ProjectCounts


class Project(pydantic_v1.BaseModel):
    id: str = pydantic_v1.Field()
    """
    Unique project identifier.
    """

    label: str = pydantic_v1.Field()
    """
    Most recently set name for the project.
    """

    archived: bool = pydantic_v1.Field()
    """
    Whether the project is archived. Archival is a soft delete.
    """

    created: str
    updated: str
    counts: ProjectCounts

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}