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
    from sayari.generated_types import BusinessPurposeProperties
    from sayari.trade import (
        DataSource,
        HsCodeInfo,
        MonetaryValue,
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
            count=13,
            qualifier="eq",
        ),
        next=True,
        data=[
            Shipment(
                id="Sdl3aYnJ23Y-3IxgIOkXPA",
                type="shipment",
                buyer=[
                    SourceOrDestinationEntity(
                        id="uWNWgzX-Kvp1j-WeXKmLQw",
                        type="receiver_of",
                        names=[
                            'ООО "ЭРБЭ ЭЛЕКТРОМЕДИЦИН"',
                            'LLC "ERBE ELECTROMEDICAL"',
                            "LIMITED LIABILITY COMPANY ERBE ELECTROMEDITSIN",
                            'GESELLSCHAFT MIT BESCHRANKTER HAFTUNG "ERBE ELEKTROMEDIZIN"',
                        ],
                        risks={
                            "imports_bis_high_priority_items": 1,
                            "imports_bis_high_priority_items_critical_components": 1,
                        },
                        countries=["RUS"],
                        business_purpose=[
                            BusinessPurposeProperties(
                                value="Торговля розничная лекарственными средствами в специализированных магазинах (аптеках)",
                                code="47.73",
                            ),
                            BusinessPurposeProperties(
                                value="Торговля розничная изделиями, применяемыми в медицинских целях, ортопедическими изделиями в специализированных магазинах",
                                code="47.74",
                            ),
                            BusinessPurposeProperties(
                                value="Торговля розничная косметическими и товарами личной гигиены в специализированных магазинах",
                                code="47.75",
                            ),
                            BusinessPurposeProperties(
                                value="Торговля оптовая фармацевтической продукцией",
                                code="46.46",
                            ),
                            BusinessPurposeProperties(
                                code="4646",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                code="4775",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Retail sale of second-hand goods",
                                code="4774",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Other retail sale of new goods in specialized stores",
                                code="4773",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Repair of electronic and optical equipment",
                                code="3313",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Ремонт электронного и оптического оборудования",
                                code="33.13",
                            ),
                        ],
                        address=[
                            {
                                "x": 37.57419598175875,
                                "city": "Г.москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, , MOSCOW, KHAMOVNICHESKY VAL STREET, 12, FLOOR 2, ROOM. X, ROOM 15,",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Г.москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, , Г.МОСКВА, УЛ.ХАМОВНИЧЕСКИЙ ВАЛ,Д.12,ЭТ.2,ПОМ.Х,КОМ.15,",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Г.москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, , MOSCOW, KHAMOVNICHESKY VAL STREET, 12, FL12, ROOM.H, ROOM 15,",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Г.москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, , Г.МОСКВА, УЛ.ХАМОВНИЧЕСКИЙ ВАЛ,Д.12,ЭТ12,ПОМ.Х,КОМ.15,",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Город Москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, ГОРОД МОСКВА, УЛ. ХАМОВНИЧЕСКИЙ ВАЛ, Д. 12, ЭТАЖ 2 ПОМ Х КОМ 15",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Город Москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, MOSCOW, KHAMOVNICHESKY VAL STREET, BUILDING 12, FLOOR 2 ROM X ROOM 15",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Город Москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, CITY MOSCOW, ST. KHAMOVNICHESKY VAL, 12, FLOOR 2 ROM X ROOM 15",
                            },
                            {
                                "x": 37.57419598175875,
                                "city": "Город Москва",
                                "y": 55.71777599664301,
                                "country": "RUS",
                                "value": "119270, ГОРОД МОСКВА, УЛИЦА ХАМОВНИЧЕСКИЙ ВАЛ, ДОМ 12, ЭТАЖ 2 ПОМ Х КОМ 15",
                            },
                        ],
                    )
                ],
                supplier=[
                    SourceOrDestinationEntity(
                        id="yNwunHdFInERKig0Thusgg",
                        type="shipper_of",
                        names=["ERBE ELEKTROMEDIZIN GMBH", "ERBE ELEKTROMED"],
                        risks={
                            "exports_bis_high_priority_items_critical_components": 1,
                            "exports_bis_high_priority_items": 1,
                        },
                        countries=[
                            "DEU",
                            "USA",
                            "MEX",
                            "BRA",
                            "BEL",
                            "ECU",
                            "ITA",
                            "SGP",
                            "CAN",
                            "SWE",
                            "ZAF",
                        ],
                        business_purpose=[
                            BusinessPurposeProperties(
                                value="Activities of holding companies",
                                code="6420",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Activities of head offices",
                                code="7010",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Holdings de instituições não-financeiras",
                                code="64.62-0",
                                standard="CNAE2",
                            ),
                            BusinessPurposeProperties(
                                value="Manufacture of irradiation, electromedical and electrotherapeutic equipment",
                                code="2660",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Manufacture of irradiation, electromedical and electrotherapeutic equipment",
                                code="26.60",
                                standard="NACE2",
                            ),
                            BusinessPurposeProperties(
                                value="Manufacture of medical and dental instruments and supplies",
                                code="3250",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Manufacture of medical and dental instruments and supplies",
                                code="32.50",
                                standard="NACE2",
                            ),
                            BusinessPurposeProperties(
                                value="Repair of electronic and optical equipment",
                                code="3313",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Repair of electronic and optical equipment",
                                code="33.13",
                                standard="NACE2",
                            ),
                            BusinessPurposeProperties(
                                value="Wholesale of other household goods",
                                code="4649",
                                standard="ISIC4",
                            ),
                            BusinessPurposeProperties(
                                value="Wholesale of pharmaceutical goods",
                                code="46.46",
                                standard="NACE2",
                            ),
                        ],
                        address=[
                            {
                                "x": 9.057763185844635,
                                "city": "Tübingen",
                                "state": "bw",
                                "y": 48.49839220684879,
                                "country": "DEU",
                                "value": "WALDHOERNLESTRASSE 17 72072 TUEBINGEN 0 GERMANY",
                            },
                            {
                                "x": 9.057763185844635,
                                "city": "Tuebingen",
                                "y": 48.49839220684879,
                                "country": "DEU",
                                "value": "72072, , TUEBINGEN, WALDHOERNLESTRASSE 17,",
                            },
                            {"value": "WALDHÖRNLESTRAßE 17"},
                            {
                                "x": 9.056857700153852,
                                "city": "Tuebingen",
                                "y": 48.49829144306095,
                                "country": "DEU",
                                "value": "WALDHOERNLESTRASSE TUEBINGEN 72072",
                            },
                            {
                                "x": 9.052098,
                                "city": "Tubingen",
                                "y": 48.522904,
                                "country": "Alemania",
                                "value": "TUBINGEN, ALEMANIA",
                            },
                            {"value": 'ООО "ЭРБЭ ЭЛЕКТРОМЕДИЦИН"'},
                            {
                                "x": 9.060085569236273,
                                "city": "Tubingen",
                                "y": 48.493932657539084,
                                "country": "DEU",
                                "value": "WALDHORNSTRASSE. 17 72072 TBINGEN D ,TUBINGEN ,INFO@ERBE-MED.COM",
                            },
                            {
                                "x": 9.052220000000034,
                                "city": "Tubinga",
                                "y": 48.52266000000003,
                                "country": "Alemania",
                                "value": "TUBINGA, ALEMANIA",
                            },
                            {
                                "value": "WALDHOERNLESTRASSE 17 72072 TUEBING ,TUBINGA ,INFO@ERBE-MED.COM"
                            },
                            {
                                "x": -64.65251108919011,
                                "y": -4.155371602541514,
                                "country": "BRA",
                                "value": "JAPON E5-107 Y AV. AMAZONAS",
                            },
                            {
                                "x": 9.052098,
                                "city": "TUBINGEN",
                                "y": 48.522904,
                                "country": "DEU",
                                "value": "1420-DE-72004 TUBINGEN",
                            },
                            {
                                "x": -78.48600274748468,
                                "city": "Quito",
                                "y": -0.17858591191971498,
                                "country": "Ecuador",
                                "value": "JAPON ES 107 AV. AMAZONAS 170506 QUITO ECUADOR",
                            },
                            {
                                "x": 9.057763185844635,
                                "y": 48.49839220684879,
                                "country": "DEU",
                                "value": "WALDHÖRNLESTRASSE  NUM. EXT. 17",
                            },
                            {
                                "x": 8.9971125,
                                "city": "TUBINGEN",
                                "y": 48.4834617,
                                "country": "Deutschland",
                                "value": "72072 TBINGEN, DEUTSCHLAND",
                            },
                            {
                                "x": 80.0602634,
                                "city": "OKÄND",
                                "y": 6.2482506,
                                "country": "LKA",
                                "value": "OKÄND",
                            },
                            {
                                "x": 80.0602634,
                                "city": "OKÄND",
                                "y": 6.2482506,
                                "country": "LKA",
                                "value": "OKÄND",
                            },
                            {
                                "x": -78.48600822430384,
                                "city": "Quito",
                                "y": -0.1786202845064082,
                                "country": "Ecuador",
                                "value": "JAPON E5-107 Y AV. AMAZONAS QUITO ECUADOR",
                            },
                            {
                                "x": -78.48600822430384,
                                "city": "Quito",
                                "y": -0.1786202845064082,
                                "country": "Ecuador",
                                "value": "JAPON E5 107 Y AV. AMAZONAS QUITO ECUADOR",
                            },
                            {
                                "x": -64.65251108919011,
                                "city": "Es-107av.",
                                "state": "Amazonas",
                                "y": -4.155371602541514,
                                "country": "BRA",
                                "value": "(EMPRESA GRUPOCOR) JAPON ES-107AV. AMAZONAS",
                            },
                            {
                                "x": -66.08332999999993,
                                "y": -3.533329999999978,
                                "country": "BRA",
                                "value": "JAPON ES 107 AV. AMAZONAS",
                            },
                            {
                                "x": -64.65251108919011,
                                "y": -4.155371602541514,
                                "country": "BRA",
                                "value": "JAPON E5 107 Y AV AMAZONAS",
                            },
                        ],
                    )
                ],
                arrival_address=ShipmentAddress(
                    country="RUS - BRB",
                ),
                arrival_date=["2022-05-25"],
                arrival_country=[],
                departure_date=["2022-05"],
                departure_country=["USA"],
                departure_address=ShipmentAddress(
                    country="DEU",
                ),
                product_origin=["DEU"],
                transit_country=[],
                countries=["DEU", "RUS"],
                monetary_value=[
                    MonetaryValue(
                        value=2570.52,
                        currency="USD",
                        context="cost_insurance_and_freight",
                    )
                ],
                weight=[
                    Weight(
                        value=5.5,
                        unit="kilogram",
                        type="net_weight",
                    )
                ],
                identifier=[
                    ShipmentIdentifier(
                        value="10013160/140524/3162513",
                        type="rus_declaration_number",
                    ),
                    ShipmentIdentifier(
                        value="1001325059",
                        type="ru_trade_internal_shipment_id",
                    ),
                ],
                sources=[
                    DataSource(
                        id="66dfefb726ae00fde8f09f34c5578d35",
                        label="Russia Imports & Exports (January 2023 - Present)",
                    )
                ],
                hs_codes=[
                    HsCodeInfo(
                        code="854231",
                        description="Electronic integrated circuits; processors and controllers, whether or not combined with memories, converters, logic circuits, amplifiers, clock and timing circuits, or other circuits",
                        imputed=False,
                    )
                ],
                product_descriptions=[
                    "СХЕМЫ ИНТЕГРАЛЬНЫЕ МОНОЛИТНЫЕ, ЦИФРОВЫЕ, НЕ ЛОМ ЭЛЕКТРООБОРУДОВАНИЯ, НЕ СОДЕРЖАТ КРИПТОГРАФИЧЕСКИХ МОДУЛЕЙ И ПРИЕМОПЕРЕДАТОЧНЫХ УСТР-В, НЕ ДЛЯ ШИФРОВАНИЯ, ГРАЖДАНСКОГО НАЗНАЧЕНИЯ, ДЛЯ ИСПОЛЬЗОВАНИЯ В СОСТАВЕ МЕДИЦИНСКОГО ОБОРУДОВАНИЯ:"
                ],
                record="4337bf42a200a30b90d536c5992167e1/1001325059/1721001600000/0",
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
