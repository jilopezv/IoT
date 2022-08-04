from kivy import Config
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from gui.control_panel import ControlPanel
from gui.room_panel import RoomPanel

Config.set('graphics', 'resizable', '0')
# fix the width of the window
Config.set('graphics', 'width', '1024')

# fix the height of the window
Config.set('graphics', 'height', '600')
Config.write()


class SmartHome(MDApp):  # kv file must be named the same
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
