from screens.screen import Screen

SCREEN_MODE_SELECT = "mode-select"


class ConfigurationSelect(Screen):
    
    def __init__(self, fonts, display):
        super().__init__(SCREEN_MODE_SELECT, display, fonts)
        pass
        


