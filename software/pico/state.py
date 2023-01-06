import constants
import time

class SystemState(object):
    def __init__(self):
        self.battery_level = 100
        self.display = True
        self.wireless = True
        # Load from fs
        #f = open("settings.txt")
        self._units = constants.UNITS_ENGLISH
        self._wheel_size = 21.0
        
        self._odometer_lifetime = 0.0
        self._odometer_last_persisted_timestamp = None
            
        self.gps_enabled = True
        self.bluetooth_enabled = False
        
    
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
    
    def set_odometer_lifetime(self, units, persist = False):
        self._units = _odometer_lifetime
        if persist:
            _odometer_last_persisted_timestamp = time.ticks_ms()
            # Persist to fs
        
    def get_odometer_lifetime(self):
        return self._odometer_lifetime
    
    
    