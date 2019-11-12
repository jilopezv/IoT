import paho.mqtt.client as mqttc
import paho.mqtt.publish as publish
import Home

# Change this parameter with the address and the credentials to your remote server
MQTT_REMOTE_SERVER = "localhost"  # Test server on local
# MQTT_REMOTE_SERVER = "192.168.43.103"  # Remote server IP address
MQTT_PATH_SEND = "home_outbound"  # topic to publish messages
MQTT_PATH_RECV = "home_1_inbound"  # topic to subscribe
USR = "danny"  # user
PASS = "danny"  # password


class ExternalComm:

    def __init__(self, home):
        print("new ExternalComm created")
        self.client = mqttc.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(USR, PASS)
        self.client.connect(MQTT_REMOTE_SERVER, 1883, 60)
        assert isinstance(home, Home.Home)
        self.myHome = home
        print("connected")

    @staticmethod
    def send_tmp(tmp):
        try:
            publish.single(MQTT_PATH_SEND, "tmp:" + tmp, hostname=MQTT_REMOTE_SERVER,
                           auth={'username': USR, 'password': PASS})
        except Exception as ex:
            print("Error in send_tmp(). ex: {}".format(ex))
        # TODO: store tmp value and send it later

    @staticmethod
    def send_alarm():
        try:
            publish.single(MQTT_PATH_SEND, "alarm", hostname=MQTT_REMOTE_SERVER,
                           auth={'username': USR, 'password': PASS})
        except Exception as ex:
            print("Error in send_alarm(). ex: {}".format(ex))

    @staticmethod
    def send_status(st):
        try:
            publish.single(MQTT_PATH_SEND, "status:" + st, hostname=MQTT_REMOTE_SERVER,
                           auth={'username': USR, 'password': PASS})
        except Exception as ex:
            print("Error in send_status(). ex: {}".format(ex))

    @staticmethod
    def send_light(st):
        try:
            publish.single(MQTT_PATH_SEND, "light:" + st, hostname=MQTT_REMOTE_SERVER,
                           auth={'username': USR, 'password': PASS})
        except Exception as ex:
            print("Error in send_status(). ex: {}".format(ex))

    def toggle_light(self):
        self.myHome.toggle_light()

    def start(self):
        print("looping ...")
        self.client.loop_forever()

    def on_message(self, client, userdata, msg):

        # Recibir mensaje, convertirlo o procesarlo y luego pasárselo a home
        # validar credenciales
        print("ExternalComm: got a message")
        print("%s %s" % (msg.topic, msg.payload))
        info = msg.payload.decode("ascii")  # msg.payload is a binary string
        self.myHome.process_msg_from_server(info)


    def on_connect(self, client, userdata, flags, rc):
        print("External Comm: connected with result code " + str(rc))
        client.subscribe(MQTT_PATH_RECV)
