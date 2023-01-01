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
        speed_unit_text = "mph" if system_state.units == UNITS_ENGLISH else "kph"
        distance_unit_text = "miles" if system_state.units == UNITS_ENGLISH else "kms"
        
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
              
        text_height = self.fonts["bally"].height
        text_width = self.fonts["bally"].width
        
        # Current speed
        self.display.draw_text(80, 20, str(ride_state.current_speed), self.fonts["bally"])
        self.display.draw_text(80 + text_width * 4, 20, speed_unit_text, self.fonts["bally"])
        
        # Distance traveled
        self.display.draw_text(50, 50, str(ride_state.distance_traveled), self.fonts["bally"])
        self.display.draw_text(50 + text_width * 3, 50, distance_unit_text, self.fonts["bally"])
        
        # Elapsed time
        self.display.draw_text(10, 25, str(ride_state.elapsed_time), self.fonts["bally"])
        #self.display.draw_text(30, 25 - text_height // 2, unit_text, self.fonts["bally"])
        
        self.display.present()
        pass
