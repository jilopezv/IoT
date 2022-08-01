from kivymd.uix.screen import MDScreen


class RoomPanel(MDScreen):

    def __init__(self, container, **kw):
        super().__init__(**kw)
        self.container = container

    def toggleLight(self):
        # Send code 2 for toggle the light device (id=0)
        self.container.home.send_msg_to_device("0", "2")

    def showControlPanel(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'controlpanel'
