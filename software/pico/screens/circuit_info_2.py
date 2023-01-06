import constants
from screens.screen import Screen
import lib.ssd1309


SCREEN_CIRCUIT_INFO_2 = "circuit-info-2"


class CircuitInfo2(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_CIRCUIT_INFO_2, display, fonts)
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
        
        # Current speed
        self.display.draw_text(60, 12, "Circuit 2", self.fonts["medium"])

        self.display.present()
        pass



