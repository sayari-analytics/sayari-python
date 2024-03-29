# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .save_entity_response_data import SaveEntityResponseData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class SaveEntityResponse(pydantic.BaseModel):
    """
    from sayari-analytics import (ResourceType, SaveEntityResponse,
                                  SaveEntityResponseData)

    SaveEntityResponse(data=SaveEntityResponseData(type=ResourceType.ENTITY, id="Ywk6qw", project="GNJbkG", label="HOME DEPOT, U. S. A., INC.", created="2024-03-12 16:12:38.528362+00", updated="2024-03-12 16:12:38.528362+00", updated_by="auth0|5e45bd8caccd890e68147513", version=0, entity_id="n9SA4T_33tDmLtS8BhC6Zg", tag_ids=[], case_status="not_assigned", ), )
    """

    data: SaveEntityResponseData

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
