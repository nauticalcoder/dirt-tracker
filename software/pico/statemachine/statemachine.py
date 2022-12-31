from .exceptions import (
    StateMachineError,
    InvalidDefinition,
    InvalidStateValue,
    InvalidDestinationState,
    InvalidTransitionIdentifier,
    TransitionNotAllowed,
    MultipleStatesFound,
    MultipleTransitionCallbacksFound,
)

class Transition(object):
    def __init__(self, *states, **options):
            self.source = states[0]
            self.destinations = states[1:]
            self.identifier = options.get('identifier')
            self.validators = options.get('validators', [])
            self.on_execute = options.get('on_execute')

    def __repr__(self):
        return "{}({!r}, {!r}, identifier={!r})".format(
            type(self).__name__, self.source, self.destinations, self.identifier)
    
    def _set_identifier(self, identifier):
        self.identifier = identifier

class State(object):

    def __init__(self, name, value=None, initial=False):
        # type: (Text, Optional[V], bool) -> None
        self.name = name
        self.value = value
        self._initial = initial
        self.identifier = None  # type: Optional[Text]
        self.transitions = []  # type: List[Transition]

    def __repr__(self):
        return "{}({!r}, identifier={!r}, value={!r}, initial={!r})".format(
            type(self).__name__, self.name, self.identifier, self.value, self.initial
        )

    def _set_identifier(self, identifier):
        self.identifier = identifier
        if self.value is None:
            self.value = identifier

    def _to_(self, *states):
        transition = Transition(self, *states)
        self.transitions.append(transition)
        return transition

    def _from_(self, *states):
        combined = None
        for origin in states:
            transition = Transition(origin, self)
            origin.transitions.append(transition)
            if combined is None:
                combined = transition
            else:
                combined |= transition
        return combined

    def _get_proxy_method_to_itself(self, method):
        def proxy(*states):
            return method(*states)

        def proxy_to_itself():
            return proxy(self)

        proxy.itself = proxy_to_itself
        return proxy

    @property
    def to(self):
        return self._get_proxy_method_to_itself(self._to_)

    @property
    def from_(self):
        return self._get_proxy_method_to_itself(self._from_)

    @property
    def initial(self):
        return self._initial


def check_state_factory(state):
    "Return a property that checks if the current state is the desired state"
    @property
    def is_in_state(self):
        # type: (BaseStateMachine) -> bool
        return bool(self.current_state == state)
    return is_in_state


class Model():

    def __init__(self):
        self.state = None  # type: Optional[V]

    def __repr__(self):
        return 'Model(state={})'.format(self.state)


class StateMachineMetaclass(type):

    def __init__(cls, name, bases, attrs):
#        super(StateMachineMetaclass, cls).__init__(name, bases, attrs)
#         registry.register(cls)
        cls.states = []
        cls.transitions = []
        cls.states_map = {}
        cls.add_inherited(bases)
        cls.add_from_attributes(attrs)

        for state in cls.states:
            setattr(cls, 'is_{}'.format(state.identifier), check_state_factory(state))

    def add_inherited(cls, bases):
        for base in bases:
            for state in getattr(base, 'states', []):
                cls.add_state(state.identifier, state)
            for transition in getattr(base, 'transitions', []):
                cls.add_transition(transition.identifier, transition)

    def add_from_attributes(cls, attrs):
        for key, value in sorted(attrs.items(), key=lambda pair: pair[0]):
            if isinstance(value, State):
                cls.add_state(key, value)
            elif isinstance(value, Transition):
                cls.add_transition(key, value)

    def add_state(cls, identifier, state):
        state._set_identifier(identifier)
        cls.states.append(state)
        cls.states_map[state.value] = state

    def add_transition(cls, identifier, transition):
        transition._set_identifier(identifier)
        cls.transitions.append(transition)
        
        
class BaseStateMachine(object):

    transitions = []  # type: List[Transition]
    states = []  # type: List[State]
    states_map = {}  # type: Dict[Any, State]

    def __init__(self, model=None, state_field='state', start_value=None):
        # type: (Any, str, Optional[V]) -> None
        self.model = model if model else Model()
        self.state_field = state_field
        self.start_value = start_value

        self.check()

    def __repr__(self):
        return "{}(model={!r}, state_field={!r}, current_state={!r})".format(
            type(self).__name__, self.model, self.state_field,
            self.current_state.identifier,
        )
    
    @property
    def current_state_value(self):
        # type: () -> V
        value = getattr(self.model, self.state_field, None)  # type: V
        return
    
    @current_state_value.setter
    def current_state_value(self, value):
        # type: (V) -> None
        if value not in self.states_map:
            raise InvalidStateValue(value)
        setattr(self.model, self.state_field, value)
        
    @property
    def current_state(self):
        # type: () -> State
        return self.states_map[self.current_state_value]
    
    @current_state.setter
    def current_state(self, value):
        self.current_state_value = value.value
        
    def check(self):
        if not self.states:
            raise InvalidDefinition('There are no states.')

        if not self.transitions:
            raise InvalidDefinition('There are no transitions.')

        initials = [s for s in self.states if s.initial]
        if len(initials) != 1:
            raise InvalidDefinition('There should be one and only one initial state. '
                                      'Your currently have these: {!r}'.format(initials))
        self.initial_state = initials[0]

        disconnected_states = self._disconnected_states(self.initial_state)
        if (disconnected_states):
            raise InvalidDefinition('There are unreachable states. '
                                    'The statemachine graph should have a single component. '
                                      'Disconnected states: [{}]'.format(disconnected_states))

        if self.current_state_value is None:
            if self.start_value:
                self.current_state_value = self.start_value
            else:
                self.current_state_value = self.initial_state.value


StateMachine = StateMachineMetaclass('StateMachine', (BaseStateMachine, ), {})