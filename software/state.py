
class Transition(object):
    def __init__(self, *states):
        self.source = states[0]
        self.destinations = states[1:]
        #self.identifier = options.get('identifier')
        #self.validators = options.get('validators', [])
        #self.on_execute = options.get('on_execute')
    
    
class State(object):
    def __init__(self, name, value=None, initial=False):
        self.name = name
        self.value = value if value else name
        self._initial = initial
        #self.identifier = None  # type: Optional[Text]
        #self.transitions = transitions  # type: List[Transition]
        
class StateMachine(object):
     
    def __init__(self, name, *states):
        self.name = name
        self.states = states
        self.states_map = {}
        self.transitions = []
        
        self._populate_state_map()
        
    def _populate_state_map(self):
        for state in self.states:
            self.states_map[state.value] = state
