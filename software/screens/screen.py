
SCREEN_UPLOAD_ENDURO_ROUTE = "upload_enduro_route"
SCREEN_MAIN = "main"


class Screen(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Screen {self.name}"

    def render(self):
        print(f"Screen {self.name}")
