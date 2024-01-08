# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MonetaryValueContext(str, enum.Enum):
    """
    Monetary value context enums describe the types of financial values an asset can have
    """

    COST_INSURANCE_AND_FREIGHT = "cost_insurance_and_freight"
    FREE_ON_BOARD = "free_on_board"

    def visit(
        self, cost_insurance_and_freight: typing.Callable[[], T_Result], free_on_board: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is MonetaryValueContext.COST_INSURANCE_AND_FREIGHT:
            return cost_insurance_and_freight()
        if self is MonetaryValueContext.FREE_ON_BOARD:
            return free_on_board()