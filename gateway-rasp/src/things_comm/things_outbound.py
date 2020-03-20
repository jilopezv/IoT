import os

import paho.mqtt.publish as publish
from things_comm.constant import *


class Things_Outbound:
    @staticmethod
    def send_message(topic, payload):
        try:
            print(topic, payload, os.environ.get("MQTT_LOCAL_SERVER"))
            publish.single(topic, payload, hostname=os.environ.get("MQTT_LOCAL_SERVER"),
                           port=int(os.environ.get("MQTT_LOCAL_PORT")))
        except Exception as ex:
            print("Error in send_conf(). ex: {}".format(ex))
