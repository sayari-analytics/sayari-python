# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from ...generated_types.types.risk import Risk
from ...generated_types.types.country import Country
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ProjectEntityUpstream(UniversalBaseModel):
    risk: typing.List[Risk]
    countries: typing.List[Country]
    entities: int
    match_has_upstream: typing.Dict[str, bool]
    match_products: typing.Dict[str, typing.List[str]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
