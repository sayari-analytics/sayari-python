# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RelationshipType(str, enum.Enum):
    AUDITOR_OF = "auditor_of"
    BENEFICIAL_OWNER_OF = "beneficial_owner_of"
    BRANCH_OF = "branch_of"
    DIRECTOR_OF = "director_of"
    EMPLOYEE_OF = "employee_of"
    FAMILY_OF = "family_of"
    FOUNDER_OF = "founder_of"
    ISSUER_OF = "issuer_of"
    LAWYER_IN = "lawyer_in"
    LAWYER_OF = "lawyer_of"
    LEGAL_PREDECESSOR_OF = "legal_predecessor_of"
    LEGAL_REPRESENTATIVE_OF = "legal_representative_of"
    LEGAL_SUCCESSOR_OF = "legal_successor_of"
    LINKED_TO = "linked_to"
    LIQUIDATOR_OF = "liquidator_of"
    MANAGER_OF = "manager_of"
    MEMBER_OF_THE_BOARD_OF = "member_of_the_board_of"
    OFFICER_OF = "officer_of"
    OWNER_OF = "owner_of"
    PARTNER_OF = "partner_of"
    PARTY_TO = "party_to"
    RECEIVER_OF = "receiver_of"
    REGISTERED_AGENT_OF = "registered_agent_of"
    SHAREHOLDER_OF = "shareholder_of"
    SHIPPER_OF = "shipper_of"
    SHIPS_TO = "ships_to"
    SUBSIDIARY_OF = "subsidiary_of"
    SUPERVISOR_OF = "supervisor_of"
    HAS_AUDITOR = "has_auditor"
    HAS_BENEFICIAL_OWNER = "has_beneficial_owner"
    HAS_BRANCH = "has_branch"
    HAS_DIRECTOR = "has_director"
    HAS_EMPLOYEE = "has_employee"
    HAS_FOUNDER = "has_founder"
    HAS_ISSUER = "has_issuer"
    HAS_LAWYER = "has_lawyer"
    HAS_LEGAL_PREDECESSOR = "has_legal_predecessor"
    HAS_LEGAL_REPRESENTATIVE = "has_legal_representative"
    HAS_LEGAL_SUCCESSOR = "has_legal_successor"
    HAS_LIQUIDATOR = "has_liquidator"
    HAS_MANAGER = "has_manager"
    HAS_MEMBER_OF_THE_BOARD = "has_member_of_the_board"
    HAS_OFFICER = "has_officer"
    HAS_OWNER = "has_owner"
    HAS_PARTNER = "has_partner"
    HAS_PARTY = "has_party"
    RECEIVED_BY = "received_by"
    HAS_REGISTERED_AGENT = "has_registered_agent"
    HAS_SHAREHOLDER = "has_shareholder"
    SHIPPED_BY = "shipped_by"
    RECEIVES_FROM = "receives_from"
    HAS_SUBSIDIARY = "has_subsidiary"
    HAS_SUPERVISOR = "has_supervisor"
    NOTIFY_PARTY_OF = "notify_party_of"
    HAS_NOTIFY_PARTY = "has_notify_party"

    def visit(
        self,
        auditor_of: typing.Callable[[], T_Result],
        beneficial_owner_of: typing.Callable[[], T_Result],
        branch_of: typing.Callable[[], T_Result],
        director_of: typing.Callable[[], T_Result],
        employee_of: typing.Callable[[], T_Result],
        family_of: typing.Callable[[], T_Result],
        founder_of: typing.Callable[[], T_Result],
        issuer_of: typing.Callable[[], T_Result],
        lawyer_in: typing.Callable[[], T_Result],
        lawyer_of: typing.Callable[[], T_Result],
        legal_predecessor_of: typing.Callable[[], T_Result],
        legal_representative_of: typing.Callable[[], T_Result],
        legal_successor_of: typing.Callable[[], T_Result],
        linked_to: typing.Callable[[], T_Result],
        liquidator_of: typing.Callable[[], T_Result],
        manager_of: typing.Callable[[], T_Result],
        member_of_the_board_of: typing.Callable[[], T_Result],
        officer_of: typing.Callable[[], T_Result],
        owner_of: typing.Callable[[], T_Result],
        partner_of: typing.Callable[[], T_Result],
        party_to: typing.Callable[[], T_Result],
        receiver_of: typing.Callable[[], T_Result],
        registered_agent_of: typing.Callable[[], T_Result],
        shareholder_of: typing.Callable[[], T_Result],
        shipper_of: typing.Callable[[], T_Result],
        ships_to: typing.Callable[[], T_Result],
        subsidiary_of: typing.Callable[[], T_Result],
        supervisor_of: typing.Callable[[], T_Result],
        has_auditor: typing.Callable[[], T_Result],
        has_beneficial_owner: typing.Callable[[], T_Result],
        has_branch: typing.Callable[[], T_Result],
        has_director: typing.Callable[[], T_Result],
        has_employee: typing.Callable[[], T_Result],
        has_founder: typing.Callable[[], T_Result],
        has_issuer: typing.Callable[[], T_Result],
        has_lawyer: typing.Callable[[], T_Result],
        has_legal_predecessor: typing.Callable[[], T_Result],
        has_legal_representative: typing.Callable[[], T_Result],
        has_legal_successor: typing.Callable[[], T_Result],
        has_liquidator: typing.Callable[[], T_Result],
        has_manager: typing.Callable[[], T_Result],
        has_member_of_the_board: typing.Callable[[], T_Result],
        has_officer: typing.Callable[[], T_Result],
        has_owner: typing.Callable[[], T_Result],
        has_partner: typing.Callable[[], T_Result],
        has_party: typing.Callable[[], T_Result],
        received_by: typing.Callable[[], T_Result],
        has_registered_agent: typing.Callable[[], T_Result],
        has_shareholder: typing.Callable[[], T_Result],
        shipped_by: typing.Callable[[], T_Result],
        receives_from: typing.Callable[[], T_Result],
        has_subsidiary: typing.Callable[[], T_Result],
        has_supervisor: typing.Callable[[], T_Result],
        notify_party_of: typing.Callable[[], T_Result],
        has_notify_party: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelationshipType.AUDITOR_OF:
            return auditor_of()
        if self is RelationshipType.BENEFICIAL_OWNER_OF:
            return beneficial_owner_of()
        if self is RelationshipType.BRANCH_OF:
            return branch_of()
        if self is RelationshipType.DIRECTOR_OF:
            return director_of()
        if self is RelationshipType.EMPLOYEE_OF:
            return employee_of()
        if self is RelationshipType.FAMILY_OF:
            return family_of()
        if self is RelationshipType.FOUNDER_OF:
            return founder_of()
        if self is RelationshipType.ISSUER_OF:
            return issuer_of()
        if self is RelationshipType.LAWYER_IN:
            return lawyer_in()
        if self is RelationshipType.LAWYER_OF:
            return lawyer_of()
        if self is RelationshipType.LEGAL_PREDECESSOR_OF:
            return legal_predecessor_of()
        if self is RelationshipType.LEGAL_REPRESENTATIVE_OF:
            return legal_representative_of()
        if self is RelationshipType.LEGAL_SUCCESSOR_OF:
            return legal_successor_of()
        if self is RelationshipType.LINKED_TO:
            return linked_to()
        if self is RelationshipType.LIQUIDATOR_OF:
            return liquidator_of()
        if self is RelationshipType.MANAGER_OF:
            return manager_of()
        if self is RelationshipType.MEMBER_OF_THE_BOARD_OF:
            return member_of_the_board_of()
        if self is RelationshipType.OFFICER_OF:
            return officer_of()
        if self is RelationshipType.OWNER_OF:
            return owner_of()
        if self is RelationshipType.PARTNER_OF:
            return partner_of()
        if self is RelationshipType.PARTY_TO:
            return party_to()
        if self is RelationshipType.RECEIVER_OF:
            return receiver_of()
        if self is RelationshipType.REGISTERED_AGENT_OF:
            return registered_agent_of()
        if self is RelationshipType.SHAREHOLDER_OF:
            return shareholder_of()
        if self is RelationshipType.SHIPPER_OF:
            return shipper_of()
        if self is RelationshipType.SHIPS_TO:
            return ships_to()
        if self is RelationshipType.SUBSIDIARY_OF:
            return subsidiary_of()
        if self is RelationshipType.SUPERVISOR_OF:
            return supervisor_of()
        if self is RelationshipType.HAS_AUDITOR:
            return has_auditor()
        if self is RelationshipType.HAS_BENEFICIAL_OWNER:
            return has_beneficial_owner()
        if self is RelationshipType.HAS_BRANCH:
            return has_branch()
        if self is RelationshipType.HAS_DIRECTOR:
            return has_director()
        if self is RelationshipType.HAS_EMPLOYEE:
            return has_employee()
        if self is RelationshipType.HAS_FOUNDER:
            return has_founder()
        if self is RelationshipType.HAS_ISSUER:
            return has_issuer()
        if self is RelationshipType.HAS_LAWYER:
            return has_lawyer()
        if self is RelationshipType.HAS_LEGAL_PREDECESSOR:
            return has_legal_predecessor()
        if self is RelationshipType.HAS_LEGAL_REPRESENTATIVE:
            return has_legal_representative()
        if self is RelationshipType.HAS_LEGAL_SUCCESSOR:
            return has_legal_successor()
        if self is RelationshipType.HAS_LIQUIDATOR:
            return has_liquidator()
        if self is RelationshipType.HAS_MANAGER:
            return has_manager()
        if self is RelationshipType.HAS_MEMBER_OF_THE_BOARD:
            return has_member_of_the_board()
        if self is RelationshipType.HAS_OFFICER:
            return has_officer()
        if self is RelationshipType.HAS_OWNER:
            return has_owner()
        if self is RelationshipType.HAS_PARTNER:
            return has_partner()
        if self is RelationshipType.HAS_PARTY:
            return has_party()
        if self is RelationshipType.RECEIVED_BY:
            return received_by()
        if self is RelationshipType.HAS_REGISTERED_AGENT:
            return has_registered_agent()
        if self is RelationshipType.HAS_SHAREHOLDER:
            return has_shareholder()
        if self is RelationshipType.SHIPPED_BY:
            return shipped_by()
        if self is RelationshipType.RECEIVES_FROM:
            return receives_from()
        if self is RelationshipType.HAS_SUBSIDIARY:
            return has_subsidiary()
        if self is RelationshipType.HAS_SUPERVISOR:
            return has_supervisor()
        if self is RelationshipType.NOTIFY_PARTY_OF:
            return notify_party_of()
        if self is RelationshipType.HAS_NOTIFY_PARTY:
            return has_notify_party()