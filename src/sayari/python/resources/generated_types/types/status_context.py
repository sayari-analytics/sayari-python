# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class StatusContext(str, enum.Enum):
    """
    Status context enums describe the different types of statuses that can be represented in a status attribute.
    """

    BROKER_LICENSE = "broker_license"
    """
    e.g., "Broker", "Intermediary". An individual who acts as an intermediary for trading, lending, and investing purposes.
    """

    INVESTMENT_ADVISOR_LICENSE = "investment_advisor_license"
    """
    e.g., "Investment Advisor". An individual who provides investment advice and/or securities analysis services for a fee.
    """

    SOLE_PROPRIETORSHIP_STATUS = "sole_proprietorship_status"
    """
    e.g., "Sole proprietor", "Sole proprietorship", "Individual entrepreneurship", "Sole trader".
    """

    GENERAL_PARTNERSHIP_STATUS = "general_partnership_status"
    """
    e.g., "Partnership". A basic form of partnership under common law. A company entity, typically unincorporated, comprised of two or more partners who agree to share in all assets, profits, and liabilities of a business.
    """

    LIMITED_LIABILITY_PARTNERSHIP_STATUS = "limited_liability_partnership_status"
    """
    e.g., "LLP", "Limited-Liability Limited Partnership". A partnership in which some or all partners have limited liabilities. Each partner's liabilities are limited to the amount they contribute to the business.
    """

    def visit(
        self,
        broker_license: typing.Callable[[], T_Result],
        investment_advisor_license: typing.Callable[[], T_Result],
        sole_proprietorship_status: typing.Callable[[], T_Result],
        general_partnership_status: typing.Callable[[], T_Result],
        limited_liability_partnership_status: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusContext.BROKER_LICENSE:
            return broker_license()
        if self is StatusContext.INVESTMENT_ADVISOR_LICENSE:
            return investment_advisor_license()
        if self is StatusContext.SOLE_PROPRIETORSHIP_STATUS:
            return sole_proprietorship_status()
        if self is StatusContext.GENERAL_PARTNERSHIP_STATUS:
            return general_partnership_status()
        if self is StatusContext.LIMITED_LIABILITY_PARTNERSHIP_STATUS:
            return limited_liability_partnership_status()
