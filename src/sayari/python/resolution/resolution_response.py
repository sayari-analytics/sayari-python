# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .resolution_response_fields import ResolutionResponseFields
from .resolution_result import ResolutionResult

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ResolutionResponse(pydantic.BaseModel):
    """
    OK
    ---
    from sayari-analytics import (Country, Entities, Identifier, MatchExplanation,
                                  ResolutionResponse, ResolutionResponseFields,
                                  ResolutionResult)

    ResolutionResponse(fields=ResolutionResponseFields(name=["victoria beckham limited"], ), data=[ResolutionResult(score=182.77252, entity_id="mGq1lpuqKssNWTjIokuPeA", label="VICTORIA BECKHAM LIMITED", type=Entities.COMPANY, identifiers=[Identifier(type="uk_company_number", value="06517802", label="Uk Company Number", ), Identifier(type="unknown", value="6517802", label="Unknown", )], psa_id=24867860645854.0, addresses=["202 HAMMERSMITH ROAD, LONDON, W6 7DN", "Hammersmith Road, London, W6 7DN", "Unit 33, Ransomes Dock Business Centre, 35-37 Parkgate Road, London SW11 4NP"], countries=[Country.GBR], sources=["2b618f1996252fe537a6d998ae14c9b2", "ecdfb3f2ecc8c3797e77d5795a8066ef", "2a4fe9a14e332c8f9ded1f8a457c2b89", "ecdfb3f2ecc8c3797e77d5795a8066ef", "4ea8bac1bed868e1510ffd21842e9551"], typed_matched_queries=["name|0", "looseName|0"], matched_queries=["name"], highlight={"name": ["<em>VICTORIA</em> <em>BECKHAM</em> <em>LIMITED</em>", "<em>VICTORIA</em> <em>BECKHAM</em> LIMITED", "<em>BECKHAM</em> VENTURES <em>LIMITED</em>", "<em>BECKHAM</em> VENTURES LIMITED"]}, explanation={"name": [MatchExplanation(matched="<em>VICTORIA</em> <em>BECKHAM</em> <em>LIMITED</em>", uploaded="victoria beckham limited", name_custom_tf_idf_score=0.5416772821044128, high_quality_match_name=True, ), MatchExplanation(matched="<em>VICTORIA</em> <em>BECKHAM</em> LIMITED", uploaded="victoria beckham limited", name_custom_tf_idf_score=0.5416772821044128, high_quality_match_name=True, ), MatchExplanation(matched="<em>BECKHAM</em> VENTURES <em>LIMITED</em>", uploaded="victoria beckham limited", name_custom_tf_idf_score=0.5, high_quality_match_name=False, ), MatchExplanation(matched="<em>BECKHAM</em> VENTURES LIMITED", uploaded="victoria beckham limited", name_custom_tf_idf_score=0.5, high_quality_match_name=False, )]}, )], )
    """

    fields: ResolutionResponseFields
    data: typing.List[ResolutionResult]

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