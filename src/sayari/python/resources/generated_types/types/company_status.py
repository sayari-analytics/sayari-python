# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class CompanyStatus(str, enum.Enum):
    """
    Company status enums describe a normalized set of statuses to which we map specific terms describing a company's status in a source document.
    """

    SEIZED = "seized"
    IN_RECEIVERSHIP = "in_receivership"
    REGISTRATION_REVOKED = "registration_revoked"
    OPENING = "opening"
    DISSOLVED = "dissolved"
    ACTIVE = "active"
    """
    e.g., "Active", "Operating," "In good standing"
    """

    INACTIVE = "inactive"
    """
    e.g., "Inactive", "Administratively dissolved". Used when the company still exists but is not operating normally.
    """

    CLOSED = "closed"
    """
    e.g., "Closed", "Struck from the register", "Registration canceled". Used when the company no longer legally exists.
    """

    CLOSING = "closing"
    """
    e.g., "In liquidation", "Dissolved". Used when the company is on track to close.
    """

    REGISTERED = "registered"
    """
    e.g., "Registration date"
    """

    INCORPORATED = "incorporated"
    """
    e.g., "Date of incorporation"
    """

    UNDER_EXTERNAL_CONTROL = "under_external_control"
    """
    e.g., "In receivership", "Bankruptcy trustee appointed", "Seized". Used when an exernal party is granted legal/operational control over the company, typically to steer it through a bankruptcy or winding-up process.
    """

    EXPIRED = "expired"
    """
    e.g., "Expired", "Inactive". Used when the business license is no longer active and up to date.
    """

    EXPANDED = "expanded"
    """
    e.g., "Expanded", "Barred". Used when a broker has been involved in one or more disclosure events involving certain final criminal matters, regulatory actions, civil judgment proceedings, or arbitrations or civil litigations.
    """

    TERMINATED = "terminated"
    """
    e.g., "Terminated", "Closed". Used when the licensing organization terminates a business license, barring the individual and/or company from performing business activities with the association of the organization.
    """

    def visit(
        self,
        seized: typing.Callable[[], T_Result],
        in_receivership: typing.Callable[[], T_Result],
        registration_revoked: typing.Callable[[], T_Result],
        opening: typing.Callable[[], T_Result],
        dissolved: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
        closing: typing.Callable[[], T_Result],
        registered: typing.Callable[[], T_Result],
        incorporated: typing.Callable[[], T_Result],
        under_external_control: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        expanded: typing.Callable[[], T_Result],
        terminated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompanyStatus.SEIZED:
            return seized()
        if self is CompanyStatus.IN_RECEIVERSHIP:
            return in_receivership()
        if self is CompanyStatus.REGISTRATION_REVOKED:
            return registration_revoked()
        if self is CompanyStatus.OPENING:
            return opening()
        if self is CompanyStatus.DISSOLVED:
            return dissolved()
        if self is CompanyStatus.ACTIVE:
            return active()
        if self is CompanyStatus.INACTIVE:
            return inactive()
        if self is CompanyStatus.CLOSED:
            return closed()
        if self is CompanyStatus.CLOSING:
            return closing()
        if self is CompanyStatus.REGISTERED:
            return registered()
        if self is CompanyStatus.INCORPORATED:
            return incorporated()
        if self is CompanyStatus.UNDER_EXTERNAL_CONTROL:
            return under_external_control()
        if self is CompanyStatus.EXPIRED:
            return expired()
        if self is CompanyStatus.EXPANDED:
            return expanded()
        if self is CompanyStatus.TERMINATED:
            return terminated()
