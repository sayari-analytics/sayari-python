# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .project_notification_data import ProjectNotificationData
from ...base_types.types.qualified_count import QualifiedCount
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ProjectNotificationsResponse(UniversalBaseModel):
    """
    OK

    Examples
    --------
    from sayari.base_types import QualifiedCount
    from sayari.notifications import (
        Notification,
        ProjectNotificationData,
        ProjectNotificationRiskData,
        ProjectNotificationsResponse,
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
                risk_notifications=ProjectNotificationRiskData(
                    added=["forced_labor_xinjiang_origin_subtier"],
                    removed=[],
                    date="2024-02-06T00:00:00.000Z",
                ),
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
                risk_notifications=ProjectNotificationRiskData(
                    added=[],
                    removed=[
                        "forced_labor_sheffield_hallam_university_reports_origin_subtier"
                    ],
                    date="2024-02-15T00:00:00.000Z",
                ),
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
                risk_notifications=ProjectNotificationRiskData(
                    added=[
                        "forced_labor_sheffield_hallam_university_reports_origin_subtier"
                    ],
                    removed=[
                        "owner_of_regulatory_action_entity",
                        "forced_labor_sheffield_hallam_university_reports_origin_direct",
                    ],
                    date="2024-02-15T00:00:00.000Z",
                ),
            ),
        ],
    )
    """

    offset: int
    limit: int
    next: bool
    data: typing.List[ProjectNotificationData]
    size: QualifiedCount

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
