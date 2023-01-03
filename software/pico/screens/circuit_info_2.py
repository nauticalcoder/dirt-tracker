from screens.screen import Screen

SCREEN_INFO_2 = "info-2"

UNITS_ENGLISH = 1
UNITS_METRIC = 2

class Info2(Screen):
    # Race
    def __init__(self, display, fonts):
        super().__init__(SCREEN_INFO_2, display, fonts)
        if not display:
            return
        # Setup sprites
        self.wireless_sprite = display.load_sprite(f"sprites/wireless.mono", 20, 20, invert=True)
        self.battery_1_sprite = display.load_sprite(f"sprites/battery_1.mono", 20, 20, invert=True)
        self.battery_2_sprite = display.load_sprite(f"sprites/battery_2.mono", 20, 20, invert=True)
        self.battery_3_sprite = display.load_sprite(f"sprites/battery_3.mono", 20, 20, invert=True)
        self.battery_4_sprite = display.load_sprite(f"sprites/battery_4.mono", 20, 20, invert=True)
        
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        unit_text = "miles" if system_state.get_units() == UNITS_ENGLISH else "kilometers"
        print(unit_text)
        if not system_state.display:
            return
        if system_state.wireless:
            self.display.draw_sprite(self.wireless_sprite, 1, 1, 20, 20)
        if system_state.battery_level < 25:
            self.display.draw_sprite(self.battery_1_sprite, 108, 1, 20, 20)
        elif system_state.battery_level < 50:
            self.display.draw_sprite(self.battery_2_sprite, 108, 1, 20, 20)
        elif system_state.battery_level < 75:
            self.display.draw_sprite(self.battery_3_sprite, 108, 1, 20, 20)
        elif system_state.battery_level <= 100:
            self.display.draw_sprite(self.battery_4_sprite, 108, 1, 20, 20)
            
        text_height = self.fonts["bally"].height
        self.display.draw_text(self.display.width, self.display.height // 2 - text_height // 2, str(ride_state.current_speed), self.fonts["bally"])
        self.display.draw_text(0, self.display.height // 2 - text_height // 2, unit_text, self.fonts["bally"])
        self.display.draw_text(self.display.width, self.display.height // 2 - text_height // 2, str(ride_state.distance_traveled), self.fonts["bally"])
        self.display.draw_text(0, self.display.height // 2 - text_height // 2, unit_text, self.fonts["bally"])
        self.display.draw_text(self.display.width, self.display.height // 2 - text_height // 2, str(ride_state.elapsed_time), self.fonts["bally"])
        self.display.draw_text(0, self.display.height // 2 - text_height // 2, unit_text, self.fonts["bally"])
        self.display.present()
        pass
