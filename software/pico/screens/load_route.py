from screens.screen import Screen
import lib.ssd1309


SCREEN_LOAD_ROUTE = "load-route"

SSID = "dirt-tracker"
IP = "192.168.1"

class LoadRoute(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_LOAD_ROUTE, display, fonts)
        if not display:
            return

    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)

        if not system_state.display:
            return

        self.display.draw_text(4, 12, f"SSID: {SSID}" , self.fonts["small"])
        self.display.draw_text(4, 22, f"IP http://{IP}/", self.fonts["small"])
        self.display.draw_text(4, 32, f"  Use your browser", self.fonts["small"])
        self.display.draw_text(4, 42, f"  to load route", self.fonts["small"])        
        
        self.display.present()
        pass


