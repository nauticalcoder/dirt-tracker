from screens.screen import Screen

SCREEN_MODE_SELECT = "mode-select"


class ModeSelect(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_MODE_SELECT, display, fonts)
    
    def render(self, menu_state, system_state):
        super().render(menu_state, system_state)
        if not system_state.display:
            return

        self.display.draw_text(4, 12, "Ride", self.fonts["small"], invert=(menu_state.selected_menu_item == 0))
        self.display.draw_text(4, 21, "Circuit", self.fonts["small"], invert=(menu_state.selected_menu_item == 1))
        self.display.draw_text(4, 30, "Enduro", self.fonts["small"], invert=(menu_state.selected_menu_item == 2))
        self.display.draw_text(4, 39, "Configuration", self.fonts["small"], invert=(menu_state.selected_menu_item == 3))
        self.display.draw_text(4, 49, "Back", self.fonts["small"], invert=(menu_state.selected_menu_item == 4))

        self.display.present()
        pass
        

