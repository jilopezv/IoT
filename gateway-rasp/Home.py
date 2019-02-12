import ExternalComm
import InternalComm


class Home:
    """ Class Home
        Home represents the smart home basic functionality

        Attributes:
            lookout: home state - True = sentry or lookout  - False = normal
            flag: used to signal the program termination
            light: state of one of the lights at home. TRUE = on - FALSE = off
    """
    def __init__(self):
        """ home constructor
        set initial state in Home class.
        """
        print("New Home created")
        self.lookout = False
        self.flag = True
        self.light = False

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
        ExternalComm.ExternalComm.send_status(format(self.lookout))
        if self.lookout:
            InternalComm.ThingsComm.send_conf("pir_conf", "1")
        else:
            InternalComm.ThingsComm.send_conf("pir_conf", "0")
        return self.lookout

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
        ExternalComm.ExternalComm.send_light(format(self.light))
        if self.light:
            InternalComm.ThingsComm.send_conf("light", "1")
        else:
            InternalComm.ThingsComm.send_conf("light", "0")
        return self.light

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
