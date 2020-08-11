from kivy.uix.screenmanager import Screen


class LookoutPanel(Screen):

    def __init__(self, home, **kw):
        super().__init__(**kw)
        self.home = home

    def toggle(self):
        """ This is the lookout function
        Callback for the 'Vigía' button
        Call the toggle_lookout method in Home class to change home state
        """
        self.state = self.home.toggle_lookout()
        if self.state:
            print('red')
        else:
            print('ghost white')

    def regresar(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'controlpanel'
