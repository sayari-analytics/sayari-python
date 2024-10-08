# This file was auto-generated by Fern from our API Definition.

from .embedded_entity import EmbeddedEntity
from .entity_risk import EntityRisk
import typing
from .entity_registration_date import EntityRegistrationDate
from .company_type import CompanyType
from .status import Status
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PsaEntity(EmbeddedEntity):
    """
    The entity that is possibly the same as the target entity.
    """

    risk: EntityRisk
    registration_date: typing.Optional[EntityRegistrationDate] = None
    company_type: typing.Optional[CompanyType] = None
    latest_status: typing.Optional[Status] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
