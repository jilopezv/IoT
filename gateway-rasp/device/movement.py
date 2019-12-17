from device.base import device


class Movement(device.Device):
    topic_prefix = "move"

    def __init__(self, id, status, connectionStatus, name, home):
        super().__init__(id, status, connectionStatus, name, home, self.topic_prefix)

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, parameter_list):
        if self.home.lookout:
            self.home.send_msg_to_server()
            self.clean_count()
        else:
            # TODO: evaluate further actions regarding home functionality (for next versions: rooms, auto mode)
            pass

    def get_topic(self):
        return f"Movemente/{self.id}"
