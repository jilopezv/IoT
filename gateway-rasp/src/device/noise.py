from kivy.properties import NumericProperty

from device.base import device


class Noise(device.Device):
    current_noise = NumericProperty(0.0)
    topic_prefix = "Noise"

    def __init__(self, id, state, connectionState, name, home):
        super().__init__(id, state, connectionState, name, home)

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        new_state = payload["msg"]
        if self.state != new_state:
            self.state = new_state
            print("noise.py: updating current_temperature ")
            self.current_noise = float(new_state)
            print("noise: ", self.current_noise)
            self.home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
