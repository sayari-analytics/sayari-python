# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .resolution_response_fields import ResolutionResponseFields
from .resolution_result import ResolutionResult


class ResolutionResponse(pydantic_v1.BaseModel):
    """
    OK
    ---
    from sayari import (
        Identifier,
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
                score=167.00832,
                entity_id="mGq1lpuqKssNWTjIokuPeA",
                label="VICTORIA BECKHAM LIMITED",
                type="company",
                identifiers=[
                    Identifier(
                        type="uk_company_number",
                        value="06517802",
                        label="Uk Company Number",
                    ),
                    Identifier(
                        type="ca_corporate_id_num",
                        value="04781466",
                        label="Ca Corporate Id Num",
                    ),
                    Identifier(
                        type="unknown",
                        value="6517802",
                        label="Unknown",
                    ),
                ],
                psa_id=695785012897.0,
                addresses=[
                    "202 HAMMERSMITH ROAD , LONDON , , UNITED KINGDOM , W6 7DN , GB",
                    "Unit 33, Ransomes Dock Business Centre, 35-37 Parkgate Road, London SW11 4NP",
                    "SAUNDERS BUILDING, 202 HAMMERSMITH ROAD, HAMMERSMITH, LONDON",
                    "Ransome's Dock, 35-37 Parkgate Road, London, SW11 4NP",
                    "Hammersmith Road, London, W6 7DN",
                    "202 HAMMERSMITH ROAD UNITED KINGDOM",
                    "202 HAMMERSMITH ROAD BRITISH ISLES",
                ],
                countries=["GBR", "USA", "VNM"],
                sources=[
                    "2b618f1996252fe537a6d998ae14c9b2",
                    "2b788dbdf9194ed5a5c309386a6516b1",
                    "a447a7b622c4ead6e1caf94983dc2337",
                    "ecdfb3f2ecc8c3797e77d5795a8066ef",
                    "e5de7b52cc88ef4cd1a10e201bdf46ee",
                    "2a4fe9a14e332c8f9ded1f8a457c2b89",
                    "ecdfb3f2ecc8c3797e77d5795a8066ef",
                    "4ea8bac1bed868e1510ffd21842e9551",
                ],
                typed_matched_queries=["name|0", "looseName|0"],
                matched_queries=["name"],
                highlight={
                    "name": [
                        "<em>VICTORIA</em> <em>BECKHAM</em> LIMITED",
                        "<em>BECKHAM</em> VENTURES LIMITED",
                    ]
                },
                explanation={
                    "name": [
                        MatchExplanation(
                            matched="<em>VICTORIA</em> <em>BECKHAM</em> LIMITED",
                            uploaded="victoria beckham limited",
                        ),
                        MatchExplanation(
                            matched="<em>BECKHAM</em> VENTURES LIMITED",
                            uploaded="victoria beckham limited",
                        ),
                    ]
                },
                match_strength=MatchStrength(
                    value="weak",
                ),
            ),
            ResolutionResult(
                profile="corporate",
                score=163.52704,
                entity_id="v7fh4Kv5aLpfk7ld8oul2w",
                label="VICTORIA BY VICTORIA BECKHAM",
                type="intellectual_property",
                identifiers=[
                    Identifier(
                        type="chn_cnipa_tm",
                        value="11314607",
                        label="Chn Cnipa Tm",
                    )
                ],
                addresses=[],
                countries=["CHN"],
                sources=["8f50655ba1d1552ab4b89d119bd9c318"],
                typed_matched_queries=["name|0", "looseName|0"],
                matched_queries=["name"],
                highlight={
                    "name": [
                        "<em>VICTORIA</em> BY <em>VICTORIA</em> <em>BECKHAM</em>"
                    ]
                },
                explanation={
                    "name": [
                        MatchExplanation(
                            matched="<em>VICTORIA</em> BY <em>VICTORIA</em> <em>BECKHAM</em>",
                            uploaded="victoria beckham limited",
                        )
                    ]
                },
                match_strength=MatchStrength(
                    value="weak",
                ),
            ),
        ],
    )
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
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
