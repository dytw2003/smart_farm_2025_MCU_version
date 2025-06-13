import uasyncio as asyncio
from md.mn_f import mn_control_motors, mn_control_ac

# _1,
# _1',
# _1_flg
# _1)


# side windows
# left right
# 1f

# left
async def sw_crtl_1f_left(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.sw_1fl_1, 'sw_1fl_1', var.sw_1f_lbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# right
async def sw_crtl_1f_right(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.sw_1fr_1, 'sw_1fr_1', var.sw_1f_rbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# 2f
# left
async def sw_crtl_2f_left(var, gpio):
    while True:
        await mn_control_motors(gpio, var, var.sw_2fl_1, 'sw_2fl_1', var.sw_2f_lbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# right


async def sw_crtl_2f_right(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.sw_2fr_1, 'sw_2fr_1', var.sw_2f_rbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# 3f
# left


async def sw_crtl_3f_left(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.sw_3fl_1, 'sw_3fl_1', var.sw_3f_lbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# right


async def sw_crtl_3f_right(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.sw_3fr_1, 'sw_3fr_1', var.sw_3f_rbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# ceiling windows
# left right
# 1f

# left
async def cw_crtl_1f_left(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.cw_1fl_1, 'cw_1fl_1', var.cw_1f_lbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping

# right


async def cw_crtl_1f_right(var, gpio):
    while True:

        await mn_control_motors(gpio, var, var.cw_1fr_1, 'cw_1fr_1', var.cw_1f_rbtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# # 2f
# # left
# async def cw_crtl_2f_left(var, gpio):
#     while True:

#         await mn_control_motors(gpio, var, var.cw_2fl_1, 'cw_2fl_1', var.cw_2f_lbtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping

# # right


# async def cw_crtl_2f_right(var, gpio):
#     while True:

#         await mn_control_motors(gpio, var, var.cw_2fr_1, 'cw_2fr_1', var.cw_2f_rbtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping

# # 3f
# # left


# async def cw_crtl_3f_left(var, gpio):
#     while True:

#         await mn_control_motors(gpio, var, var.cw_3fl_1, 'cw_3fl_1', var.cw_3f_lbtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping

# # right


# async def cw_crtl_3f_right(var, gpio):
#     while True:

#         await mn_control_motors(gpio, var, var.cw_3fr_1, 'cw_3fr_1', var.cw_3f_rbtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping


# AC actuators
# async def mn_control_ac(gpio, var, btn_val, io_pin, auto_mode):
# yudong fan
async def cf_fan_crtl_01(var, gpio):
    while True:

        await mn_control_ac(gpio, var, var.cf_01_1, 'cf_01_1', var.cf_01_ambtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# async def cf_fan_crtl_02(var, gpio):
#     while True:

#         await mn_control_ac(gpio, var, var.cf_02_1, 'cf_02_1', var.cf_02_ambtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping

# fegi fan


async def ef_fan_crtl(var, gpio):
    while True:

        await mn_control_ac(gpio, var, var.ef_1, 'ef_1', var.ef_ambtn_1)
        await asyncio.sleep(1)  # Small delay to prevent tight looping


# # co2
# async def co2_crtl(var, gpio):
#     while True:

#         await mn_control_ac(gpio, var, var.co2_1, 'co2_1', var.co2_ambtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping


# # water curtain
# async def wc_crtl(var, gpio):
#     while True:

#         await mn_control_ac(gpio, var, var.wc_1, 'wc_1', var.wc_ambtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping


# # fog valve
# async def fv_crtl(var, gpio):
#     while True:

#         await mn_control_ac(gpio, var, var.fv_1, 'fv_1', var.fv_ambtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping


# # supplement light
# async def sl_crtl(var, gpio):
#     while True:

#         await mn_control_ac(gpio, var, var.sl_1, 'sl_1', var.sl_ambtn_1)
#         await asyncio.sleep(1)  # Small delay to prevent tight looping
