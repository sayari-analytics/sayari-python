# This file was auto-generated by Fern from our API Definition.

from ...base_types.types.paginated_response import PaginatedResponse
import typing
from .shipment import Shipment
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ShipmentSearchResponse(PaginatedResponse):
    """
    OK

    Examples
    --------
    from sayari.base_types import QualifiedCount
    from sayari.trade import (
        DataSource,
        Shipment,
        ShipmentAddress,
        ShipmentIdentifier,
        ShipmentSearchResponse,
        SourceOrDestinationEntity,
        Weight,
    )

    ShipmentSearchResponse(
        offset=0,
        limit=1,
        size=QualifiedCount(
            count=10000,
            qualifier="gte",
        ),
        next=True,
        data=[
            Shipment(
                id="KIB4wNCMtzLhG-onltADgQ",
                type="shipment",
                buyer=[
                    SourceOrDestinationEntity(
                        id="M_vGQfA6PWYdNkj5a_XMNQ",
                        names=["HEMINGWAY RUM COMPANY LLC"],
                        risks={"basel_aml": 4.63, "cpi_score": 67},
                        countries=["USA"],
                        business_purpose=[],
                    )
                ],
                supplier=[
                    SourceOrDestinationEntity(
                        id="9NQnfZhEFrRnp4YWk5yAVQ",
                        names=["FOURSQUARE RUM DISTILLERY FOURSQUARE"],
                        risks={
                            "eu_high_risk_third": true,
                            "basel_aml": 5.81,
                            "cpi_score": 65,
                        },
                        countries=["BRB"],
                        business_purpose=[],
                    )
                ],
                arrival_date="2022-05-25",
                departure_date="2022-05",
                departure_address=ShipmentAddress(
                    x=-79.4861,
                    city="ALAMANCE",
                    state="NC",
                    y=36.035,
                    value="27201",
                ),
                product_origin=["USA"],
                monetary_value=[],
                weight=[
                    Weight(
                        value=5388.0,
                        unit="kilogram",
                        type="gross_weight",
                    )
                ],
                identifier=[
                    ShipmentIdentifier(
                        value="TSCW15541208",
                        type="bill_of_lading",
                    )
                ],
                sources=[
                    DataSource(
                        id="16a4cc2d0f467fa993b28587d542a25d",
                        label="USA Imports (2021 - Present)",
                    )
                ],
                hs_codes=[],
                product_descriptions=["0000000006FOURSQUARE 5YR OLD RUM"],
                record="16a4cc2d0f467fa993b28587d542a25d/TSCW15541208/1653523200000/0",
            )
        ],
    )
    """

    offset: int
    next: bool
    data: typing.List[Shipment]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
