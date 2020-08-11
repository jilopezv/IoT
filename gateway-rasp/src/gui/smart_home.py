import kivysome
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from gui.camera_panel import CameraPanel
from gui.control_panel import ControlPanel
from gui.door_panel import DoorsPanel
from gui.lights_panel import LightsPanel
from gui.lookout_panel import LookoutPanel
from gui.movement_panel import MovementPanel
from gui.temp_panel import TemperaturePanel


class SmartHome(App):  # el archivo kv debe llamarse igual
    sm = ScreenManager()

    def __init__(self, home, **kwargs):
        super().__init__(**kwargs)
        kivysome.enable("https://kit.fontawesome.com/ddee73d32d.js", group=kivysome.FontGroup.SOLID)
        self.home = home

    def build(self):
        self.sm.add_widget(ControlPanel(name="controlpanel"))
        self.sm.add_widget(LightsPanel(name="lightspanel"))
        self.sm.add_widget(TemperaturePanel(name="temperaturepanel"))
        self.sm.add_widget(CameraPanel(name="camerapanel"))
        self.sm.add_widget(DoorsPanel(name="doorspanel"))
        self.sm.add_widget(MovementPanel(name="movementpanel"))
        self.sm.add_widget(LookoutPanel(self.home, name="lookoutpanel"))
        return self.sm


