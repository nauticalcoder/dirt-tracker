from screen import Screen

SCREEN_UPLOAD_ENDURO_ROUTE = "upload_enduro_route"
SCREEN_MAIN = "main"

class Main(Screen):
    def __init__(self):
        super().__init__(SCREEN_MAIN)
    
    def render(self):
        #return
        print(f"Screen {self.name}")
         