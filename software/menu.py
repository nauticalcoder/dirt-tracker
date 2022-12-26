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
        pass
    def handle_input(self):
        pass


class InfoMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_INFO
        self.index = 0

    def handle_input(self):
        pass


class ChangeModesMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_CHANGE_MODES
        self.selected_menu_item = 0

    def handle_input(self):
        pass


class ConfigurationMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_CONFIGURATION
        self.selected_menu_item = 0

    def handle_input(self):
        pass


class LoadRouteSheetMenuState(MenuState):
    def __init__(self):
        self.value = MENU_STATE_LOAD_ROUTE_SHEET
        self.selected_menu_item = 0

    def handle_input(self):
        pass


class Menu(object):
    def __init__(self):
        self.states = stack.Stack()
        self.states.push(InfoMenuState())

