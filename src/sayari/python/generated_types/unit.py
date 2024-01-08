# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Unit(str, enum.Enum):
    """
    Unit of measurement (i.e. SI base units)
    """

    METRE = "metre"
    KILOGRAM = "kilogram"
    UNIT = "unit"

    def visit(
        self,
        metre: typing.Callable[[], T_Result],
        kilogram: typing.Callable[[], T_Result],
        unit: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Unit.METRE:
            return metre()
        if self is Unit.KILOGRAM:
            return kilogram()
        if self is Unit.UNIT:
            return unit()