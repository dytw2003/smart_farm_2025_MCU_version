import uasyncio as asyncio  # Import asyncio at the top

from md.at_fac import handle_time_based_control, ac_ctrl_func_time_temp_humi, co2_ctrl_func, ac_ctrl_fog
# change for the other house
# _1"
# _1,
# _1)


#  ac_ctrl_func_time_temp_humi(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, indi, at_btn, hw_slt_switch):

async def cf01_fan_ctrl_auto(var, gpio):
    while True:

       # setting 1
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s1_temp_1), int(var.envin_humi_1), int(var.cf_01_s1_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s1_sh_1), int(
                                              var.cf_01_s1_sm_1), int(var.cf_01_s1_eh_1), int(var.cf_01_s1_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 2
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s2_temp_1), int(var.envin_humi_1), int(var.cf_01_s2_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s2_sh_1), int(
                                              var.cf_01_s2_sm_1), int(var.cf_01_s2_eh_1), int(var.cf_01_s2_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 3
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s3_temp_1), int(var.envin_humi_1), int(var.cf_01_s3_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s3_sh_1), int(
                                              var.cf_01_s3_sm_1), int(var.cf_01_s3_eh_1), int(var.cf_01_s3_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 4
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s4_temp_1), int(var.envin_humi_1), int(var.cf_01_s4_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s4_sh_1), int(
                                              var.cf_01_s4_sm_1), int(var.cf_01_s4_eh_1), int(var.cf_01_s4_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 5
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s5_temp_1), int(var.envin_humi_1), int(var.cf_01_s5_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s5_sh_1), int(
                                              var.cf_01_s5_sm_1), int(var.cf_01_s5_eh_1), int(var.cf_01_s5_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 6
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_01_1", int(var.envin_temp_1), int(var.cf_01_s6_temp_1), int(var.envin_humi_1), int(var.cf_01_s6_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_01_s6_sh_1), int(
                                              var.cf_01_s6_sm_1), int(var.cf_01_s6_eh_1), int(var.cf_01_s6_em_1),
                                          "cf_01_oc_1",  var.cf_01_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)


async def cf02_fan_ctrl_auto(var, gpio):
    while True:

        # setting 1
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s1_temp_1), int(var.envin_humi_1), int(var.cf_02_s1_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s1_sh_1), int(
                                              var.cf_02_s1_sm_1), int(var.cf_02_s1_eh_1), int(var.cf_02_s1_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 2
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s2_temp_1), int(var.envin_humi_1), int(var.cf_02_s2_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s2_sh_1), int(
                                              var.cf_02_s2_sm_1), int(var.cf_02_s2_eh_1), int(var.cf_02_s2_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 3
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s3_temp_1), int(var.envin_humi_1), int(var.cf_02_s3_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s3_sh_1), int(
                                              var.cf_02_s3_sm_1), int(var.cf_02_s3_eh_1), int(var.cf_02_s3_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 4
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s4_temp_1), int(var.envin_humi_1), int(var.cf_02_s4_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s4_sh_1), int(
                                              var.cf_02_s4_sm_1), int(var.cf_02_s4_eh_1), int(var.cf_02_s4_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 5
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s5_temp_1), int(var.envin_humi_1), int(var.cf_02_s5_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s5_sh_1), int(
                                              var.cf_02_s5_sm_1), int(var.cf_02_s5_eh_1), int(var.cf_02_s5_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 6
        await ac_ctrl_func_time_temp_humi(var, gpio, "cf_02_1", int(var.envin_temp_1), int(var.cf_02_s6_temp_1), int(var.envin_humi_1), int(var.cf_02_s6_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.cf_02_s6_sh_1), int(
                                              var.cf_02_s6_sm_1), int(var.cf_02_s6_eh_1), int(var.cf_02_s6_em_1),
                                          "cf_02_oc_1",  var.cf_02_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)


async def ef_fan_ctrl_auto(var, gpio):
    while True:
       # setting 1
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s1_temp_1), int(var.envin_humi_1), int(var.ef_s1_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s1_sh_1), int(
            var.ef_s1_sm_1), int(var.ef_s1_eh_1), int(var.ef_s1_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 2
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s2_temp_1), int(var.envin_humi_1), int(var.ef_s2_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s2_sh_1), int(
            var.ef_s2_sm_1), int(var.ef_s2_eh_1), int(var.ef_s2_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 3
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s3_temp_1), int(var.envin_humi_1), int(var.ef_s3_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s3_sh_1), int(
            var.ef_s3_sm_1), int(var.ef_s3_eh_1), int(var.ef_s3_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 4
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s4_temp_1), int(var.envin_humi_1), int(var.ef_s4_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s4_sh_1), int(
            var.ef_s4_sm_1), int(var.ef_s4_eh_1), int(var.ef_s4_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 5
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s5_temp_1), int(var.envin_humi_1), int(var.ef_s5_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s5_sh_1), int(
            var.ef_s5_sm_1), int(var.ef_s5_eh_1), int(var.ef_s5_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)

        # setting 6
        await ac_ctrl_func_time_temp_humi(var, gpio, "ef_1", int(var.envin_temp_1), int(var.ef_s6_temp_1), int(var.envin_humi_1), int(var.ef_s6_humi_1),
                                          int(var.c_hour_1), int(var.c_min_1), int(var.ef_s6_sh_1), int(
            var.ef_s6_sm_1), int(var.ef_s6_eh_1), int(var.ef_s6_em_1),
            "ef_oc_1",  var.ef_ambtn_1,  var.hw_switch_1)

        await asyncio.sleep(0.2)


















# async def ac_ctrl_fog(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset,
        # c_hour, c_min, o_hour, o_min, cl_hour, cl_min, indi, at_btn, hw_slt_switch):


# async def ac_ctrl_fog(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, c_hour, c_min, o_hour, o_min,  cl_hour, cl_min, indi, at_btn, hw_slt_switch)
# self.fv_ejt1_1 = 0
# self.fv_wt1_1 = 0
# async def fv_ctrl_auto(var, gpio):  # (NEED CORRECTION HERE)
#     while True:

#         # setting 1
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s1_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),

#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s1_sh_1), int(var.fv_s1_sm_1), int(var.fv_s1_eh_1), int(var.fv_s1_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)
#         # setting 2
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s2_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),
#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s2_sh_1), int(var.fv_s2_sm_1), int(var.fv_s2_eh_1), int(var.fv_s2_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)
#         # setting 3
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s3_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),
#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s3_sh_1), int(var.fv_s3_sm_1), int(var.fv_s3_eh_1), int(var.fv_s3_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)
#         # setting 4
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s4_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),
#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s4_sh_1), int(var.fv_s4_sm_1), int(var.fv_s4_eh_1), int(var.fv_s4_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)
#         # setting 5
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s5_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),
#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s5_sh_1), int(var.fv_s5_sm_1), int(var.fv_s5_eh_1), int(var.fv_s5_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)
#         # setting 6
#         await ac_ctrl_fog(var, gpio, "fv_1", int(var.envin_humi_1), int(var.fv_s6_humi_1), int(var.fv_ejt1_1), int(var.fv_wt1_1), int(var.fv_humi_ofset_n_1), int(var.fv_humi_ofset_p_1),
#                           int(var.c_hour_1), int(var.c_min_1), int(var.fv_s6_sh_1), int(var.fv_s6_sm_1), int(var.fv_s6_eh_1), int(var.fv_s6_em_1), "fv_oc_1",  var.fv_ambtn_1,  var.hw_switch_1)
#         await asyncio.sleep(0.2)


# co2_ctrl_func(var, gpio, pin,  envin_temp, max_temp_set, min_temp_set,
        #  envin_co2, co2_thresh, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset,
        #  c_hour, c_min, o_hour, o_min, cl_hour, cl_min,
        # at_btn, min_temp_run_flg, min_temp_run_flg_n, indi, hw_slt_switch):

