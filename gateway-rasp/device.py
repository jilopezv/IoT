from .home import Home
from abc import ABC, abstractmethod


class Device(ABC):
    """ Class Device
        Attributes:    
    """
    home = Home
    topic_prefix = ""

    def __init__(self, id, status, connectionStatus, name, home, topic_prefix):
        self.id = id
        self.status = status
        self.connectionStatus = connectionStatus
        self.name = name
        self.home = home
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
        self.connectionStatus = "ONLINE"
        # TODO: create mechanism to set connectionStatus to "OFFLINE"
        #  when no message has been received during a given time
        self._process_internal_msg_on_device(payload)
        self.eval_status_to_report()
        pass

    @abstractmethod
    def _process_internal_msg_on_device(self, parameter_list):
        pass

    @abstractmethod
    def get_topic(self):
        pass

    def eval_status_to_report(self):
        self.msg_count += 1
        # TODO: change explicit number 5 to a constant variable
        if self.msg_count == 5:
            self.home.send_alive_msg(id)
            self.msg_count = 0

    def clean_count(self):
        self.msg_count = 0

    @abstractmethod
    def get_json(self, parameter_list):
        pass


class Light(Device):
    topic_prefix = "light"

    def __init__(self, id, status, connectionStatus, name, home):
        super().__init__(id, status, connectionStatus, name, home, self.topic_prefix)

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
        if payload != "ONLINE":
            if self.status != payload:
                self.status = payload
                self.home.send_msg_to_server(self.status)
                self.clean_count()


    def get_topic(self):
        return f"Light/{self.id}"


class Camera(Device):
    topic_prefix = "camera"

    def __init__(self, id, status, connectionStatus, name, home):
        super().__init__(id, status, connectionStatus, name, home, self.topic_prefix)

    def process_external_msg(self, parameter_list):
        raise NotImplementedError

    def _process_internal_msg_on_device(self, payload):
        print(payload)
        if self.status != payload:
            self.status = payload
            self.home.send_msg_to_server(payload)
            self.clean_count()

    def get_topic(self):
        return f"Camera/{self.id}"


class Temperature(Device):
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

class Movement(Device):
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