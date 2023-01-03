
UNITS_ENGLISH = 1
UNITS_METRIC = 2

class SystemState(object):
    def __init__(self):
        self.battery_level = 100
        self.display = True
        self.wireless = True
        # Load from fs
        #f = open("settings.txt")
        self._units = UNITS_ENGLISH
        self._wheel_size = 21.0
        
    def set_units(self, units):
        self._units = units
        # Persist to fs
        
    def get_units(self):
        return self._units
    
    def set_wheel_size(self, wheel_size):
        self._wheel_size = wheel_size
        # Persist to fs
        
    def get_wheel_size(self):
        return self._wheel_size
    