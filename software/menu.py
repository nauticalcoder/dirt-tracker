import buttons
from screens import info_1, info_2, mode_select
import stack

MENU_STATE_INFO = "info"
MENU_STATE_CHANGE_MODES = "change-modes"
MENU_STATE_CONFIGURATION = "configuration"
MENU_STATE_LOAD_ROUTE_SHEET = "load-route-sheet"


# class MenuItem(object):
#     def __init__(self, name):
#         items = []

class MenuState(object):
    def __init__(self):
        self.value = None
        self._screens = []
        self._screen = None
        pass
    
    def handle_input(self, button, action):
        #print(f"Handle Input {button} {action}")
        pass


class InfoMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_INFO
        self._index = 0
        self._screens = []
        self._screens.append(info_1.Info1())
        self._screens.append(info_2.Info2())
    
    def _cycle_screen(self):
        #print(f"Cycle screen B {self._index}")
        self._index += 1
        if self._index >= len(self._screens):
            self._index = 0
        #print(f"Cycle screen A {self._index}")
       
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action):
        super().handle_input(button, action)
        #print(f"Handle input InfoMenuState {button} {action}")
        #print(f"Handle input InfoMenuState {buttons.COMMAND_BUTTON_1} {buttons.COMMAND_BUTTON_ACTION_SHORTPRESS}")
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Cycle
            self._cycle_screen()
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_LONGPRESS:
            # Button 2 Long Press - Change Modes
            return ChangeModesMenuState()
        pass


class ChangeModesMenuState(MenuState):
    # Get these from the screen
    menu_items = ["Start Circuit Race", "Start Enduro Race", "Configuration", "Back"]
    
    def __init__(self):
        self.value = MENU_STATE_CHANGE_MODES
        self.selected_menu_item = 0
        
        self._index = 0
        self._screens = []
        self._screens.append(mode_select.ModeSelect())
        
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action):
        super().handle_input(button, action)
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Next menu item
            self._cycle_screen()
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 2 - Select
            self._cycle_screen()
        pass
    
    def _cycle_menu_item(self):
        self.selected_menu_item += 1
        if self.selected_menu_item >= len(menu_items):
            self.selected_menu_item = 0
        print(self.selected_menu_item)

class ConfigurationMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_CONFIGURATION
        self.selected_menu_item = 0
        self._screens = []

    def handle_input(self, button, action):
        super().handle_input(button, action)
        pass


class LoadRouteSheetMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_LOAD_ROUTE_SHEET
        self.selected_menu_item = 0
        self._screens = []

    def handle_input(self, button, action):
        MenuState.handle_input(self, button, action)
        pass


class Menu(object):
    def __init__(self):
        self.states = stack.Stack()
        self.states.push(InfoMenuState())
    
    def _to(self, state):
        self.states.push(state)
        
    def handle_input(self, button, action):
        new_state = self.states.peek().handle_input(button, action)
        if new_state:
            self._to(new_state)
            
    def get_screen(self):
        return self.states.peek().get_screen()

