from abc import ABC, abstractmethod

import home
import logging


# from things_comm.things_outbound import send_message

class Device(ABC):
    """ Class Device
        Attributes:    
    """
    topic_prefix = ""
    ONLINE_STATE = "100"
    OFFLINE_STATE = "-100"
    UNKNOWN = "-1"

    def __init__(self, id, state, connectionStatus, name, ref_home):
        self.id = id
        self.state = state
        self.connectionStatus = connectionStatus
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
        print('PAYLOAD', payload)
        self.connectionStatus = self.ONLINE_STATE
        # TODO: create mechanism to set connectionState to "OFFLINE"
        #  when no message has been received during a given time
        self._process_internal_msg_on_device(payload)
        self.eval_state_to_report()
        pass

    @abstractmethod
    def _process_internal_msg_on_device(self, parameter_list):
        pass

    @abstractmethod
    def get_topic(self):
        pass

    def eval_state_to_report(self):
        print('Evalúa estado para reportar al servidor')
        self.msg_count += 1
        # TODO: change explicit number 5 to a constant variable
        if self.msg_count == 5:
            self.my_home.send_alive_msg(id)
            self.msg_count = 0

    def clean_count(self):
        self.msg_count = 0

    # @abstractmethod
    # def get_json(self, parameter_list):
    #   pass
