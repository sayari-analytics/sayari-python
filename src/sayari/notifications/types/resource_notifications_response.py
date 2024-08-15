# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .resource_notification_data import ResourceNotificationData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ResourceNotificationsResponse(UniversalBaseModel):
    """
    OK

    Examples
    --------
    from sayari.notifications import (
        ResourceNotificationData,
        ResourceNotificationsResponse,
    )

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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
