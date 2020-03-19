import paho.mqtt.publish as publish
from things_comm.constant import *


class Things_Outbound:
    @staticmethod
    def send_message(topic, payload):
        try:
            print(topic, payload,MQTT_LOCAL_SERVER)
            publish.single(topic, payload, hostname=MQTT_LOCAL_SERVER, port= MQTT_PORT)
        except Exception as ex:
            print("Error in send_conf(). ex: {}".format(ex))
