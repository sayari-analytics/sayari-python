# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .resolution_response_fields import ResolutionResponseFields
from .resolution_result import ResolutionResult


class ResolutionResponse(pydantic_v1.BaseModel):
    """
    Examples
    --------
    from sayari import (
        MatchExplanation,
        MatchStrength,
        ResolutionResponse,
        ResolutionResponseFields,
        ResolutionResult,
    )

    ResolutionResponse(
        fields=ResolutionResponseFields(
            name=["victoria beckham limited"],
        ),
        data=[
            ResolutionResult(
                profile="corporate",
                score=491.08936,
                entity_id="ds5rQ3rMIeoN3xZUzVyVNQ",
                label="VICTORIA BECKHAM",
                type="person",
                identifiers=[],
                addresses=[
                    "C/O LEE & THOMPSON LLP, 4 GEE'S COURT, ST-CHRISTOPHER'S PLACE"
                ],
                countries=["GBR", "MEX"],
                sources=["b9d809b02049993ba8dc2e4c5f7cceca"],
                typed_matched_queries=[
                    "name|0",
                    "name|100phrase|0",
                    "name|100match|0",
                    "looseName|0",
                ],
                matched_queries=["name"],
                highlight={"name": ["<em>VICTORIA</em> <em>BECKHAM</em>"]},
                explanation={
                    "name": [
                        MatchExplanation(
                            matched="<em>VICTORIA</em> <em>BECKHAM</em>",
                            uploaded="victoria beckham limited",
                            name_custom_tf_idf_score=0.5416772821044128,
                            high_quality_match_name=True,
                            is_deletion_recommended=False,
                            n_common_term_matches=1,
                            n_uncommon_term_matches=1,
                        )
                    ]
                },
                match_strength=MatchStrength(
                    value="weak",
                ),
            )
        ],
    )
    """

    fields: ResolutionResponseFields
    data: typing.List[ResolutionResult]

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
