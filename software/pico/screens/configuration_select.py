from screens.screen import Screen

CONFIGURATION_SELECT = "configuration-select"


class ConfigurationSelect(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(CONFIGURATION_SELECT, display, fonts)
        pass
    
    def render(self, menu_state, system_state):
        super().render(menu_state, system_state)
        if not system_state.display:
            return

        self.display.draw_text(10, 12, "Load Route", self.fonts["small"], invert=(menu_state.selected_menu_item == 0))
        self.display.draw_text(10, 21, "Wheel Size", self.fonts["small"], invert=(menu_state.selected_menu_item == 1))
        self.display.draw_text(10, 30, "Set Units", self.fonts["small"], invert=(menu_state.selected_menu_item == 2))
        self.display.draw_text(10, 39, "About", self.fonts["small"], invert=(menu_state.selected_menu_item == 3))
        self.display.draw_text(10, 49, "Back", self.fonts["small"], invert=(menu_state.selected_menu_item == 4))

        self.display.present()
        pass
        


        


