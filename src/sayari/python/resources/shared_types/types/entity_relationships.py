# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...base_types.types.paginated_response import PaginatedResponse


class EntityRelationships(PaginatedResponse):
    """
    All relationships the entity is a part of.
    """

    data: typing.List["RelationshipData"]

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
        json_encoders = {dt.datetime: serialize_datetime}


from .entity_details import EntityDetails  # noqa: E402
from .relationship_data import RelationshipData  # noqa: E402

EntityRelationships.update_forward_refs(RelationshipData=RelationshipData)
