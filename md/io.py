import  pyb 
# NEED TO CHANGE FOR OTHER HOUSE
# _1":


class GPIOController:
    def __init__(self):
        # Define GPIO pin mappings with user-friendly names
        self.pin_mappings = {
            # side windows (측창)
            # 1f (좌측)/우측

            "sw_1fl_1": "D9",
            "sw_1fl_c_1": "D10",
            "sw_1fr_1": "D11",
            "sw_1fr_c_1": "D12",
            # 2f (좌측)/우측

            "sw_2fl_1": "D13",
            "sw_2fl_c_1": "D14",
            "sw_2fr_1": "D15",
            "sw_2fr_c_1": "D16",
            # 3f (좌측)/우측

            # 1f (좌측)/우측
            "cw_1fl_1": "D41",
            "cw_1fl_c_1": "D42",
            "cw_1fr_1": "D43",
            "cw_1fr_c_1": "D44",

            "sw_3fl_1": "D45",
            "sw_3fl_c_1": "D46",
            "sw_3fr_1": "D47",
            "sw_3fr_c_1": "D48",
            # ceiling windows (천창)
            
            # # 2f (좌측)/우측
            # "cw_2fl_1": "D25",
            # "cw_2fl_c_1": "D26",
            # "cw_2fr_1": "D27",
            # "cw_2fr_c_1": "D28",
            # # 3f (좌측)/우측
            # "cw_3fl_1": "D29",
            # "cw_3fl_c_1": "D30",
            # "cw_3fr_1": "D31",
            # "cw_3fr_c_1": "D32",

            # Ac Actuators
            # 유동팬 1
            "ef_1": "D57",  # 배기팬
            "cf_01_1": "D62",
            # "cf_01_fwd_1": "D50",  # 정방향
            # "cf_01_rev_1": "D51",  # 역방향
            # 유동팬 2
            #"cf_02_1": "D52",
            # "cf_02_fwd_1": "D53",  # 정방향
            # "cf_02_rev_1": "D54",  # 역방향

         
            # "wc_1": "D56",  # 수막
            # "co2_1": "D57",  # CO₂
            # "fv_1": "D59",  # 포그밸브
            # "sl_1": "D60",  # 보광등
            # "if_1": "D61",  # 흡기팬

            

        }

        self.init_gpio_pins()

    # THIS METHOD IS TO CHECK THE --AVAILABILITY OF THE PINS --
    def init_gpio_pins(self):
        for pin_name in self.pin_mappings:
            pin_id = self.pin_mappings[pin_name]
            try:
                pin = pyb.Pin(pin_id, mode=pyb.Pin.OUT_PP)  # Set pin as output
                pin.value(0)  # Set pin to LOW state
                # pin.off()  # Set pins initially to OFF state
                print(f"Initialized pin {pin_name} ({pin_id}) {pin.value(0)}successfully.")
            except ValueError as e:
                print(f"Error initializing pin {pin_name} ({pin_id}): {e}")

    # THIS METHOD IS TO -- TUREN--ON--
    def turn_on_pins(self, pin_name):
        
        pin_id = self.pin_mappings.get(pin_name)
        if pin_id:
            pin = pyb.Pin(pin_id, mode=pyb.Pin.OUT_PP)  # Set pin as output
            pin.value(1)
            # pin.on()
            print(f'{pin_id},is ON {pin.value(1)}')

    # THIS METHOD IS TO -- TUREN--OFF--
    def turn_off_pins(self, pin_name):
        pin_id = self.pin_mappings.get(pin_name)
        if pin_id:
            pin = pyb.Pin(pin_id, mode=pyb.Pin.OUT_PP)  # Set pin as output
            # pin.off()
            pin.value(0)
            print(f'{pin_id},is OFF {pin.value(0)}')
