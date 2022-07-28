from kivymd.uix.screen import MDScreen


class LookoutPanel(MDScreen):

    def __init__(self, home, **kw):
        super().__init__(**kw)
        self.home = home

    def toggle(self):
        """ This is the lookout function
        Callback for the 'lookout' button
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
