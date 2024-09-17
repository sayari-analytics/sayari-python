# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...shared_types.types.entity_details import EntityDetails
from ...shared_types.types.entity_relationships import EntityRelationships
from ...shared_types.types.relationship_data import RelationshipData
from .supplier_metadata import SupplierMetadata
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic
from ...core.pydantic_utilities import update_forward_refs


class SupplierOrBuyer(EntityDetails):
    metadata: SupplierMetadata

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(EntityDetails, SupplierOrBuyer=SupplierOrBuyer)
update_forward_refs(EntityRelationships, SupplierOrBuyer=SupplierOrBuyer)
update_forward_refs(RelationshipData, SupplierOrBuyer=SupplierOrBuyer)
