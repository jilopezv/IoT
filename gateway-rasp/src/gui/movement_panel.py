from kivy.uix.screenmanager import Screen


class MovementPanel(Screen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'controlpanel'
