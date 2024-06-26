# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...base_types.types.qualified_count import QualifiedCount
from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .project_notification_data import ProjectNotificationData


class ProjectNotificationsResponse(pydantic_v1.BaseModel):
    """
    OK

    Examples
    --------
    from sayari import (
        Notification,
        ProjectNotificationData,
        ProjectNotificationsResponse,
        QualifiedCount,
    )

    ProjectNotificationsResponse(
        offset=0,
        limit=20,
        next=False,
        size=QualifiedCount(
            count=3,
            qualifier="eq",
        ),
        data=[
            ProjectNotificationData(
                id="dlOL1cZzEkIEZcRUcrBZCQ",
                entity_id="dlOL1cZzEkIEZcRUcrBZCQ",
                resource_id="0eZQ43",
                notifications=[
                    Notification(
                        type="risk",
                        field="forced_labor_xinjiang_origin_subtier",
                        values=["false"],
                        date="2024-02-06T00:00:00.000Z",
                    )
                ],
                custom_fields={"properties": {"custom_name": "Victoria Beckham"}},
            ),
            ProjectNotificationData(
                id="wxwqZshCF4trlrmOa2eu9w",
                entity_id="wxwqZshCF4trlrmOa2eu9w",
                resource_id="03ePyj",
                notifications=[
                    Notification(
                        type="risk",
                        field="forced_labor_sheffield_hallam_university_reports_origin_subtier",
                        values=["3"],
                        date="2024-02-15T00:00:00.000Z",
                    )
                ],
            ),
            ProjectNotificationData(
                id="dX9cfM3FPefIp8VAuBKgIQ",
                entity_id="dX9cfM3FPefIp8VAuBKgIQ",
                resource_id="0XEQaX",
                notifications=[
                    Notification(
                        type="risk",
                        field="owner_of_regulatory_action_entity",
                        values=["1"],
                        date="2024-02-06T00:00:00.000Z",
                    ),
                    Notification(
                        type="risk",
                        field="forced_labor_sheffield_hallam_university_reports_origin_direct",
                        values=["1"],
                        date="2024-02-15T00:00:00.000Z",
                    ),
                    Notification(
                        type="risk",
                        field="forced_labor_sheffield_hallam_university_reports_origin_subtier",
                        values=["false"],
                        date="2024-02-15T00:00:00.000Z",
                    ),
                ],
                custom_fields={"properties": {"custom_identifier": "abc123"}},
            ),
        ],
    )
    """

    offset: int
    limit: int
    next: bool
    data: typing.List[ProjectNotificationData]
    size: QualifiedCount

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
