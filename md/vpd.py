import uasyncio as asyncio
import math


def calculate_vpd(temp_celsius, relative_humidity):
    print(
        f"Calculating VPD with temp: {temp_celsius}°C and RH: {relative_humidity}%")
    # Saturation vapor pressure
    es = 0.6108 * math.exp((17.27 * temp_celsius) / (temp_celsius + 237.3))
    ea = es * (relative_humidity / 100.0)  # Actual vapor pressure
    vpd = es - ea  # Vapor pressure deficit
    return round(vpd, 2)


# def calculate_dli_from_par_readings(par_readings, interval_seconds=5):
#     print(
#         f"Calculating ---light with temp: {par_readings}°C and RH: {interval_seconds}%")

#     total_par = sum(par * interval_seconds for par in par_readings)
#     total_joules_cm2 = (total_par * 0.217)//10_000  # Convert to J/m²

#     return int(total_joules_cm2)


def accum_temp(temp_max, temp_min, Tbase):
    # Tbase=10 # cucumber

    GDD = round((temp_max + temp_min)/2 - Tbase, 2)
    return GDD


async def vpd_cli_actemp(var):
    while True:
        # calculate VPD
        var.envin_vpd_1 = calculate_vpd(
            int(var.envin_temp_1), int(var.envin_humi_1))
        # calculate accumulated temperature
        var.envin_at_1 = accum_temp(
            int(var.temp_max_1), int(var.temp_min_1), int(var.Tbase_1))
        # # calculate DLI
        # if len(var.buffer_lgt_1) == 5:
        #     var.envin_dli_1 = calculate_dli_from_par_readings(var.buffer_lgt_1)
        await asyncio.sleep(5)
