import paho.mqtt.publish as publish
from things_comm.constant import *

@staticmethod
def send_message(topic, payload):
    try:
        publish.single(topic, payload, hostname=MQTT_LOCAL_SERVER)
    except Exception as ex:
        print("Error in send_conf(). ex: {}".format(ex))