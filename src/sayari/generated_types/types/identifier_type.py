# This file was auto-generated by Fern from our API Definition.

import typing

IdentifierType = typing.Union[
    typing.Literal[
        "cn_tianyancha_company_id",
        "cn_tianyancha_human_id",
        "cn_unified_social_credit_code",
        "cn_registration_number",
        "cn_organization_code",
        "cn_qichacha_internal_id",
        "cn_hk_cr_number",
        "cn_hk_filing_number",
        "bh_cr_number",
        "bh_cr_number_and_branch",
        "jo_internal_id",
        "jo_national_institution_number",
        "jo_institution_number",
        "malta_company_number",
        "malta_national_id",
        "malta_accountancy_registration_id",
        "uk_company_number",
        "uk_firm_reference_number",
        "uk_person_number",
        "mx_rfc_person",
        "mx_curp",
        "mx_rfc_company",
        "mx_office_fme",
        "ru_inn",
        "ru_ogrn",
        "ven_saren_internal_employer_number",
        "bra_cnpj",
        "ven_rif",
        "ven_cedula_number",
        "mdv_registration_number",
        "ind_director_id_number",
        "ind_permanent_account_number",
        "ind_corporate_id_number",
        "kaz_tin",
        "kaz_bin",
        "kaz_state_reg_num",
        "kaz_okpo_num",
        "kaz_identifier",
        "rks_registration_number",
        "grc_gemi_number",
        "ven_rnc_number",
        "usa_va_reg_id",
        "usa_ny_reg_id",
        "usa_fei_number",
        "ukr_moj_id",
        "mus_reg_id",
        "uk_title_number",
        "mng_reg_number",
        "mne_reg_number",
        "kgz_reg_number",
        "cn_importexport_code",
        "prk_entity_id",
        "prk_registration_id",
        "yugoslav_master_citizen_num",
        "bfa_entity_id",
        "afghan_tin_number",
        "afg_business_license",
        "mdg_nif_number",
        "mdg_stat_number",
        "mdg_rcs_number",
        "lva_personal_code",
        "iban",
        "lva_reg_number",
        "twn_unified_number",
        "lux_rcs_number",
        "mkd_embs_number",
        "mkd_embs_branch_number",
        "mda_idno_number",
        "ury_ruc_number",
        "che_uid_number",
        "slv_commercial_reg_number",
        "slv_uid_number",
        "mato_grosso_legal_id",
        "lei",
        "vat",
        "ita_fiscal_code",
        "ita_vat_number",
        "rio_de_janeiro_legal_id",
        "isl_tin_number",
        "lao_enterprise_number",
        "svk_ico_number",
        "khm_tin_number",
        "cze_ico_number",
        "irn_national_id",
        "ecu_ruc_number",
        "grc_vat_number",
        "can_corporation_number",
        "can_cra_program_account_number",
        "mne_pib",
        "chl_cedula_number",
        "bra_case_number",
        "ind_llpin",
        "ind_fcrn",
        "bmu_registration_number",
        "bra_cpf_number",
        "irn_national_number",
        "chn_customs_registration_code",
        "lie_public_reg_no",
        "cn_tax_identification_number",
        "mac_registration_no",
        "siger_internal_id",
        "lbn_national_id",
        "int_maritime_org_id",
        "ru_ship_register_id",
        "sayari_internal_identifier",
        "aruba_chamber_of_commerce_id",
        "imo_no",
        "vgb_company_number",
        "yem_coc_registration_number",
        "mys_id_card_no",
        "mys_company_reg_no",
        "pry_ruc_number",
        "pry_cedula_number",
        "pry_old_ruc_number",
        "rccm_no",
        "bra_rg_number",
        "ninea_no",
        "alb_tax_id",
        "alb_registration_number",
        "arg_igj_number",
        "arg_dni_number",
        "arg_cuit_number",
        "arg_cuil_number",
        "arg_cdi_number",
        "bih_mbs_number",
        "bih_jib_number",
        "bih_customs_number",
        "usa_puerto_rico_register_number",
        "dji_rcs_number",
        "cri_cedula_number",
        "moz_id_number",
        "moz_nuit_person",
        "moz_nuit_co",
        "moz_passport",
        "moz_dire_no",
        "moz_voter_no",
        "moz_nuel_no",
        "irq_voter_id",
        "jor_voter_card_no",
        "jor_id_no",
        "per_ruc_no",
        "ecu_company_id",
        "usa_ny_dos_id",
        "bfa_rccm_number",
        "fl_prop_folio",
        "qat_qfc_number",
        "grc_afm_number",
        "vnm_enterprise_code",
        "tha_registration_no",
        "vnm_citizenship_no",
        "vnm_person_id_no",
        "arg_lib_civica_number",
        "arg_lib_enrolamiento_number",
        "nzl_nzbn",
        "nzl_co_no",
        "usa_ofac_sdn_number",
        "swift_bic_code",
        "duns_number",
        "bitcoin_address",
        "litecoin_address",
        "rus_micex_code",
        "tx_prop_id",
        "tx_pacs_id",
        "tx_land_id",
        "png_ipa_reg_id",
        "gtm_nit_number",
        "gtm_cui_number",
        "dom_rnc",
        "qat_cr_number",
        "isin",
        "usa_fl_document_no",
        "usa_fl_fic_name_reg_no",
        "bra_servidor_portal",
        "bra_codigo_da_unidade_organizacional",
        "usa_sec_cik_number",
        "hr_mbs",
        "hr_oib",
        "slv_numero_identificacion_tributaria",
        "slv_mcas",
        "aus_company_number",
        "aus_business_number",
        "deu_registernummer",
        "usa_irs_ein",
        "hong_kong_case_number",
        "irn_coc_internal_id",
        "pan_folio_ficha_id",
        "pan_cedula_number",
        "xxx_cedar_rose_uid",
        "xxx_rccm",
        "vnm_dichvuthongtin_internal_id",
        "xxx_intel_internal_id",
        "usa_washington_state_ubi",
        "nga_registration_number",
        "ng_check_internal_id",
        "nyc_bbl",
        "nyc_crfn",
        "tx_corp_file_num",
        "tx_tax_id",
        "usa_ga_business_id",
        "phl_pse_id",
        "phl_sec_id",
        "phl_tin",
        "afg_passport",
        "irn_passport",
        "kwt_passport",
        "lby_passport",
        "pak_passport",
        "rus_passport",
        "tun_passport",
        "yem_passport",
        "un_sanction_prn",
        "eu_sanction_rn",
        "ca_lp_file_num",
        "tx_entity_filing_num",
        "usa_social_security_number",
        "usa_wy_party_id",
        "usa_wy_filing_id",
        "usa_wy_internal_filing_id",
        "usa_wy_filing_num",
        "usa_or_regno",
        "usa_nv_corpno",
        "usa_nv_bizid",
        "prk_internal_trade_id",
        "lso_corpreg_id",
        "uzb_tin_number",
        "ca_corporate_id_num",
        "gbr_hm_treasury_sanction_group_id",
        "gbr_ipo_trademark_reg_no",
        "usa_ga_control_no",
        "hnd_coc_company_registration_number",
        "mne_property_uid",
        "phl_bnn",
        "rou_company_registration_code",
        "rou_identity_card",
        "rou_personal_id_number",
        "cub_cod",
        "fl_prop_folio_dade",
        "per_dni_no",
        "per_carne_de_extranjeria",
        "fra_siren",
        "fra_siret",
        "fra_rna",
        "fro_reg_num",
        "cze_file_number",
        "esp_borme_reg_id",
        "mex_tm_no",
        "mus_file_no",
        "col_nit_no",
        "jpn_corporate_no",
        "usa_cgac_agency_code",
        "usa_govt_agency_id",
        "usa_govt_office_id",
        "col_cedula_no",
        "col_secop_no",
        "jordan_company_no",
        "dnk_cvr",
        "dnk_production_unit_no",
        "dnk_entity",
        "nor_org_no",
        "swe_org_no",
        "usa_co_reg_no",
        "usa_ia_corp_no",
        "sgp_unqiue_entity_number",
        "usa_ak_entity_no",
        "usa_oh_charter_num",
        "tur_istanbul_coc_reg_no",
        "tur_mersis_number",
        "che_ch_id_number",
        "are_difc_reg_no",
        "idn_tax_id",
        "usa_vt_biz_id",
        "usa_wv_reg_id",
        "usa_ms_biz_id",
        "usa_id_control_no",
        "usa_id_party_id",
        "irn_coc_internal_id_cardno",
        "usa_az_corp_reg_entity_num",
        "usa_ok_filing_no",
        "usa_tn_control_no",
        "usa_tn_party_id",
        "usa_ks_biz_id",
        "usa_hi_corporate_registry_id",
        "usa_hi_corporate_registry_person_id",
        "pol_krs_number",
        "pol_regon_number",
        "pol_nip_number",
        "pol_rejestr_person_id",
        "arm_vat_no",
        "arm_enterprise_code",
        "arm_registration_no",
        "usa_me_corp_id",
        "cyp_reg_no",
        "usa_nd_control_id",
        "usa_mi_corp_id",
        "usa_mi_corp_id_old",
        "usa_hi_trade_name_cert",
        "usa_dc_entity_no",
        "usa_va_old_reg_id",
        "usa_consolidated_screening_list_synthetic_id",
        "usa_ar_filing_no",
        "usa_nc_internal_id",
        "usa_ne_acct_no",
        "usa_ne_agent_id",
        "usa_nm_business_no",
        "usa_nm_license_id",
        "usa_dc_file_no",
        "usa_ri_fei_no",
        "internal_md5",
        "usa_mo_corp_id",
        "usa_wi_dfi_id",
        "geo_identification_code",
        "geo_personal_number",
        "geo_state_registration_number",
        "mac_raem_case_url_id",
        "rou_company_tin",
        "usa_md_dpt_tax",
        "usa_sd_corp_id",
        "hnd_tegucigalpa_matricula",
        "usa_fl_property_id",
        "usa_fl_property_mp_id",
        "usa_fl_property_state_par_id",
        "mex_cluni",
        "usa_pa_corporate_registry_id",
        "pak_ind_ntn",
        "pak_co_ntn",
        "mex_rnie",
        "pak_ngo_reg_no",
        "iraqi_stock_exchange_symbol",
        "bgr_uic",
        "bgr_egn_hashed",
        "south_africa_enterprise_number",
        "south_africa_passport_number",
        "nld_kvk_number",
        "nld_kvk_branch_number",
        "usa_central_registration_depository_number",
        "usa_sec_file_number_bd",
        "chn_cnipa_tm",
        "cyp_passport",
        "cyp_infocredit_entity_id",
        "cyp_id_card",
        "cyp_ssn",
        "aut_firmenbuch_no",
        "swe_per_id_no",
        "chn_shanghai_stock_exchange_company_code",
        "usa_sec_file_number_ia",
        "chn_shenzen_sec_code",
        "usa_ct_business_id",
        "ecu_cedula_number",
        "hkg_stock_code",
        "can_bc_company_registration_id",
        "can_bc_extraprovincial_registration_id",
        "can_ipo_trademark_application_no",
        "ltu_company_registration_code",
        "usa_sec_private_fund",
        "lva_insolvency_proceeding_id",
        "chn_cninfo_internal_shareholder_id",
        "euid",
        "fin_business_id",
        "est_business_reg_code",
        "usa_cusip_number",
        "svn_co_reg_no",
        "isr_company_number",
        "rks_business_number",
        "rks_fiscal_number",
        "jpn_edinet_code",
        "bel_enterprise_number",
        "bel_establishment_number",
        "aus_afs_licence_number",
        "aus_afs_rep_number",
        "aus_adv_number",
        "aus_credit_licence_number",
        "aus_credit_rep_number",
        "dart_cik",
        "krx_ticker_code",
        "kor_corporate_registration_number",
        "kor_business_tin",
        "est_personal_id",
        "bze_bicar_reg_no",
        "usa_il_chicago_account_number",
        "cym_co_no",
        "ggy_corporate_reg_number",
        "jey_corporate_reg_number",
        "cok_corp_reg_corpid",
        "cok_corp_reg_corpofficerid",
        "cok_corp_reg_number",
        "mex_open_contracts_internal_id",
        "gib_corp_reg_number",
        "dom_onapi_num",
        "rus_tourist_obj",
        "bill_of_lading",
        "twn_factory_registration_number",
        "twn_factory_establishment_permit_case_number",
        "ken_personal_id",
        "col_dian_numero_formulario",
        "vut_corp_reg_number",
        "geo_legal_code",
        "mmr_corp_id",
        "mmr_reg_no",
        "mmr_prior_reg_no",
        "mmr_officer_id",
        "arm_passport_number",
        "ukr_reg_num",
        "validatis_number",
        "are_dubai_land_case_no",
        "ago_matricula_number",
        "ago_nif_number",
        "mmr_personal_id_no",
        "blr_registration_number",
        "aer_free_zone_license",
        "aer_free_zone_reg_no",
        "can_nl_corporate_registry",
        "can_data_axle_hash",
        "svn_ajpes_zapst_number",
        "usa_corpwatch_id",
        "usa_de_file_number",
        "imn_company_number",
        "svn_vat_number",
        "xxx_acuris_id",
        "pak_egm_id",
        "usa_de_registered_agent_id",
        "icij_offshore_internal_id",
        "icij_offshore_node_id",
        "ecu_branch_id",
        "pse_registration_id",
        "srb_mb_number",
        "srb_pib_number",
        "srb_branch_id",
        "rus_bik_code",
        "panadata_internal_id",
        "smr_economic_operator_code",
        "usa_ct_internal_id",
        "alei",
        "can_ns_corporate_registry",
        "som_ubi",
        "bhs_tin",
        "ita_rea_number",
        "mex_denue_clee",
        "ihs_owner_code",
        "aus_consolidated_sanctions_reference",
        "che_seco_sanction_number",
        "gbr_vat_no",
        "gbr_company_number",
        "esp_nif",
        "usa_sam_uei_number",
        "usa_usvi_corp_number",
        "nic_numero_unico",
        "cri_cedula_juridica",
        "cri_cedula_citizen_person",
        "cri_cedula_foreign_person",
        "bol_matricula",
        "bol_old_matricula",
        "nga_crp_reg_internal_id",
        "nga_registration_sn",
        "nga_nin",
        "nga_drivers",
        "nga_tax_id",
        "dma_business_registry_internal_id",
        "cage",
        "atg_business_registry_internal_id",
        "lca_business_registry_internal_id",
        "prt_trust_number",
        "prt_vat_number",
        "mar_passport",
        "cod_passport",
        "prk_passport",
        "sgp_passport",
        "chn_passport",
        "omn_passport",
        "caf_passport",
        "ssd_passport",
        "tto_biz_number",
        "tur_tax_id",
        "bmu_registrar_of_companies_number",
        "cod_rccm_number",
        "cod_rccm_ohada_number",
        "are_reg_auth_number",
        "prk_shipment_id",
        "ecu_importer_id",
        "ecu_exporter_id",
        "ecu_shipment_ref_no",
        "xxx_crb_monitor_entity_id",
        "xxx_edi_global_issuer_id",
        "xxx_edi_global_security_id",
        "chl_import_export_control_id",
        "chl_import_manifest_number",
        "chl_importer_exporter_id",
        "arg_import_export_id",
        "arg_partial_cuit",
        "pan_importer_exporter_id",
        "pan_declaration_number",
        "mex_shipment_number",
        "cri_exp",
        "cri_imp",
        "cri_op_no",
        "col_nur",
        "npl_co_reg_no",
        "usa_sam_exclusions_number",
        "usa_npi_number",
        "usa_upin_number",
        "can_bc_registration_number",
        "can_business_number",
        "chn_csrc_no",
        "usa_mn_master_id",
        "usa_mn_filing_number",
        "usa_in_biz_no",
        "lloyds_internal_vessel_id",
        "lloyds_internal_entity_id",
        "usa_nh_business_id",
        "gbr_uk_sanctions_id",
        "montana_sos_internal_entity_id",
        "usa_mass_sos_company_id",
        "chn_resident_id_number",
        "usa_nj_business_id",
        "utah_corporate_registry_internal_entity_number",
        "usa_la_sos_id",
        "usa_al_sos_id",
        "usa_sc_corp_id",
        "usa_ky_org_no",
        "usa_il_file_number",
        "idn_transaction_number",
        "idn_ubo_owner_id",
        "swe_tax_number",
        "panadata_internal_sid",
        "pry_tax_id",
        "pry_shipment_number",
        "tokyo_stock_exchange_no",
        "swe_fi_id",
        "deu_bafin_id",
        "global_trade_internal_shipment_id",
        "china_vessel_inspection_registration",
        "china_vessel_registration",
        "ccs_registration",
        "usa_oti_id",
        "stock_ticker",
        "can_mb_registry",
        "quebec_enterprise_number",
        "ontario_corporation_number",
        "saskatchewan_registry_number",
        "alberta_corporation_number",
        "bra_shipment_number",
        "ukr_sanctions_nazk_company_internal_id",
        "ukr_sanctions_nazk_person_internal_id",
        "ethereum_address",
        "dash_address",
        "zcash_address",
        "usa_uspto_serial_number",
        "usa_uspto_reg_no",
        "usa_uspto_foreign_application_no",
        "usa_uspto_foreign_reg_no",
        "wipo_intl_reg_no",
        "wipo_intl_ref_no",
        "gbr_charity_no",
        "gbr_trustee_id",
        "gbr_go_no",
        "irl_registration_no",
        "irl_rcn",
        "blz_bccar_reg_no",
        "chn_customs_registration_no",
        "isl_vat_num",
        "can_tm_registration_no",
        "aze_tin_number",
        "tjk_tin_number",
        "tjk_ein_number",
        "mco_rci_number",
        "mco_nis",
        "on_business_id_number",
        "syria_commercial_register_number",
        "cn_hurd_internal_company_id",
        "hun_tax_number",
        "hun_company_register_number",
        "hun_person_tax_id",
        "mw_tpin_tax_reg_num",
        "lr_tin",
        "cm_nui_tax_reg_num",
        "eu_fsd_id",
        "cn_hk_br_number",
        "bwa_uin_reg_number",
        "can_nrd",
        "usa_irs_giin",
        "can_nrd_individual_id",
        "jam_company_id",
        "esp_internal_employee_number",
    ],
    typing.Any,
]
