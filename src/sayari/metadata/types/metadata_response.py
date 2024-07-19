# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .user_info import UserInfo


class MetadataResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from sayari import MetadataResponse, UserInfo

    MetadataResponse(
        version="v2.1.0-4841-g41af84af8",
        master_release="reiko_20240712182628",
        watchlist_release="watchlist_reiko_20240718024049",
        user=UserInfo(
            id="abcdefghijklmnopqrstuvwxyz@clients",
            group_display_names="",
            roles="",
        ),
    )
    """

    version: str = pydantic_v1.Field()
    """
    Currently deployed version of the application.
    """

    master_release: str = pydantic_v1.Field()
    """
    Currently deployed main data release.
    """

    watchlist_release: str = pydantic_v1.Field()
    """
    Currently deployed watchlist release.
    """

    user: UserInfo

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
