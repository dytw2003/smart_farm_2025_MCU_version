import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import sw_cw_rn_control
# change for the other house
# _1"
# _1,
# _1)


# async def sw_cw_rn_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n,  (9)
# step, scan, temp_thresh,  env_in_temp, rain_max, rain, wind_max, wind, (8)
#  c_hour, c_min, o_hour, o_min, cl_hour, cl_min,  at_btn, rain_btn, pin_btn, (9)
#  cl_flag, o_flag, cl_flg_n, o_flg_n, indi, indi_stat,  hw_slt_swtch):    (7)  total = 33


async def sw_1f_lt_control(var, gpio):
    while True:
        print('----------------------------------------------left')

        # setting 1(_s1_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s1_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s1_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s1_sh_1), int(var.sw_1f_s1_sm_1), int(
            var.sw_1f_s1_eh_1), int(var.sw_1f_s1_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 2(_s2_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s2_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s2_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s2_sh_1), int(var.sw_1f_s2_sm_1), int(
            var.sw_1f_s2_eh_1), int(var.sw_1f_s2_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 3(_s3_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s3_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s3_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s3_sh_1), int(var.sw_1f_s3_sm_1), int(
            var.sw_1f_s3_eh_1), int(var.sw_1f_s3_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 4(_s4_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s4_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s4_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s4_sh_1), int(var.sw_1f_s4_sm_1), int(
            var.sw_1f_s4_eh_1), int(var.sw_1f_s4_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 5(_s5_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s5_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s5_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s5_sh_1), int(var.sw_1f_s5_sm_1), int(
            var.sw_1f_s5_eh_1), int(var.sw_1f_s5_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 6(_s6_)
        await sw_cw_rn_control(var, gpio, "sw_1fl_1", "sw_1fl_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fl_o_runt_1), int(var.sw_1fl_cl_runt_1), "sw_1fl_o_runt_1", "sw_1fl_cl_runt_1",
                               int(var.sw_1f_s6_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s6_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s6_sh_1), int(var.sw_1f_s6_sm_1), int(
            var.sw_1f_s6_eh_1), int(var.sw_1f_s6_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_lbtn_1,
            var.sw_1fl_cl_flg_1, var.sw_1fl_o_flg_1, "sw_1fl_cl_flg_1", "sw_1fl_o_flg_1", var.sw_1fl_atflg_1, "sw_1fl_atflg_1", "sw_1fl_oc_1", "sw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


async def sw_1f_rt_control(var, gpio):
    while True:
        print("-------------------------------------------------right")

        # setting 1(_s1_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s1_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s1_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s1_sh_1), int(var.sw_1f_s1_sm_1), int(
            var.sw_1f_s1_eh_1), int(var.sw_1f_s1_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 2(_s2_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s2_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s2_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s2_sh_1), int(var.sw_1f_s2_sm_1), int(
            var.sw_1f_s2_eh_1), int(var.sw_1f_s2_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 3(_s3_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s3_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s3_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s3_sh_1), int(var.sw_1f_s3_sm_1), int(
            var.sw_1f_s3_eh_1), int(var.sw_1f_s3_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 4(_s4_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s4_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s4_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s4_sh_1), int(var.sw_1f_s4_sm_1), int(
            var.sw_1f_s4_eh_1), int(var.sw_1f_s4_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 5(_s5_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s5_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s5_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s5_sh_1), int(var.sw_1f_s5_sm_1), int(
            var.sw_1f_s5_eh_1), int(var.sw_1f_s5_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 6(_s6_)
        await sw_cw_rn_control(var, gpio, "sw_1fr_1", "sw_1fr_c_1", int(var.sw_1f_mtr_1), int(var.sw_1fr_o_runt_1), int(var.sw_1fr_cl_runt_1), "sw_1fr_o_runt_1", "sw_1fr_cl_runt_1",
                               int(var.sw_1f_s6_stp_1), int(var.sw_1f_sc_1), int(var.sw_1f_s6_temp_1),  int(var.envin_temp_1), int(
            var.sw_1f_max_temp_1), int(var.rain_status_1), int(var.sw_1f_max_ws_1), int(var.envout_ws_1),
            int(var.c_hour_1), int(var.c_min_1), int(var.sw_1f_s6_sh_1), int(var.sw_1f_s6_sm_1), int(
            var.sw_1f_s6_eh_1), int(var.sw_1f_s6_em_1), var.sw_1f_ambtn_1, var.sw_1f_rnbtn_1, var.sw_1f_rbtn_1,
            var.sw_1fr_cl_flg_1, var.sw_1fr_o_flg_1, "sw_1fr_cl_flg_1", "sw_1fr_o_flg_1", var.sw_1fr_atflg_1, "sw_1fr_atflg_1", "sw_1fr_oc_1", "sw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)
