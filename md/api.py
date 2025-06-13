
import uasyncio as asyncio  # Import asyncio at the top
import urequests  # Ensure you have a library like urequests for HTTP requests
import aiohttp
import json

# change for the other house
# _1
# jbsy24

# jbsy24
def device_status_motor(name, indi, indi_stat,condition):
    status = {
        "db_name": "jbsy24",
        "device_name": name,
        "device_status": indi,
        "device_status_percent": indi_stat,
        "condition":condition
        }
    return status

def device_status_ac(name, indi,condition):
    status = {
        "db_name": "jbsy24",
        "device_name": name,
        "device_status": indi,
        "condition":condition,
        }
    return status


async def get_current_time_from_cloud(var):

    # Replace with your PHP API endpoint
    cloud_time_url = "http://www.adas.today/sf/time_api/time_api.php"
    try:
        print("-----------------------------------------------------------------------------Fetching current time from the cloud...")
        response = urequests.get(cloud_time_url)
        if response.status_code == 200:
            data = response.json()
            print(f"Current Time from Cloud: {data}")

            # Extract hour, minute, and second from the response
            current_hour = int(data.get("hour", 0))
            current_min = int(data.get("minute", 0))
            current_sec = int(data.get("second", 0))

            # Set the attribute to indicate the time has been fetched
            setattr(var, "cld_rtc_flg", True)

            # Set attributes on the passed `var` object
            setattr(var, "cld_hour", f"{current_hour:02d}")
            setattr(var, "cld_min", f"{current_min:02d}")
            setattr(var, "cld_sec", f"{current_sec:02d}")

            print(
                f"Server Time -> Hour: {current_hour:02d}, Minute: {current_min:02d}, Second: {current_sec:02d}")
        else:
            print(
                f"Failed to fetch time. HTTP status code: {response.status_code}")
        response.close()
    except Exception as e:
        print(f"Error fetching time from the [cloud_Time]: {e}")



async def publish_sensor_to_server_db(var):
    while True:
        try:
            sensor_data = {

                "envout_temp_1": round(var.envout_temp_1, 2),
                "envout_humi_1": round(var.envout_humi_1, 2),
                "envout_light_intensity_1": round(var.envout_light_intensity_1, 2),
                "rain_status_1": round(var.rain_status_1, 2),
                "envout_rf_1": round(var.envout_rf_1, 2),
                "envout_wd_1": round(var.envout_wd_1, 2),
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
            
            print("Sending sensor data:", sensor_data)  # Optional debug

    
        
            API_URL = "http://www.adas.today/sf/backend/gateway_sensor_post_api/jbsy24_sensor_post.php"
            async with aiohttp.ClientSession() as session:
                async with session.post(API_URL, json=sensor_data) as response:
                    if response.status == 200:
                        print("Successfully sent [sensor data] to the API OK!")
                    else:
                        print(
                            f"Failed to send [sensor data]. HTTP Status Code: {response.status}")
        except Exception as e:
            print(f"Error publishing [sensor data] to the API : {e}")
        await asyncio.sleep(60)


async def send_settings_to_server_db(data):   

    try:
        api_url = "http://www.adas.today/sf/backend/gateway_post_api/jbsy24_post.php"

        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=data) as response:
                if response.status == 200:
                    print("Successfully sent [setting data] to the REST API")
                else:
                    print(
                        f"Failed to send [setting data]. HTTP Status Code: {response.status}")
    except Exception as e:
        print(f"Error sending [setting data] to REST API: {e}")

async def send_status_to_server_db(data):   

    try:
        api_url = "http://www.adas.today/sf/backend/gateway_post_api/jbsy24_status_post_t.php"

        async with aiohttp.ClientSession() as session:
            async with session.post(api_url, json=data) as response:
                if response.status == 200:
                    print("Successfully sent [status data] to the REST API")
                else:
                    print(
                        f"Failed to send [status data]. HTTP Status Code: {response.status}")
    except Exception as e:
        print(f"Error sending [status data] to REST API: {e}")