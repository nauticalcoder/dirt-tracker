import buttons
from datetime import datetime
from screens import about, load_route, ride_info_1, ride_info_2, mode_select, configuration_select, configuration_set_units, configuration_set_wheel_size 
import stack

MENU_STATE_INFO = "info"
MENU_STATE_CHANGE_MODES = "change-modes"
MENU_STATE_CONFIGURATION = "configuration"
MENU_STATE_LOAD_ROUTE_SHEET = "load-route-sheet"
MENU_STATE_SET_UNITS = "set-units"
MENU_STATE_WHEEL_SIZE = "wheel-size"
MENU_STATE_ABOUT = "about"

UNITS_ENGLISH = 1
UNITS_METRIC = 2
WHEEL_SIZE_MINUMUM = 16.0
WHEEL_SIZE_MAXIMUM = 20.0
WHEEL_SIZE_INCREMENT = 0.2

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
    
    def handle_input(self, button, action, system_state):
        #print(f"Handle Input {button} {action}")
        pass
    
    def get_screen(self):
        pass



class ChangeModesMenuState(MenuState):
    # Get these from the screen
    menu_items = ["Ride Mode", "Start Circuit Race", "Start Enduro Race", "Configuration", "Back"]
    
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_CHANGE_MODES
        self.selected_menu_item = 0
        self._index = 0
        self._screens.append(mode_select.ModeSelect(display, fonts))
        
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
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
                4: Pop(self.display)
            }
            return switch[self.selected_menu_item]
        pass
    
    def _cycle_menu_item(self):
        self.selected_menu_item += 1
        if self.selected_menu_item >= len(self.menu_items):
            self.selected_menu_item = 0
        print(self.selected_menu_item)



class InfoMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_INFO
        self._index = 0
        #self._screens = []
        self._screens.append(ride_info_1.Info1(display, fonts))
        self._screens.append(ride_info_2.Info2(display, fonts))

        self.current_speed = 14.2
        self.average_speed = 0
        self.distance_traveled = 7.8
        self.elapsed_time = datetime.timedelta(seconds = 14, minutes = 10)
        
    def _cycle_screen(self):
        self._index += 1
        if self._index >= len(self._screens):
            self._index = 0
        
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        #print(f"Handle input InfoMenuState {button} {action}")
        #print(f"Handle input InfoMenuState {buttons.COMMAND_BUTTON_1} {buttons.COMMAND_BUTTON_ACTION_SHORTPRESS}")
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Cycle
            self._cycle_screen()
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_LONGPRESS:
            # Button 2 Long Press - Change Modes
            return ChangeModesMenuState(self.display, self.fonts)
        pass


class ConfigurationMenuState(MenuState):
    menu_items = ["Load Route Sheet", "Set Wheel Size", "Set Units", "About", "Back"]
   
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_CONFIGURATION
        self.selected_menu_item = 0
        self._index = 0
        self._screens.append(configuration_select.ConfigurationSelect(display, fonts))
    
    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Next menu item
            self._cycle_menu_item()
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 2 - Select
            switch = {
                0: LoadRouteSheetMenuState(self.display, self.fonts),
                1: SetWheelSizeMenuState(self.display, self.fonts),
                2: SetUnitsMenuState(self.display, self.fonts),
                3: AboutMenuState(self.display, self.fonts),
                4: Pop(self.display)
            }
            return switch[self.selected_menu_item]
        pass

    def _cycle_menu_item(self):
            self.selected_menu_item += 1
            if self.selected_menu_item >= len(self.menu_items):
                self.selected_menu_item = 0
            print(self.selected_menu_item)

class LoadRouteSheetMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_LOAD_ROUTE_SHEET
        self._index = 0
        self._screens.append(load_route.LoadRoute(display, fonts))
        self.selected_menu_item = 0

    def get_screen(self):
        return self._screens[self._index]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            return Pop(self.display)
        pass


class SetUnitsMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_SET_UNITS
        self._screens.append(configuration_set_units.ConfigurationSetUnits(display, fonts))
    
    def get_screen(self):
        return self._screens[0]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - Next unit
            if system_state.units == UNITS_ENGLISH:
                system_state.units = UNITS_METRIC
            else:
                system_state.units = UNITS_ENGLISH
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            return Pop(self.display)
        pass

class SetWheelSizeMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_WHEEL_SIZE
        self._screens.append(configuration_set_wheel_size.ConfigurationSetWheelSize(display, fonts))
    
    def get_screen(self):
        return self._screens[0]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        if button == buttons.COMMAND_BUTTON_1 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            # Button 1 - increment wheel size
            system_state.wheel_size += WHEEL_SIZE_INCREMENT
            if system_state.wheel_size > WHEEL_SIZE_MAXIMUM:
                system_state.wheel_size = WHEEL_SIZE_MINUMUM
                
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            return Pop(self.display)
        pass
    
class AboutMenuState(MenuState):
    def __init__(self, display, fonts):
        super().__init__(display, fonts)
        self.value = MENU_STATE_ABOUT
        self._screens.append(about.About(display, fonts))
    
    def get_screen(self):
        return self._screens[0]
    
    def handle_input(self, button, action, system_state):
        super().handle_input(button, action, system_state)
        if button == buttons.COMMAND_BUTTON_2 and action == buttons.COMMAND_BUTTON_ACTION_SHORTPRESS:
            return Pop(self.display)
        pass
    
class Pop(MenuState):
    def __init__(self, display):
        display.clear()
        pass


class Menu(object):
    def __init__(self, display, fonts):
        self.state_stack = stack.Stack()
        self.state_stack.push(InfoMenuState(display, fonts))
    
    def _to(self, state):
        self.state_stack.push(state)
        
    def handle_input(self, button, action, system_state):
        new_state = self.state_stack.peek().handle_input(button, action, system_state)
        #print(f"Handle Input {new_state}")
        if isinstance(new_state, Pop):
            self.state_stack.pop()
        elif new_state:
            self._to(new_state)
            
    def get_screen(self):
        return self.state_stack.peek().get_screen()

    def render(self, system_state):
        #print(self.state_stack.length())
        self.get_screen().render(self.state_stack.peek(), system_state)

