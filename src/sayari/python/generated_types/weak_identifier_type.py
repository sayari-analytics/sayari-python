# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WeakIdentifierType(str, enum.Enum):
    """
    All weak (non-unique) identifiers in Sayari's database
    """

    UNKNOWN = "unknown"
    """
    A string that is thought to be an ID number, but whose type is unknown
    """

    MX_PARTIAL_RFC_PERSON = "mx_partial_rfc_person"
    RU_OKTMO = "ru_oktmo"
    RU_KPP = "ru_kpp"
    RU_OKPO = "ru_okpo"
    """
    A unique identifier that is reissued when a company dissolves
    """

    UNKNOWN_PASSPORT = "unknown_passport"
    """
    A passport number whose country of origin is not known
    """

    RKS_KTA_NUMBER = "rks_kta_number"
    """
    An identifier from the Kosovo company registry
    """

    BRA_PARTIAL_CPF = "bra_partial_cpf"
    """
    Individual taxpayer registry identification (https://en.wikipedia.org/wiki/Cadastro_de_Pessoas_F%C3%ADsicas)
    """

    VEN_COLEGIADO_NUMBER = "ven_colegiado_number"
    """
    Identification number for Venezuelan comisarios
    """

    PAN_FOLIO = "pan_folio"
    KGZ_OKPO = "kgz_okpo"
    """
    A unique identifier that is reissued when a company dissolves
    """

    KGZ_INN = "kgz_inn"
    LBN_REGISTRATION_NUMBER = "lbn_registration_number"
    ITA_EBR_REG_NUMBER = "ita_ebr_reg_number"
    """
    Number in registry per EBR
    """

    ITA_EBR_SHORT_SEARCH_CODE = "ita_ebr_short_search_code"
    """
    EBR short search code
    """

    CHL_SANTIAGO_GAZETTE_CVE = "chl_santiago_gazette_cve"
    """
    CVE number in Chile Santiago Gazette
    """

    BMU_REGISTRATION_NUMBER = "bmu_registration_number"
    """
    Bermuda registration number
    """

    BRAZILIAN_OAB = "brazilian_oab"
    """
    Brazilian Lawyer Identification number
    """

    IRN_REG_NUMBER = "irn_reg_number"
    """
    Iranian registration number
    """

    MX_FME = "mx_fme"
    """
    Mexican FME
    """

    UKR_EDRPOU = "ukr_edrpou"
    """
    See https://www.wikidata.org/wiki/Property:P3125
    """

    RU_LICENSE_NUMBER = "ru_license_number"
    """
    Label for various license numbers extracted from EGRUL documents
    """

    MARITIME_CALL_SIGN = "maritime_call_sign"
    """
    Unique call sign for vessels
    """

    PRK_SHIP_REG_NO = "prk_ship_reg_no"
    """
    Registration numbers for North Korean ships
    """

    COFI_CODE = "cofi_code"
    """
    National identification number for enterprises and associations (Senegal)
    """

    RU_NZA = "ru_nza"
    """
    Foreign entity accreditation number
    """

    ARG_IGJ_NUMBER = "arg_igj_number"
    """
    Unique company id from Inspección General de Justicia in Argentina
    """

    UNKNOWN_BRA_CASE_NUMBER = "unknown_bra_case_number"
    """
    Brazilian Lawyer Identification number
    """

    IRQ_PROVISION_CARD = "irq_provision_card"
    MBL_HM_SN = "mbl_hm_sn"
    """
    Mobile Home Serial Number
    """

    MBL_HM_HUD_NUM = "mbl_hm_hud_num"
    """
    Mobile Home HUD Number
    """

    MBL_HM_TITLE_NUM = "mbl_hm_title_num"
    """
    Mobile Home Title Number
    """

    MEX_DECLARANET_ACUSE = "mex_declaranet_acuse"
    """
    Time stamp unique to each politician's filing on Declaranet
    """

    DEU_REGISTERNUMMER = "deu_registernummer"
    """
    The company number given to each company listed in Handelsregister, the German Commercial Register. It is not unique unless combined with the district court XJustiz ID, which this weak identifier does not contain because in some cases it is not provided.
    """

    UNKNOWN_NATIONAL_ID_NUM = "unknown_national_id_num"
    """
    A National ID Number whose country of origin is not known
    """

    UNKNOWN_CIVIL_REG_NUM = "unknown_civil_reg_num"
    """
    A Civil Reg Number whose country of origin is not known
    """

    UNKNOWN_RESIDENCY_NUM = "unknown_residency_num"
    """
    A Residency Number whose country of origin is not known
    """

    UNKNOWN_FOLIO_ID_NUM = "unknown_folio_id_num"
    """
    A Folio ID Number whose country of origin is not known
    """

    UNKNOWN_COMMERCIAL_REGISTER_ID = "unknown_commercial_register_id"
    """
    A commercial registration number of unknown origin
    """

    UNKNOWN_CHAMBER_OF_COMMERCE_ID = "unknown_chamber_of_commerce_id"
    """
    A chamber of commerce number of unknwon origin
    """

    UNKNOWN_LICENSE_NUM = "unknown_license_num"
    """
    A license number of unknown origin
    """

    UNKNOWN_INDUSTRIAL_LICENSE_NUM = "unknown_industrial_license_num"
    """
    An industrial license number of unknown origin
    """

    CZE_FILE_NUMBER = "cze_file_number"
    """
    Czechia file number from Moj registry
    """

    MEX_TM_APP_NO = "mex_tm_app_no"
    """
    Mexican trademark application number
    """

    MEX_TM_REG_NO = "mex_tm_reg_no"
    """
    Mexican trademark registration number
    """

    JORDAN_COMPANY_NO = "jordan_company_no"
    """
    Company number from Jordan corporate registry
    """

    CN_QCC_INTERNAL_ID = "cn_qcc_internal_id"
    """
    Part of a qichacha URL, used to uniquely identify people within the site
    """

    JOR_SOL_PROP_INSTITUTION_NUMBER = "jor_sol_prop_institution_number"
    """
    Weak identifier found in sole proprietor source
    """

    USA_NC_CORP_NO = "usa_nc_corp_no"
    """
    North Carolina SoS corporation number
    """

    USA_NM_LICENSE_ID = "usa_nm_license_id"
    """
    New Mexico Secretary of State License Id
    """

    KHM_TIN_NUMBER = "khm_tin_number"
    """
    Cambodia tax identification number
    """

    USA_MO_ENTITY_ID = "usa_mo_entity_id"
    """
    Entity ID from Missouri Corporate Registry
    """

    USA_MO_CORP_NUMBER = "usa_mo_corp_number"
    """
    Corporation Number from Missouri Corporate Registry - used on SoS search
    """

    MAC_RAEM_CASE_NUMBER = "mac_raem_case_number"
    """
    Case number for legal matters from Macao Tribunais da RAEM Judgments
    """

    HND_TEGUCIGALPA_NOTARY = "hnd_tegucigalpa_notary"
    """
    Notary office number for notaries in Honduras Tegucigalpa source
    """

    LBN_FAMILY_NUMBER = "lbn_family_number"
    """
    Lebanese family number
    """

    TX_BEXAR_PROPERTY_GEO_ID = "tx_bexar_property_geo_id"
    PAK_CNIC_FAMILY_NO = "pak_cnic_family_no"
    ROU_COMMERCIAL_REGISTER_ID = "rou_commercial_register_id"
    """
    Romanian Commercial Register ID (concatenated from jud_com, nr_com, and an_com from ROU/taxpayers)
    """

    SOUTH_AFRICA_PARTIAL_ID_NUMBER = "south_africa_partial_id_number"
    """
    Partial South African ID number for individuals
    """

    PRK_INTERNAL_TRADE_ID = "prk_internal_trade_id"
    """
    Internal ID used to link companies between PRK/CN exports and trade dict sources. Downgraded to weak id.
    """

    CHN_CUSTOMS_REGISTRATION_CODE = "chn_customs_registration_code"
    """
    Chinese custums registration code. Downgraded to weak identifier.
    """

    AUT_FORMER_CR_NO = "aut_former_cr_no"
    """
    Austrian Company Register Number (no longer used)
    """

    AUT_NATL_BANK_NO = "aut_natl_bank_no"
    """
    Austrian National Bank ID Number
    """

    LVA_PERSON_ID_MASKED = "lva_person_id_masked"
    """
    Latvian Personal ID Number (last 5 digits masked)
    """

    LVA_COURT_CASE_ID = "lva_court_case_id"
    """
    Latvian Court Case ID Number
    """

    CHN_CNINFO_LEGAL_PERSON_ID = "chn_cninfo_legal_person_id"
    """
    Internal identifier for legal persons from CHN cninfo data
    """

    RKS_BUSINESS_NUMBER = "rks_business_number"
    RKS_FISCAL_NUMBER = "rks_fiscal_number"
    """
    A fiscal number from the Kosovo company registry
    """

    MDG_NIF_NUMBER = "mdg_nif_number"
    """
    A tax identifier number in Madagascar.
    """

    MDG_RCS_NUMBER = "mdg_rcs_number"
    """
    A tax identifier number in Madagascar.
    """

    VAT = "vat"
    """
    See https://en.wikipedia.org/wiki/VAT_identification_number
    """

    USA_IL_CHICAGO_SITE_NUMBER = "usa_il_chicago_site_number"
    """
    Site number of business registered in Chicago, IL business license registry (unique to account number)
    """

    USA_GENERIC_TICKER = "usa_generic_ticker"
    """
    Ticker symbol for securities without exchange information
    """

    VEN_RNC_NUMBER = "ven_rnc_number"
    """
    A certificate number for the National Registry of Contractors in Venezuela
    """

    USA_IMPORTS_SYSTEM_IDENTITY_ID = "usa_imports_system_identity_id"
    """
    Identifier for shipment transactions
    """

    COL_BILL_OF_LADING = "col_bill_of_lading"
    """
    Bill of lading number for Colombian trade data
    """

    COL_SECOP_NO = "col_secop_no"
    """
    Colombian SECOP internal ID
    """

    POL_REGON_NUMBER = "pol_regon_number"
    """
    The register REGON fulfils the function of the national official Register of National Economy Entities
    """

    POL_NIP_NUMBER = "pol_nip_number"
    """
    Tax identification number from Poland
    """

    BILL_OF_LADING = "bill_of_lading"
    """
    Bill of lading number for trade data
    """

    PAN_IBC_RUC = "pan_ibc_ruc"
    """
    Panama IBC RUC
    """

    PAK_OLD_COMPANY_CODE = "pak_old_company_code"
    """
    Old Pakistan company code
    """

    JPN_PERMIT_NO = "jpn_permit_no"
    """
    Japan ministry of land, infrastructure, transportation and tourism permit number
    """

    DMA_CORPORATE_REGISTRY_ENTITY_NUM = "dma_corporate_registry_entity_num"
    """
    Dominica Business Registry Entity Number
    """

    ATG_CORPORATE_REGISTRY_ENTITY_NUM = "atg_corporate_registry_entity_num"
    """
    Antigua and Barbuda Business Registry Entity Number
    """

    LCA_CORPORATE_REGISTRY_ENTITY_NUM = "lca_corporate_registry_entity_num"
    """
    St. Lucia Business Registry Entity Number
    """

    VEN_MANIFIESTO_NUMBER = "ven_manifiesto_number"
    """
    Manifiesto number for Venezuelan shipments
    """

    COL_MATRICULA_MERCANTIL = "col_matricula_mercantil"
    """
    Matricula mercantil number which is non unique across different chambers of commerce
    """

    MARITIME_MOBILE_SERVICE_IDENTITY = "maritime_mobile_service_identity"
    """
    Maritime Mobile Service Identity Number (https://en.wikipedia.org/wiki/Maritime_Mobile_Service_Identity)
    """

    USA_FORMER_FEIN = "usa_former_fein"
    """
    Former USA/IRS FEI/EIN Number
    """

    USA_CBP_WRO_ID = "usa_cbp_wro_id"
    """
    USA Customs and Border Protection Withhold Release Order ID
    """

    CCS_SHIP_CLASS_NUMBER = "ccs_ship_class_number"
    """
    China Classification Society Ship Class Number
    """

    TUR_PARTIAL_MERSIS_NUMBER = "tur_partial_mersis_number"
    """
    Partial Turkish Central Registry Number System MERSIS number
    """

    TUR_OFFICE_REGISTRATION_NUMBER = "tur_office_registration_number"
    """
    Turkey municipal trade registry ID number. Assigned by municipal chambers of commerce in Turkey.
    """

    PARTIAL_VEN_CEDULA = "partial_ven_cedula"
    """
    A Identification Card or Passport Document for people in Venezuela
    """

    RUS_CBR_ID = "rus_cbr_id"
    """
    Russia Central Bank ID
    """

    GEO_STATE_REGISTRATION_NUMBER = "geo_state_registration_number"
    """
    Georgian state registration number
    """

    BIH_MBS_NUMBER = "bih_mbs_number"
    """
    Bosnia and Herzegovenia business register registration number
    """

    GBR_GRANT_INFO_NUMBER = "gbr_grant_info_number"
    """
    UK entity ID number assigned to entities registered in the UK Government Grants Information System.
    """

    MALFORMED_MMR_PRIOR_REG_NO = "malformed mmr_prior_reg_no"
    """
    A temporary malformed type
    """

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        mx_partial_rfc_person: typing.Callable[[], T_Result],
        ru_oktmo: typing.Callable[[], T_Result],
        ru_kpp: typing.Callable[[], T_Result],
        ru_okpo: typing.Callable[[], T_Result],
        unknown_passport: typing.Callable[[], T_Result],
        rks_kta_number: typing.Callable[[], T_Result],
        bra_partial_cpf: typing.Callable[[], T_Result],
        ven_colegiado_number: typing.Callable[[], T_Result],
        pan_folio: typing.Callable[[], T_Result],
        kgz_okpo: typing.Callable[[], T_Result],
        kgz_inn: typing.Callable[[], T_Result],
        lbn_registration_number: typing.Callable[[], T_Result],
        ita_ebr_reg_number: typing.Callable[[], T_Result],
        ita_ebr_short_search_code: typing.Callable[[], T_Result],
        chl_santiago_gazette_cve: typing.Callable[[], T_Result],
        bmu_registration_number: typing.Callable[[], T_Result],
        brazilian_oab: typing.Callable[[], T_Result],
        irn_reg_number: typing.Callable[[], T_Result],
        mx_fme: typing.Callable[[], T_Result],
        ukr_edrpou: typing.Callable[[], T_Result],
        ru_license_number: typing.Callable[[], T_Result],
        maritime_call_sign: typing.Callable[[], T_Result],
        prk_ship_reg_no: typing.Callable[[], T_Result],
        cofi_code: typing.Callable[[], T_Result],
        ru_nza: typing.Callable[[], T_Result],
        arg_igj_number: typing.Callable[[], T_Result],
        unknown_bra_case_number: typing.Callable[[], T_Result],
        irq_provision_card: typing.Callable[[], T_Result],
        mbl_hm_sn: typing.Callable[[], T_Result],
        mbl_hm_hud_num: typing.Callable[[], T_Result],
        mbl_hm_title_num: typing.Callable[[], T_Result],
        mex_declaranet_acuse: typing.Callable[[], T_Result],
        deu_registernummer: typing.Callable[[], T_Result],
        unknown_national_id_num: typing.Callable[[], T_Result],
        unknown_civil_reg_num: typing.Callable[[], T_Result],
        unknown_residency_num: typing.Callable[[], T_Result],
        unknown_folio_id_num: typing.Callable[[], T_Result],
        unknown_commercial_register_id: typing.Callable[[], T_Result],
        unknown_chamber_of_commerce_id: typing.Callable[[], T_Result],
        unknown_license_num: typing.Callable[[], T_Result],
        unknown_industrial_license_num: typing.Callable[[], T_Result],
        cze_file_number: typing.Callable[[], T_Result],
        mex_tm_app_no: typing.Callable[[], T_Result],
        mex_tm_reg_no: typing.Callable[[], T_Result],
        jordan_company_no: typing.Callable[[], T_Result],
        cn_qcc_internal_id: typing.Callable[[], T_Result],
        jor_sol_prop_institution_number: typing.Callable[[], T_Result],
        usa_nc_corp_no: typing.Callable[[], T_Result],
        usa_nm_license_id: typing.Callable[[], T_Result],
        khm_tin_number: typing.Callable[[], T_Result],
        usa_mo_entity_id: typing.Callable[[], T_Result],
        usa_mo_corp_number: typing.Callable[[], T_Result],
        mac_raem_case_number: typing.Callable[[], T_Result],
        hnd_tegucigalpa_notary: typing.Callable[[], T_Result],
        lbn_family_number: typing.Callable[[], T_Result],
        tx_bexar_property_geo_id: typing.Callable[[], T_Result],
        pak_cnic_family_no: typing.Callable[[], T_Result],
        rou_commercial_register_id: typing.Callable[[], T_Result],
        south_africa_partial_id_number: typing.Callable[[], T_Result],
        prk_internal_trade_id: typing.Callable[[], T_Result],
        chn_customs_registration_code: typing.Callable[[], T_Result],
        aut_former_cr_no: typing.Callable[[], T_Result],
        aut_natl_bank_no: typing.Callable[[], T_Result],
        lva_person_id_masked: typing.Callable[[], T_Result],
        lva_court_case_id: typing.Callable[[], T_Result],
        chn_cninfo_legal_person_id: typing.Callable[[], T_Result],
        rks_business_number: typing.Callable[[], T_Result],
        rks_fiscal_number: typing.Callable[[], T_Result],
        mdg_nif_number: typing.Callable[[], T_Result],
        mdg_rcs_number: typing.Callable[[], T_Result],
        vat: typing.Callable[[], T_Result],
        usa_il_chicago_site_number: typing.Callable[[], T_Result],
        usa_generic_ticker: typing.Callable[[], T_Result],
        ven_rnc_number: typing.Callable[[], T_Result],
        usa_imports_system_identity_id: typing.Callable[[], T_Result],
        col_bill_of_lading: typing.Callable[[], T_Result],
        col_secop_no: typing.Callable[[], T_Result],
        pol_regon_number: typing.Callable[[], T_Result],
        pol_nip_number: typing.Callable[[], T_Result],
        bill_of_lading: typing.Callable[[], T_Result],
        pan_ibc_ruc: typing.Callable[[], T_Result],
        pak_old_company_code: typing.Callable[[], T_Result],
        jpn_permit_no: typing.Callable[[], T_Result],
        dma_corporate_registry_entity_num: typing.Callable[[], T_Result],
        atg_corporate_registry_entity_num: typing.Callable[[], T_Result],
        lca_corporate_registry_entity_num: typing.Callable[[], T_Result],
        ven_manifiesto_number: typing.Callable[[], T_Result],
        col_matricula_mercantil: typing.Callable[[], T_Result],
        maritime_mobile_service_identity: typing.Callable[[], T_Result],
        usa_former_fein: typing.Callable[[], T_Result],
        usa_cbp_wro_id: typing.Callable[[], T_Result],
        ccs_ship_class_number: typing.Callable[[], T_Result],
        tur_partial_mersis_number: typing.Callable[[], T_Result],
        tur_office_registration_number: typing.Callable[[], T_Result],
        partial_ven_cedula: typing.Callable[[], T_Result],
        rus_cbr_id: typing.Callable[[], T_Result],
        geo_state_registration_number: typing.Callable[[], T_Result],
        bih_mbs_number: typing.Callable[[], T_Result],
        gbr_grant_info_number: typing.Callable[[], T_Result],
        malformed_mmr_prior_reg_no: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WeakIdentifierType.UNKNOWN:
            return unknown()
        if self is WeakIdentifierType.MX_PARTIAL_RFC_PERSON:
            return mx_partial_rfc_person()
        if self is WeakIdentifierType.RU_OKTMO:
            return ru_oktmo()
        if self is WeakIdentifierType.RU_KPP:
            return ru_kpp()
        if self is WeakIdentifierType.RU_OKPO:
            return ru_okpo()
        if self is WeakIdentifierType.UNKNOWN_PASSPORT:
            return unknown_passport()
        if self is WeakIdentifierType.RKS_KTA_NUMBER:
            return rks_kta_number()
        if self is WeakIdentifierType.BRA_PARTIAL_CPF:
            return bra_partial_cpf()
        if self is WeakIdentifierType.VEN_COLEGIADO_NUMBER:
            return ven_colegiado_number()
        if self is WeakIdentifierType.PAN_FOLIO:
            return pan_folio()
        if self is WeakIdentifierType.KGZ_OKPO:
            return kgz_okpo()
        if self is WeakIdentifierType.KGZ_INN:
            return kgz_inn()
        if self is WeakIdentifierType.LBN_REGISTRATION_NUMBER:
            return lbn_registration_number()
        if self is WeakIdentifierType.ITA_EBR_REG_NUMBER:
            return ita_ebr_reg_number()
        if self is WeakIdentifierType.ITA_EBR_SHORT_SEARCH_CODE:
            return ita_ebr_short_search_code()
        if self is WeakIdentifierType.CHL_SANTIAGO_GAZETTE_CVE:
            return chl_santiago_gazette_cve()
        if self is WeakIdentifierType.BMU_REGISTRATION_NUMBER:
            return bmu_registration_number()
        if self is WeakIdentifierType.BRAZILIAN_OAB:
            return brazilian_oab()
        if self is WeakIdentifierType.IRN_REG_NUMBER:
            return irn_reg_number()
        if self is WeakIdentifierType.MX_FME:
            return mx_fme()
        if self is WeakIdentifierType.UKR_EDRPOU:
            return ukr_edrpou()
        if self is WeakIdentifierType.RU_LICENSE_NUMBER:
            return ru_license_number()
        if self is WeakIdentifierType.MARITIME_CALL_SIGN:
            return maritime_call_sign()
        if self is WeakIdentifierType.PRK_SHIP_REG_NO:
            return prk_ship_reg_no()
        if self is WeakIdentifierType.COFI_CODE:
            return cofi_code()
        if self is WeakIdentifierType.RU_NZA:
            return ru_nza()
        if self is WeakIdentifierType.ARG_IGJ_NUMBER:
            return arg_igj_number()
        if self is WeakIdentifierType.UNKNOWN_BRA_CASE_NUMBER:
            return unknown_bra_case_number()
        if self is WeakIdentifierType.IRQ_PROVISION_CARD:
            return irq_provision_card()
        if self is WeakIdentifierType.MBL_HM_SN:
            return mbl_hm_sn()
        if self is WeakIdentifierType.MBL_HM_HUD_NUM:
            return mbl_hm_hud_num()
        if self is WeakIdentifierType.MBL_HM_TITLE_NUM:
            return mbl_hm_title_num()
        if self is WeakIdentifierType.MEX_DECLARANET_ACUSE:
            return mex_declaranet_acuse()
        if self is WeakIdentifierType.DEU_REGISTERNUMMER:
            return deu_registernummer()
        if self is WeakIdentifierType.UNKNOWN_NATIONAL_ID_NUM:
            return unknown_national_id_num()
        if self is WeakIdentifierType.UNKNOWN_CIVIL_REG_NUM:
            return unknown_civil_reg_num()
        if self is WeakIdentifierType.UNKNOWN_RESIDENCY_NUM:
            return unknown_residency_num()
        if self is WeakIdentifierType.UNKNOWN_FOLIO_ID_NUM:
            return unknown_folio_id_num()
        if self is WeakIdentifierType.UNKNOWN_COMMERCIAL_REGISTER_ID:
            return unknown_commercial_register_id()
        if self is WeakIdentifierType.UNKNOWN_CHAMBER_OF_COMMERCE_ID:
            return unknown_chamber_of_commerce_id()
        if self is WeakIdentifierType.UNKNOWN_LICENSE_NUM:
            return unknown_license_num()
        if self is WeakIdentifierType.UNKNOWN_INDUSTRIAL_LICENSE_NUM:
            return unknown_industrial_license_num()
        if self is WeakIdentifierType.CZE_FILE_NUMBER:
            return cze_file_number()
        if self is WeakIdentifierType.MEX_TM_APP_NO:
            return mex_tm_app_no()
        if self is WeakIdentifierType.MEX_TM_REG_NO:
            return mex_tm_reg_no()
        if self is WeakIdentifierType.JORDAN_COMPANY_NO:
            return jordan_company_no()
        if self is WeakIdentifierType.CN_QCC_INTERNAL_ID:
            return cn_qcc_internal_id()
        if self is WeakIdentifierType.JOR_SOL_PROP_INSTITUTION_NUMBER:
            return jor_sol_prop_institution_number()
        if self is WeakIdentifierType.USA_NC_CORP_NO:
            return usa_nc_corp_no()
        if self is WeakIdentifierType.USA_NM_LICENSE_ID:
            return usa_nm_license_id()
        if self is WeakIdentifierType.KHM_TIN_NUMBER:
            return khm_tin_number()
        if self is WeakIdentifierType.USA_MO_ENTITY_ID:
            return usa_mo_entity_id()
        if self is WeakIdentifierType.USA_MO_CORP_NUMBER:
            return usa_mo_corp_number()
        if self is WeakIdentifierType.MAC_RAEM_CASE_NUMBER:
            return mac_raem_case_number()
        if self is WeakIdentifierType.HND_TEGUCIGALPA_NOTARY:
            return hnd_tegucigalpa_notary()
        if self is WeakIdentifierType.LBN_FAMILY_NUMBER:
            return lbn_family_number()
        if self is WeakIdentifierType.TX_BEXAR_PROPERTY_GEO_ID:
            return tx_bexar_property_geo_id()
        if self is WeakIdentifierType.PAK_CNIC_FAMILY_NO:
            return pak_cnic_family_no()
        if self is WeakIdentifierType.ROU_COMMERCIAL_REGISTER_ID:
            return rou_commercial_register_id()
        if self is WeakIdentifierType.SOUTH_AFRICA_PARTIAL_ID_NUMBER:
            return south_africa_partial_id_number()
        if self is WeakIdentifierType.PRK_INTERNAL_TRADE_ID:
            return prk_internal_trade_id()
        if self is WeakIdentifierType.CHN_CUSTOMS_REGISTRATION_CODE:
            return chn_customs_registration_code()
        if self is WeakIdentifierType.AUT_FORMER_CR_NO:
            return aut_former_cr_no()
        if self is WeakIdentifierType.AUT_NATL_BANK_NO:
            return aut_natl_bank_no()
        if self is WeakIdentifierType.LVA_PERSON_ID_MASKED:
            return lva_person_id_masked()
        if self is WeakIdentifierType.LVA_COURT_CASE_ID:
            return lva_court_case_id()
        if self is WeakIdentifierType.CHN_CNINFO_LEGAL_PERSON_ID:
            return chn_cninfo_legal_person_id()
        if self is WeakIdentifierType.RKS_BUSINESS_NUMBER:
            return rks_business_number()
        if self is WeakIdentifierType.RKS_FISCAL_NUMBER:
            return rks_fiscal_number()
        if self is WeakIdentifierType.MDG_NIF_NUMBER:
            return mdg_nif_number()
        if self is WeakIdentifierType.MDG_RCS_NUMBER:
            return mdg_rcs_number()
        if self is WeakIdentifierType.VAT:
            return vat()
        if self is WeakIdentifierType.USA_IL_CHICAGO_SITE_NUMBER:
            return usa_il_chicago_site_number()
        if self is WeakIdentifierType.USA_GENERIC_TICKER:
            return usa_generic_ticker()
        if self is WeakIdentifierType.VEN_RNC_NUMBER:
            return ven_rnc_number()
        if self is WeakIdentifierType.USA_IMPORTS_SYSTEM_IDENTITY_ID:
            return usa_imports_system_identity_id()
        if self is WeakIdentifierType.COL_BILL_OF_LADING:
            return col_bill_of_lading()
        if self is WeakIdentifierType.COL_SECOP_NO:
            return col_secop_no()
        if self is WeakIdentifierType.POL_REGON_NUMBER:
            return pol_regon_number()
        if self is WeakIdentifierType.POL_NIP_NUMBER:
            return pol_nip_number()
        if self is WeakIdentifierType.BILL_OF_LADING:
            return bill_of_lading()
        if self is WeakIdentifierType.PAN_IBC_RUC:
            return pan_ibc_ruc()
        if self is WeakIdentifierType.PAK_OLD_COMPANY_CODE:
            return pak_old_company_code()
        if self is WeakIdentifierType.JPN_PERMIT_NO:
            return jpn_permit_no()
        if self is WeakIdentifierType.DMA_CORPORATE_REGISTRY_ENTITY_NUM:
            return dma_corporate_registry_entity_num()
        if self is WeakIdentifierType.ATG_CORPORATE_REGISTRY_ENTITY_NUM:
            return atg_corporate_registry_entity_num()
        if self is WeakIdentifierType.LCA_CORPORATE_REGISTRY_ENTITY_NUM:
            return lca_corporate_registry_entity_num()
        if self is WeakIdentifierType.VEN_MANIFIESTO_NUMBER:
            return ven_manifiesto_number()
        if self is WeakIdentifierType.COL_MATRICULA_MERCANTIL:
            return col_matricula_mercantil()
        if self is WeakIdentifierType.MARITIME_MOBILE_SERVICE_IDENTITY:
            return maritime_mobile_service_identity()
        if self is WeakIdentifierType.USA_FORMER_FEIN:
            return usa_former_fein()
        if self is WeakIdentifierType.USA_CBP_WRO_ID:
            return usa_cbp_wro_id()
        if self is WeakIdentifierType.CCS_SHIP_CLASS_NUMBER:
            return ccs_ship_class_number()
        if self is WeakIdentifierType.TUR_PARTIAL_MERSIS_NUMBER:
            return tur_partial_mersis_number()
        if self is WeakIdentifierType.TUR_OFFICE_REGISTRATION_NUMBER:
            return tur_office_registration_number()
        if self is WeakIdentifierType.PARTIAL_VEN_CEDULA:
            return partial_ven_cedula()
        if self is WeakIdentifierType.RUS_CBR_ID:
            return rus_cbr_id()
        if self is WeakIdentifierType.GEO_STATE_REGISTRATION_NUMBER:
            return geo_state_registration_number()
        if self is WeakIdentifierType.BIH_MBS_NUMBER:
            return bih_mbs_number()
        if self is WeakIdentifierType.GBR_GRANT_INFO_NUMBER:
            return gbr_grant_info_number()
        if self is WeakIdentifierType.MALFORMED_MMR_PRIOR_REG_NO:
            return malformed_mmr_prior_reg_no()
