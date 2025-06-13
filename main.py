# main.py
# CHANGE FOR THE OTHER HOUSE
# rst_1
import uasyncio as asyncio
import gc
import network
import machine
import json

# rtc get from the cloud and match
from md.api import get_current_time_from_cloud
# MASTER READ UART
from md.mg import read_master
# variable store on the
from md.sv import store_var
# to store variable in the var.csv
from md.sv import update_csv_file_periodically
# variable store on the  var.csv
from md.psv import publish_sen_atmn_stat
# loas store variable from  var.csv MCU
from md.load import load_csv_to_var
from md.am import am_status
from md.rn import read_rain_status
from md.rs import read_sensors
from md.vpd import vpd_cli_actemp
from md. api import publish_sensor_to_server_db
from md.rtc import current_rtc
from md.rs_o import read_uart_envout
from md.am import am_status_sent_db
# MANUAL
# ventillation
from md.mnc import sw_crtl_1f_left, sw_crtl_1f_right, sw_crtl_2f_left, sw_crtl_2f_right, sw_crtl_3f_left, sw_crtl_3f_right
from md.mnc import cw_crtl_1f_left, cw_crtl_1f_right #, cw_crtl_2f_left, cw_crtl_2f_right, cw_crtl_3f_left, cw_crtl_3f_right
# AC actuators
from md.mnc import cf_fan_crtl_01, ef_fan_crtl #, co2_crtl, wc_crtl, fv_crtl, sl_crtl

# AUTO
# ventillation
from md.atc_sw_1fltrt import sw_1f_lt_control, sw_1f_rt_control
from md.atc_sw_2fltrt import sw_2f_lt_control, sw_2f_rt_control
from md.atc_tccw_ltrt import tccw_1fl_control, tccw_1fr_control
from md.atc_tcsw_ltrt import tcvt_lt_control, tcvt_rt_control
# AC actuators
from md.atc_ac import cf01_fan_ctrl_auto,  ef_fan_ctrl_auto #cf02_fan_ctrl_auto, ef_fan_ctrl_auto #, wc_ctrl_auto, sl_ctrl_auto, fv_ctrl_auto, co2_ctrl_auto


from md.var import VariableData
from md.io import GPIOController
from md.simple import MQTTClient
# if master is connected

uart_hmi = machine.UART(5, baudrate=115200)  # Example UART initialization


var = VariableData()
gpio = GPIOController()
network_connected = False  # Flag to track network status
cloud_client = None  # Cloud MQTT client








async def check_network_connection(nic, retries=5, delay=2):
    global network_connected
    attempt = 0
    while attempt < retries:
        try:
            nic.active(False)  # Reset the NIC fully
            await asyncio.sleep(0.5)
            nic.active(True)
            await asyncio.sleep(1.0)  # Let it initialize

            if nic.isconnected():
                print("✅ Ethernet connected:", nic.ifconfig()[0])
                network_connected = True
                return
            else:
                print(f"⏳ Attempt {attempt+1}: Waiting for Ethernet...")
        except Exception as e:
            print("⚠️ Ethernet error:", e)

        attempt += 1
        await asyncio.sleep(delay)

    print("❌ Ethernet still not connected after retries.")
    network_connected = False



async def network_monitor_cloud():
    global network_connected, cloud_client
    nic = network.LAN()
    nic.active(True)

    while True:
        try:
            if not nic.isconnected():
                if network_connected:
                    print("❌ Ethernet lost. Disconnecting MQTT and retrying...")
                    network_connected = False
                    if cloud_client:
                        try:
                            cloud_client.disconnect()
                        except Exception as e:
                            print("Error disconnecting MQTT:", e)
                        cloud_client = None

                await check_network_connection(nic)

                if network_connected:
                    try:
                        print("✅ Network recovered. Reconnecting MQTT...")
                        await setup_cloud_mqtt()
                        asyncio.create_task(mqtt_task())
                    except Exception as e:
                        print("⚠️ Failed to reconnect MQTT:", e)

            await asyncio.sleep(600)  # 5 to 10 minutes
            print("--------------------Checking network status...---------------------OK ✅")
        except Exception as e:
            print("⚠️ Error in network monitor loop:", e)
            network_connected = False
            await asyncio.sleep(5)
























def mqtt_callback_cloud(topic, msg):
    global cloud_client
    try:
        msg_decoded = msg.decode('utf-8').strip()
        print(f"Received MQTT message: {msg_decoded}")
        try:
            json_data = json.loads(msg_decoded)
            for switch_name, switch_state in json_data.items():
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state, cloud_client))
        except ValueError:  # Catch ValueError instead of JSONDecodeError
            switch_data = msg_decoded.split(":")
            if len(switch_data) == 2:
                switch_name = switch_data[0].strip().strip('{"}')
                switch_state = switch_data[1].strip().strip('"}')
                # Pass cloud_client or missing argument here
                asyncio.create_task(
                    store_var(var, switch_name, switch_state,  cloud_client))
            else:
                print(f"Invalid message format: {msg_decoded}")
    except Exception as e:
        print("Error processing MQTT message:", e)


async def setup_cloud_mqtt():
    global cloud_client
    MQTT_BROKER = "121.78.116.56"
    MQTT_PORT = 1883
    MQTT_TOPIC_SUBSCRIBE = b"jbsy24"  # ----------- change the topic ID
    MQTT_CLIENT_ID = "mqtt_ch1_jbsy24_web1"

    cloud_client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT)
    try:
        cloud_client.connect()
        cloud_client.set_callback(mqtt_callback_cloud)
        cloud_client.subscribe(MQTT_TOPIC_SUBSCRIBE)
        print("Connected to cloud MQTT broker and subscribed to topic.")
    except Exception as e:
        print("Error connecting to cloud MQTT broker:", e)


async def mqtt_task():
    global cloud_client
    mqtt_failure_count = 0
    max_failures = 10

    while True:
        if cloud_client:
            try:
                cloud_client.check_msg()
            except OSError as e:
                print(f"Cloud MQTT OSError: {e}. Attempting to reconnect.")
                mqtt_failure_count += 1
                cloud_client = None
                if mqtt_failure_count >= max_failures:
                    print("Cloud MQTT failed multiple times. Resetting the board...")
                    machine.reset()
        await asyncio.sleep(0.1)


async def publish_rst_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                # await load_csv_to_var_mqtt(cloud_client, var)
                # await publish_sensor(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(5)


async def publish_sensor_task_cloud():
    while True:
        try:
            if cloud_client:
                print("Publishing to cloud client...")
                # await load_csv_to_var_mqtt(cloud_client, var)
                await publish_sen_atmn_stat(var, cloud_client)
            else:
                print("Cloud client is not available")
        except Exception as e:
            print("Error in cloud publish_sensor task:", e)
        await asyncio.sleep(5)


async def reset_board_func():
    while True:
        if var.rst_1 == "on":
            print("--------Resetting the board...---------")
            machine.reset()
        await asyncio.sleep(3)


async def read_master_task():
    while True:
        await read_master(var, uart_hmi)
        await asyncio.sleep(3)


async def cloud_time_task(var):
    while True:
        await get_current_time_from_cloud(var)
        if var.cld_rtc_flg:
            setattr(var, "rtc_init", False)
            # Fetch every hour, adjust as needed   (3600)
            await asyncio.sleep(3600)
        else:
            await asyncio.sleep(3)


async def non_network_tasks():

    # manual
    # side ventillation
    asyncio.create_task(sw_crtl_1f_left(var, gpio))
    asyncio.create_task(sw_crtl_1f_right(var, gpio))
    asyncio.create_task(sw_crtl_2f_left(var, gpio))
    asyncio.create_task(sw_crtl_2f_right(var, gpio))
    asyncio.create_task(sw_crtl_3f_left(var, gpio))
    asyncio.create_task(sw_crtl_3f_right(var, gpio))
    # ceiling ventillation
    asyncio.create_task(cw_crtl_1f_left(var, gpio))
    asyncio.create_task(cw_crtl_1f_right(var, gpio))
    # asyncio.create_task(cw_crtl_2f_left(var, gpio))
    # asyncio.create_task(cw_crtl_2f_right(var, gpio))
    # asyncio.create_task(cw_crtl_3f_left(var, gpio))
    # asyncio.create_task(cw_crtl_3f_right(var, gpio))
    # AC actuators
    asyncio.create_task(cf_fan_crtl_01(var, gpio))
#     asyncio.create_task(cf_fan_crtl_02(var, gpio))
    asyncio.create_task(ef_fan_crtl(var, gpio))
    # asyncio.create_task(co2_crtl(var, gpio))
    # asyncio.create_task(wc_crtl(var, gpio))
    # asyncio.create_task(fv_crtl(var, gpio))
    # asyncio.create_task(sl_crtl(var, gpio))

    # auto
    # ventillation
    asyncio.create_task(sw_1f_lt_control(var, gpio))
    asyncio.create_task(sw_1f_rt_control(var, gpio))
    asyncio.create_task(sw_2f_lt_control(var, gpio))
    asyncio.create_task(sw_2f_rt_control(var, gpio))

    asyncio.create_task(tccw_1fl_control(var, gpio))
    asyncio.create_task(tccw_1fr_control(var, gpio))


    asyncio.create_task(tcvt_lt_control(var, gpio))
    asyncio.create_task(tcvt_rt_control(var, gpio))

    # ceiling ventillation
    # AC actuators
    asyncio.create_task(cf01_fan_ctrl_auto(var, gpio))
    # asyncio.create_task(cf02_fan_ctrl_auto(var, gpio))
    asyncio.create_task(ef_fan_ctrl_auto(var, gpio))
    # asyncio.create_task(wc_ctrl_auto(var, gpio))
    # asyncio.create_task(sl_ctrl_auto(var, gpio))
    # asyncio.create_task(fv_ctrl_auto(var, gpio))
    # asyncio.create_task(co2_ctrl_auto(var, gpio))


async def main():
    try:
        print("Starting the main loop...")

        asyncio.create_task(load_csv_to_var(var))
        # hw selector switch
        asyncio.create_task(am_status(var))
        # rain
        asyncio.create_task(read_rain_status(var))
        # # master
        # asyncio.create_task(read_master_task())
        # reset/watchdog timer
        # asyncio.create_task(reset_board_func())
        # sensors
        asyncio.create_task(read_sensors(var))

        asyncio.create_task(vpd_cli_actemp(var))

        asyncio.create_task(read_uart_envout(var))
        # Local and cloud Network monitor
        asyncio.create_task(network_monitor_cloud())

        # cloud time task
        asyncio.create_task(cloud_time_task(var))

        asyncio.create_task(publish_sensor_task_cloud())
        # asyncio.create_task(publish_sensor_task_local())
        asyncio.create_task(publish_sensor_to_server_db(var))
        #
        # asyncio.create_task(publish_rst_task_cloud())
        # asyncio.create_task(publish_rst_task_local())

        # rtc mcu
        asyncio.create_task(current_rtc(var))

        # to store on the var.csv
        asyncio.create_task(update_csv_file_periodically())

        # selectors switch an MCU reset  status to db
        asyncio.create_task(am_status_sent_db(var))

        # GPIO control Auto/Manual
        asyncio.create_task(non_network_tasks())

        while True:
            # Debug memory usage periodically
            gc.collect()
            free_memory = gc.mem_free()
            var.mcu_f_mem = gc.mem_free()
            # var.cpu_clk = machine.freq()

            allocated_memory = gc.mem_alloc()
            total_memory = free_memory + allocated_memory
            print("Free Memory: {} bytes".format(free_memory))
            print("Allocated Memory: {} bytes".format(allocated_memory))
            print("Total Memory: {} bytes".format(total_memory))

            await asyncio.sleep(5)
    except Exception as e:
        print(f"Unexpected error in main loop: {e}")

# Start the main loop
asyncio.run(main())
