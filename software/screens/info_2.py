from screens.screen import Screen

SCREEN_INFO_2 = "info-2"


class Info2(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_INFO_2, display, fonts)
        #self.name = SCREEN_INFO_2
        pass
        
    def render(self, ride_state):
        #text_height = self.fonts["bally"].height
        #self.display.draw_text(self.display.width, self.display.height // 2 - text_height // 2, "Bally", self.fonts["bally"])
        #self.display.draw_text(0, self.display.height // 2 - text_height // 2, str(ride_state.speed),
        #                       self.fonts["bally"])
        #self.display.draw_text(75, self.display.height // 2 - text_height // 2, str(ride_state.average_speed),
        #                       self.fonts["bally"])
        #self.display.draw_text(125, self.display.height // 2 - text_height // 2, str(ride_state.distance_traveled),
        #                       self.fonts["bally"])
        #self.present()
        pass
