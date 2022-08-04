from kivymd.uix.screen import MDScreen


class DoorsPanel(MDScreen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'controlpanel'
