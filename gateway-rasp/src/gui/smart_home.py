from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from gui.control_panel import ControlPanel
from gui.room_panel import RoomPanel


class SmartHome(MDApp):  # el archivo kv debe llamarse igual
    sm = ScreenManager()

    def __init__(self, home, **kwargs):
        super().__init__(**kwargs)
        self.home = home

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.sm.add_widget(ControlPanel(self, name="controlpanel"))
        self.sm.add_widget(RoomPanel(self, name="roompanel"))
        return self.sm

    def on_start(self):
        self.fps_monitor_start()
