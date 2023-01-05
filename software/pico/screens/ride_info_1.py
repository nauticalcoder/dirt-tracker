import constants
from screens.screen import Screen
import lib.ssd1309


SCREEN_INFO_1 = "ride-info-1"

class Info1(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_INFO_1, display, fonts)
        if not display:
            return
        # Setup sprites


    def clear(self):
        self.display.clear()
        
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        speed_unit_text = "mph" if system_state.get_units() == constants.UNITS_ENGLISH else "kph"
        distance_unit_text = "miles" if system_state.get_units() == constants.UNITS_ENGLISH else "kms"
        
        if not system_state.display:
            return

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
