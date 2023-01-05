from gadgets.status_bar import StatusBar

SCREEN_UPLOAD_ENDURO_ROUTE = "upload_enduro_route"
SCREEN_MAIN = "main"
SCREEN_INFO_1 = "info-1"
SCREEN_INFO_2 = "info-2"
SCREEN_MODE_SELECT = "mode-select"


class Screen(object):

    def __init__(self, name, display, fonts):
        self.name = name
        self.display = display
        self.fonts = fonts
        
        self.display.clear()

    def __str__(self):
        return f"Screen {self.name}"

    def render(self, state, system_state):
        
        #print(f"Screen {self.name}")
        
        if not system_state.display:
            return
        
        StatusBar(self.display, self.fonts).render(system_state)
        
        
    def format_time(self, time_delta):
        return str(time_delta)