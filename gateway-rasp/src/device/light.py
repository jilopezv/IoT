import enum

from device.base import device

# TOGGLE_LIGHT_MESSAGE = 2
from things_comm.things_outbound import Things_Outbound




class Light(device.Device):
    TOPIC_PREFIX = "Light"

    class LightStates(enum.Enum):
        TOGGLE_CODE = "2"
        OFF_CODE = "0"
        ON_CODE = "1"

        @classmethod
        def has_member_key(cls, key):
            return key in cls.__members__

    def __init__(self, id, state, connection_status, name, home):
        super().__init__(id, state, connection_status, name, home)
        self.home = home

    def process_external_msg(self, message):
        print(message)
        values = [member.value for member in self.LightStates]
        if self.state == device.Device.Status.ONLINE_STATE.value:
            if message in values:
                Things_Outbound.send_message(self.get_topic(), message)
            else:
                # TODO: send error message "invalid message"
                raise NotImplementedError
        else:
            # TODO: send error message "offline device"
            raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        # print(payload)
        new_state = payload["msg"]
        if new_state != device.Device.Status.ONLINE_STATE:
            if self.state != new_state:
                self.state = new_state

                self.my_home.send_msg_to_server(payload)
                self.clean_count()

    def get_topic(self):
        return f"{self.TOPIC_PREFIX}/{self.id}"
