from device.base import device


class Temperature(device.Device):

    topic_prefix = "temp"

    def __init__(self, id, status, connectionStatus, name, home):
        super().__init__(id, status, connectionStatus, name, home, self.topic_prefix)

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
            self.home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"Temperature/{self.id}"
