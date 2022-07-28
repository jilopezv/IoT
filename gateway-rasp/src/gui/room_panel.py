from kivymd.uix.screen import MDScreen


class RoomPanel(MDScreen):

    def __init__(self, container, **kw):
        super().__init__(**kw)
        self.container = container

    def toggleLight(self):
        self.container.home.send_msg_to_device("0", "TOGGLE")

    def showControlPanel(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'controlpanel'
