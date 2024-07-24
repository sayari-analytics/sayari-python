# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .notification import Notification
from .project_notification_risk_data import ProjectNotificationRiskData


class ProjectNotificationData(pydantic_v1.BaseModel):
    id: str = pydantic_v1.Field()
    """
    The ID of the entity
    """

    resource_id: str = pydantic_v1.Field()
    """
    The ID of the saved resource
    """

    entity_id: str = pydantic_v1.Field()
    """
    The ID of the entity
    """

    notifications: typing.List[Notification]
    custom_fields: typing.Optional[typing.Any] = pydantic_v1.Field(default=None)
    """
    <Warning>This property is in beta and is subject to change. It is provided for early access and testing purposes only.</Warning> custom user key/value pairs (key must be prefixed with "custom\_" and value must be "string" type)
    """

    risk_notifications: ProjectNotificationRiskData = pydantic_v1.Field()
    """
    Aggregated risk notifications
    """

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
