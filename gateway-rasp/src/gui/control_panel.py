from time import strftime

from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class ControlPanel(Screen):
    currentTime = StringProperty("NOT SET")
    home_status = StringProperty("shield-off")

    def __init__(self, container, **kw):
        super().__init__(**kw)
        self.container = container
        Clock.schedule_interval(self.update_clock, 1)
        self.container.home.bind(lookout=self.update_home_status)

    def on_enter(self):
        EventLoop.window.clear_color = (.5, .5, .5, 1)

    def update_clock(self, *args):
        self.currentTime = strftime('%H:%M:%S %p')

    def toggle_lookout(self):
        self.container.home.toggle_lookout()

    def update_home_status(self, *args):
        lookout = args[1]
        if lookout:
            self.home_status = "shield-home"
        else:
            self.home_status = "shield-off"

    def showRoomPanel(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'roompanel'

    def showTemperaturePanel(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'temperaturepanel'

    def showCameraPanel(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'camerapanel'

    def showDoorsPanel(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'doorspanel'

    def showMovementPanel(self):
        self.manager.transition.direction = 'up'
        self.manager.current = 'movementpanel'

    def showLookoutPanel(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'lookoutpanel'
