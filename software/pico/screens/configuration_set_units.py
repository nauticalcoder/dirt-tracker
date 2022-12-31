from screens.screen import Screen

CONFIGURATION_SET_UNITS = "configuration-set-units"


class ConfigurationSetUnits(Screen):
    
    def __init__(self, fonts, display):
        super().__init__(CONFIGURATION_SET_UNITS, display, fonts)
        pass
    
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        print(f"Units: {system_state.units}")
        if not system_state.display:
            return
        
        text_height = self.fonts["bally"].height
        unit_text = "English" if system_state.units == UNITS_ENGLISH else "Metric"
        self.display.draw_text(self.display.width, self.display.height // 2 - text_height // 2, unit_text, self.fonts["bally"])
        self.present()
        pass
        


