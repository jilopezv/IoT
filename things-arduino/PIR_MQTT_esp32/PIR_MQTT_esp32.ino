/*  Temperature Sensor and light controller
 *  (Light is represented using the built-in led)
 *  IoT Course 
 *  Universidad de Antioquia
 */


#include <WiFi.h>
#include <SPIFFS.h>
#include <PubSubClient.h>

#include "config.h"  // Sustituir con datos de vuestra red
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"

int inputPin = 4; // for ESP32 microcontroller

// Variable state represents home state-> 0 normal  - 1 lookout
char home_state = 0;

void setup() {

  //Ajustar la velocidad para el monitor serie
  Serial.begin(115200);
  
  pinMode(inputPin, INPUT);    // BUILTIN_LED pin as an output
  
  SPIFFS.begin();
  ConnectWiFi_STA(true);
  InitMqtt();

}


char msg[50];

void loop() {
  HandleMqtt();
  Serial.print(home_state);
  if (home_state){
    int val = digitalRead(inputPin);
    if (val == HIGH) {
      Serial.println("Motion detected!");
      snprintf (msg, 50, "alarm");
      Serial.print("Publish message: ");
      Serial.println(msg);
      // sending alarm to gateway!!!
      PublisMqttString("casa/pir", msg);
    }
    else {
      Serial.println("No Motion detected!");
      //snprintf (msg, 50, "0");
      //Serial.print("Publish message: ");
      //Serial.println(msg);
    }
  }

  delay(500);
}
