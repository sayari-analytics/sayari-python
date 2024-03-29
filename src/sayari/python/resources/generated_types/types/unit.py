# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Unit(str, enum.Enum):
    """
    These enums describe the unit of measurement (i.e., using SI base units) for some dimension of an entity.
    """

    METRE = "metre"
    """
    Indicates meters (m)
    """

    KILOGRAM = "kilogram"
    """
    Indicates kilograms (kg)
    """

    UNIT = "unit"
    """
    Used to show the number of units of a product
    """

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
