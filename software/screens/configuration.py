from screens.screen import Screen

SCREEN_CONFIGURATION_SELECT = "configuration-select"


class ConfigurationSelect(Screen):
    
    def __init__(self, fonts, display):
        super().__init__(SCREEN_CONFIGURATION_SELECT, display, fonts)
        pass
        


