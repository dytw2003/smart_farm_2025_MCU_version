import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import sw_cw_control
# change for the other house
# _1"
# _1,
# _1)
# _1_flg

# async def sw_cw_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, =(9)
#  step, scan, temp_thresh,  env_in_temp,=(4)
#  c_hour, c_min, o_hour, o_min, cl_hour, cl_min,  at_btn, pin_btn, =(8)
# cl_flag, o_flag, cl_flg_n, o_flg_n, indi, indi_stat,  hw_slt_swtch)=(7)
# total = 9 + 4 + 8 + 7 = 28


async def sw_2f_lt_control(var, gpio):
    while True:

        # setting 1(_s1_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s1_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s1_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s1_sh_1), int(var.sw_2f_s1_sm_1), int(
                                var.sw_2f_s1_eh_1), int(var.sw_2f_s1_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1",var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 2(_s2_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s2_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s2_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s2_sh_1), int(var.sw_2f_s2_sm_1), int(
                                var.sw_2f_s2_eh_1), int(var.sw_2f_s2_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1",var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 3(_s3_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s3_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s3_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s3_sh_1), int(var.sw_2f_s3_sm_1), int(
                                var.sw_2f_s3_eh_1), int(var.sw_2f_s3_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1", var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 4(_s4_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s4_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s4_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s4_sh_1), int(var.sw_2f_s4_sm_1), int(
                                var.sw_2f_s4_eh_1), int(var.sw_2f_s4_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1", var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 5(_s5_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s5_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s5_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s5_sh_1), int(var.sw_2f_s5_sm_1), int(
                                var.sw_2f_s5_eh_1), int(var.sw_2f_s5_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1", var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 6(_s6_)
        await sw_cw_control(var, gpio, "sw_2fl_1", "sw_2fl_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fl_o_runt_1), int(var.sw_2fl_cl_runt_1), "sw_2fl_o_runt_1", "sw_2fl_cl_runt_1",
                            int(var.sw_2f_s6_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s6_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s6_sh_1), int(var.sw_2f_s6_sm_1), int(
                                var.sw_2f_s6_eh_1), int(var.sw_2f_s6_em_1), var.sw_2f_ambtn_1,  var.sw_2f_lbtn_1,
                            var.sw_2fl_cl_flg_1, var.sw_2fl_o_flg_1, "sw_2fl_cl_flg_1", "sw_2fl_o_flg_1",var.sw_2fl_atflg_1, "sw_2fl_atflg_1", "sw_2fl_oc_1", "sw_2fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


async def sw_2f_rt_control(var, gpio):
    while True:

        # setting 1(_s1_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s1_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s1_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s1_sh_1), int(var.sw_2f_s1_sm_1), int(
                                var.sw_2f_s1_eh_1), int(var.sw_2f_s1_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1",var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 2(_s2_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s2_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s2_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s2_sh_1), int(var.sw_2f_s2_sm_1), int(
                                var.sw_2f_s2_eh_1), int(var.sw_2f_s2_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1",var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 3(_s3_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s3_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s3_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s3_sh_1), int(var.sw_2f_s3_sm_1), int(
                                var.sw_2f_s3_eh_1), int(var.sw_2f_s3_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1", var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 4(_s4_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s4_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s4_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s4_sh_1), int(var.sw_2f_s4_sm_1), int(
                                var.sw_2f_s4_eh_1), int(var.sw_2f_s4_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1",var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 5(_s5_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s5_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s5_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s5_sh_1), int(var.sw_2f_s5_sm_1), int(
                                var.sw_2f_s5_eh_1), int(var.sw_2f_s5_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1",var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 6(_s6_)
        await sw_cw_control(var, gpio, "sw_2fr_1", "sw_2fr_c_1", int(var.sw_2f_mtr_1), int(var.sw_2fr_o_runt_1), int(var.sw_2fr_cl_runt_1), "sw_2fr_o_runt_1", "sw_2fr_cl_runt_1",
                            int(var.sw_2f_s6_stp_1), int(var.sw_2f_sc_1), int(
                                var.sw_2f_s6_temp_1),  int(var.envin_temp_1),
                            int(var.c_hour_1), int(var.c_min_1), int(var.sw_2f_s6_sh_1), int(var.sw_2f_s6_sm_1), int(
                                var.sw_2f_s6_eh_1), int(var.sw_2f_s6_em_1), var.sw_2f_ambtn_1,  var.sw_2f_rbtn_1,
                            var.sw_2fr_cl_flg_1, var.sw_2fr_o_flg_1, "sw_2fr_cl_flg_1", "sw_2fr_o_flg_1",var.sw_2fr_atflg_1, "sw_2fr_atflg_1", "sw_2fr_oc_1", "sw_2fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)
