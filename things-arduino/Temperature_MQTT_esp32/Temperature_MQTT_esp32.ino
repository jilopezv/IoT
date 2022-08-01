/*  Temperature Sensor and light controller
 *  (Light is represented using the built-in led)
 *  IoT Course 
 *  Universidad de Antioquia
 */

//Library for Wifi connection (included with board info)
#include <WiFi.h>
// Library for MQTT connection (by Nick O'Leary)
#include <PubSubClient.h>
//Libraries for the temperature sensor
#include <OneWire.h> // by Paul Stoffregen
#include <DallasTemperature.h> // by Miles Burton


#include "config.h"  // Set your network  SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"


//Select the pin you are connecting your temp sensor, pin 4 in my case.
const int oneWireBus = 4;

// Pin for builtin led in the esp32 board
#define RELAY 14
int light_state = 0; // Initial led's state

//Set the onewire interface
OneWire oneWire(oneWireBus);

//Set the temp sensor to use the onewire interface
DallasTemperature sensors (&oneWire);

void setup() {
  pinMode(RELAY, OUTPUT);    // BUILTIN_LED pin as an output
  digitalWrite(RELAY, LOW);  // Light initial state is OFF

  // Set the serial monitor baud rate
  Serial.begin(115200);
  sensors.begin();
  ConnectWiFi_STA(false);
  InitMqtt();

}

//Counter for sending keep alive message each 5 seconds
int counter_KA = 0;

char msg[50];

void loop() {

  // Read the temperature value
  Serial.print("Sending a command to sensors");
  sensors.requestTemperatures();

  // Temperature read in celcius
  float temperatureC = sensors.getTempCByIndex(0);

  // Write data to serial monitor 
  Serial.print("Temperature sensor : ");
  Serial.print(temperatureC);
  Serial.println("°C");

  HandleMqtt();

  // Send temperature value to the MQTT server
  snprintf (msg, 50, "%.2f", temperatureC);
  Serial.print("Publish message: ");
  Serial.println(msg);
  PublisMqttString("casa/tmp", msg);

  counter_KA++;
  if(counter_KA == 10){
    counter_KA = 0;
    // DeviceID,ONLINE_STATE
    snprintf (msg, 50, "0,100" );
    Serial.print("Sending keep alive message to Rpi: ");
    Serial.println(msg);
    PublisMqttString("home", msg);
  }

  // Read temperature each 5 seconds
  delay(500);
}
