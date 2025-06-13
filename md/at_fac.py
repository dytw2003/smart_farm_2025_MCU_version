import uasyncio as asyncio  # Import asyncio at the top
from md.mnsf import mn_signal
# Change For the Other House
# _1

from md.mnsf import mn_signal
# Helper function to turn a device on

from md.api import send_status_to_server_db, device_status_ac


async def turn_on_device(var, gpio, pin, indi, condition):
    gpio.turn_on_pins(pin)
    print(f"Device ON: {pin}")
    if getattr(var, indi) != "RUN":
        await send_status_to_server_db(device_status_ac(pin, "RUN", condition))
    setattr(var, indi, "RUN")


async def turn_off_device(var, gpio, pin, indi, condition):
    gpio.turn_off_pins(pin)

    print(f"Device OFF: {pin}")
    if getattr(var, indi) != "STOP":
        await send_status_to_server_db(device_status_ac(pin, "STOP", condition))
    setattr(var, indi, "STOP")


async def handle_time_based_control_multiple_ac(var, gpio, pin, o_time, cl_time, c_time, indi):
    condition = "time"
    if c_time >= o_time and c_time < cl_time:
        await turn_on_device(var, gpio, pin, indi, condition)
        print("[MULTIPLE] device --[ON]")
    elif c_time == cl_time:
        await turn_off_device(var, gpio, pin, indi, condition)
        print("[MULTIPLE] device --[OFF]")
    else:
        print("[MULTIPLE] condition Not Match--[NONE]")


async def handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi):
    condition = "temp&humi"
    if (temp_thresh > 0 and c_temp >= temp_thresh) or (humi_thresh > 0 and c_humi >= humi_thresh):
        await turn_on_device(var, gpio, pin, indi, condition)
        print(
            f"[TEMP] ------------device --[ON]----Temp:{c_temp} Humidity:{c_humi} Threshold Temp:{temp_thresh} Humidity:{humi_thresh}")
    else:
        await turn_off_device(var, gpio, pin, indi, condition)
        print(
            f"[TEMP] device --[OFF]-------Temp:{c_temp} Humidity:{c_humi} Threshold Temp:{temp_thresh} Humidity:{humi_thresh}")


async def handle_time_based_control(var, gpio, pin, o_hour, o_min, cl_hour, cl_min, c_hour, c_min, indi, at_btn, hw_slt_switch):

    if hw_slt_switch == "at":
        if at_btn == "on" or at_btn == "ON":
            await handle_time_based_control_multiple_ac(var, gpio, pin, (o_hour, o_min),  (cl_hour, cl_min), (c_hour, c_min), indi)
        elif (at_btn == "off" or at_btn == "OFF") and getattr(var, indi) is not None:
            await turn_off_device(var, gpio, pin, indi)
            setattr(var, indi, None)
    elif hw_slt_switch == "mn":
        await mn_signal(gpio, var)


# ac_ctrl_func_time_temp_humi(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh,
#                             c_hour, c_min, o_hour, o_min, cl_hour, cl_min, indi,
#                              at_btn,  hw_slt_switch)
# Fan control function: supports temperature-only, time-only, or combined control
async def ac_ctrl_func_time_temp_humi(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, indi, at_btn, hw_slt_switch):

    open_time = False
    close_time = False
# open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")
    if hw_slt_switch == "at":
        if at_btn == "on" or at_btn == "ON":
            # time based control
            if temp_thresh == 0 and humi_thresh == 0:
                if open_time and close_time:
                    print("[TIME ONLY]")
                    await handle_time_based_control_multiple_ac(var, gpio, pin, (o_hour, o_min),  (cl_hour, cl_min), (c_hour, c_min), indi)
                else:
                    print("[MULTIPLE] condition Not Match--[NONE]")
            else:
                # time and sensor sensor based control
                if c_hour >= o_hour and c_hour <= cl_hour:
                    print("[WITH IN INTERVAL]")
                    if c_hour == o_hour:
                        if c_min >= o_min:
                            if c_hour < cl_hour:
                                print("[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                await handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi)
                            elif c_hour == cl_hour:
                                if c_min < cl_min:
                                    print(
                                        "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                    await handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi)
                    elif c_hour > o_hour:
                        if c_hour < cl_hour:
                            print("[HOUR DIFFERENCE]")
                            await handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi)
                        elif c_hour == cl_hour:
                            if c_min < cl_min:
                                print("[MINUTE DIFFERENCE]")
                                await handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi)
                    else:
                        print(
                            "[NOT OPERATE] not in the time interval")
                else:
                    condition = "time"
                    # print(
                    #     f"[TEMPERATRE ONLY CONTROL] open Time:{open_time} || close Time:{close_time} ")
                    # await handle_temp_humi_based_control(var, gpio, pin, c_temp, temp_thresh, c_humi, humi_thresh, indi)
                    print("[OFF CONTROL] not in the time interval")
                    await turn_off_device(var, gpio, pin, indi, condition)
        elif (at_btn == "off" or at_btn == "OFF") and getattr(var, indi) is not None:
            gpio.turn_off_pins(pin)
            setattr(var, indi, None)
    elif hw_slt_switch == "mn":
        await mn_signal(gpio, var)


async def fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi):
    condition = "humidity"
    status = getattr(var, indi, None)
    if c_humi < (humi_thresh - humi_min_ofset):

        await turn_on_device(var, gpio, pin, indi, condition)
        print("[FOG] device --[ON]")
        await asyncio.sleep(run_time)
        await turn_off_device(var, gpio, pin, indi, condition)
        print("[FOG] device --[OFF]")
        await asyncio.sleep(wait_time)
    elif status == "RUN" and (c_humi > (humi_max_ofset + humi_thresh)):
        await turn_off_device(var, gpio, pin, indi, condition)
        print(f"------------------{status}-------- device --[OFF]---------")
    else:
        print("[FOG] device NO condition Match--")


async def ac_ctrl_fog(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, c_hour, c_min, o_hour, o_min,  cl_hour, cl_min, indi, at_btn, hw_slt_switch):

    open_time = False
    close_time = False
# open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")
    if hw_slt_switch == "at":
        if at_btn == "on" or at_btn == "ON":
            # time based control
            if humi_thresh == 0:
                if open_time and close_time:
                    print("[TIME ONLY]")
                    await handle_time_based_control_multiple_ac(var, gpio, pin, (o_hour, o_min),  (cl_hour, cl_min), (c_hour, c_min), indi)
                else:
                    print("[MULTIPLE] condition Not Match--[NONE]")
            elif humi_thresh > 0:
                # time and sensor sensor based control
                if c_hour >= o_hour and c_hour <= cl_hour:
                    print("[WITH IN INTERVAL]")
                    if c_hour == o_hour:
                        if c_min >= o_min:
                            if c_hour < cl_hour:
                                print("[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                await fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi)
                            elif c_hour == cl_hour:
                                if c_min < cl_min:
                                    print(
                                        "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                    await fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi)
                    elif c_hour > o_hour:
                        if c_hour < cl_hour:
                            print("[HOUR DIFFERENCE]")
                            await fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi)
                        elif c_hour == cl_hour:
                            if c_min < cl_min:
                                print("[MINUTE DIFFERENCE]")
                                await fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi)
                    else:
                        print(
                            "[NOT OPERATE] not in the time interval")
                else:
                    print(
                        f"[TEMPERATRE ONLY CONTROL] open Time:{open_time} || close Time:{close_time} ")
                    # await fog_logic_func(var, gpio, pin, c_humi, humi_thresh, run_time, wait_time, humi_max_ofset, humi_min_ofset, indi)
        elif at_btn == "off" or at_btn == "OFF" and getattr(var, indi) is not None:
            gpio.turn_off_pins(pin)
            setattr(var, indi, None)
    elif hw_slt_switch == "mn":
        await mn_signal(gpio, var)


# ===================================================================================================================================== co2 control


async def co2_control_logic(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, envin_co2, co2_thresh, min_temp_run_flg, min_temp_run_flg_n):
    print("co2 control system")
    if not min_temp_run_flg and envin_temp <= (min_temp_set - min_temp_neg_offset):
        condition = "Min_Temp"
        print(
            "-----min_temp_set:{min_temp_set} envin_temp:{envin_temp} ------- lets activate the co2")
        await turn_on_device(var, gpio, pin, indi, condition)
        setattr(var, min_temp_run_flg_n, True)

    elif min_temp_run_flg and envin_temp >= (min_temp_set + min_temp_pos_offset):
        condition = "Min_Temp"
        await turn_off_device(var, gpio, pin, indi, condition)
        setattr(var, min_temp_run_flg_n, False)

    elif (min_temp_set < envin_temp < max_temp_set) and not min_temp_run_flg:
        condition = "Co2"
        print("-checking condition for the co2 temperature is in range")
        if envin_co2 != 0:
            if envin_co2 <= (co2_thresh - co2_neg_offset):
                await turn_on_device(var, gpio, pin, indi, condition)
            elif envin_co2 >= (co2_thresh + co2_pos_offset):
                await turn_off_device(var, gpio, pin, indi, condition)
        else:
            print(
                f"-----co2 ----- senosor in not working please check-----co2 seonsor:{envin_co2}------ and co2 threshold:{co2_thresh}-------")
    elif envin_temp >= max_temp_set:
        condition = "Max_Temp"
        print(
            f"------------max_temp_set:{max_temp_set} envin_temp:{envin_temp} ------------------- lets OFFFFF the co2")
        await turn_off_device(var, gpio, pin, indi, condition)


async def Handle_co2_time_threshold_based_control(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset,  envin_co2, co2_thresh, o_hour, o_min, cl_hour, cl_min, c_hour, c_min, min_temp_run_flg, min_temp_run_flg_n):

    if c_hour >= o_hour and c_hour <= cl_hour:
        print("[WITH IN INTERVAL]")
        if c_hour == o_hour:
            if c_min >= o_min:
                if c_hour < cl_hour:
                    print("[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                    await co2_control_logic(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, envin_co2, co2_thresh, min_temp_run_flg, min_temp_run_flg_n)
                elif c_hour == cl_hour:
                    if c_min < cl_min:
                        print(
                            "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                        await co2_control_logic(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, envin_co2, co2_thresh, min_temp_run_flg, min_temp_run_flg_n)
        elif c_hour > o_hour:
            if c_hour < cl_hour:
                print("[HOUR DIFFERENCE]")
                await co2_control_logic(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, envin_co2, co2_thresh, min_temp_run_flg, min_temp_run_flg_n)
            elif c_hour == cl_hour:
                if c_min < cl_min:
                    print("[MINUTE DIFFERENCE]")
                    await co2_control_logic(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, envin_co2, co2_thresh, min_temp_run_flg, min_temp_run_flg_n)
        else:
            print(
                "[NOT OPERATE] not in the time interval")


async def co2_ctrl_func(var, gpio, pin,  envin_temp, max_temp_set, min_temp_set, envin_co2, co2_thresh, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn,  min_temp_run_flg, min_temp_run_flg_n, indi, hw_slt_switch):

    c_time = (c_hour, c_min)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)

    if hw_slt_switch == "at":
        # print("----------------AUTO MOD FAN CONTROL FUNCTION  mode active")
        if at_btn == "on" or at_btn == "ON":
            print(
                f"------------min_temp_set:{min_temp_set} max_temp_set:{max_temp_set} co2_thresh:{co2_thresh}")
            if (min_temp_set, max_temp_set, co2_thresh) == (0, 0, 0):
                print("---------- all values are time based co2 control")
                # await any_device_time_based_control(var, gpio, pin, am_flag, am_flag_n, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn)
                await handle_time_based_control_multiple_ac(var, gpio, pin, o_time, cl_time, c_time, indi)

                # check the miniumun temperature only first
            elif envin_temp != 0 and (min_temp_set, max_temp_set, co2_thresh) != (0, 0, 0):
                print(
                    f"---------- all values are time based co2 control {envin_temp} {min_temp_set} {max_temp_set} {co2_thresh}")
                await Handle_co2_time_threshold_based_control(var, gpio, pin, indi, envin_temp, max_temp_set, min_temp_set, min_temp_neg_offset, min_temp_pos_offset, co2_neg_offset, co2_pos_offset,  envin_co2, co2_thresh, o_hour, o_min, cl_hour, cl_min, c_hour, c_min, min_temp_run_flg, min_temp_run_flg_n)
            else:
                print(
                    f"------------sensor in not working please check-----Environment temp:{envin_temp}------ and MInimum temp:{min_temp_set} and Maximum temp:{max_temp_set} ----------co2 threshold:{co2_thresh}-----------------------")

        elif (at_btn == "off" or at_btn == "OFF") and getattr(var, indi) is not None:
            gpio.turn_off_pins(pin)
            setattr(var, indi, None)
    elif hw_slt_switch == "mn":
        # print("--------FAC------Manual mode active")
        await mn_signal(gpio, var)
