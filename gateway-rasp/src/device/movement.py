from device.base import device


class Movement(device.Device):
    topic_prefix = "Movement"

    def __init__(self, id, state, connectionState, name, home):
        super().__init__(id, state, connectionState, name, home)
        self.home=home

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        payload
        if self.home.lookout:
            print("alarm")
            #self.home.send_msg_to_server()
            self.clean_count()
        else:
            print("movement detected")
            # TODO: evaluate further actions regarding home functionality (for next versions: rooms, auto mode)
            pass

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
