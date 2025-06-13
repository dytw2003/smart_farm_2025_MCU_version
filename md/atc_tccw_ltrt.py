import uasyncio as asyncio  # Import asyncio at the top
from md.at_f import tc_sun_temp_control
# change for the other house
# _1"
# _1,
# _1)
# _1_flg



# async def tc_sun_temp_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, =9
                            #  step, scan,  env_in_temp, low_temp_thresh,  sun_light, sun_light_thresh, sun_data_btn,
                            #   c_hour, c_min, o_hour, o_min, cl_hour, cl_min,  =6
                            # at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n, indi, indi_stat,  hw_slt_swtch): =11
                            #  Total = 32

 

async def tccw_1fl_control(var, gpio):
    while True:

        # setting 1(_s1_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s1_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s1_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s1_sh_1), int(var.cw_1f_s1_sm_1), int( var.cw_1f_s1_eh_1), int(var.cw_1f_s1_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)
        
         # setting 1(_s2_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s2_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s2_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s2_sh_1), int(var.cw_1f_s2_sm_1), int( var.cw_1f_s2_eh_1), int(var.cw_1f_s2_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

            # setting 1(_s3_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s3_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s3_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s3_sh_1), int(var.cw_1f_s3_sm_1), int( var.cw_1f_s3_eh_1), int(var.cw_1f_s3_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


            # setting 1(_s4_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s4_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s4_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s4_sh_1), int(var.cw_1f_s4_sm_1), int( var.cw_1f_s4_eh_1), int(var.cw_1f_s4_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


            # setting 1(_s5_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s5_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s5_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s5_sh_1), int(var.cw_1f_s5_sm_1), int( var.cw_1f_s5_eh_1), int(var.cw_1f_s5_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


            # setting 1(_s6_)
        await tc_sun_temp_control(var, gpio, "cw_1fl_1", "cw_1fl_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fl_o_runt_1), int(var.cw_1fl_cl_runt_1), "cw_1fl_o_runt_1", "cw_1fl_cl_runt_1",
                                  int(var.cw_1f_s6_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s6_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s6_sh_1), int(var.cw_1f_s6_sm_1), int( var.cw_1f_s6_eh_1), int(var.cw_1f_s6_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_lbtn_1, var.cw_1fl_cl_flg_1, var.cw_1fl_o_flg_1, "cw_1fl_cl_flg_1", "cw_1fl_o_flg_1", var.cw_1fl_atflg_1, "cw_1fl_atflg_1", "cw_1fl_oc_1", "cw_1fl_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

       


async def tccw_1fr_control(var, gpio):
    while True:
        # setting 1(_s1_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s1_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s1_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s1_sh_1), int(var.cw_1f_s1_sm_1), int( var.cw_1f_s1_eh_1), int(var.cw_1f_s1_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s2_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s2_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s2_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s2_sh_1), int(var.cw_1f_s2_sm_1), int( var.cw_1f_s2_eh_1), int(var.cw_1f_s2_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)

        # setting 1(_s3_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s3_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s3_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s3_sh_1), int(var.cw_1f_s3_sm_1), int( var.cw_1f_s3_eh_1), int(var.cw_1f_s3_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s4_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s4_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s4_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s4_sh_1), int(var.cw_1f_s4_sm_1), int( var.cw_1f_s4_eh_1), int(var.cw_1f_s4_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s5_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s5_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s5_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s5_sh_1), int(var.cw_1f_s5_sm_1), int( var.cw_1f_s5_eh_1), int(var.cw_1f_s5_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)


        # setting 1(_s6_)
        await tc_sun_temp_control(var, gpio, "cw_1fr_1", "cw_1fr_c_1", int(var.cw_1f_mtr_1), int(var.cw_1fr_o_runt_1), int(var.cw_1fr_cl_runt_1), "cw_1fr_o_runt_1", "cw_1fr_cl_runt_1",
                                  int(var.cw_1f_s6_stp_1), int(var.cw_1f_sc_1), int(var.envin_temp_1), int( var.cw_1f_min_temp_1), int(var.envin_light_intensity_1),  int(var.cw_1f_s6_humi_1),var.cw_1f_li_1,
                                  int(var.c_hour_1), int(var.c_min_1), int(var.cw_1f_s6_sh_1), int(var.cw_1f_s6_sm_1), int( var.cw_1f_s6_eh_1), int(var.cw_1f_s6_em_1), 
                                    var.cw_1f_ambtn_1, var.cw_1f_rbtn_1, var.cw_1fr_cl_flg_1, var.cw_1fr_o_flg_1, "cw_1fr_cl_flg_1", "cw_1fr_o_flg_1", var.cw_1fr_atflg_1, "cw_1fr_atflg_1", "cw_1fr_oc_1", "cw_1fr_stat_1", var.hw_switch_1)
        await asyncio.sleep(0.2)