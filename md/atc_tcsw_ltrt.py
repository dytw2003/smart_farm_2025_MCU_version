import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import tc_vt_wind_control
# change for the other house
# _1"
# _1,
# _1)
# _1_flg

# tc_vt_wind_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, 
                    # step, scan,  env_in_temp, low_temp_thresh, wind, wind_thresh,
                    #  c_hour, c_min, o_hour, o_min, cl_hour, cl_min,
                    #  at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n, indi, indi_stat,  hw_slt_swtch):


async def tcvt_lt_control(var, gpio):
    while True:

        # setting 1(_s1_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s1_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s1_sh_1), int(var.sw_3f_s1_sm_1), int(  var.sw_3f_s1_eh_1), int(var.sw_3f_s1_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s2_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s2_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s2_sh_1), int(var.sw_3f_s2_sm_1), int(  var.sw_3f_s2_eh_1), int(var.sw_3f_s2_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s3_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s3_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s3_sh_1), int(var.sw_3f_s3_sm_1), int(  var.sw_3f_s3_eh_1), int(var.sw_3f_s3_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s4_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s4_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s4_sh_1), int(var.sw_3f_s4_sm_1), int(  var.sw_3f_s4_eh_1), int(var.sw_3f_s4_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s5_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s5_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s5_sh_1), int(var.sw_3f_s5_sm_1), int(  var.sw_3f_s5_eh_1), int(var.sw_3f_s5_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s6_)
        await tc_vt_wind_control(var, gpio, "sw_3fl_1", "sw_3fl_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fl_o_runt_1), int(var.sw_3fl_cl_runt_1), "sw_3fl_o_runt_1", "sw_3fl_cl_runt_1",
                            int(var.sw_3f_s6_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s6_sh_1), int(var.sw_3f_s6_sm_1), int(  var.sw_3f_s6_eh_1), int(var.sw_3f_s6_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_lbtn_1, var.sw_3fl_cl_flg_1, var.sw_3fl_o_flg_1, "sw_3fl_cl_flg_1", "sw_3fl_o_flg_1",var.sw_3fl_atflg_1, "sw_3fl_atflg_1", "sw_3fl_oc_1", "sw_3fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

       

async def tcvt_rt_control(var, gpio):
    while True:

        # setting 1(_s1_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s1_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s1_sh_1), int(var.sw_3f_s1_sm_1), int(  var.sw_3f_s1_eh_1), int(var.sw_3f_s1_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s2_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s2_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s2_sh_1), int(var.sw_3f_s2_sm_1), int(  var.sw_3f_s2_eh_1), int(var.sw_3f_s2_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s3_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s3_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s3_sh_1), int(var.sw_3f_s3_sm_1), int(  var.sw_3f_s3_eh_1), int(var.sw_3f_s3_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s4_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s4_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s4_sh_1), int(var.sw_3f_s4_sm_1), int(  var.sw_3f_s4_eh_1), int(var.sw_3f_s4_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s5_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s5_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s5_sh_1), int(var.sw_3f_s5_sm_1), int(  var.sw_3f_s5_eh_1), int(var.sw_3f_s5_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s6_)
        await tc_vt_wind_control(var, gpio, "sw_3fr_1", "sw_3fr_c_1", int(var.sw_3f_mtr_1), int(var.sw_3fr_o_runt_1), int(var.sw_3fr_cl_runt_1), "sw_3fr_o_runt_1", "sw_3fr_cl_runt_1",
                            int(var.sw_3f_s6_stp_1), int(var.sw_3f_sc_1), int(var.envin_temp_1), int(var.cw_1f_min_temp_1), int(var.envout_ws_1), int(var.sw_3f_max_ws_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_3f_s6_sh_1), int(var.sw_3f_s6_sm_1), int(  var.sw_3f_s6_eh_1), int(var.sw_3f_s6_em_1),
                            var.sw_3f_ambtn_1,  var.sw_3f_rbtn_1, var.sw_3fr_cl_flg_1, var.sw_3fr_o_flg_1, "sw_3fr_cl_flg_1", "sw_3fr_o_flg_1",var.sw_3fr_atflg_1, "sw_3fr_atflg_1", "sw_3fr_oc_1", "sw_3fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)
