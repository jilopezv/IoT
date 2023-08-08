from kivy.properties import BooleanProperty

from device.base import device


class Movement(device.Device):
    topic_prefix = "Movement"
    movement_detected = BooleanProperty(False)

    def __init__(self, id, state, connection_state, name, home):
        super().__init__(id, state, connection_state, name, home)
        self.home = home

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        new_state = payload["msg"]
        if self.home.lookout:
            print("alarm")
            # self.home.send_msg_to_server()
            self.clean_count()
        else:
            print("movement detected")
            if new_state == '1':
                self.movement_detected = True
            else:
                self.movement_detected = False

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
