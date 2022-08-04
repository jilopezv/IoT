from device.base import device

# TOGGLE_LIGHT_MESSAGE = 2
from things_comm.things_outbound import Things_Outbound


class Light(device.Device):
    TOPIC_PREFIX = "Light"
    TOGGLE_CODE = "2"

    def __init__(self, id, state, connection_status, name, home):
        super().__init__(id, state, connection_status, name, home)
        self.home = home

    def process_external_msg(self, message):
        print(message)
        if self.connection_status == "ONLINE":
            if message == "TOGGLE":
                Things_Outbound.send_message(self.get_topic(), self.TOGGLE_CODE)
            else:
                # TODO: send error message "invalid message"
                raise NotImplementedError
        else:
            # TODO: send error message "offline device"
            raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        if payload != device.Device.ONLINE_STATE:
            if self.state != payload:
                self.state = payload
                self.my_home.send_msg_to_server(self.state)
                self.clean_count()

    def get_topic(self):
        return f"{self.TOPIC_PREFIX}/{self.id}"
