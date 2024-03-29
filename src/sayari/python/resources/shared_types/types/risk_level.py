# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RiskLevel(str, enum.Enum):
    CRITICAL = "critical"
    HIGH = "high"
    ELEVATED = "elevated"
    RELEVANT = "relevant"

    def visit(
        self,
        critical: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        elevated: typing.Callable[[], T_Result],
        relevant: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskLevel.CRITICAL:
            return critical()
        if self is RiskLevel.HIGH:
            return high()
        if self is RiskLevel.ELEVATED:
            return elevated()
        if self is RiskLevel.RELEVANT:
            return relevant()
