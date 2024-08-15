# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .qualified_count import QualifiedCount
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class PaginatedResponse(UniversalBaseModel):
    """
    Response fields that represent unbounded collections, such as a search result or an entity's attributes or relationships, or a record's references, can all be paginated in cases where the collection is larger than can be efficiently returned in a single request.
    """

    limit: int
    size: QualifiedCount

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
