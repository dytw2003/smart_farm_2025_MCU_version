# mnsf.py

import uasyncio as asyncio

# CHANGE FOR THE OTHER HOUSE
# _1"
# _1_flg"
# mnsig_flag_1


async def mn_signal_gpio_fun(gpio, pin):
    gpio.turn_off_pins(pin)
    print(f"GPIO {pin} turned OFF----:::::----")

async def mn_signal_flg_func(var, fname):
    setattr(var, fname, False)
    print(f"FLAG {fname} turned OFF::::: {getattr(var, fname)}")
async def mn_signal_oc_func(var, fname):
    setattr(var, fname, None)
    print(f"FLAG {fname} turned OFF::::: {getattr(var, fname)}")

async def mn_signal_stat_time_func(var, fname):
    setattr(var, fname, 0)
    print(f"FLAG {fname} turned OFF::::: {getattr(var, fname)}")

async def mn_signal(gpio, var):
    # set the all the gpio pins OFF

    pins = {
        "sw_1fl_1": "",
        "sw_1fl_c_1": "",
        "sw_1fr_1": "",
        "sw_1fr_c_1": "",
        # 2f (좌측)/우측

        "sw_2fl_1": "",
        "sw_2fl_c_1": "",
        "sw_2fr_1": "",
        "sw_2fr_c_1": "",
        # 3f (좌측)/우측

        "sw_3fl_1": "",
        "sw_3fl_c_1": "",
        "sw_3fr_1": "",
        "sw_3fr_c_1": "",
        # ceiling windows (천창)
        # 1f (좌측)/우측
        "cw_1fl_1": "",
        "cw_1fl_c_1": "",
        "cw_1fr_1": "",
        "cw_1fr_c_1": "",
        # 2f (좌측)/우측
        "cw_2fl_1": "",
        "cw_2fl_c_1": "",
        "cw_2fr_1": "",
        "cw_2fr_c_1": "",
        # 3f (좌측)/우측
        "cw_3fl_1": "",
        "cw_3fl_c_1": "",
        "cw_3fr_1": "",
        "cw_3fr_c_1": "",

        # Ac Actuators
        # 유동팬 1
        "cf_01_1": "",
        # "cf_01_fwd_1": "",  # 정방향
        # "cf_01_rev_1": "",  # 역방향
        # 유동팬 2
        "cf_02_1": "",
        # "cf_02_fwd_1": "",  # 정방향
        # "cf_02_rev_1": "",  # 역방향

        "ef_1": "",  # 배기팬
        # "wc_1": "",  # 수막
        # "co2_1": "",  # CO₂
        # "fv_1": "",  # 포그밸브
        # "sl_1": "",  # 보광등
        # "if_1": "",  # 흡기팬


    }

    flags = {
        # 1f (좌측)/우측
        "sw_1fl_o_flg_1": "",
        "sw_1fl_cl_flg_1": "",
        "sw_1fr_o_flg_1": "",
        "sw_1fr_cl_flg_1": "",
        # 2f (좌측)/우측
        "sw_2fl_o_flg_1": "",
        "sw_2fl_cl_flg_1": "",
        "sw_2fr_o_flg_1": "",
        "sw_2fr_cl_flg_1": "",
        # 3f (좌측)/우측
        "sw_3fl_o_flg_1": "",
        "sw_3fl_cl_flg_1": "",
        "sw_3fr_o_flg_1": "",
        "sw_3fr_cl_flg_1": "",
        # ceiling windows (천창)
        # 1f (좌측)/우측
        "cw_1fl_o_flg_1": "",
        "cw_1fl_cl_flg_1": "",
        "cw_1fr_o_flg_1": "",
        "cw_1fr_cl_flg_1": "",
        # 2f (좌측)/우측
        "cw_2fl_o_flg_1": "",
        "cw_2fl_cl_flg_1": "",
        "cw_2fr_o_flg_1": "",
        "cw_2fr_cl_flg_1": "",
        # 3f (좌측)/우측
        "cw_3fl_o_flg_1": "",
        "cw_3fl_cl_flg_1": "",
        "cw_3fr_o_flg_1": "",
        "cw_3fr_cl_flg_1": "",


    }
    ocs = {
        "sw_1fl_oc_1": "",
        "sw_1fr_oc_1": "",

        # 2f (좌측)/우측

        "sw_2fl_oc_1": "",
        "sw_2fr_oc_1": "",

        # 3f (좌측)/우측

        "sw_3fl_oc_1": "",
        "sw_3fr_oc_1": "",

        # ceiling windows (천창)
        # 1f (좌측)/우측
        "cw_1fl_oc_1": "",
        "cw_1fr_oc_1": "",

        # 2f (좌측)/우측
        "cw_2fl_oc_1": "",
        "cw_2fr_oc_1": "",

        # 3f (좌측)/우측
        "cw_3fl_oc_1": "",
        "cw_3fr_oc_1": "",


        # ============================ AC ACTUATORS=======
        # -------------------------------------------------  flags
        # -------------------------------------------------  status
        # 유동팬 1
        "cf_01_oc_1": "",
        # 유동팬 2
        "cf_02_oc_1": "",
        "ef_oc_1": "",  # 배기팬
        "wc_oc_1": "",  # 수막
        "co2_oc_1": "",  # CO₂
        "fv_oc_1": "",  # 포그밸브
        "sl_oc_1": "",  # 보광등
        "if_oc_1": "",  # 흡기팬

        # "hu_oc_1": "",  # 난방기
        # "cu_oc_1": "",  # 냉방기


    }
    stats = {
        "sw_1fl_stat_1": "",
        "sw_1fr_stat_1": "",
        # 2f (좌측)/우측

        "sw_2fl_stat_1": "",
        "sw_2fr_stat_1": "",
        # 3f (좌측)/우측

        "sw_3fl_stat_1": "",
        "sw_3fr_stat_1": "",
        # ceiling windows (천창)
        # 1f (좌측)/우측
        "cw_1fl_stat_1": "",
        "cw_1fr_stat_1": "",
        # 2f (좌측)/우측
        "cw_2fl_stat_1": "",
        "cw_2fr_stat_1": "",
        # 3f (좌측)/우측
        "cw_3fl_stat_1": "",
        "cw_3fr_stat_1": "",


    }
    mtr_run_times = {
        "sw_1fl_o_runt_1": "",
        "sw_1fl_cl_runt_1": "",
        "sw_1fr_o_runt_1": "",
        "sw_1fr_cl_runt_1": "",
        # 2f (좌측)/우측
        "sw_2fl_o_runt_1": "",
        "sw_2fl_cl_runt_1": "",
        "sw_2fr_o_runt_1": "",
        "sw_2fr_cl_runt_1": "",
        # 3f (좌측)/우측
        "sw_3fl_o_runt_1": "",
        "sw_3fl_cl_runt_1": "",
        "sw_3fr_o_runt_1": "",
        "sw_3fr_cl_runt_1": "",
        # ceiling windows (천창)
        # 1f (좌측)/우측
        "cw_1fl_o_runt_1": "",
        "cw_1fl_cl_runt_1": "",
        "cw_1fr_o_runt_1": "",
        "cw_1fr_cl_runt_1": "",
        # 2f (좌측)/우측
        "cw_2fl_o_runt_1": "",
        "cw_2fl_cl_runt_1": "",
        "cw_2fr_o_runt_1": "",
        "cw_2fr_cl_runt_1": "",
        # 3f (좌측)/우측
        "cw_3fl_o_runt_1": "",
        "cw_3fl_cl_runt_1": "",
        "cw_3fr_o_runt_1": "",
        "cw_3fr_cl_runt_1": "",
    }

    if not var.mnsig_flag_1:

        for pin in pins:
            await mn_signal_gpio_fun(gpio, pin)       
        for flag in flags:
            await mn_signal_flg_func(var, flag)
        
        for oc in ocs:
            await mn_signal_oc_func(var,oc)

        for stat in stats:
            await mn_signal_stat_time_func(var, stat)
        
        for mtr_time in mtr_run_times:
            await mn_signal_stat_time_func(var, mtr_time)

        setattr(var, "mnsig_flag_1", True)

        print(f"ATMN FLAG  is ----I{getattr(var,
              "mnsig_flag_1")}--- AND -- MANUAL --MODE ")
    else:
        print("ATMN FLAG 1 is ----------True-------")

    await asyncio.sleep(2)
