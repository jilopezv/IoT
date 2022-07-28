from kivymd.uix.screen import MDScreen


class MovementPanel(MDScreen):

    def toggle(self):
        pass

    def regresar(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'controlpanel'
