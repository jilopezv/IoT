/*  PIR Sensor
 *  IoT Course 
 *  Universidad de Antioquia
 */

#include <ESP8266WiFi.h>
#include <PubSubClient.h> // client for publish/subscribe messaging with MQTT

#define BUILTIN_LED 2
#define PIR_MOTION_SENSOR D5

// Wifi network credentials
const char* ssid = "Nett1"; 
const char* password ="zvwq1218"; 
// MQTT server ip address
const char* mqtt_server = "192.168.43.225";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

// Variable state represents home state-> 0 normal  - 1 lookout
char state = 0;

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);      // BUILTIN_LED pin as an output
  pinMode(PIR_MOTION_SENSOR, INPUT); // PIR_MOTION_SENSOR pin as input
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void setup_wifi() {
  delay(10);
  // Connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

// Callback for incoming mqtt messages
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();

  //If payload is "1", change sensor state to lookout
  if ((char)payload[5]=='1')
    state = 1; // Set sensor state ->  1 lookout
  else
    state = 0; // Clear sensor state ->  0 normal
}//end void callback

// Connection to mqtt server
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect from ESP8266Client2
    if (client.connect("ESP8266Client2")) { 
      Serial.println("connected");
      // Subscribe to "casa/pir_conf" topic
      client.subscribe("casa/pir_conf");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
  
  long now = millis(); 
  //get PIR data each 500ms 
  if (now - lastMsg > 500) { 
    lastMsg = now;
    Serial.print(state);
    if (state){
      // lookout state
      if(digitalRead(PIR_MOTION_SENSOR)){//if it detects the moving people?
        //Serial.println("Hi,people is coming");
        snprintf (msg, 50, "alarm");
        Serial.print("Publish message: ");
        Serial.println(msg);
        // sending alarm to gateway!!!
        client.publish("casa/pir", msg);
      } else{
        // normal state
        snprintf (msg, 50, "0");
        Serial.print("Publish message: ");
        Serial.println(msg);
      }
    }
  }
}
