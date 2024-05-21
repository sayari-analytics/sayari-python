# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .resource_notification_data import ResourceNotificationData


class ResourceNotificationsResponse(pydantic_v1.BaseModel):
    """
    OK

    Examples
    --------
    from sayari import ResourceNotificationData, ResourceNotificationsResponse

    ResourceNotificationsResponse(
        offset=0,
        limit=20,
        next=False,
        data=[
            ResourceNotificationData(
                saved_resource_id="03ePyj",
                project_id="0oZnoG",
                entity_id="wxwqZshCF4trlrmOa2eu9w",
                type="risk",
                field="forced_labor_sheffield_hallam_university_reports_origin_subtier",
                value="3",
                date="2024-02-15T00:00:00.000Z",
            )
        ],
    )
    """

    offset: int
    limit: int
    next: bool
    data: typing.List[ResourceNotificationData]

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
