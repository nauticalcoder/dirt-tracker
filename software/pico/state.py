
UNITS_ENGLISH = 1
UNITS_METRIC = 2

class SystemState(object):
    def __init__(self):
        self.battery_level = 100
        self.display = True
        self.wireless = True
        self.units = UNITS_ENGLISH
        self.wheel_size = 21
        
    
    
