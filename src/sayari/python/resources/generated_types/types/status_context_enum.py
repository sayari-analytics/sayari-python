# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StatusContextEnum(str, enum.Enum):
    BROKER_LICENSE = "broker_license"
    INVESTMENT_ADVISOR_LICENSE = "investment_advisor_license"
    SOLE_PROPRIETORSHIP_STATUS = "sole_proprietorship_status"
    GENERAL_PARTNERSHIP_STATUS = "general_partnership_status"
    LIMITED_LIABILITY_PARTNERSHIP_STATUS = "limited_liability_partnership_status"

    def visit(
        self,
        broker_license: typing.Callable[[], T_Result],
        investment_advisor_license: typing.Callable[[], T_Result],
        sole_proprietorship_status: typing.Callable[[], T_Result],
        general_partnership_status: typing.Callable[[], T_Result],
        limited_liability_partnership_status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusContextEnum.BROKER_LICENSE:
            return broker_license()
        if self is StatusContextEnum.INVESTMENT_ADVISOR_LICENSE:
            return investment_advisor_license()
        if self is StatusContextEnum.SOLE_PROPRIETORSHIP_STATUS:
            return sole_proprietorship_status()
        if self is StatusContextEnum.GENERAL_PARTNERSHIP_STATUS:
            return general_partnership_status()
        if self is StatusContextEnum.LIMITED_LIABILITY_PARTNERSHIP_STATUS:
            return limited_liability_partnership_status()
