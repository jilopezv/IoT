const char* MQTT_BROKER_ADRESS = "192.168.64.106";
const uint16_t MQTT_PORT = 1883;
const char* MQTT_CLIENT_NAME = "ESPClient_2";


extern char home_state;

// Topics
const char* DEVICE_TYPE = "Movement";
const char* DEVICE_ID = "3";

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void SuscribeMqtt()
{
  char topic_sub[100];
  sprintf(topic_sub,"%s/%s", DEVICE_TYPE, DEVICE_ID);
  mqttClient.subscribe(topic_sub);
}

String payload;
void PublisMqtt(unsigned long data)
{
   payload = "";
   payload = String(data);
   mqttClient.publish("hello/world", (char*)payload.c_str());
}

void PublisMqttString(char* topic, char* msg)
{
   mqttClient.publish(topic, msg);
}

String content = "";

void OnMqttReceived(char* topic, byte* payload, unsigned int length) 
{
   Serial.print("Received on ");
   Serial.print(topic);
   Serial.print(": ");

   content = "";   
   for (size_t i = 0; i < length; i++) {
      content.concat((char)payload[i]);
   }
   Serial.print(content);
   Serial.println();

   //If payload is "1", change sensor state to lookout
   if ((char)payload[0]=='1')
     home_state = 1; // Set sensor state ->  1 lookout
   else
     home_state = 0; // Clear sensor state ->  0 normal
   

}
