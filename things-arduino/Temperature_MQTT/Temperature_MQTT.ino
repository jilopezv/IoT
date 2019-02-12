/*  Temperature Sensor and light controller
 *  (Light is represented using the built-in led)
 *  IoT Course 
 *  Universidad de Antioquia
 */

#include <ESP8266WiFi.h>
#include <PubSubClient.h> // client for publish/subscribe messaging with MQTT

// temperature sensor from A0 pin
#define TEMP_SENSOR A0

// Define the B-value of the thermistor.
// This value is a property of the thermistor used in the Grove - Temperature Sensor,
// and used to convert from the analog value it measures and a temperature value.
const int B = 3975;

#define BUILTIN_LED 2

// Wifi network credentials
const char* ssid = "Nett1";
const char* password = "zvwq1218";
// MQTT server ip address
const char* mqtt_server = "192.168.43.225";

WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
  pinMode(BUILTIN_LED, OUTPUT);    // BUILTIN_LED pin as an output
  pinMode(TEMP_SENSOR, INPUT);     // TEMP_SENSOR pin as an input
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  digitalWrite(BUILTIN_LED, HIGH); // Light initial state is OFF
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
    Serial.print(i);
    Serial.print((char)payload[i]);
    
  }
  Serial.println();
  
  if((char)payload[5] == '1') {
    digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on 
  }
  else if ((char)payload[5] == '0') {
    digitalWrite(BUILTIN_LED, HIGH);   // Turn the LED off
  }
}

// Connection to mqtt server
void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect ESP8266Client1
    if (client.connect("ESP8266Client1")) {
      Serial.println("connected");
      // Subscribe to "casa/light" topic
      client.subscribe("casa/light");
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
  //get temperature data each 10s 
  if (now - lastMsg > 10000) {
    // Get the (raw) value of the temperature sensor.
    int val = analogRead(pinTemp);
    // Determine the current resistance of the thermistor based on the sensor value.
    float resistance = (float)(1023-val)*10000/val;
    // Calculate the temperature based on the resistance value.
    float temperature = 1/(log(resistance/10000)/B+1/298.15)-273.15;
    lastMsg = now;
    //++value;
    snprintf (msg, 75, "%.2f", temperature);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("casa/tmp", msg);
  }
}
