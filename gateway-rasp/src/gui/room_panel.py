from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen


class RoomPanel(MDScreen):
    light_color = StringProperty("red")
    tmp_value = StringProperty("-")
    mov_icon = StringProperty("motion-sensor-off")
    mov_text = StringProperty("No detection")

    def __init__(self, container, **kw):
        super().__init__(**kw)
        self.container = container
        self.light = container.home.get_device_by_id("0")
        self.tmp = container.home.get_device_by_id("2")
        self.mov = container.home.get_device_by_id("3")
        self.light.bind(state=self.update_light_color)
        self.tmp.bind(current_temperature=self.update_temperature)
        self.mov.bind(movement_detected=self.update_movement)

    def toggle_light(self):
        # Send code 2 for toggle the light device (id=0)
        self.container.home.send_msg_to_device("0", "2")

    def update_light_color(self, *args):
        state = args[1]
        if state == "1":
            self.light_color = "yellow"
        else:
            self.light_color = "gray"

    def update_temperature(self, *args):
        value = args[1]
        self.tmp_value = str(value)

    def update_movement(self, *args):
        detected = args[1]
        if detected:
            self.mov_icon = "motion-sensor"
            self.mov_text = "Detection!"
        else:
            self.mov_icon = "motion-sensor-off"
            self.mov_text = "No detection"

    def toggle_camera(self):
        # TODO Danny acá vendría la lógica para activar la cámara
        # podría ser con self.container.home.toggle_camera()
        # así podríamos meter toda esa lógica de la cámara en la clase home
        pass

    def show_control_panel(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'controlpanel'
