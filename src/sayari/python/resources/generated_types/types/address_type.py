# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AddressType(str, enum.Enum):
    """
    indicates what location an address is referring to
    """

    ARRIVAL = "arrival"
    """
    the port to which a shipment is sent
    """

    DEPARTURE = "departure"
    """
    the port from which a shipment leaves
    """

    MAILING = "mailing"
    """
    an address at which an entity receives mail
    """

    PHYSICAL = "physical"
    """
    an address at which an entity has a physical presence
    """

    REGISTERED = "registered"
    """
    an address an entity has listed for its registration
    """

    BUSINESS = "business"
    """
    an address at which an entity conducts its operations
    """

    def visit(
        self,
        arrival: typing.Callable[[], T_Result],
        departure: typing.Callable[[], T_Result],
        mailing: typing.Callable[[], T_Result],
        physical: typing.Callable[[], T_Result],
        registered: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddressType.ARRIVAL:
            return arrival()
        if self is AddressType.DEPARTURE:
            return departure()
        if self is AddressType.MAILING:
            return mailing()
        if self is AddressType.PHYSICAL:
            return physical()
        if self is AddressType.REGISTERED:
            return registered()
        if self is AddressType.BUSINESS:
            return business()
