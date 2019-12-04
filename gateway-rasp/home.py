from .external_comm import ExternalComm
from .internal_comm import ThingsComm
from .device import *
import subprocess

# TODO: analyze which methods must be synchronized
class Home:
    """ Class Home
        Home represents the smart home basic functionality

        Attributes:
            lookout: home state - True = sentry or lookout  - False = normal
            flag: used to signal the program termination
            light: state of one of the lights at home. TRUE = on - FALSE = off
    """
    topic_prefix = "home"
    devices = []

    def __init__(self):
        """ home constructor
        set initial state in Home class.
        """
        print("New Home created")
        self.lookout = False
        self.light = False
        self.flag = True
        self.devices = {}
        self.devices = self.get_devices()

    def get_devices(self):
        # This structure simulates the initial configuration obtained from a remote server
        # TODO: implement by consuming a REST service 
        lv_light = Light(0, "online", "connected", "living room light", self)
        lv_cam = Camera(1, "online", "connected", "living room camera", self)
        lv_tmp = Temperature(2, "online", "connected", "living room temperature sensor", self)
        lv_mov = Movement(3, "online", "connected", "living room PIR sensor", self)
        devices = {
            0: lv_light,
            1: lv_cam,
            2: lv_tmp,
            3: lv_mov
        }
        return devices

    def process_msg_from_device(self, payload):
        info = self.parse_payload(payload)
        source_device = self.devices.get(info[0], None)
        if source_device is None:
            # TODO: Notify server that gateway receives msg from unknown device
            raise AssertionError
        source_device.process_internal_msg(payload)

    def send_msg_to_server(self, msg):
        # TODO: send message to server
        raise NotImplementedError

    def send_msg_to_device(self, dev_id, message):
        target_device = self.devices.get(dev_id, None)
        if target_device is None:
            # TODO: Notify caller that device id is not found
            raise AssertionError
        if target_device.connectionStatus == "ONLINE":
            # TODO: check with target_device whether message is valid or not
            ThingsComm.send_message(f"home/+/{target_device.get_topic()}", message)
        

    def process_msg_from_server(self, msg):
        # TODO: extract msg_type: home, room or device
        # home e.g.: lookout_mode, turnoff all (generic messages) wildcards
        # device e.g.: to an specific device

        # TODO: Extract target
        # Room_type, Room_id, Device_type, Device_id
        # TODO: Define payload format
        # Depends on device type

        source_device = self.devices.get(id, "invalid")
        if source_device == "invalid":
            # TODO: Notify server that gateway receives msg from unknown device
            raise AssertionError

        if msg == "start_streaming":
            print("starting streaming...")
            if not self.get_light():
                self.toggle_light()
            self.process = subprocess.Popen(['python3', 'streaming.py'])  # create streaming process
        elif msg == "stop_streaming":
            print("stop streaming...")
            self.process.kill()  # Kill streaming process
            if self.get_light():
                self.toggle_light()
        elif msg == "light":
            print("ext: must toggle light")
            self.toggle_light()
        raise NotImplementedError

    def send_alive_msg(self, msg):
        # TODO: send alive message to server
        raise NotImplementedError

    def toggle_lookout(self):
        """ This is the toggle_lookout function
        It toggles the state of the inner representation of a given  at home.
        It also sends mqtt messages to the arduino actuator through InternalComm
        and to the remote server through the ExternalComm

        Returns:
            Final state of lookout attribute
        """
        self.lookout = not self.lookout
        print("new lookout state to " + format(self.lookout))
        '''ExternalComm.ExternalComm.send_status(format(self.lookout))
        if self.lookout:
            InternalComm.ThingsComm.send_conf("pir_conf", "1")
        else:
            InternalComm.ThingsComm.send_conf("pir_conf", "0")
        return self.lookout'''

    def toggle_light(self):
        """ This is the toggle_lookout function
        It toggles the state of the inner representation of a given  at home.
        It also sends mqtt messages to the arduino actuator through InternalComm
        and to the remote server through the ExternalComm

        Returns
        -------
        lookout: bool
            Final state of lookout attribute (True = sentry or lookout - False = normal)
        """
        self.light = not self.light
        print("new light state to " + format(self.light))
        # ExternalComm.ExternalComm.send_light(format(self.light))
        '''if self.light:
            InternalComm.ThingsComm.send_conf("light", "1")
        else:
            InternalComm.ThingsComm.send_conf("light", "0")
        return self.light'''

    def get_lookout(self):
        return self.lookout

    def get_light(self):
        return self.light

    def end_program(self):
        self.flag = False

    def is_ended(self):
        """ This is the function is_ended
        This function is called to poll the termination of the program.

        Returns
        -------
        flag: bool
            When False program must finish
        """
        return self.flag


    def parse_payload(self, payload):
        info = payload.split(",")
        # TODO: check whether the list the right size (must be 2)
        return info



home = Home()
home.process_msg_from_device(0, "hello")
