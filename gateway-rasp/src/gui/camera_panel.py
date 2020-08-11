from kivy.uix.screenmanager import Screen


class CameraPanel(Screen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'controlpanel'
