from device.base import device


# TOGGLE_LIGHT_MESSAGE = 10

class Light(device.Device):
    topic_prefix = "light"

    def __init__(self, id, state, connectionState, name, home):
        super().__init__(id, state, connectionState, name, home, self.topic_prefix)

    def process_external_msg(self, message):
        print(message)
        if self.connectionStatus == "ONLINE":
            if message == "TOGGLE":
                pass
            else:
                # TODO: send error message "invalid message"
                raise NotImplementedError
        else:
            # TODO: send error message "offline device"
            raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        if payload != device.Device.ONLINE_STATE:
            if self.status != payload:
                self.status = payload
                self.home.send_msg_to_server(self.status)
                self.clean_count()

    def get_topic(self):
        return f"Light/{self.id}"
