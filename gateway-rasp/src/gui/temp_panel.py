from kivy.uix.screenmanager import Screen


class TemperaturePanel(Screen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'controlpanel'
