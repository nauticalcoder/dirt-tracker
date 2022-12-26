DEFAULT_SIZE = 10


class Stack:

    def __init__(self, size = DEFAULT_SIZE):
        self.max_size = size
        self._stack = []

    def push(self, item):
        if len(self._stack) >= self.max_size:
            self._stack.pop()
        self._stack.insert(0, item)

    def pop(self):
        if len(self._stack) <= 0:
            return None
        return self._stack.pop(0)

    def peek(self):
        if len(self._stack) <= 0:
            return None
        return self._stack[0]