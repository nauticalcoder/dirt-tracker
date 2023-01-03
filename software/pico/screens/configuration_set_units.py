import constants
from screens.screen import Screen

CONFIGURATION_SET_UNITS = "configuration-set-units"


class ConfigurationSetUnits(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(CONFIGURATION_SET_UNITS, display, fonts)
        pass
    
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        if not system_state.display:
            return
        
        unit_text = "English  " if system_state.get_units() == constants.UNITS_ENGLISH else "Metric  "
        self.display.draw_text(50, 30, unit_text, self.fonts["small"])
        self.display.present()
        pass
        


