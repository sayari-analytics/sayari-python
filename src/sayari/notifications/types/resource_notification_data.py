# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from ...generated_types.types.risk import Risk
from ...shared_types.types.risk_value import RiskValue
from .notification_type import NotificationType


class ResourceNotificationData(pydantic_v1.BaseModel):
    saved_resource_id: str = pydantic_v1.Field(alias="savedResourceId")
    """
    The ID of the saved resource
    """

    project_id: str = pydantic_v1.Field(alias="projectId")
    """
    The ID of the project the entity is saved to
    """

    entity_id: str = pydantic_v1.Field(alias="entityId")
    """
    The ID of the entity
    """

    type: NotificationType = pydantic_v1.Field()
    """
    The type of notification, currently limited to 'risk'
    """

    field: Risk = pydantic_v1.Field()
    """
    The field that the notification is for
    """

    value: RiskValue = pydantic_v1.Field()
    """
    The previous value of the field
    """

    date: str = pydantic_v1.Field()
    """
    The date the notification was created
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}