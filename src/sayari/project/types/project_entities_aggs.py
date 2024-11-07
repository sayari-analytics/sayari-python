# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .bucket_agg import BucketAgg
from .tier_count_agg import TierCountAgg
from .hs_code_agg import HsCodeAgg
from .int_key_value import IntKeyValue
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ProjectEntitiesAggs(UniversalBaseModel):
    """
    Aggregation buckets for entities in a project.
    """

    hit_count: typing.Optional[typing.List[BucketAgg]] = None
    country: typing.Optional[typing.List[BucketAgg]] = None
    upstream_country: typing.Optional[typing.List[BucketAgg]] = None
    upstream_country_tiers: typing.Optional[TierCountAgg] = None
    risk: typing.Optional[typing.List[BucketAgg]] = None
    upstream_risk: typing.Optional[typing.List[BucketAgg]] = None
    upstream_risk_tiers: typing.Optional[TierCountAgg] = None
    source: typing.Optional[typing.List[BucketAgg]] = None
    business_purpose: typing.Optional[typing.List[BucketAgg]] = None
    tag_ids: typing.Optional[typing.List[BucketAgg]] = None
    case_statuses: typing.Optional[typing.List[BucketAgg]] = None
    shipment_counts: typing.Optional[typing.List[BucketAgg]] = None
    shipped_hs_codes: typing.Optional[HsCodeAgg] = None
    received_hs_codes: typing.Optional[HsCodeAgg] = None
    combined_hs_codes: typing.Optional[HsCodeAgg] = None
    match_results: typing.Optional[typing.List[BucketAgg]] = None
    custom_fields: typing.Optional[typing.List[BucketAgg]] = None
    custom_fields_count: typing.Optional[IntKeyValue] = None
    location: typing.Optional[typing.List[BucketAgg]] = None
    source_type: typing.Optional[typing.List[BucketAgg]] = None
    region: typing.Optional[typing.List[BucketAgg]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
