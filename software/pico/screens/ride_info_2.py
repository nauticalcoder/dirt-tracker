from gadgets.late_early_bar import LateEarlyBar
from screens.screen import Screen

SCREEN_INFO_2 = "info-2"

UNITS_ENGLISH = 1
UNITS_METRIC = 2

class Info2(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_INFO_2, display, fonts)
        if not display:
            return
        # Setup sprites
    
    def clear(self):
        self.display.clear()
      
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        speed_unit_text = "mph" if system_state.get_units() == UNITS_ENGLISH else "kph"
        if not system_state.display:
            return
            
        small_text_width = self.fonts["small"].width
        text_height = self.fonts["medium"].height
        text_width = self.fonts["medium"].width
        large_text_width = self.fonts["large"].width
        
        # Current speed
        #self.display.draw_text(60, 12, str(ride_state.current_speed), self.fonts["large"])
        #self.display.draw_text(60 + large_text_width * 4, 24, speed_unit_text, self.fonts["small"])
        #self.display.draw_rectangle(58, 12, 70, 22)
        
        LateEarlyBar().render(self.display, -10, 20, 52, 90)
        
        self.display.present()
        pass
        
