# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Tag(str, enum.Enum):
    PEP = "pep"
    STATE_OWNED = "state_owned"
    FORMER_SOE = "former_soe"
    SANCTIONED = "sanctioned"
    FORMERLY_SANCTIONED = "formerly_sanctioned"
    REPUTATIONAL_RISK_TERRORISM = "reputational_risk_terrorism"
    REPUTATIONAL_RISK_ORGANIZED_CRIME = "reputational_risk_organized_crime"
    REPUTATIONAL_RISK_FINANCIAL_CRIME = "reputational_risk_financial_crime"
    REPUTATIONAL_RISK_BRIBERY_AND_CORRUPTION = "reputational_risk_bribery_and_corruption"
    REPUTATIONAL_RISK_OTHER = "reputational_risk_other"
    REPUTATIONAL_RISK_CYBERCRIME = "reputational_risk_cybercrime"
    REPUTATIONAL_RISK_MODERN_SLAVERY = "reputational_risk_modern_slavery"
    REGULATORY_ACTION = "regulatory_action"
    LAW_ENFORCEMENT_ACTION = "law_enforcement_action"
    EXPORT_CONTROLS = "export_controls"
    FORCED_LABOR_XINJIANG_CONTRACTORS = "forced_labor_xinjiang_contractors"
    WRO_ENTITY = "wro_entity"
    UFLPA_ENTITY = "uflpa_entity"
    SHEFFIELD_HALLAM_UNIVERSITY_FORCED_LABOR_ENTITY = "sheffield_hallam_university_forced_labor_entity"

    def visit(
        self,
        pep: typing.Callable[[], T_Result],
        state_owned: typing.Callable[[], T_Result],
        former_soe: typing.Callable[[], T_Result],
        sanctioned: typing.Callable[[], T_Result],
        formerly_sanctioned: typing.Callable[[], T_Result],
        reputational_risk_terrorism: typing.Callable[[], T_Result],
        reputational_risk_organized_crime: typing.Callable[[], T_Result],
        reputational_risk_financial_crime: typing.Callable[[], T_Result],
        reputational_risk_bribery_and_corruption: typing.Callable[[], T_Result],
        reputational_risk_other: typing.Callable[[], T_Result],
        reputational_risk_cybercrime: typing.Callable[[], T_Result],
        reputational_risk_modern_slavery: typing.Callable[[], T_Result],
        regulatory_action: typing.Callable[[], T_Result],
        law_enforcement_action: typing.Callable[[], T_Result],
        export_controls: typing.Callable[[], T_Result],
        forced_labor_xinjiang_contractors: typing.Callable[[], T_Result],
        wro_entity: typing.Callable[[], T_Result],
        uflpa_entity: typing.Callable[[], T_Result],
        sheffield_hallam_university_forced_labor_entity: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Tag.PEP:
            return pep()
        if self is Tag.STATE_OWNED:
            return state_owned()
        if self is Tag.FORMER_SOE:
            return former_soe()
        if self is Tag.SANCTIONED:
            return sanctioned()
        if self is Tag.FORMERLY_SANCTIONED:
            return formerly_sanctioned()
        if self is Tag.REPUTATIONAL_RISK_TERRORISM:
            return reputational_risk_terrorism()
        if self is Tag.REPUTATIONAL_RISK_ORGANIZED_CRIME:
            return reputational_risk_organized_crime()
        if self is Tag.REPUTATIONAL_RISK_FINANCIAL_CRIME:
            return reputational_risk_financial_crime()
        if self is Tag.REPUTATIONAL_RISK_BRIBERY_AND_CORRUPTION:
            return reputational_risk_bribery_and_corruption()
        if self is Tag.REPUTATIONAL_RISK_OTHER:
            return reputational_risk_other()
        if self is Tag.REPUTATIONAL_RISK_CYBERCRIME:
            return reputational_risk_cybercrime()
        if self is Tag.REPUTATIONAL_RISK_MODERN_SLAVERY:
            return reputational_risk_modern_slavery()
        if self is Tag.REGULATORY_ACTION:
            return regulatory_action()
        if self is Tag.LAW_ENFORCEMENT_ACTION:
            return law_enforcement_action()
        if self is Tag.EXPORT_CONTROLS:
            return export_controls()
        if self is Tag.FORCED_LABOR_XINJIANG_CONTRACTORS:
            return forced_labor_xinjiang_contractors()
        if self is Tag.WRO_ENTITY:
            return wro_entity()
        if self is Tag.UFLPA_ENTITY:
            return uflpa_entity()
        if self is Tag.SHEFFIELD_HALLAM_UNIVERSITY_FORCED_LABOR_ENTITY:
            return sheffield_hallam_university_forced_labor_entity()