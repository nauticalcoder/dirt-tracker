from screens.screen import Screen
import lib.ssd1309


SCREEN_INFO_1 = "info-1"

UNITS_ENGLISH = 1
UNITS_METRIC = 2

class Info1(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_INFO_1, display, fonts)
        if not display:
            return
        # Setup sprites
        #self.wireless_sprite = display.load_sprite(f"sprites/wireless.mono", 20, 20, invert=True)
        #self.battery_1_sprite = display.load_sprite(f"sprites/battery_1.mono", 20, 20, invert=True)
        #self.battery_2_sprite = display.load_sprite(f"sprites/battery_2.mono", 20, 20, invert=True)
        #self.battery_3_sprite = display.load_sprite(f"sprites/battery_3.mono", 20, 20, invert=True)
        #self.battery_4_sprite = display.load_sprite(f"sprites/battery_4.mono", 20, 20, invert=True)

    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        speed_unit_text = "mph" if system_state.get_units() == UNITS_ENGLISH else "kph"
        distance_unit_text = "miles" if system_state.get_units() == UNITS_ENGLISH else "kms"
        
        if not system_state.display:
            return
        #if system_state.wireless:
        #    self.display.draw_sprite(self.wireless_sprite, 1, 1, 20, 20)
        #if system_state.battery_level < 25:
        #    self.display.draw_sprite(self.battery_1_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level < 50:
        #    self.display.draw_sprite(self.battery_2_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level < 75:
        #    self.display.draw_sprite(self.battery_3_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level <= 100:
        #    self.display.draw_sprite(self.battery_4_sprite, 108, 1, 20, 20)
        small_text_width = self.fonts["small"].width
        text_height = self.fonts["medium"].height
        text_width = self.fonts["medium"].width
        large_text_width = self.fonts["large"].width
        
        # Top bar
        #self.display.fill_rectangle(0, 0, 128, 10)

        # Current speed
        self.display.draw_text(60, 12, str(ride_state.current_speed), self.fonts["large"])
        self.display.draw_text(60 + large_text_width * 4, 24, speed_unit_text, self.fonts["small"])
        self.display.draw_rectangle(58, 12, 70, 22)
        
        # Distance traveled
        self.display.draw_text(35, 50, str(ride_state.distance_traveled), self.fonts["medium"])
        self.display.draw_text(35 + text_width * 3, 50, distance_unit_text, self.fonts["small"])
        
        # Elapsed time
        self.display.draw_text(5, 25, self.format_time(ride_state.elapsed_time), self.fonts["medium"])
        #self.display.draw_text(30, 25 - text_height // 2, unit_text, self.fonts["bally"])
        
        self.display.present()
        pass
