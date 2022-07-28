from kivymd.uix.screen import MDScreen


class CameraPanel(MDScreen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'controlpanel'
