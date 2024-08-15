# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
from .attribute_response_data import AttributeResponseData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class AttributeResponse(UniversalBaseModel):
    """
    OK

    Examples
    --------
    from sayari.attributes import (
        AttributeProperties,
        AttributeResponse,
        AttributeResponseData,
    )

    AttributeResponse(
        data=AttributeResponseData(
            value={
                "street1": "1600 Pennsylvania Avenue NW",
                "city": "Washington DC",
                "state": "Washington DC",
                "postalCode": "20500",
                "country": "US",
            },
            properties=[
                AttributeProperties(
                    editable=True,
                    record_count=0,
                    id="enEwNGF4WDJkTG45dEU2VzZROFFoZ3xhZGRyZXNzfDBwbEVCMHxVNzhzN21yOUVFTThIZ3pwREM3UDFB",
                )
            ],
        ),
    )
    """

    data: AttributeResponseData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
