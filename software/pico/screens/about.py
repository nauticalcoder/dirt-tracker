import constants
from screens.screen import Screen
import lib.ssd1309


SCREEN_ABOUT = "about"


class About(Screen):
    
    def __init__(self, display, fonts):
        super().__init__(SCREEN_ABOUT, display, fonts)
        if not display:
            return
        # Setup sprites
        #self.wireless_sprite = display.load_sprite(f"sprites/wireless.mono", 20, 20, invert=True)
        #self.battery_1_sprite = display.load_sprite(f"sprites/battery_1.mono", 20, 20, invert=True)
        #self.battery_2_sprite = display.load_sprite(f"sprites/battery_2.mono", 20, 20, invert=True)
        #self.battery_3_sprite = display.load_sprite(f"sprites/battery_3.mono", 20, 20, invert=True)
        #self.battery_4_sprite = display.load_sprite(f"sprites/battery_4.mono", 20, 20, invert=True)

    def render(self, ride_state, system_state):
        super().render(ride_state, system_state)

        if not system_state.display:
            return
        #if system_state.wireless:
        #    self.display.draw_sprite(self.wireless_sprite, 1, 1, 20, 20)
        #if system_state.battery_level < 25:
        #    self.display.draw_sprite(self.battery_1_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level < 50:
        #    self.display.draw_sprite(self.battery_2_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level < 75:
        #    self.display.draw_sprite(self.battery_3_sprite, 108, 1, 20, 20)
        #elif system_state.battery_level <= 100:
        #    self.display.draw_sprite(self.battery_4_sprite, 108, 1, 20, 20)
        small_text_width = self.fonts["small"].width
        text_height = self.fonts["medium"].height
        text_width = self.fonts["medium"].width
        large_text_width = self.fonts["large"].width
        
        self.display.draw_text(10, 12, constants.APP_NAME, self.fonts["small"])
        self.display.draw_text(10, 22, f"Version {constants.VERSION}", self.fonts["small"])
        self.display.draw_text(10, 32, f"Display {constants.SCREEN_WIDTH}x{constants.SCREEN_HEIGHT}", self.fonts["small"])
        self.display.draw_text(10, 42, f"(c) 2023", self.fonts["small"])        
        self.display.draw_text(10, 52, f"Iron Goat Software", self.fonts["small"])
        
        self.display.present()
        pass

