import enum
from abc import ABC, abstractmethod

from kivy.event import EventDispatcher
from kivy.properties import StringProperty

import home


# from things_comm.things_outbound import send_message

class Device(ABC, EventDispatcher):
    """ Class Device
        Attributes:    
    """
    topic_prefix = ""

    class Status(enum.Enum):
        ONLINE_STATE = "100"
        OFFLINE_STATE = "-100"
        UNKNOWN = "-1"
        @classmethod
        def has_member_key(cls, key):
            return key in cls.__members__

    state = StringProperty("0")

    def __init__(self, id, state, connection_status, name, ref_home):
        self.id = id
        self.state = state
        self.connection_status = connection_status
        self.name = name
        assert isinstance(ref_home, home.Home)
        self.my_home = ref_home
        self.msg_count = 0
        super().__init__()

    ''' process_external_msg
        process a message incoming from a external component (GUI or Sever)
    '''

    @abstractmethod
    def process_external_msg(self, message):
        pass

    # TODO: refactor this method. opt1: create a concrete method with current implementation
    ''' process_internal_msg
        process a message incoming from a physical device
    '''

    def process_internal_msg(self, payload):
        # print('PAYLOAD', payload)
        self.connection_status = self.Status.ONLINE_STATE
        # TODO: create mechanism to set connectionState to "OFFLINE"
        #  when no message has been received during a given time

        new_state = payload["msg"]
        if new_state != self.Status.ONLINE_STATE.value:
            self._process_internal_msg_on_device(payload)
        self.eval_state_to_report()


    @abstractmethod
    def _process_internal_msg_on_device(self, parameter_list):
        pass

    @abstractmethod
    def get_topic(self):
        pass

    def eval_state_to_report(self):
        print('Eval status to report to server')
        self.msg_count += 1
        # TODO: change explicit number 5 to a constant
        if self.msg_count == 5:
            msg_dict = {'home_id': self.my_home.HOME_ID, 'dev_id': self.id, 'msg': "ONLINE"}
            print(msg_dict)
            self.my_home.send_msg_to_server(msg_dict)
            self.msg_count = 0

    def clean_count(self):
        self.msg_count = 0

    # @abstractmethod
    # def get_json(self, parameter_list):
    #   pass
