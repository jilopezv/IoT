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
        changed_state = True
        # TODO: extract streaming state from payload
        # compare old state against new state
        # if change then home should send data
        # raise NotImplementedError
        if changed_state:
            print("temperature.py: updating current_temperature ")
            self.current_temperature = float(payload)
            print("temp: ", self.current_temperature)
            # self.home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
