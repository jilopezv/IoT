/*  Temperature Sensor and light controller
 *  (Light is represented using the built-in led)
 *  IoT Course 
 *  Universidad de Antioquia
 */

//Library for Wifi connection (included with board info)
#include <WiFi.h>
// Library for MQTT connection (by Nick O'Leary)
#include <PubSubClient.h>


#include "config.h"  // Set your network  SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"


// Pin for PIR sensor in the esp32 board
#define PIR_MOTION_SENSOR 5

long lastMsg = 0;
char msg[50];
int value = 0;

// Variable state represents home state-> 0 normal  - 1 lookout
char home_state = 0;


void setup() {
  pinMode(PIR_MOTION_SENSOR, INPUT);    // set PIN_PIR a pin as an input
  
  // Set the serial monitor baud rate
  Serial.begin(115200);
  ConnectWiFi_STA(false);
  InitMqtt();
  delay(5000);
}

void loop() {


  HandleMqtt();
  long now = millis(); 
  //get PIR data each 500ms 
  if (now - lastMsg > 500) { 
    lastMsg = now;
    Serial.print(home_state);
    if (home_state){
      // lookout state
      if(digitalRead(PIR_MOTION_SENSOR)){//if it detects the moving people?
        //Serial.println("Hi,people is coming");
        snprintf (msg, 50, "alarm");
        Serial.print("Publish message: ");
        Serial.println(msg);
        // sending alarm to gateway!!!
        //client.publish("casa/pir", msg);
        PublisMqttString("casa/pir",msg);
      } else{
        // normal state
        snprintf (msg, 50, "0");
        Serial.print("movement: ");
        Serial.println(msg);
      }
    }
  }

 
  
}
