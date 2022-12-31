from screens.screen import Screen

CONFIGURATION_SELECT = "configuration-select"


class ConfigurationSelect(Screen):
    
    def __init__(self, fonts, display):
        super().__init__(CONFIGURATION_SELECT, display, fonts)
        pass
        


