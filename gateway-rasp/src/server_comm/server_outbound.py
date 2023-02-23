import os

import paho.mqtt.publish as publish
from server_comm import constant


class Server_Outbound:
    @staticmethod
    def send_status(st):
        try:
            publish.single(constant.MQTT_SERVER_OUTBOUND_DEFAULT_TOPIC, "status:" + st, hostname=os.environ.get("MQTT_REMOTE_SERVER"),
                           port=int(os.environ.get("MQTT_REMOTE_PORT")),
                           auth={'username': os.environ.get("MQTT_USR"), 'password': os.environ.get("MQTT_PWD")})
        except Exception as ex:
            print("Error in send_status(). ex: {}".format(ex))