import asyncio
# from var import VariableData
# from simple import MQTTClient
import json

# var = VariableData()
# NEED TO CHANGE FOR OTHER HOUSE

# _1":
# _1,
# _1}


def get_wind_direction(degree=0):
    print("Wind Direction: ", degree)
    if degree >= 338 or degree <= 22:
        return "N"
    elif 23 <= degree <= 67:
        return "NE"
    elif 68 <= degree <= 112:
        return "E"
    elif 113 <= degree <= 157:
        return "SE"
    elif 158 <= degree <= 202:
        return "S"
    elif 203 <= degree <= 247:
        return "SW"
    elif 248 <= degree <= 292:
        return "W"
    elif 293 <= degree <= 337:
        return "NW"

async def envout_sensor(var, client):    # Topics
    MQTT_TOPIC_SENSOR = "jbsy24"
    sensor_data = {
        "envout_ws_2": round(var.envout_ws_1, 2),
        "envout_ws_3": round(var.envout_ws_1, 2),
        "envout_ws_4": round(var.envout_ws_1, 2),
        "envout_ws_5": round(var.envout_ws_1, 2),
        "envout_ws_6": round(var.envout_ws_1, 2),
        "envout_ws_7": round(var.envout_ws_1, 2),
    }
    try:
        client.publish(MQTT_TOPIC_SENSOR, json.dumps(sensor_data))
    except Exception as e:
        print("Error publishing sensor Envout data:", e)


async def sensor(var, client):
    # Topics
    MQTT_TOPIC_SENSOR = "dytw_1/sensor"
    MQTT_TOPIC_HW_INFO = "dytw_1/info"
    if not var.psv_sen_flg:
        var.psv_sen_flg = True
        degree =get_wind_direction(var.envout_wd_1)      
        
        wind_final=f'{degree}{var.envout_wd_1}'

        sensor_data = {
            "mcu_free_memory_1": var.mcu_mem,            
            "hr_1": var.c_hour_1,
            "min_1": var.c_min_1,
            "hw_switch_1": var.hw_switch_1,

            "envout_temp_1": round(var.envout_temp_1, 2),
            "envout_humi_1": round(var.envout_humi_1, 2),
            "envout_light_intensity_1": round(var.envout_light_intensity_1, 2),
            "rain_status_1": round(var.rain_status_1, 2),
            "envout_rf_1": round(var.envout_rf_1, 2),
            "envout_wd_1": wind_final,
            "envout_ws_1": round(var.envout_ws_1, 2),

            "envin_temp_1": round(var.envin_temp_1, 2),
            "envin_humi_1": round(var.envin_humi_1, 2),
            "envin_co2_1": round(var.envin_co2_1, 2),
            "envin_hd_1": round(var.envin_hd_1, 2),
            "envin_vpd_1": round(var.envin_vpd_1, 2),

            "envin_abs_humi_1": round(var.envin_abs_humi_1, 2),
            "envin_dp_1": round(var.envin_dp_1, 2),
            "envin_at_1": round(var.envin_at_1, 2),
            "envin_light_intensity_1": round(var.envin_light_intensity_1, 2),
            "envin_cli_1": round(var.envin_cli_1, 2),

            "soil_temp_1": round(var.soil_temp_1, 2),
            "soil_moisture_1": round(var.soil_moisture_1, 2),
            "soil_ec_1": round(var.soil_ec_1, 2),
            "soil_ph_1": round(var.soil_ph_1, 2),

            "waste_ec_1": round(var.waste_ec_1, 2),
            "waste_ph_1": round(var.waste_ph_1, 2),
            "waste_dl_1": round(var.waste_dl_1, 2),
        }

        try:
            # Publish sensor data
           
            client.publish(MQTT_TOPIC_SENSOR, json.dumps(sensor_data))
        except Exception as e:
            print("Error publishing sensor data:", e)

        # await asyncio.sleep(3)
        var.psv_sen_flg = False


async def auto_publish(on_condition, manuaL_data, auto_data, client):
    MQTT_TOPIC_AUTO = "dytw_1/auto"
    MQTT_TOPIC_MANUAL = "dytw_1/manual"

    if on_condition == "on" or on_condition == "ON":
        try:
            client.publish(MQTT_TOPIC_AUTO, json.dumps(auto_data))
            print(" AUTO PUBLISH : ", auto_data)
        except Exception as e:
            print("Error publishing auto data:", e)
    else:
        try:
            client.publish(MQTT_TOPIC_MANUAL, json.dumps(manuaL_data))
            print(" MANUAL  PUBLISH : ", manuaL_data)
        except Exception as e:
            print("Error publishing manual data:", e)


async def auto_stat_manual(var, client):

    if not var.psv_ato_flg:
        var.psv_ato_flg = True
        # ========================== MANUAL MODE CONTROL

        # side windows (측창)
        # 1f (좌측)/우측

        sw_1fl_1_m = {
            "sw_1fl_1": var.sw_1fl_1}
        sw_1fr_1_m = {
            "sw_1fr_1": var.sw_1fr_1}
        # 2f (좌측)/우측

        sw_2fl_1_m = {
            "sw_2fl_1": var.sw_2fl_1}
        sw_2fr_1_m = {
            "sw_2fr_1": var.sw_2fr_1}
        # 3f (좌측)/우측

        sw_3fl_1_m = {
            "sw_3fl_1": var.sw_3fl_1}
        sw_3fr_1_m = {
            "sw_3fr_1": var.sw_3fr_1}
        # ceiling windows (천창)
        # 1f (좌측)/우측
        cw_1fl_1_m = {
            "cw_1fl_1": var.cw_1fl_1}
        cw_1fr_1_m = {
            "cw_1fr_1": var.cw_1fr_1}
        # 2f (좌측)/우측
        
#         
#         cw_2fl_1_m = {
#             "cw_2fl_1": var.cw_2fl_1}
#         cw_2fr_1_m = {
#             "cw_2fr_1": var.cw_2fr_1}
#         # 3f (좌측)/우측
#         cw_3fl_1_m = {
#             "cw_3fl_1": var.cw_3fl_1}
#         cw_3fr_1_m = {
#             "cw_3fr_1": var.cw_3fr_1}
#         
        
        
        
        
        cf_01_1_m = {"cf_01_1": var.cf_01_1}
#                      "cf_01_fwd_1": var.cf_01_fwd_1,
#                      "cf_01_rev_1": var.cf_01_rev_1}

#         cf_02_1_m = {"cf_02_1": var.cf_02_1}
# #                      "cf_02_fwd_1": var.cf_02_fwd_1,
# #                      "cf_02_rev_1": var.cf_02_rev_1}

        ef_m = {"ef_1": var.ef_1}
        # wc_m = {"wc_1": var.wc_1}
        # co2_m = {"co2_1": var.co2_1}
        # fv_m = {"fv_1": var.fv_1}
        # sl_m = {"sl_1": var.sl_1}
        # if_m = {"if_1": var.if_1}
        # hu_m = {"hu_1": var.hu_1}
        # cu_m = {"cu_1": var.cu_1}

        # =====================================AUTO MODE STATUS SEND

        # side windows (측창)
        # 1f (좌측)/우측
        sw_1fl_1_a = {
            "sw_1fl_oc_1": var.sw_1fl_oc_1,
            "sw_1fl_stat_1": var.sw_1fl_stat_1,
        }
        sw_1fr_1_a = {
            "sw_1fr_oc_1": var.sw_1fr_oc_1,
            "sw_1fr_stat_1": var.sw_1fr_stat_1,
        }
        # 2f (좌측)/우측
        sw_2fl_1_a = {
            "sw_2fl_oc_1": var.sw_2fl_oc_1,
            "sw_2fl_stat_1": var.sw_2fl_stat_1,
        }
        sw_2fr_1_a = {
            "sw_2fr_oc_1": var.sw_2fr_oc_1,
            "sw_2fr_stat_1": var.sw_2fr_stat_1,
        }
        # 3f (좌측)/우측
        sw_3fl_1_a = {
            "sw_3fl_oc_1": var.sw_3fl_oc_1,
            "sw_3fl_stat_1": var.sw_3fl_stat_1,
        }
        sw_3fr_1_a = {
            "sw_3fr_oc_1": var.sw_3fr_oc_1,
            "sw_3fr_stat_1": var.sw_3fr_stat_1,
        }
        # ceiling windows (천창)
        # 1f (좌측)/우측
        cw_1fl_1_a = {
            "cw_1fl_oc_1": var.cw_1fl_oc_1,
            "cw_1fl_stat_1": var.cw_1fl_stat_1,
        }
        cw_1fr_1_a = {
            "cw_1fr_oc_1": var.cw_1fr_oc_1,
            "cw_1fr_stat_1": var.cw_1fr_stat_1,
        }
        
        
        
#         # 2f (좌측)/우측
#         cw_2fl_1_a = {
#             "cw_2fl_oc_1": var.cw_2fl_oc_1,
#             "cw_2fl_stat_1": var.cw_2fl_stat_1,
#         }
#         cw_2fr_1_a = {
#             "cw_2fr_oc_1": var.cw_2fr_oc_1,
#             "cw_2fr_stat_1": var.cw_2fr_stat_1,
#         }
#         # 3f (좌측)/우측
#         cw_3fl_1_a = {
#             "cw_3fl_oc_1": var.cw_3fl_oc_1,
#             "cw_3fl_stat_1": var.cw_3fl_stat_1,
#         }
#         cw_3fr_1_a = {
#             "cw_3fr_oc_1": var.cw_3fr_oc_1,
#             "cw_3fr_stat_1": var.cw_3fr_stat_1,
#         }
#         
#         
#         
        
        

        cf_01_a = {
            "cf_01_oc_1": var.cf_01_oc_1,
        }

        ef_a = {"ef_oc_1": var.ef_oc_1}
        # wc_a = {"wc_oc_1": var.wc_oc_1}
        # co2_a = {"co2_oc_1": var.co2_oc_1}
        # fv_a = {"fv_oc_1": var.fv_oc_1}
        # sl_a = {"sl_oc_1": var.sl_oc_1}
        # if_a = {"if_oc_1": var.if_oc_1}
      

        # chukjang
        tasks = [
            # ============= 1F(1중 )
            # 4 연동
            # 01

            # 02
            auto_publish(var.sw_1f_lbtn_1, sw_1fl_1_m, sw_1fl_1_a, client),
            auto_publish(var.sw_1f_rbtn_1, sw_1fr_1_m, sw_1fr_1_a, client),
            # ============= 2F(2중 )
            # 03
            auto_publish(var.sw_2f_lbtn_1, sw_2fl_1_m, sw_2fl_1_a, client),
            auto_publish(var.sw_2f_rbtn_1, sw_2fr_1_m, sw_2fr_1_a, client),
            # ============= 3F(3중 )
            # 04
            auto_publish(var.sw_3f_lbtn_1, sw_3fl_1_m, sw_3fl_1_a, client),
            auto_publish(var.sw_3f_rbtn_1, sw_3fr_1_m, sw_3fr_1_a, client),
            # ============= 천창(4중 )
            # 05
            auto_publish(var.cw_1f_lbtn_1, cw_1fl_1_m, cw_1fl_1_a, client),
            auto_publish(var.cw_1f_rbtn_1, cw_1fr_1_m, cw_1fr_1_a, client),
            # 06
            
            
            
#             auto_publish(var.cw_2f_lbtn_1, cw_2fl_1_m, cw_2fl_1_a, client),
#             auto_publish(var.cw_2f_rbtn_1, cw_2fr_1_m, cw_2fr_1_a, client),
#             # 07
#             auto_publish(var.cw_3f_lbtn_1, cw_3fl_1_m, cw_3fl_1_a, client),
#             auto_publish(var.cw_3f_rbtn_1, cw_3fr_1_m, cw_3fr_1_a, client),
#             
#             
#             
            

            auto_publish(var.cf_01_ambtn_1, cf_01_1_m, cf_01_a, client),
            # ============= 환기팬(5중 )

            # 08
            auto_publish(var.ef_ambtn_1, ef_m, ef_a, client),
            # ============= 환기팬(5중 )
            # # 09
            # auto_publish(var.wc_ambtn_1, wc_m, wc_a, client),
            # # ============= CO2(6중 )
            # # 10
            # auto_publish(var.co2_ambtn_1, co2_m, co2_a, client),
            # # ============= FAN(7중 )
            # # 11
            # auto_publish(var.fv_ambtn_1, fv_m, fv_a, client),
            # # ============= SL(8중 )
            # # 12
            # auto_publish(var.sl_ambtn_1, sl_m, sl_a, client),
            # # ============= IF(9중 )
            # # 13
            # auto_publish(var.if_ambtn_1, if_m, if_a, client),
            # ============= HU(10중 )         


        ]

        await asyncio.gather(*tasks)

        # await asyncio.sleep(3)
        var.psv_ato_flg = False


async def publish_sen_atmn_stat(var, client):
    await asyncio.gather(
        sensor(var, client),
        auto_stat_manual(var, client),
        envout_sensor(var, client),

    )
