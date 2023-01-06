UNITS_ENGLISH = 1
UNITS_METRIC = 2

class StatusBar(object):

    def __init__(self, display, fonts):
        if not display:
            return
        self.display = display
        # Setup sprites
        self.sprite_wireless = display.load_sprite("./sprites/wireless.mono", 10, 8, invert=False)
        self.sprite_battery_100 = display.load_sprite("./sprites/charge-100.mono", 5, 10, invert=False)
     
        #self.wireless_sprite = display.load_sprite(f"sprites/wireless.mono", 20, 20, invert=True)
        #self.battery_1_sprite = display.load_sprite(f"sprites/battery_1.mono", 20, 20, invert=True)
        #self.battery_2_sprite = display.load_sprite(f"sprites/battery_2.mono", 20, 20, invert=True)
        #self.battery_3_sprite = display.load_sprite(f"sprites/battery_3.mono", 20, 20, invert=True)
        #self.battery_4_sprite = display.load_sprite(f"sprites/battery_4.mono", 20, 20, invert=True)

    def render(self, system_state):
        speed_unit_text = "mph" if system_state.get_units() == UNITS_ENGLISH else "kph"
        if not system_state.display:
            return
        #self.display.fill_rectangle(0, 0, 128, 10)
        if system_state.wireless:
            self.display.draw_sprite(self.sprite_wireless, 1, 1, 10, 8)
        if system_state.battery_level < 25:
            self.display.draw_sprite(self.sprite_battery_100, 108, 1, 5, 10)
        elif system_state.battery_level < 50:
            self.display.draw_sprite(self.sprite_battery_100, 108, 1, 5, 10)
        elif system_state.battery_level < 75:
            self.display.draw_sprite(self.sprite_battery_100, 108, 1, 5, 10)
        elif system_state.battery_level <= 100:
            self.display.draw_sprite(self.sprite_battery_100, 108, 1, 5, 10)
        