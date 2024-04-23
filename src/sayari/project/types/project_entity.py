# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...shared_types.types.core_entity import CoreEntity
from .project_entity_upstream import ProjectEntityUpstream
from .psa_summary import PsaSummary


class ProjectEntity(pydantic_v1.BaseModel):
    id: str
    project: str
    label: str = pydantic_v1.Field()
    """
    Entity label (display name).
    """

    created: str
    updated: str
    updated_by: str
    version: int = pydantic_v1.Field()
    """
    Will be 0.
    """

    type: typing.Literal["entity"]
    entity_id: str = pydantic_v1.Field()
    """
    Entity ID.
    """

    tag_ids: typing.List[str]
    case_status: str
    match_strength: typing.Any
    shipped_hs_codes: typing.List[str] = pydantic_v1.Field()
    """
    HS codes shipped by the entity.
    """

    received_hs_codes: typing.List[str] = pydantic_v1.Field()
    """
    HS codes received by the entity.
    """

    upstream: ProjectEntityUpstream
    summary: CoreEntity
    psa: typing.Optional[PsaSummary] = None

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