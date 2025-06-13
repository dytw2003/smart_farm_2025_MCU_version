# control_gpio.py
# NEED TO CHANGE FOR OTHER HOUSE
# 1_flg =
# _1 =
# am_flg_1 =
class VariableData:
    def __init__(self):
        # ld flag
        # self.cpu_clk=None
        self.mcu_mem = 0
        self.ld_flg = False
        self.hw_switch_1 = None
        self.rst_1 = None
        self.rst_atmn_flg = False
        self.mnsig_flag_1 = False
        self.cld_rtc_flg = False
        # self.cld_rtc_lcl = False
        self.rtc_init = False
        self.psv_sen_flg = False
        self.psv_ato_flg = False

        # -------------------------------------------------  flags
        # ========================auto flags
        # side windows (측창)
        # 1f (좌측)/우측

        self.sw_1fl_atflg_1 = False
        self.sw_1fr_atflg_1 = False
        # 2f (좌측)/우측

        self.sw_2fl_atflg_1 = False
        self.sw_2fr_atflg_1 = False
        # 3f (좌측)/우측

        self.sw_3fl_atflg_1 = False
        self.sw_3fr_atflg_1 = False
        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1fl_atflg_1 = False
        self.cw_1fr_atflg_1 = False
        # # 2f (좌측)/우측
        # self.cw_2fl_atflg_1 = False
        # self.cw_2fr_atflg_1 = False
        # # 3f (좌측)/우측
        # self.cw_3fl_atflg_1 = False
        # self.cw_3fr_atflg_1 = False
        # 유동팬 1
        self.cf_01_atflg_1 = None   
        # 유동팬 2
        self.cf_02_atflg_1 = None  


        self.ef_atflg_1 = None  # ,#배기팬
        self.wc_atflg_1 = None  # ,#수막
        # self.co2_atflg_1 = None  # ,#CO₂
        # self.fv_atflg_1 = None  # ,#포그밸브
        # self.sl_atflg_1 = None  # ,#보광등
        # self.if_atflg_1 = None  # ,#흡기팬


        # ======================= open close flag

        # 1f (좌측)/우측
        self.sw_1fl_o_flg_1 = False
        self.sw_1fl_cl_flg_1 = False
        self.sw_1fr_o_flg_1 = False
        self.sw_1fr_cl_flg_1 = False
        # 2f (좌측)/우측
        self.sw_2fl_o_flg_1 = False
        self.sw_2fl_cl_flg_1 = False
        self.sw_2fr_o_flg_1 = False
        self.sw_2fr_cl_flg_1 = False
        # 3f (좌측)/우측
        self.sw_3fl_o_flg_1 = False
        self.sw_3fl_cl_flg_1 = False
        self.sw_3fr_o_flg_1 = False
        self.sw_3fr_cl_flg_1 = False
        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1fl_o_flg_1 = False
        self.cw_1fl_cl_flg_1 = False
        self.cw_1fr_o_flg_1 = False
        self.cw_1fr_cl_flg_1 = False
        # # 2f (좌측)/우측
        # self.cw_2fl_o_flg_1 = False
        # self.cw_2fl_cl_flg_1 = False
        # self.cw_2fr_o_flg_1 = False
        # self.cw_2fr_cl_flg_1 = False
        # # 3f (좌측)/우측
        # self.cw_3fl_o_flg_1 = False
        # self.cw_3fl_cl_flg_1 = False
        # self.cw_3fr_o_flg_1 = False
        # self.cw_3fr_cl_flg_1 = False

        # -------------------------------------------motor run time
        # side windows (측창)
        # 1f (좌측)/우측
        self.sw_1fl_o_runt_1 = 0
        self.sw_1fl_cl_runt_1 = 0
        self.sw_1fr_o_runt_1 = 0
        self.sw_1fr_cl_runt_1 = 0
        # 2f (좌측)/우측
        self.sw_2fl_o_runt_1 = 0
        self.sw_2fl_cl_runt_1 = 0
        self.sw_2fr_o_runt_1 = 0
        self.sw_2fr_cl_runt_1 = 0
        # 3f (좌측)/우측
        self.sw_3fl_o_runt_1 = 0
        self.sw_3fl_cl_runt_1 = 0
        self.sw_3fr_o_runt_1 = 0
        self.sw_3fr_cl_runt_1 = 0
        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1fl_o_runt_1 = 0
        self.cw_1fl_cl_runt_1 = 0
        self.cw_1fr_o_runt_1 = 0
        self.cw_1fr_cl_runt_1 = 0
        # # 2f (좌측)/우측
        # self.cw_2fl_o_runt_1 = 0
        # self.cw_2fl_cl_runt_1 = 0
        # self.cw_2fr_o_runt_1 = 0
        # self.cw_2fr_cl_runt_1 = 0
        # # 3f (좌측)/우측
        # self.cw_3fl_o_runt_1 = 0
        # self.cw_3fl_cl_runt_1 = 0
        # self.cw_3fr_o_runt_1 = 0
        # self.cw_3fr_cl_runt_1 = 0

        # -------------------------------------------------  status
        # side windows (측창)
        # 1f (좌측)/우측

        self.sw_1fl_oc_1 = None
        self.sw_1fl_stat_1 = None
        self.sw_1fr_oc_1 = None
        self.sw_1fr_stat_1 = None
        # 2f (좌측)/우측

        self.sw_2fl_oc_1 = None
        self.sw_2fl_stat_1 = None
        self.sw_2fr_oc_1 = None
        self.sw_2fr_stat_1 = None
        # 3f (좌측)/우측

        self.sw_3fl_oc_1 = None
        self.sw_3fl_stat_1 = None
        self.sw_3fr_oc_1 = None
        self.sw_3fr_stat_1 = None
        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1fl_oc_1 = None
        self.cw_1fl_stat_1 = None
        self.cw_1fr_oc_1 = None
        self.cw_1fr_stat_1 = None
        # # 2f (좌측)/우측
        # self.cw_2fl_oc_1 = None
        # self.cw_2fl_stat_1 = None
        # self.cw_2fr_oc_1 = None
        # self.cw_2fr_stat_1 = None
        # # 3f (좌측)/우측
        # self.cw_3fl_oc_1 = None
        # self.cw_3fl_stat_1 = None
        # self.cw_3fr_oc_1 = None
        # self.cw_3fr_stat_1 = None

        # ============================ AC ACTUATORS=======
        # -------------------------------------------------  flags
        # co2
        self.co2_temp_run_flg_1 = False
        # -------------------------------------------------  status
        # 유동팬 1
        self.cf_01_oc_1 = None
        # 유동팬 2
        self.cf_02_oc_1 = None
        self.ef_oc_1 = None  # 배기팬
        # self.wc_oc_1 = None  # 수막
        # self.co2_oc_1 = None  # CO₂
        # self.fv_oc_1 = None  # 포그밸브
        # self.sl_oc_1 = None  # 보광등
        # self.if_oc_1 = None  # 흡기팬

        # self.hu_oc_1 = None  # 난방기
        # self.cu_oc_1 = None  # 냉방기

        # ========================================================Manual (수동/자동 버튼)

        # side windows (측창)
        # 1f (좌측)/우측

        self.sw_1fl_1 = None
        self.sw_1fr_1 = None
        # 2f (좌측)/우측

        self.sw_2fl_1 = None
        self.sw_2fr_1 = None
        # 3f (좌측)/우측

        self.sw_3fl_1 = None
        self.sw_3fr_1 = None
        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1fl_1 = None
        self.cw_1fr_1 = None
        # # 2f (좌측)/우측
        # self.cw_2fl_1 = None
        # self.cw_2fr_1 = None
        # # 3f (좌측)/우측
        # self.cw_3fl_1 = None
        # self.cw_3fr_1 = None
        # ==================================================AC Actuators

        # 유동팬 1
        self.cf_01_1 = None  # ,
        # self.cf_01_fwd_1 = None  # ,#정방향
        # self.cf_01_rev_1 = None  # ,#역방향
        # 유동팬 2
        self.cf_02_1 = None  # ,
        # self.cf_02_fwd_1 = None  # ,#정방향
        # self.cf_02_rev_1 = None  # ,#역방향

        self.ef_1 = None  # ,#배기팬
        self.wc_1 = None  # ,#수막
        self.co2_1 = None  # ,#CO₂
        self.fv_1 = None  # ,#포그밸브
        self.sl_1 = None  # ,#보광등
        self.if_1 = None  # ,#흡기팬

        # self.hu_1 = None  # ,#난방기
        # self.cu_1 = None  # ,#냉방기

        # ================================================================== AUTO BUTTON 자동

        # side windows (측창)
        # 1f (좌측)/우측
        self.sw_1f_lbtn_1 = None
        self.sw_1f_rbtn_1 = None
        self.sw_1f_rnbtn_1 = None
        self.sw_1f_ambtn_1 = None

        # 2f (좌측)/우측
        self.sw_2f_lbtn_1 = None
        self.sw_2f_rbtn_1 = None
        # self.sw_2f_rnbtn_1 = None
        self.sw_2f_ambtn_1 = None

        # 3f (좌측)/우측
        self.sw_3f_lbtn_1 = None
        self.sw_3f_rbtn_1 = None
        # self.sw_3f_rnbtn_1 = None
        self.sw_3f_ambtn_1 = None

        self.sw_3f_li_1 = None

        # ceiling windows (천창)
        # 1f (좌측)/우측
        self.cw_1f_lbtn_1 = None
        self.cw_1f_rbtn_1 = None
        self.cw_1f_rnbtn_1 = None
        self.cw_1f_ambtn_1 = None

        self.cw_1f_li_1 = None

        # # 2f (좌측)/우측
        # self.cw_2f_lbtn_1 = None
        # self.cw_2f_rbtn_1 = None
        # # self.cw_2f_rnbtn_1 = None
        # self.cw_2f_ambtn_1 = None
        # self.cw_2f_li_1 = None

        # # 3f (좌측)/우측
        # self.cw_3f_lbtn_1 = None
        # self.cw_3f_rbtn_1 = None
        # # self.cw_3f_rnbtn_1 = None
        # self.cw_3f_ambtn_1 = None
        # self.cw_3f_li_1 = None

        # ==================================================AC Actuators
        # 유동팬 1
        self.cf_01_ambtn_1 = None
        # 유동팬 2
        self.cf_02_ambtn_1 = None
        # 배기팬
        self.ef_ambtn_1 = None
        # 수막
        self.wc_ambtn_1 = None
        # CO₂
        self.co2_ambtn_1 = None
        # 포그밸브
        self.fv_ambtn_1 = None
        # 보광등
        self.sl_ambtn_1 = None
        # 흡기팬
        self.if_ambtn_1 = None

        # 난방기
        # 냉방기

        # ABCDself.EF
        # 버튼01
        # 버튼02
        # 버튼03

    # Auto setting variables-----------------------------------------------------------------------------------------------------
    # ================================= side windows (측창)
        # 1f (좌측)/우측
        # 1중
        # (left_right) 좌측/우측
        # temperature row (온도)
        self.sw_1f_s1_temp_1 = 0
        self.sw_1f_s2_temp_1 = 0
        self.sw_1f_s3_temp_1 = 0
        self.sw_1f_s4_temp_1 = 0
        self.sw_1f_s5_temp_1 = 0
        self.sw_1f_s6_temp_1 = 0
        # Humidity row (습도)
        self.sw_1f_s1_humi_1 = 0
        self.sw_1f_s2_humi_1 = 0
        self.sw_1f_s3_humi_1 = 0
        self.sw_1f_s4_humi_1 = 0
        self.sw_1f_s5_humi_1 = 0
        self.sw_1f_s6_humi_1 = 0
        # environment out wind speed (외부 풍속)
        self.sw_1f_s1_eows_1 = 0
        self.sw_1f_s2_eows_1 = 0
        self.sw_1f_s3_eows_1 = 0
        self.sw_1f_s4_eows_1 = 0
        self.sw_1f_s5_eows_1 = 0
        self.sw_1f_s6_eows_1 = 0
        # start time (시작 시간)
        # minutes(분)
        self.sw_1f_s1_sm_1 = 0
        self.sw_1f_s2_sm_1 = 0
        self.sw_1f_s3_sm_1 = 0
        self.sw_1f_s4_sm_1 = 0
        self.sw_1f_s5_sm_1 = 0
        self.sw_1f_s6_sm_1 = 0
        # hours(시)
        self.sw_1f_s1_sh_1 = 0
        self.sw_1f_s2_sh_1 = 0
        self.sw_1f_s3_sh_1 = 0
        self.sw_1f_s4_sh_1 = 0
        self.sw_1f_s5_sh_1 = 0
        self.sw_1f_s6_sh_1 = 0
        # end time(종료 시간)
        # minutes(분)
        self.sw_1f_s1_em_1 = 0
        self.sw_1f_s2_em_1 = 0
        self.sw_1f_s3_em_1 = 0
        self.sw_1f_s4_em_1 = 0
        self.sw_1f_s5_em_1 = 0
        self.sw_1f_s6_em_1 = 0
        # hours(시)
        self.sw_1f_s1_eh_1 = 0
        self.sw_1f_s2_eh_1 = 0
        self.sw_1f_s3_eh_1 = 0
        self.sw_1f_s4_eh_1 = 0
        self.sw_1f_s5_eh_1 = 0
        self.sw_1f_s6_eh_1 = 0
        # steps row (스텝)
        self.sw_1f_s1_stp_1 = 0
        self.sw_1f_s2_stp_1 = 0
        self.sw_1f_s3_stp_1 = 0
        self.sw_1f_s4_stp_1 = 0
        self.sw_1f_s5_stp_1 = 0
        self.sw_1f_s6_stp_1 = 0
        # single input fields
        self.sw_1f_mtr_1 = 0
        self.sw_1f_max_temp_1 = 0
        # (정밀 설정)
        self.sw_1f_sc_1 = 0
        self.sw_1f_temp_ofset_p_1 = 0
        self.sw_1f_temp_ofset_n_1 = 0
        self.sw_1f_humi_ofset_p_1 = 0
        self.sw_1f_humi_ofset_n_1 = 0
        self.sw_1f_ws_ofset_p_1 = 0
        self.sw_1f_ws_ofset_n_1 = 0
        self.sw_1f_max_ws_1 = 0

        # 2f (좌측)/우측
        # (left_right) 좌측/우측
        # temperature row (온도)
        self.sw_2f_s1_temp_1 = 0
        self.sw_2f_s2_temp_1 = 0
        self.sw_2f_s3_temp_1 = 0
        self.sw_2f_s4_temp_1 = 0
        self.sw_2f_s5_temp_1 = 0
        self.sw_2f_s6_temp_1 = 0
        # Humidity row (습도)
        self.sw_2f_s1_humi_1 = 0
        self.sw_2f_s2_humi_1 = 0
        self.sw_2f_s3_humi_1 = 0
        self.sw_2f_s4_humi_1 = 0
        self.sw_2f_s5_humi_1 = 0
        self.sw_2f_s6_humi_1 = 0
        # environment out wind speed (외부 풍속)
        self.sw_2f_s1_eows_1 = 0
        self.sw_2f_s2_eows_1 = 0
        self.sw_2f_s3_eows_1 = 0
        self.sw_2f_s4_eows_1 = 0
        self.sw_2f_s5_eows_1 = 0
        self.sw_2f_s6_eows_1 = 0
        # start time (시작 시간)
        # minutes(분)
        self.sw_2f_s1_sm_1 = 0
        self.sw_2f_s2_sm_1 = 0
        self.sw_2f_s3_sm_1 = 0
        self.sw_2f_s4_sm_1 = 0
        self.sw_2f_s5_sm_1 = 0
        self.sw_2f_s6_sm_1 = 0
        # hours(시)
        self.sw_2f_s1_sh_1 = 0
        self.sw_2f_s2_sh_1 = 0
        self.sw_2f_s3_sh_1 = 0
        self.sw_2f_s4_sh_1 = 0
        self.sw_2f_s5_sh_1 = 0
        self.sw_2f_s6_sh_1 = 0
        # end time(종료 시간)
        # minutes(분)
        self.sw_2f_s1_em_1 = 0
        self.sw_2f_s2_em_1 = 0
        self.sw_2f_s3_em_1 = 0
        self.sw_2f_s4_em_1 = 0
        self.sw_2f_s5_em_1 = 0
        self.sw_2f_s6_em_1 = 0
        # hours(시)
        self.sw_2f_s1_eh_1 = 0
        self.sw_2f_s2_eh_1 = 0
        self.sw_2f_s3_eh_1 = 0
        self.sw_2f_s4_eh_1 = 0
        self.sw_2f_s5_eh_1 = 0
        self.sw_2f_s6_eh_1 = 0
        # steps row (스텝)
        self.sw_2f_s1_stp_1 = 0
        self.sw_2f_s2_stp_1 = 0
        self.sw_2f_s3_stp_1 = 0
        self.sw_2f_s4_stp_1 = 0
        self.sw_2f_s5_stp_1 = 0
        self.sw_2f_s6_stp_1 = 0
        # single input fields
        self.sw_2f_mtr_1 = 0
        self.sw_2f_max_temp_1 = 0
        # (정밀 설정)
        self.sw_2f_sc_1 = 0
        self.sw_2f_temp_ofset_p_1 = 0
        self.sw_2f_temp_ofset_n_1 = 0
        self.sw_2f_humi_ofset_p_1 = 0
        self.sw_2f_humi_ofset_n_1 = 0
        self.sw_2f_ws_ofset_p_1 = 0
        self.sw_2f_ws_ofset_n_1 = 0
        self.sw_2f_max_ws_1 = 0

        # 3f (좌측)/우측
        # (left_right) 좌측/우측
        # temperature row (온도)
        self.sw_3f_s1_temp_1 = 0
        self.sw_3f_s2_temp_1 = 0
        self.sw_3f_s3_temp_1 = 0
        self.sw_3f_s4_temp_1 = 0
        self.sw_3f_s5_temp_1 = 0
        self.sw_3f_s6_temp_1 = 0
        # Humidity row (습도)
        self.sw_3f_s1_humi_1 = 0
        self.sw_3f_s2_humi_1 = 0
        self.sw_3f_s3_humi_1 = 0
        self.sw_3f_s4_humi_1 = 0
        self.sw_3f_s5_humi_1 = 0
        self.sw_3f_s6_humi_1 = 0
        # environment out wind speed (외부 풍속)
        self.sw_3f_s1_eows_1 = 0
        self.sw_3f_s2_eows_1 = 0
        self.sw_3f_s3_eows_1 = 0
        self.sw_3f_s4_eows_1 = 0
        self.sw_3f_s5_eows_1 = 0
        self.sw_3f_s6_eows_1 = 0
        # start time (시작 시간)
        # minutes(분)
        self.sw_3f_s1_sm_1 = 0
        self.sw_3f_s2_sm_1 = 0
        self.sw_3f_s3_sm_1 = 0
        self.sw_3f_s4_sm_1 = 0
        self.sw_3f_s5_sm_1 = 0
        self.sw_3f_s6_sm_1 = 0
        # hours(시)
        self.sw_3f_s1_sh_1 = 0
        self.sw_3f_s2_sh_1 = 0
        self.sw_3f_s3_sh_1 = 0
        self.sw_3f_s4_sh_1 = 0
        self.sw_3f_s5_sh_1 = 0
        self.sw_3f_s6_sh_1 = 0
        # end time(종료 시간)
        # minutes(분)
        self.sw_3f_s1_em_1 = 0
        self.sw_3f_s2_em_1 = 0
        self.sw_3f_s3_em_1 = 0
        self.sw_3f_s4_em_1 = 0
        self.sw_3f_s5_em_1 = 0
        self.sw_3f_s6_em_1 = 0
        # hours(시)
        self.sw_3f_s1_eh_1 = 0
        self.sw_3f_s2_eh_1 = 0
        self.sw_3f_s3_eh_1 = 0
        self.sw_3f_s4_eh_1 = 0
        self.sw_3f_s5_eh_1 = 0
        self.sw_3f_s6_eh_1 = 0
        # steps row (스텝)
        self.sw_3f_s1_stp_1 = 0
        self.sw_3f_s2_stp_1 = 0
        self.sw_3f_s3_stp_1 = 0
        self.sw_3f_s4_stp_1 = 0
        self.sw_3f_s5_stp_1 = 0
        self.sw_3f_s6_stp_1 = 0
        # single input fields
        self.sw_3f_mtr_1 = 0
        self.sw_3f_max_temp_1 = 0
        # (정밀 설정)
        self.sw_3f_sc_1 = 0

        self.sw_3f_temp_ofset_p_1 = 0
        self.sw_3f_temp_ofset_n_1 = 0
        self.sw_3f_humi_ofset_p_1 = 0
        self.sw_3f_humi_ofset_n_1 = 0
        self.sw_3f_ws_ofset_p_1 = 0
        self.sw_3f_ws_ofset_n_1 = 0
        self.sw_3f_max_ws_1 = 0

        self.sw_3f_min_temp_1 = 0

        # ==========================ceiling windows (천창)    curtain
        # 1f (좌측)/우측
        # (left_right) 좌측/우측
        # temperature row (온도)
        self.cw_1f_s1_temp_1 = 0
        self.cw_1f_s2_temp_1 = 0
        self.cw_1f_s3_temp_1 = 0
        self.cw_1f_s4_temp_1 = 0
        self.cw_1f_s5_temp_1 = 0
        self.cw_1f_s6_temp_1 = 0
        # Humidity row (습도)
        self.cw_1f_s1_humi_1 = 0
        self.cw_1f_s2_humi_1 = 0
        self.cw_1f_s3_humi_1 = 0
        self.cw_1f_s4_humi_1 = 0
        self.cw_1f_s5_humi_1 = 0
        self.cw_1f_s6_humi_1 = 0
        # environment out wind speed (외부 풍속)
        self.cw_1f_s1_eows_1 = 0
        self.cw_1f_s2_eows_1 = 0
        self.cw_1f_s3_eows_1 = 0
        self.cw_1f_s4_eows_1 = 0
        self.cw_1f_s5_eows_1 = 0
        self.cw_1f_s6_eows_1 = 0
        # start time (시작 시간)
        # minutes(분)
        self.cw_1f_s1_sm_1 = 0
        self.cw_1f_s2_sm_1 = 0
        self.cw_1f_s3_sm_1 = 0
        self.cw_1f_s4_sm_1 = 0
        self.cw_1f_s5_sm_1 = 0
        self.cw_1f_s6_sm_1 = 0
        # hours(시)
        self.cw_1f_s1_sh_1 = 0
        self.cw_1f_s2_sh_1 = 0
        self.cw_1f_s3_sh_1 = 0
        self.cw_1f_s4_sh_1 = 0
        self.cw_1f_s5_sh_1 = 0
        self.cw_1f_s6_sh_1 = 0
        # end time(종료 시간)
        # minutes(분)
        self.cw_1f_s1_em_1 = 0
        self.cw_1f_s2_em_1 = 0
        self.cw_1f_s3_em_1 = 0
        self.cw_1f_s4_em_1 = 0
        self.cw_1f_s5_em_1 = 0
        self.cw_1f_s6_em_1 = 0
        # hours(시)
        self.cw_1f_s1_eh_1 = 0
        self.cw_1f_s2_eh_1 = 0
        self.cw_1f_s3_eh_1 = 0
        self.cw_1f_s4_eh_1 = 0
        self.cw_1f_s5_eh_1 = 0
        self.cw_1f_s6_eh_1 = 0
        # steps row (스텝)
        self.cw_1f_s1_stp_1 = 0
        self.cw_1f_s2_stp_1 = 0
        self.cw_1f_s3_stp_1 = 0
        self.cw_1f_s4_stp_1 = 0
        self.cw_1f_s5_stp_1 = 0
        self.cw_1f_s6_stp_1 = 0
        # single input fields
        self.cw_1f_mtr_1 = 0
        self.cw_1f_max_temp_1 = 0
        # (정밀 설정)
        self.cw_1f_sc_1 = 0

        self.cw_1f_temp_ofset_p_1 = 0
        self.cw_1f_temp_ofset_n_1 = 0
        self.cw_1f_humi_ofset_p_1 = 0
        self.cw_1f_humi_ofset_n_1 = 0
        self.cw_1f_ws_ofset_p_1 = 0
        self.cw_1f_ws_ofset_n_1 = 0
        self.cw_1f_max_ws_1 = 0

        self.cw_1f_min_temp_1 = 0
















        # # 2f (좌측)/우측
        # # (left_right) 좌측/우측
        # # temperature row (온도)
        # self.cw_2f_s1_temp_1 = 0
        # self.cw_2f_s2_temp_1 = 0
        # self.cw_2f_s3_temp_1 = 0
        # self.cw_2f_s4_temp_1 = 0
        # self.cw_2f_s5_temp_1 = 0
        # self.cw_2f_s6_temp_1 = 0
        # # Humidity row (습도)
        # self.cw_2f_s1_humi_1 = 0
        # self.cw_2f_s2_humi_1 = 0
        # self.cw_2f_s3_humi_1 = 0
        # self.cw_2f_s4_humi_1 = 0
        # self.cw_2f_s5_humi_1 = 0
        # self.cw_2f_s6_humi_1 = 0
        # # environment out wind speed (외부 풍속)
        # self.cw_2f_s1_eows_1 = 0
        # self.cw_2f_s2_eows_1 = 0
        # self.cw_2f_s3_eows_1 = 0
        # self.cw_2f_s4_eows_1 = 0
        # self.cw_2f_s5_eows_1 = 0
        # self.cw_2f_s6_eows_1 = 0
        # # start time (시작 시간)
        # # minutes(분)
        # self.cw_2f_s1_sm_1 = 0
        # self.cw_2f_s2_sm_1 = 0
        # self.cw_2f_s3_sm_1 = 0
        # self.cw_2f_s4_sm_1 = 0
        # self.cw_2f_s5_sm_1 = 0
        # self.cw_2f_s6_sm_1 = 0
        # # hours(시)
        # self.cw_2f_s1_sh_1 = 0
        # self.cw_2f_s2_sh_1 = 0
        # self.cw_2f_s3_sh_1 = 0
        # self.cw_2f_s4_sh_1 = 0
        # self.cw_2f_s5_sh_1 = 0
        # self.cw_2f_s6_sh_1 = 0
        # # end time(종료 시간)
        # # minutes(분)
        # self.cw_2f_s1_em_1 = 0
        # self.cw_2f_s2_em_1 = 0
        # self.cw_2f_s3_em_1 = 0
        # self.cw_2f_s4_em_1 = 0
        # self.cw_2f_s5_em_1 = 0
        # self.cw_2f_s6_em_1 = 0
        # # hours(시)
        # self.cw_2f_s1_eh_1 = 0
        # self.cw_2f_s2_eh_1 = 0
        # self.cw_2f_s3_eh_1 = 0
        # self.cw_2f_s4_eh_1 = 0
        # self.cw_2f_s5_eh_1 = 0
        # self.cw_2f_s6_eh_1 = 0
        # # steps row (스텝)
        # self.cw_2f_s1_stp_1 = 0
        # self.cw_2f_s2_stp_1 = 0
        # self.cw_2f_s3_stp_1 = 0
        # self.cw_2f_s4_stp_1 = 0
        # self.cw_2f_s5_stp_1 = 0
        # self.cw_2f_s6_stp_1 = 0
        # # single input fields
        # self.cw_2f_mtr_1 = 0
        # self.cw_2f_max_temp_1 = 0
        # # (정밀 설정)
        # self.cw_2f_sc_1 = 0
        # self.cw_2f_temp_ofset_p_1 = 0
        # self.cw_2f_temp_ofset_n_1 = 0
        # self.cw_2f_humi_ofset_p_1 = 0
        # self.cw_2f_humi_ofset_n_1 = 0
        # self.cw_2f_ws_ofset_p_1 = 0
        # self.cw_2f_ws_ofset_n_1 = 0
        # self.cw_2f_max_ws_1 = 0

        # self.cw_2f_min_temp_1 = 0

        # # 3f (좌측)/우측
        # # (left_right) 좌측/우측
        # # temperature row (온도)
        # self.cw_3f_s1_temp_1 = 0
        # self.cw_3f_s2_temp_1 = 0
        # self.cw_3f_s3_temp_1 = 0
        # self.cw_3f_s4_temp_1 = 0
        # self.cw_3f_s5_temp_1 = 0
        # self.cw_3f_s6_temp_1 = 0
        # # Humidity row (습도)
        # self.cw_3f_s1_humi_1 = 0
        # self.cw_3f_s2_humi_1 = 0
        # self.cw_3f_s3_humi_1 = 0
        # self.cw_3f_s4_humi_1 = 0
        # self.cw_3f_s5_humi_1 = 0
        # self.cw_3f_s6_humi_1 = 0
        # # environment out wind speed (외부 풍속)
        # self.cw_3f_s1_eows_1 = 0
        # self.cw_3f_s2_eows_1 = 0
        # self.cw_3f_s3_eows_1 = 0
        # self.cw_3f_s4_eows_1 = 0
        # self.cw_3f_s5_eows_1 = 0
        # self.cw_3f_s6_eows_1 = 0
        # # start time (시작 시간)
        # # minutes(분)
        # self.cw_3f_s1_sm_1 = 0
        # self.cw_3f_s2_sm_1 = 0
        # self.cw_3f_s3_sm_1 = 0
        # self.cw_3f_s4_sm_1 = 0
        # self.cw_3f_s5_sm_1 = 0
        # self.cw_3f_s6_sm_1 = 0
        # # hours(시)
        # self.cw_3f_s1_sh_1 = 0
        # self.cw_3f_s2_sh_1 = 0
        # self.cw_3f_s3_sh_1 = 0
        # self.cw_3f_s4_sh_1 = 0
        # self.cw_3f_s5_sh_1 = 0
        # self.cw_3f_s6_sh_1 = 0
        # # end time(종료 시간)
        # # minutes(분)
        # self.cw_3f_s1_em_1 = 0
        # self.cw_3f_s2_em_1 = 0
        # self.cw_3f_s3_em_1 = 0
        # self.cw_3f_s4_em_1 = 0
        # self.cw_3f_s5_em_1 = 0
        # self.cw_3f_s6_em_1 = 0
        # # hours(시)
        # self.cw_3f_s1_eh_1 = 0
        # self.cw_3f_s2_eh_1 = 0
        # self.cw_3f_s3_eh_1 = 0
        # self.cw_3f_s4_eh_1 = 0
        # self.cw_3f_s5_eh_1 = 0
        # self.cw_3f_s6_eh_1 = 0
        # # steps row (스텝)
        # self.cw_3f_s1_stp_1 = 0
        # self.cw_3f_s2_stp_1 = 0
        # self.cw_3f_s3_stp_1 = 0
        # self.cw_3f_s4_stp_1 = 0
        # self.cw_3f_s5_stp_1 = 0
        # self.cw_3f_s6_stp_1 = 0
        # # single input fields
        # self.cw_3f_mtr_1 = 0
        # self.cw_3f_max_temp_1 = 0
        # # (정밀 설정)
        # self.cw_3f_sc_1 = 0
        # self.cw_3f_temp_ofset_p_1 = 0
        # self.cw_3f_temp_ofset_n_1 = 0
        # self.cw_3f_humi_ofset_p_1 = 0
        # self.cw_3f_humi_ofset_n_1 = 0
        # self.cw_3f_ws_ofset_p_1 = 0
        # self.cw_3f_ws_ofset_n_1 = 0
        # self.cw_3f_max_ws_1 = 0

        # self.cw_3f_min_temp_1 = 0



        

        # ===============================================================AC Actuators
        # ================================= 유동팬 1
        # fan hatching rate (부화율)
        self.cf_01_s1_spd_1 = 0
        self.cf_01_s2_spd_1 = 0
        self.cf_01_s3_spd_1 = 0
        self.cf_01_s4_spd_1 = 0
        self.cf_01_s5_spd_1 = 0
        self.cf_01_s6_spd_1 = 0
        # temperature row   (온도)
        self.cf_01_s1_temp_1 = 0
        self.cf_01_s2_temp_1 = 0
        self.cf_01_s3_temp_1 = 0
        self.cf_01_s4_temp_1 = 0
        self.cf_01_s5_temp_1 = 0
        self.cf_01_s6_temp_1 = 0
        # Humidity row (습도)
        self.cf_01_s1_humi_1 = 0
        self.cf_01_s2_humi_1 = 0
        self.cf_01_s3_humi_1 = 0
        self.cf_01_s4_humi_1 = 0
        self.cf_01_s5_humi_1 = 0
        self.cf_01_s6_humi_1 = 0

        # start time (시작 시간)
        # minutes
        self.cf_01_s1_sm_1 = 0
        self.cf_01_s2_sm_1 = 0
        self.cf_01_s3_sm_1 = 0
        self.cf_01_s4_sm_1 = 0
        self.cf_01_s5_sm_1 = 0
        self.cf_01_s6_sm_1 = 0
        # hours
        self.cf_01_s1_sh_1 = 0
        self.cf_01_s2_sh_1 = 0
        self.cf_01_s3_sh_1 = 0
        self.cf_01_s4_sh_1 = 0
        self.cf_01_s5_sh_1 = 0
        self.cf_01_s6_sh_1 = 0
        # end time (종료 시간)
        # minutes
        self.cf_01_s1_em_1 = 0
        self.cf_01_s2_em_1 = 0
        self.cf_01_s3_em_1 = 0
        self.cf_01_s4_em_1 = 0
        self.cf_01_s5_em_1 = 0
        self.cf_01_s6_em_1 = 0
        # hours
        self.cf_01_s1_eh_1 = 0
        self.cf_01_s2_eh_1 = 0
        self.cf_01_s3_eh_1 = 0
        self.cf_01_s4_eh_1 = 0
        self.cf_01_s5_eh_1 = 0
        self.cf_01_s6_eh_1 = 0
        # (정밀 설정)
        self.cf_01_temp_ofset_1 = 0
        self.cf_01_humi_ofset_1 = 0

        self.cf_01_start_spd_1 = 0
        self.cf_01_max_temp_1 = 0

        # ===================================== 유동팬 2
        # # fan hatching rate (부화율)
        # self.cf_02_s1_spd_1 = 0
        # self.cf_02_s2_spd_1 = 0
        # self.cf_02_s3_spd_1 = 0
        # self.cf_02_s4_spd_1 = 0
        # self.cf_02_s5_spd_1 = 0
        # self.cf_02_s6_spd_1 = 0
        # # temperature row   (온도)
        # self.cf_02_s1_temp_1 = 0
        # self.cf_02_s2_temp_1 = 0
        # self.cf_02_s3_temp_1 = 0
        # self.cf_02_s4_temp_1 = 0
        # self.cf_02_s5_temp_1 = 0
        # self.cf_02_s6_temp_1 = 0
        # # Humidity row (습도)
        # self.cf_02_s1_humi_1 = 0
        # self.cf_02_s2_humi_1 = 0
        # self.cf_02_s3_humi_1 = 0
        # self.cf_02_s4_humi_1 = 0
        # self.cf_02_s5_humi_1 = 0
        # self.cf_02_s6_humi_1 = 0

        # # start time (시작 시간)
        # # minutes
        # self.cf_02_s1_sm_1 = 0
        # self.cf_02_s2_sm_1 = 0
        # self.cf_02_s3_sm_1 = 0
        # self.cf_02_s4_sm_1 = 0
        # self.cf_02_s5_sm_1 = 0
        # self.cf_02_s6_sm_1 = 0
        # # hours
        # self.cf_02_s1_sh_1 = 0
        # self.cf_02_s2_sh_1 = 0
        # self.cf_02_s3_sh_1 = 0
        # self.cf_02_s4_sh_1 = 0
        # self.cf_02_s5_sh_1 = 0
        # self.cf_02_s6_sh_1 = 0
        # # end time (종료 시간)
        # # minutes
        # self.cf_02_s1_em_1 = 0
        # self.cf_02_s2_em_1 = 0
        # self.cf_02_s3_em_1 = 0
        # self.cf_02_s4_em_1 = 0
        # self.cf_02_s5_em_1 = 0
        # self.cf_02_s6_em_1 = 0
        # # hours
        # self.cf_02_s1_eh_1 = 0
        # self.cf_02_s2_eh_1 = 0
        # self.cf_02_s3_eh_1 = 0
        # self.cf_02_s4_eh_1 = 0
        # self.cf_02_s5_eh_1 = 0
        # self.cf_02_s6_eh_1 = 0
        # # (정밀 설정)
        # self.cf_02_temp_ofset_1 = 0
        # self.cf_02_humi_ofset_1 = 0

        # self.cf_02_start_spd_1 = 0
        # self.cf_02_max_temp_1 = 0

        # =======================================배기팬
        # temperature row   (온도)
        self.ef_s1_temp_1 = 0
        self.ef_s2_temp_1 = 0
        self.ef_s3_temp_1 = 0
        self.ef_s4_temp_1 = 0
        self.ef_s5_temp_1 = 0
        self.ef_s6_temp_1 = 0
        # Humidity row (습도)
        self.ef_s1_humi_1 = 0
        self.ef_s2_humi_1 = 0
        self.ef_s3_humi_1 = 0
        self.ef_s4_humi_1 = 0
        self.ef_s5_humi_1 = 0
        self.ef_s6_humi_1 = 0
        # start time (시작 시간)
        # # minutes
        self.ef_s1_sm_1 = 0
        self.ef_s2_sm_1 = 0
        self.ef_s3_sm_1 = 0
        self.ef_s4_sm_1 = 0
        self.ef_s5_sm_1 = 0
        self.ef_s6_sm_1 = 0
        # hours
        self.ef_s1_sh_1 = 0
        self.ef_s2_sh_1 = 0
        self.ef_s3_sh_1 = 0
        self.ef_s4_sh_1 = 0
        self.ef_s5_sh_1 = 0
        self.ef_s6_sh_1 = 0
        # end time (종료 시간)
        # # minutes
        self.ef_s1_em_1 = 0
        self.ef_s2_em_1 = 0
        self.ef_s3_em_1 = 0
        self.ef_s4_em_1 = 0
        self.ef_s5_em_1 = 0
        self.ef_s6_em_1 = 0
        # hours
        self.ef_s1_eh_1 = 0
        self.ef_s2_eh_1 = 0
        self.ef_s3_eh_1 = 0
        self.ef_s4_eh_1 = 0
        self.ef_s5_eh_1 = 0
        self.ef_s6_eh_1 = 0
        # 정밀 설정
        self.ef_temp_ofset_1 = 0
        self.ef_humi_ofset_1 = 0

      

        # # 난방기
        # # 냉방기

        # # -----------------------------------  sensor  variable
        # self. envin_temp_r = 0

        # ---- envirment out sensor ID(외부 ​​환경 센서)
        self.envout_temp_1 = 0   # (외부 온도)
        self.envout_humi_1 = 0  # D1,  # (외부 습도)
        self.envout_light_intensity_1 = 0   # (외부 일사)
        self.rain_status_1 = 0   # (강우 감지)
        self.envout_rf_1 = 0   # (강수량)
        self.envout_wd_1 = 0   # (외부 풍향)
        self.envout_ws_1 = 0   # (외부 풍속)

        # ---- envirment in #(​환경내부)
        self.envin_temp_1 = 0   # (온도)
        self.envin_humi_1 = 0   # (상대습도)
        self.envin_co2_1 = 0   # (CO2)
        self.envin_hd_1 = 0   # (HD)
        self.envin_vpd_1 = 0   # (VPD)
        self.envin_light_intensity_1 = 0   # (광량)

        self.envin_abs_humi_1 = 0   # (절대습도)
        self.envin_dp_1 = 0   # (이슬점)
        self.envin_at_1 = 0   # (적산온도)
        self.envin_cli_1 = 0   # (누적광량)

        # ---- soil  #(배지)
        self.soil_temp_1 = 0   # (온도)
        self.soil_moisture_1 = 0   # (습도)
        self.soil_ec_1 = 0   # (EC)
        self.soil_ph_1 = 0   # (PH)

        # ---- waste/drain (배액)
        self.waste_ec_1 = 0   # (EC)
        self.waste_ph_1 = 0   # (PH)
        self.waste_dl_1 = 0   # (유량)

        # cloud rtc for the api

        self.cld_hour = 0
        self.cld_min = 0
        self.cld_sec = 0

        self.c_hour_1 = 0
        self.c_min_1 = 0

        # cumulative light
        self.buffer_lgt_1 = []
        # accumulated temp
        self.temp_max_1 = 0
        self.temp_min_1 = 0

        self.Tbase_1 = 5  # strawberry
