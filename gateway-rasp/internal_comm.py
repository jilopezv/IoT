import paho.mqtt.client as mqttc
import paho.mqtt.publish as publish
import Home

MQTT_LOCAL_SERVER = "localhost"  # Address of local MQTT server (must be always localhost)
MQTT_PATH = "home"  # Topic to establish communication with 'Things' at home


class ThingsComm:
    """ class ThingsComm
        Implements the communication with the 'Things' at home using a mqtt client
        Attributes:
        ----------
            client : paho.mqtt.client
                MQTT client
        """
    def __init__(self, home):
        print("Hello")
        self.client = mqttc.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(MQTT_LOCAL_SERVER, 1883, 60)
        print("connected")
        assert isinstance(home, Home.Home)
        self.myHome = home

    def start(self):
        print("Looping")
        self.client.loop_forever()

    '''@staticmethod
    def send_conf(subtopic, conf):
        try:
            publish.single(MQTT_PATH+"/"+subtopic, "conf:" + conf, hostname=MQTT_LOCAL_SERVER)
        except Exception as ex:
            print("Error in send_conf(). ex: {}".format(ex))'''

    @staticmethod
    def send_message(topic, payload):
        try:
            publish.single(topic, payload, hostname = MQTT_LOCAL_SERVER)
        except Exception as ex:
            print("Error in send_conf(). ex: {}".format(ex))

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        client.subscribe(MQTT_PATH + "/+")

    def on_message(self, client, userdata, msg):
        print("InternalComm got a message")
        self.myHome.process_msg_from_device(msg)
