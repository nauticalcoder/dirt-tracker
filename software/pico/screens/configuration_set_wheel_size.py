from screens.screen import Screen

CONFIGURATION_SET_WHEEL_SIZE = "configuration-set-wheel-size"


class ConfigurationSetWheelSize(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(CONFIGURATION_SET_WHEEL_SIZE, display, fonts)
        pass
    
    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)
        if not system_state.display:
            return
        
        self.display.draw_text(55, 30, f"{system_state.wheel_size:.1f}", self.fonts["small"])
        self.display.present()
        pass
        
