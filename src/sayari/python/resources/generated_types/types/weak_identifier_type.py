# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WeakIdentifierType(str, enum.Enum):
    UNKNOWN = "unknown"
    MX_PARTIAL_RFC_PERSON = "mx_partial_rfc_person"
    RU_OKTMO = "ru_oktmo"
    RU_KPP = "ru_kpp"
    RU_OKPO = "ru_okpo"
    UNKNOWN_PASSPORT = "unknown_passport"
    RKS_KTA_NUMBER = "rks_kta_number"
    BRA_PARTIAL_CPF = "bra_partial_cpf"
    VEN_COLEGIADO_NUMBER = "ven_colegiado_number"
    PAN_FOLIO = "pan_folio"
    KGZ_OKPO = "kgz_okpo"
    KGZ_INN = "kgz_inn"
    LBN_REGISTRATION_NUMBER = "lbn_registration_number"
    ITA_EBR_REG_NUMBER = "ita_ebr_reg_number"
    ITA_EBR_SHORT_SEARCH_CODE = "ita_ebr_short_search_code"
    CHL_SANTIAGO_GAZETTE_CVE = "chl_santiago_gazette_cve"
    BMU_REGISTRATION_NUMBER = "bmu_registration_number"
    BRAZILIAN_OAB = "brazilian_oab"
    IRN_REG_NUMBER = "irn_reg_number"
    MX_FME = "mx_fme"
    UKR_EDRPOU = "ukr_edrpou"
    RU_LICENSE_NUMBER = "ru_license_number"
    MARITIME_CALL_SIGN = "maritime_call_sign"
    PRK_SHIP_REG_NO = "prk_ship_reg_no"
    COFI_CODE = "cofi_code"
    RU_NZA = "ru_nza"
    ARG_IGJ_NUMBER = "arg_igj_number"
    UNKNOWN_BRA_CASE_NUMBER = "unknown_bra_case_number"
    IRQ_PROVISION_CARD = "irq_provision_card"
    MBL_HM_SN = "mbl_hm_sn"
    MBL_HM_HUD_NUM = "mbl_hm_hud_num"
    MBL_HM_TITLE_NUM = "mbl_hm_title_num"
    MEX_DECLARANET_ACUSE = "mex_declaranet_acuse"
    DEU_REGISTERNUMMER = "deu_registernummer"
    UNKNOWN_NATIONAL_ID_NUM = "unknown_national_id_num"
    UNKNOWN_CIVIL_REG_NUM = "unknown_civil_reg_num"
    UNKNOWN_RESIDENCY_NUM = "unknown_residency_num"
    UNKNOWN_FOLIO_ID_NUM = "unknown_folio_id_num"
    UNKNOWN_COMMERCIAL_REGISTER_ID = "unknown_commercial_register_id"
    UNKNOWN_CHAMBER_OF_COMMERCE_ID = "unknown_chamber_of_commerce_id"
    UNKNOWN_LICENSE_NUM = "unknown_license_num"
    UNKNOWN_INDUSTRIAL_LICENSE_NUM = "unknown_industrial_license_num"
    CZE_FILE_NUMBER = "cze_file_number"
    MEX_TM_APP_NO = "mex_tm_app_no"
    MEX_TM_REG_NO = "mex_tm_reg_no"
    JORDAN_COMPANY_NO = "jordan_company_no"
    CN_QCC_INTERNAL_ID = "cn_qcc_internal_id"
    JOR_SOL_PROP_INSTITUTION_NUMBER = "jor_sol_prop_institution_number"
    USA_NC_CORP_NO = "usa_nc_corp_no"
    USA_NM_LICENSE_ID = "usa_nm_license_id"
    KHM_TIN_NUMBER = "khm_tin_number"
    USA_MO_ENTITY_ID = "usa_mo_entity_id"
    USA_MO_CORP_NUMBER = "usa_mo_corp_number"
    MAC_RAEM_CASE_NUMBER = "mac_raem_case_number"
    HND_TEGUCIGALPA_NOTARY = "hnd_tegucigalpa_notary"
    LBN_FAMILY_NUMBER = "lbn_family_number"
    TX_BEXAR_PROPERTY_GEO_ID = "tx_bexar_property_geo_id"
    PAK_CNIC_FAMILY_NO = "pak_cnic_family_no"
    ROU_COMMERCIAL_REGISTER_ID = "rou_commercial_register_id"
    SOUTH_AFRICA_PARTIAL_ID_NUMBER = "south_africa_partial_id_number"
    PRK_INTERNAL_TRADE_ID = "prk_internal_trade_id"
    CHN_CUSTOMS_REGISTRATION_CODE = "chn_customs_registration_code"
    AUT_FORMER_CR_NO = "aut_former_cr_no"
    AUT_NATL_BANK_NO = "aut_natl_bank_no"
    LVA_PERSON_ID_MASKED = "lva_person_id_masked"
    LVA_COURT_CASE_ID = "lva_court_case_id"
    CHN_CNINFO_LEGAL_PERSON_ID = "chn_cninfo_legal_person_id"
    RKS_BUSINESS_NUMBER = "rks_business_number"
    RKS_FISCAL_NUMBER = "rks_fiscal_number"
    MDG_NIF_NUMBER = "mdg_nif_number"
    MDG_RCS_NUMBER = "mdg_rcs_number"
    VAT = "vat"
    USA_IL_CHICAGO_SITE_NUMBER = "usa_il_chicago_site_number"
    USA_GENERIC_TICKER = "usa_generic_ticker"
    VEN_RNC_NUMBER = "ven_rnc_number"
    USA_IMPORTS_SYSTEM_IDENTITY_ID = "usa_imports_system_identity_id"
    COL_BILL_OF_LADING = "col_bill_of_lading"
    COL_SECOP_NO = "col_secop_no"
    POL_REGON_NUMBER = "pol_regon_number"
    POL_NIP_NUMBER = "pol_nip_number"
    BILL_OF_LADING = "bill_of_lading"
    PAN_IBC_RUC = "pan_ibc_ruc"
    PAK_OLD_COMPANY_CODE = "pak_old_company_code"
    JPN_PERMIT_NO = "jpn_permit_no"
    DMA_CORPORATE_REGISTRY_ENTITY_NUM = "dma_corporate_registry_entity_num"
    ATG_CORPORATE_REGISTRY_ENTITY_NUM = "atg_corporate_registry_entity_num"
    LCA_CORPORATE_REGISTRY_ENTITY_NUM = "lca_corporate_registry_entity_num"
    VEN_MANIFIESTO_NUMBER = "ven_manifiesto_number"
    COL_MATRICULA_MERCANTIL = "col_matricula_mercantil"
    MARITIME_MOBILE_SERVICE_IDENTITY = "maritime_mobile_service_identity"
    USA_FORMER_FEIN = "usa_former_fein"
    USA_CBP_WRO_ID = "usa_cbp_wro_id"
    CCS_SHIP_CLASS_NUMBER = "ccs_ship_class_number"
    TUR_PARTIAL_MERSIS_NUMBER = "tur_partial_mersis_number"
    TUR_OFFICE_REGISTRATION_NUMBER = "tur_office_registration_number"
    PARTIAL_VEN_CEDULA = "partial_ven_cedula"
    RUS_CBR_ID = "rus_cbr_id"
    GEO_STATE_REGISTRATION_NUMBER = "geo_state_registration_number"
    BIH_MBS_NUMBER = "bih_mbs_number"

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