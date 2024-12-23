# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .resolution_persisted_response_fields import ResolutionPersistedResponseFields
import typing
from .resolution_persisted_result import ResolutionPersistedResult
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ResolutionPersistedResponse(UniversalBaseModel):
    """
    Examples
    --------
    from sayari.resolution import (
        MatchExplanation,
        MatchStrength,
        ResolutionPersistedResponse,
        ResolutionPersistedResponseFields,
        ResolutionPersistedResult,
    )
    from sayari.shared_types import Identifier

    ResolutionPersistedResponse(
        fields=ResolutionPersistedResponseFields(
            name=["victoria beckham limited"],
            custom_name="Victoria Beckham",
        ),
        data=[
            ResolutionPersistedResult(
                saved_entity_id="xG8wYP",
                profile="corporate",
                score=167.28214,
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
                psa_id=4655744767230.0,
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
                            name_custom_tf_idf_score=0.5416772821044128,
                            high_quality_match_name=True,
                        ),
                        MatchExplanation(
                            matched="<em>BECKHAM</em> VENTURES LIMITED",
                            uploaded="victoria beckham limited",
                            name_custom_tf_idf_score=0.5,
                            high_quality_match_name=False,
                        ),
                    ]
                },
                match_strength=MatchStrength(
                    value="weak",
                ),
            )
        ],
    )
    """

    fields: ResolutionPersistedResponseFields
    data: typing.List[ResolutionPersistedResult]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow