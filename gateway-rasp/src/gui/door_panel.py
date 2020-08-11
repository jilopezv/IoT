from kivy.uix.screenmanager import Screen


class DoorsPanel(Screen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'controlpanel'
