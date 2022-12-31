

class Display(object):

    def __init__(self, name, height, width, allows_graphics=True):
        self.name = name
        self.height = height
        self.width = width
        self.allows_graphics = allows_graphics

    def __str__(self):
        return f"Display {self.name} {self.width}x{self.height}"
