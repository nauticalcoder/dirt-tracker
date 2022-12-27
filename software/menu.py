import buttons
from screens import info_1, info_2, mode_select, configuration_select
import stack

MENU_STATE_INFO = "info"
MENU_STATE_CHANGE_MODES = "change-modes"
MENU_STATE_CONFIGURATION = "configuration"
MENU_STATE_LOAD_ROUTE_SHEET = "load-route-sheet"


# class MenuItem(object):
#     def __init__(self, name):
#         items = []

class MenuState(object):
    def __init__(self, display, fonts):
        self.value = None
        self._screens = []
        self._screen = None
        self.display = display
        self.fonts = fonts
        pass
    
    def handle_input(self, button, action):
        #print(f"Handle Input {button} {action}")
        pass
    
    def get_screen(self):
        pass


class InfoMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_INFO
        self._index = 0
        #self._screens = []
        self._screens.append(info_1.Info1(display, fonts))
        self._screens.append(info_2.Info2(display, fonts))

        self.speed = 0
        self.average_speed = 0
        self.distance_traveled = 0

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
            return ChangeModesMenuState(self.display, self.fonts)
        pass


class ChangeModesMenuState(MenuState):
    # Get these from the screen
    menu_items = ["Start Circuit Race", "Start Enduro Race", "Configuration", "Back"]
    
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_CHANGE_MODES
        self.selected_menu_item = 0
        self._index = 0
        self._screens.append(mode_select.ModeSelect(display, fonts))
        
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action):
        super().handle_input(button, action)
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Next menu item
            self._cycle_menu_item()
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 2 - Select
            switch = {
                0: None,  # TODO figure out how to initiate secondary FSM for each mode - Ride Mode,
                1: None,  # TODO figure out how to initiate secondary FSM for each mode - Circuit Mode,
                2: None,  # TODO figure out how to initiate secondary FSM for each mode - Enduro Mode,
                3: ConfigurationMenuState(self.display, self.fonts),
                4: Pop()
            }
            return switch[self.selected_menu_item]
        pass
    
    def _cycle_menu_item(self):
        self.selected_menu_item += 1
        if self.selected_menu_item >= len(self.menu_items):
            self.selected_menu_item = 0
        print(self.selected_menu_item)


class ConfigurationMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_CONFIGURATION
        self.selected_menu_item = 0
        self._index = 0
        self._screens.append(configuration_select.ConfigurationSelect(display, fonts))
    
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action):
        super().handle_input(button, action)
        pass


class LoadRouteSheetMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_LOAD_ROUTE_SHEET
        self.selected_menu_item = 0
        # self._screens = []

    def handle_input(self, button, action):
        MenuState.handle_input(self, button, action)
        pass


class Pop(MenuState):
    def __init__(self):
        pass


class Menu(object):
    def __init__(self, display, fonts):
        self.state_stack = stack.Stack()
        self.state_stack.push(InfoMenuState(display, fonts))
    
    def _to(self, state):
        self.state_stack.push(state)
        
    def handle_input(self, button, action):
        new_state = self.state_stack.peek().handle_input(button, action)
        #print(f"Handle Input {new_state}")
        if isinstance(new_state, Pop):
            self.state_stack.pop()
        elif new_state:
            self._to(new_state)
            
    def get_screen(self):
        return self.state_stack.peek().get_screen()

    def render(self):
        #print(self.state_stack.length())
    
        self.get_screen().render(self.state_stack.peek())
