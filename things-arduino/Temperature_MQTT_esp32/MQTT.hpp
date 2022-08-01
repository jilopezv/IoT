const char* MQTT_BROKER_ADRESS = "192.168.64.106";
const uint16_t MQTT_PORT = 1883;
const char* MQTT_CLIENT_NAME = "ESPClient_1";

// Topics
const char* DEVICE_TYPE = "Light";
const char* DEVICE_ID = "0";
#define RELAY 14

extern int light_state;

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


   // This code indicates what to do with the received message
   if((char)payload[0] == '1') {
      light_state=1;
      digitalWrite(RELAY, HIGH);
   }
   else if ((char)payload[0] == '0') {
      light_state=0;
      digitalWrite(RELAY, LOW);
   }
   else if ((char)payload[0] == '2') { 
      // Toggle light 
      if (light_state == 1){
        light_state=0;
        digitalWrite(RELAY, LOW);
      }
      else{
        light_state=1;
        digitalWrite(RELAY, HIGH);
      }
  }
}
