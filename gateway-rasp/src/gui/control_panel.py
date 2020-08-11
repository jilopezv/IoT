from kivy.base import EventLoop
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.base import EventLoop
from kivy.uix.widget import Widget


class ControlPanel(Screen):
    numeroIngresado = StringProperty()
    resultado = StringProperty()
    gridDinamico = ObjectProperty()

    def build(self):
        EventLoop.window.clear_color = (.5, .5, .5, 1)

    def showLightsPanel(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'lightspanel'

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


