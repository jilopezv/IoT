import os
import logging

import paho.mqtt.client as mqttc
import home
from server_comm.constant import *


class ServerInbound:

    def __init__(self, ref_home):
        print("new ExternalComm created")
        self.client = mqttc.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.username_pw_set(os.environ.get("MQTT_USR"), os.environ.get("MQTT_PWD"))
        try:
            self.client.connect(os.environ.get("MQTT_REMOTE_SERVER"), int(os.environ.get("MQTT_REMOTE_PORT")), 60)
        except Exception as ex:
            logging.error("#### Home IoT ####: no connection to remote MQTT Server "+str(ex))
        assert isinstance(ref_home, home.Home)
        self.myHome = ref_home

    def start(self):
        logging.debug("looping ...")
        self.client.loop_forever()

    def on_message(self, client, userdata, msg):
        # Recibir mensaje, convertirlo o procesarlo y luego pasárselo a home
        # validar credenciales
        print("ExternalComm: got a message")
        print("%s %s" % (msg.topic, msg.payload))
        info = msg.payload.decode("ascii")  # msg.payload is a binary string
        self.myHome.process_msg_from_server(info)

    def on_connect(self, client, userdata, flags, rc):
        print("External Comm: connected with result code ", str(rc), "[SERVER_INBOUND]")
        client.subscribe(MQTT_SERVER_INBOUND_HOME_TOPIC)
