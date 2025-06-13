import asyncio
from md.mnsf import mn_signal

from md.api import send_status_to_server_db, device_status_motor

# percentage to second converted


def step_sec(mtr_time, step_percent):
    stp_sec = round(mtr_time/100, 2)
    step = stp_sec * step_percent
    print(f"step  in second motor run time {step}")
    return int(step)
# second to percentage converter


def step_percent(mtr_time, running_time):
    stp_percent = round(running_time/mtr_time, 2)
    stp_percent = stp_percent*100
    print(f"step percent  % {stp_percent}")
    return int(stp_percent)


def run_time_update(mtr_run_sec, mtr_run_time):
    mtr_run_time = int(mtr_run_time) + int(mtr_run_sec)
    print(f"total motor run time update {mtr_run_time}")
    return mtr_run_time


async def ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition):

    if not o_flag:
        # First OFF the OPPOSITE pin(CLOSE)
        gpio.turn_off_pins(cl_pin)  # OFF the close pin
        # setattr(var, cl_pin, "off")
        setattr(var, cl_flg_n, False)  # CLOSE o_flag False
        # ON the OPEN
        gpio.turn_on_pins(o_pin)
        setattr(var, indi, "OPEN")
        # setattr(var, o_pin, "on")
        await asyncio.sleep(mtr_time)
        gpio.turn_off_pins(o_pin)
        setattr(var, indi_stat, 100)
        setattr(var, o_run_time_n, 0)
        setattr(var, cl_run_time_n, 0)
        setattr(var, o_flg_n, True)  # OPEN o_flag True
        await send_status_to_server_db(device_status_motor(o_pin, "open", 100, condition))
    else:
        print(f"OPEN o_FLAG IS TRUE:{o_flag}")


async def ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition):
    if not cl_flag:
        # First OFF the OPPOSITE pin(open)
        gpio.turn_off_pins(o_pin)  # OFF the open pin
        # setattr(var, o_pin, "off")
        setattr(var, o_flg_n, False)  # OPEN cl_flag False
        # ON the OPEN
        gpio.turn_on_pins(cl_pin)
        setattr(var, indi, "CLOSE")
        # setattr(var, cl_pin, "on")
        await asyncio.sleep(mtr_time)
        gpio.turn_off_pins(cl_pin)
        setattr(var, indi_stat, 100)
        setattr(var, o_run_time_n, 0)
        setattr(var, cl_run_time_n, 0)
        setattr(var, cl_flg_n, True)  # CLOSE cl_flag True
        await send_status_to_server_db(device_status_motor(o_pin, "close", 100, condition))

    else:
        print(f"OPEN cl_FLAG IS TRUE:{cl_flag}")


async def ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, o_run_time_n, cl_run_time_n, o_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition):
    print(f"Scan time: {scan}")
    print(f"Step: {step}")
    print(f"Motor full time: {mtr_time}")
    print(f"Open run time (current): {o_run_time}")
    print(f"Open run time (next): {o_run_time_n}")
    print(f"Open flag: {o_flag}")
    print(f"Open flag (next): {o_flg_n}")
    print(f"Close flag (next): {cl_flg_n}")
    if not o_flag:
        if int(o_run_time) < int(mtr_time):
            gpio.turn_off_pins(cl_pin)
            gpio.turn_on_pins(o_pin)
            setattr(var, indi, "open")
            step_duration = step_sec(mtr_time, step)
            await asyncio.sleep(int(step_duration))
            if o_run_time == 0:
                o_run_time = step_duration
            step_percentage = step_percent(mtr_time, o_run_time)

            setattr(var, indi_stat, step_percentage)
            gpio.turn_off_pins(o_pin)
            o_rt_val = getattr(var, o_run_time_n)
            updated_time = run_time_update(step_duration, o_rt_val)
            setattr(var, o_run_time_n, updated_time)
            cl_run_update = mtr_time-updated_time
            setattr(var, cl_run_time_n, cl_run_update)
            await send_status_to_server_db(device_status_motor(o_pin, "open", step_percentage, condition))

            await asyncio.sleep(scan)
        else:
            setattr(var, indi_stat, 100)
            setattr(var, cl_run_time_n, 0)
            setattr(var, o_flg_n, True)
            setattr(var, cl_flg_n, False)
            print(f"Motor is fully open.")
            await send_status_to_server_db(device_status_motor(o_pin, "open", 100, condition))
    else:
        print(f"-- Motor for pin {o_pin} is already open. Flag: {o_flag}")


async def ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_run_time, o_run_time_n, cl_run_time_n, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition):

    print(f"Scan time: {scan}")
    print(f"Step: {step}")
    print(f"Motor full time: {mtr_time}")
    print(f"Close run time (current): {cl_run_time}")
    print(f"Close run time (next): {cl_run_time_n}")
    print(f"Close flag: {cl_flag}")
    print(f"Open flag (next): {o_flg_n}")
    print(f"Close flag (next): {cl_flg_n}")

    if not cl_flag:
        if int(cl_run_time) < int(mtr_time):
            gpio.turn_off_pins(o_pin)
            gpio.turn_on_pins(cl_pin)
            setattr(var, indi, "close")
            step_duration = step_sec(mtr_time, step)
            print(f"Sleeping for step duration: {step_duration}")
            await asyncio.sleep(int(step_duration))
            if int(cl_run_time) == 0:
                cl_run_time = step_duration
            step_percentage = step_percent(mtr_time, cl_run_time)
            setattr(var, indi_stat, step_percentage)
            gpio.turn_off_pins(cl_pin)
            # ✅ Fix: Read previous value from var, not from string
            cl_rt_val = getattr(var, cl_run_time_n)
            updated_time = run_time_update(step_duration, cl_rt_val)
            setattr(var, cl_run_time_n, updated_time)
            o_run_update = mtr_time-updated_time
            setattr(var, o_run_time_n, o_run_update)
            # open pin is Actual pin/actuatorname
            await send_status_to_server_db(device_status_motor(o_pin, "close", step_percentage, condition))

            await asyncio.sleep(scan)
        else:
            setattr(var, indi_stat, 100)
            setattr(var, o_run_time_n, 0)
            setattr(var, cl_flg_n, True)
            setattr(var, o_flg_n, False)
            print(f"Motor is fully closed")
            # open pin is Actual pin/actuatorname
            await send_status_to_server_db(device_status_motor(o_pin, "close", 100, condition))
    else:
        print(f"Motor for pin {cl_pin} already closed. Flag: {cl_flag}")


#  temperature based control


async def handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh):
    condition = "temperature"
    if env_in_temp > temp_thresh:
        await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, o_run_time_n, cl_run_time_n, o_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition)
        print("Temperature Based Control [Open]")
    elif env_in_temp < temp_thresh:
        await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_run_time, o_run_time_n, cl_run_time_n, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition)
        print("Temperature Based Control [Close]")
    else:
        print(
            f"-------------------- temperature is matched -------------- currnet temp:{env_in_temp}=====Temperature:Threshold{temp_thresh}")

# #  P-Band temperature based control


async def handle_pband_temp_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh, pband_btn):
    if pband_btn == "on":
        if env_in_temp > temp_thresh:
            await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, o_run_time_n, cl_run_time_n, o_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
    elif env_in_temp < temp_thresh:
        await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_run_time, o_run_time_n, cl_run_time_n, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
    else:
        print(
            f"-------------------- temperature is matched -------------- currnet temp:{env_in_temp}=====Temperature:Threshold{temp_thresh}")

#  sunlight based control for the curtain


async def handle_sunlight_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, sun_light, sun_light_thresh, sun_data_btn):
    condition = "sunlight"
    if sun_data_btn == "on" or sun_data_btn == "ON":
        if sun_light_thresh > 0 and sun_light > 0:
            if sun_light > sun_light_thresh:
                await ctrl_close_stp(var, gpio, o_pin, cl_pin, mtr_time, cl_run_time, o_run_time_n, cl_run_time_n, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition)
            elif sun_light < sun_light_thresh:
                await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, o_run_time_n, cl_run_time_n, o_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition)
            else:
                print(
                    f"------ sunlight is matched --- currnet sunlight:{sun_light}=====sunlight:Threshold{sun_light_thresh}")
        else:
            print(
                f"-- sunlight is matched --- currnet sunlight:{sun_light}=====sunlight:Threshold{sun_light_thresh}")
    else:
        print(f"Sunlight button is off {sun_data_btn}")


# #  singal time based control


# async def handle_time_based_control_single(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat):
#     if o_time < cl_time:
#         if c_time >= o_time:
#             if c_time < cl_time:
#                 print("[SINGLE] Current time is within open interval. Opening motor.")
#                 await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat)
#             else:
#                 print(
#                     "[SINGLE] Current time has passed close interval. Closing motor.")
#                 ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat)
#     elif cl_time < o_time:
#         if c_time >= cl_time:
#             if c_time < o_time:
#                 print(
#                     "[SINGLE] Current time is within close-first interval. Closing motor.")
#                 ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat)
#             else:
#                 print(
#                     "[SINGLE] Current time has passed open interval. Opening motor.")
#                 await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat)
#     else:
#         print(
#             "[SINGLE] none of the above condtion match----------------time based--- No matched")


#  multiple time based control
# await handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_hour, o_min, cl_hour, cl_min,  c_hour, c_min,  cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat)


async def handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, o_run_time_n, cl_run_time_n, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat):
    condition = "time"
    if o_time < cl_time:
        if c_time >= o_time and c_time < cl_time:
            print(
                "[MULTIPLE] Current time is within open-first interval. Opening motor.")
            await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)
        elif c_time == cl_time:
            print(
                "[MULTIPLE] Current time has passed close-last interval. Closing motor.")
            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag,
                                  o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)
        else:
            print(
                "[MULTIPLE] none of the above condtion match--[open-fist]")
    elif cl_time < o_time:
        if c_time >= cl_time and c_time < o_time:
            print(
                "[MULTIPLE] Current time is within close-first interval. Closing motor.")
            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag,
                                  o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)
        elif c_time == o_time:
            print(
                "[MULTIPLE] Current time has passed open-last interval. Opening motor.")
            await ctrl_open_full(var, gpio, o_pin, cl_pin, mtr_time, o_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)
        else:
            print(
                "[MULTIPLE] none of the above condtion match--[close-fist]")
    else:
        print(" [MULTIPLE] setting doensnt match")


async def rain_func(env_in_temp,  rain_max, rain_btn, var, gpio, o_pin, cl_pin, mtr_time, o_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat):
    condition = "rain"
    # NOTE: RAIN BUTTUN IS NOT USED (need to add)
    # if rain_btn == "on" :
    # print(f"Rain Based Control [Rain:{rain_btn}]")
    if rain_max > 0 and int(env_in_temp) > int(rain_max):
        print("Raining but -- {Max Temperature is reached}")
        await ctrl_open_stp(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, o_run_time_n, cl_run_time_n, o_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, condition)
    else:
        await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag,  o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)
        print("Rain detected {Max temp NOT set}")
    # else:
    #     print(f"Rain button is off {rain_btn}")


async def wind_func(wind,  wind_thresh,  var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat):
    condition = "wind"

    if wind != 0 and wind > wind_thresh:
        await ctrl_close_stp(
            var, gpio, o_pin, cl_pin,
            mtr_time, cl_run_time, o_run_time_n,
            cl_run_time_n, cl_flag, o_flg_n, cl_flg_n,
            step, scan, indi, indi_stat, condition)
        print(f"Wind detected : {wind} > {wind_thresh}")
    elif wind != 0 and wind < wind_thresh:
        await ctrl_open_stp(
            var, gpio, o_pin, cl_pin,
            mtr_time, o_run_time, o_run_time_n,
            cl_run_time_n, o_flag, o_flg_n, cl_flg_n,
            step, scan, indi, indi_stat, condition)
        print(f"Wind detected : {wind} < {wind_thresh}")
    else:
        print(f"Error [wind sensor] : {wind} ")


async def sw_cw_rn_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, step, scan, temp_thresh,  env_in_temp, rain_max, rain, wind_max, wind, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, rain_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n,  indi, indi_stat,  hw_slt_swtch):
    # (o_hour, o_min,) (cl_hour, cl_min),(c_hour, c_min)
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    c_time = (c_hour, c_min)
    open_time = False
    close_time = False
    if mtr_time == 0:
        mtr_time = 120
    else:
        print(f"Motor run time : {mtr_time}")
    if scan == 0:
        scan = 30
    else:
        print(f"Scan value : {scan}")
    if step == 0:
        step = 10
    else:
        print(f"Step value : {step}")

# open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")

    if hw_slt_swtch == "at":
        print(f" Hw ON {hw_slt_swtch}")
        if at_btn == "on" or at_btn == "ON":
            print(f" WEB AT ON {at_btn}")
            if pin_btn == "on" or pin_btn == "ON":
                print(f" WEB PIN ------------ON {pin_btn}")
                setattr(var, at_flg_n, True)
                if int(rain) == 1:
                    setattr(var, o_flg_n, True)
                    setattr(var, cl_flg_n, False)
                    print(f"Rain Based Control [Rain:{rain}]")
                    await rain_func(env_in_temp,  rain_max, rain_btn, var, gpio, o_pin, cl_pin, mtr_time, o_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
                elif wind != 0 and int(wind_max) > 0 and int(wind) > int(wind_max):
                    conditon = "max_wind"
                    setattr(var, o_flg_n, True)
                    setattr(var, cl_flg_n, False)
                    print(f"Wind Based Control [Wind:{wind}]")
                    await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)
                else:
                    print(f" Elsse running {pin_btn}")
                    if temp_thresh == 0:
                        print(f" Temp Threshold is ::{temp_thresh}")

                        if open_time and close_time:
                            print("[TIME ONLY]")
                            await handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, o_run_time_n, cl_run_time_n, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat)
                         # only close case
                        elif not open_time and close_time:
                            print("[TIME ONLY] close case running")
                            if c_hour == cl_hour and c_min == cl_min:
                                conditon = "time_only_close"
                                await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)
                        else:
                            print("[TIME ONLY] SETTING WRONG")
                    elif temp_thresh > 0:
                        print(f" temperature  threshold {temp_thresh}")
                        if env_in_temp != 0:

                            if open_time and close_time:

                                if c_hour >= o_hour and c_hour <= cl_hour:
                                    print("[WITH IN INTERVAL]")
                                    if c_hour == o_hour:
                                        if c_min >= o_min:
                                            if c_hour < cl_hour:
                                                print(
                                                    "[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                                await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                            elif c_hour == cl_hour:
                                                if c_min < cl_min:
                                                    print(
                                                        "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                                    await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                    elif c_hour > o_hour:
                                        if c_hour < cl_hour:
                                            print("[HOUR DIFFERENCE]")
                                            await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                        elif c_hour == cl_hour:
                                            if c_min < cl_min:
                                                print("[MINUTE DIFFERENCE]")
                                                await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                else:
                                    print(
                                        "[NOT OPERATE] not in the time interval")
                            else:
                                print(
                                    f"[TEMPERATRE ONLY CONTROL] open Time:{open_time} || close Time:{close_time} ")
                                await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)

                        else:
                            print(f"[SENSOR ERROR] : {env_in_temp}")
                    else:
                        print("[SETTING ERROR] TEMPERATURE SETTING ERROR.")
            elif (pin_btn == "off" or pin_btn == "OFF") and at_flg:
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                setattr(var, at_flg_n, False)
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)
                setattr(var, cl_flg_n, False)
                setattr(var, indi, None)
                setattr(var, indi_stat, 0)
            else:
                print(f"[DEBUG]--CURRENT ACTUATOR PIN : {pin_btn}")
                print(f"[DEBUG]--CURRENT  at flag: {at_flg}")

        elif at_btn == "off" or at_btn == "OFF":

            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            gpio.turn_off_pins(o_pin)
            gpio.turn_off_pins(cl_pin)

            setattr(var, o_flg_n, False)
            setattr(var, cl_flg_n, False)
            setattr(var, indi, None)
            setattr(var, indi_stat, 0)
    elif hw_slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {hw_slt_swtch}")
        await mn_signal(gpio, var)


async def sw_cw_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, step, scan, temp_thresh,  env_in_temp, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n, indi, indi_stat,  hw_slt_swtch):
    ''' Control function for switch and curtain motor with time and temperature based logic. '''

    open_time = False
    close_time = False
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    c_time = (c_hour, c_min)

    if mtr_time == 0:
        mtr_time = 150
    else:
        print(f"Motor run time : {mtr_time}")
    if scan == 0:
        scan = 30
    else:
        print(f"Scan value : {scan}")
    if step == 0:
        step = 10
    else:
        print(f"Step value : {step}")
    # open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")

    if hw_slt_swtch == "at":
        if at_btn == "on" or at_btn == "ON":
            if (pin_btn == "on" or pin_btn == "ON"):
                setattr(var, at_flg_n, True)
                if temp_thresh == 0:
                    if open_time and close_time:
                        print("[TIME ONLY]")
                        await handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, o_run_time_n, cl_run_time_n, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat)
                     # only close case
                    elif not open_time and close_time:
                        if c_hour == cl_hour and c_min == cl_min:
                            conditon = "time_only_close"
                            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)
                    else:
                        print("[TIME ONLY] SETTING WRONG")
                elif temp_thresh > 0:
                    if env_in_temp != 0:
                        if open_time and close_time:
                            if c_hour >= o_hour and c_hour <= cl_hour:
                                print("[WITH IN INTERVAL]")
                                if c_hour == o_hour:
                                    if c_min >= o_min:
                                        if c_hour < cl_hour:
                                            print(
                                                "[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                            await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                        elif c_hour == cl_hour:
                                            if c_min < cl_min:
                                                print(
                                                    "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                                await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                elif c_hour > o_hour:
                                    if c_hour < cl_hour:
                                        print("[HOUR DIFFERENCE]")
                                        await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                                    elif c_hour == cl_hour:
                                        if c_min < cl_min:
                                            print("[MINUTE DIFFERENCE]")
                                            await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                            else:
                                print(
                                    "[NOT OPERATE] not in the time interval")

                        else:
                            print(
                                f"[TEMPERATRE ONLY CONTROL] open Time:{open_time} || close Time:{close_time} ")
                            await handle_temp_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, env_in_temp, temp_thresh)
                    else:
                        print(f"[SENSOR ERROR] : {env_in_temp}")
                else:
                    print("[SETTING ERROR] TEMPERATURE SETTING ERROR.")
            elif (pin_btn == "off" or pin_btn == "OFF") and at_flg:
                setattr(var, at_flg_n, False)
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)
                setattr(var, cl_flg_n, False)
                setattr(var, indi, None)
                setattr(var, indi_stat, 0)
            else:
                print(f"[DEBUG]--CURRENT ACTUATOR PIN : {pin_btn}")
                print(f"[DEBUG]--CURRENT  at flag: {at_flg}")
        elif at_btn == "off" or at_btn == "OFF":

            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            # gpio.turn_off_pins(o_pin)
            # gpio.turn_off_pins(cl_pin)

            setattr(var, o_flg_n, False)
            setattr(var, cl_flg_n, False)
            setattr(var, indi, None)
            setattr(var, indi_stat, 0)
    elif hw_slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {hw_slt_swtch}")
        await mn_signal(gpio, var)


async def tc_sun_temp_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, step, scan,  env_in_temp, low_temp_thresh,  sun_light, sun_light_thresh, sun_data_btn,  c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n, indi, indi_stat,  hw_slt_swtch):
    ''' Control function for low temperature and sunlight based control of a motorized curtain system. '''

    open_time = False
    close_time = False
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    c_time = (c_hour, c_min)
    if mtr_time == 0:
        mtr_time = 600
    else:
        print(f"Motor run time : {mtr_time}")
    if scan == 0:
        scan = 30
    else:
        print(f"Scan value : {scan}")
    if step == 0:
        step = 20
    else:
        print(f"Step value : {step}")
    if low_temp_thresh == 0:
        low_temp_thresh = 5
    else:
        print(f"Low Temp Threshold value : {low_temp_thresh}")
    # open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")

    if hw_slt_swtch == "at":
        if at_btn == "on" or at_btn == "ON":
            if (pin_btn == "on" or pin_btn == "ON"):
                setattr(var, at_flg_n, True)
                if sun_light_thresh == 0:
                    if open_time and close_time:
                        print("[TIME ONLY]")
                        await handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, o_run_time_n, cl_run_time_n, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat)
                     # only close case
                    elif not open_time and close_time:
                        if c_hour == cl_hour and c_min == cl_min:
                            conditon = "time_only_close"
                            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)
                    else:
                        print("[TIME ONLY] SETTING WRONG")
                elif low_temp_thresh > 0:
                    if env_in_temp != 0:
                        if env_in_temp > low_temp_thresh:
                            if open_time and close_time:
                                if c_hour >= o_hour and c_hour <= cl_hour:
                                    print("[WITH IN INTERVAL]")
                                    if c_hour == o_hour:
                                        if c_min >= o_min:
                                            if c_hour < cl_hour:
                                                print(
                                                    "[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                                await handle_sunlight_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, sun_light, sun_light_thresh, sun_data_btn)
                                            elif c_hour == cl_hour:
                                                if c_min < cl_min:
                                                    print(
                                                        "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                                    await handle_sunlight_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, sun_light, sun_light_thresh, sun_data_btn)
                                    elif c_hour > o_hour:
                                        if c_hour < cl_hour:
                                            print("[HOUR DIFFERENCE]")
                                            await handle_sunlight_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, sun_light, sun_light_thresh, sun_data_btn)
                                        elif c_hour == cl_hour:
                                            if c_min < cl_min:
                                                print("[MINUTE DIFFERENCE]")
                                                await handle_sunlight_based_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat, sun_light, sun_light_thresh, sun_data_btn)
                                else:
                                    print(
                                        "[NOT OPERATE] not in the time interval")
                            else:
                                print(
                                    f"[SETTING ERROR] open Time:{open_time} || close Time:{close_time} ")
                        elif env_in_temp <= low_temp_thresh:
                            condition = "low_temp"
                            print(f"[TEMPERATURE LOW] : {env_in_temp}")
                            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, condition)

                    else:
                        print(f"[SENSOR ERROR] : {env_in_temp}")
                else:
                    print("[SETTING ERROR] TEMPERATURE SETTING ERROR.")
            elif (pin_btn == "off" or pin_btn == "OFF") and at_flg:
                setattr(var, at_flg_n, False)
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)
                setattr(var, cl_flg_n, False)
                setattr(var, indi, None)
                setattr(var, indi_stat, 0)
            else:
                print(f"[DEBUG]--CURRENT ACTUATOR PIN : {pin_btn}")
                print(f"[DEBUG]--CURRENT  at flag: {at_flg}")
        elif at_btn == "off" or at_btn == "OFF":

            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            # gpio.turn_off_pins(o_pin)
            # gpio.turn_off_pins(cl_pin)

            setattr(var, o_flg_n, False)
            setattr(var, cl_flg_n, False)
            setattr(var, indi, None)
            setattr(var, indi_stat, 0)
    elif hw_slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {hw_slt_swtch}")
        await mn_signal(gpio, var)

# # wind control virtical curtain


# # wind control virtical curtain


async def tc_vt_wind_control(var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time, o_run_time_n, cl_run_time_n, step, scan,  env_in_temp, low_temp_thresh, wind, wind_thresh, c_hour, c_min, o_hour, o_min, cl_hour, cl_min, at_btn, pin_btn, cl_flag, o_flag, cl_flg_n, o_flg_n, at_flg, at_flg_n, indi, indi_stat,  hw_slt_swtch):
    open_time = False
    close_time = False
    o_time = (o_hour, o_min)
    cl_time = (cl_hour, cl_min)
    c_time = (c_hour, c_min)
    if mtr_time == 0:
        mtr_time = 300
    else:
        print(f"Motor run time : {mtr_time}")
    if scan == 0:
        scan = 30
    else:
        print(f"Scan value : {scan}")
    if step == 0:
        step = 20
    else:
        print(f"Step value : {step}")
    if low_temp_thresh == 0:
        low_temp_thresh = 5
    else:
        print(f"Low Temp Threshold value : {low_temp_thresh}")
    # open time and close time True flase check
    if (o_hour != 0 or o_min != 0):
        open_time = True
        print(f" Open Time is ::{open_time}")

    if (cl_hour != 0 or cl_min != 0):
        close_time = True
        print(f" Close  Time is ::{close_time}")

    if hw_slt_swtch == "at":
        if at_btn == "on" or at_btn == "ON":
            if (pin_btn == "on" or pin_btn == "ON"):
                setattr(var, at_flg_n, True)
                if wind_thresh == 0:
                    if open_time and close_time:
                        print("[TIME ONLY]")
                        await handle_time_based_control_multiple(var, gpio, o_pin, cl_pin, mtr_time, o_time, cl_time, c_time, o_run_time_n, cl_run_time_n, cl_flag, o_flag, o_flg_n, cl_flg_n, indi, indi_stat)
                     # only close case
                    elif not open_time and close_time:
                        print("[CLOSE ONLY]")
                        conditon = "time_only_close"
                        if c_hour == cl_hour and c_min == cl_min:
                            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)
                    else:
                        print("[TIME ONLY] SETTING WRONG")
                elif low_temp_thresh > 0:
                    if env_in_temp != 0:
                        if env_in_temp > low_temp_thresh:
                            if open_time and close_time:
                                if c_hour >= o_hour and c_hour <= cl_hour:
                                    print("[WITH IN INTERVAL]")
                                    if c_hour == o_hour:
                                        if c_min >= o_min:
                                            if c_hour < cl_hour:
                                                print(
                                                    "[WITH IN THE INTERVAL] HOUR DIFFERENCE")
                                                await wind_func(wind,  wind_thresh,  var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
                                            elif c_hour == cl_hour:
                                                if c_min < cl_min:
                                                    print(
                                                        "[WITH IN THE INTERVAL]  CLOSE MINUTE DIFFERENCE")
                                                    await wind_func(wind,  wind_thresh,  var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
                                    elif c_hour > o_hour:
                                        if c_hour < cl_hour:
                                            print("[HOUR DIFFERENCE]")
                                            await wind_func(wind,  wind_thresh,  var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
                                        elif c_hour == cl_hour:
                                            if c_min < cl_min:
                                                print("[MINUTE DIFFERENCE]")
                                                await wind_func(wind,  wind_thresh,  var, gpio, o_pin, cl_pin, mtr_time, o_run_time, cl_run_time,  o_run_time_n, cl_run_time_n, o_flag, cl_flag, o_flg_n, cl_flg_n, step, scan, indi, indi_stat)
                                else:
                                    print(
                                        "[NOT OPERATE] not in the time interval")
                            else:
                                print(
                                    f"[SETTING ERROR] open Time:{open_time} || close Time:{close_time} ")

                        elif env_in_temp <= low_temp_thresh:
                            conditon = "low_temp"
                            print(f"[TEMPERATURE LOW] : {env_in_temp}")
                            await ctrl_close_full(var, gpio, o_pin, cl_pin, mtr_time, cl_flag, o_flg_n, cl_flg_n, o_run_time_n, cl_run_time_n, indi, indi_stat, conditon)

                    else:
                        print(f"[SENSOR ERROR] : {env_in_temp}")
                else:
                    print(
                        f"[SETTING ERROR] TEMPERATURE SETTING ERROR.{low_temp_thresh}")
            elif (pin_btn == "off" or pin_btn == "OFF") and at_flg:
                setattr(var, at_flg_n, False)
                print(f"[DEBUG]--CURRENT ACTUATOR PIN OFF: {pin_btn}")
                gpio.turn_off_pins(o_pin)
                gpio.turn_off_pins(cl_pin)
                setattr(var, o_flg_n, False)
                setattr(var, cl_flg_n, False)
                setattr(var, indi, None)
                setattr(var, indi_stat, 0)
            else:
                print(f"[DEBUG]--CURRENT ACTUATOR PIN : {pin_btn}")
                print(f"[DEBUG]--CURRENT  at flag: {at_flg}")
        elif at_btn == "off" or at_btn == "OFF":

            print(f"[DEBUG] Web Auto mode OFF: {at_btn}")
            # gpio.turn_off_pins(o_pin)
            # gpio.turn_off_pins(cl_pin)

            setattr(var, o_flg_n, False)
            setattr(var, cl_flg_n, False)
            setattr(var, indi, None)
            setattr(var, indi_stat, 0)
    elif hw_slt_swtch == "mn":
        print(f"[DEBUG] Manual mode active: {hw_slt_swtch}")
        await mn_signal(gpio, var)
