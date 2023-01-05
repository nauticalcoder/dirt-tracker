

class Distance(object):
    def __init__(self, logging = False):
        self.logging = logging
        self.distance_traveled_since_last_update = None
    
    def get_distance_traveled_since_last_update(self):
        return self.distance_traveled_since_last_update
        
    
