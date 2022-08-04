from device.base import device


class Camera(device.Device):
    topic_prefix = "Camera"

    def __init__(self, id, state, connection_state, name, home):
        super().__init__(id, state, connection_state, name, home)

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        if self.status != payload:
            self.status = payload
            self.home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"{self.topic_prefix}/{self.id}"
