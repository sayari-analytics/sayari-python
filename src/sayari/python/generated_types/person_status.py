# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PersonStatus(str, enum.Enum):
    """
    Person status enums describe different life events
    """

    BORN = "born"
    DIED = "died"
    MARRIED = "married"

    def visit(
        self,
        born: typing.Callable[[], T_Result],
        died: typing.Callable[[], T_Result],
        married: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PersonStatus.BORN:
            return born()
        if self is PersonStatus.DIED:
            return died()
        if self is PersonStatus.MARRIED:
            return married()
