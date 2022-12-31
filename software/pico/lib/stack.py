DEFAULT_SIZE = 10


class Stack:

    def __init__(self, size = DEFAULT_SIZE):
        self.max_size = size
        self._stack = []
    
    def length(self):
        return len(self._stack)
        
    def push(self, item):
        if len(self._stack) >= self.max_size:
            self._stack.pop()
        self._stack.insert(0, item)

    def pop(self):
        if len(self._stack) <= 0:
            return None
        return self._stack.pop(0)

    def peek(self):
        #print(f"Peek length {len(self._stack)}")
        #print(f"Peek {self._stack[0]}")
        #print(f"Peek {self._stack[1]}")
        if len(self._stack) <= 0:
            #print(f"Peek return None {len(self._stack)}")
            return None
        return self._stack[0]