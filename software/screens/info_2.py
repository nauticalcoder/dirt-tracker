from screen import Screen

SCREEN_INFO_2 = "info-2"


class Info2(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.name = SCREEN_INFO_2
        pass
        