from kivy.properties import NumericProperty

from device.base import device


class Temperature(device.Device):
    current_temperature = NumericProperty(0.0)
    topic_prefix = "Temp"

    def __init__(self, id, state, connectionState, name, home):
        super().__init__(id, state, connectionState, name, home)

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        new_state = payload["msg"]
        if self.state != new_state:
            self.state = new_state
            print("temperature.py: updating current_temperature ")
            self.current_temperature = float(new_state)
            print("temp: ", self.current_temperature)
            self.my_home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
