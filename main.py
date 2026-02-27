from direct.showbase.ShowBase import ShowBase

class App(ShowBase):
    def __init__(self):
        super().__init__()
        self.setBackgroundColor(0.1, 0.1, 0.12, 1)

App().run()