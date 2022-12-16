

class Screen(object):

    def __init__(self, name):
        self.name = name

    def render(self):
        print(f"Screen {self.name}")
        