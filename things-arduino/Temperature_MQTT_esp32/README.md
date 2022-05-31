#Light contol and temperature sensor (end-device)

This code project implements an ESP32-based end-point device which controls a light in the smart home application (light is currently simulated by a built-in LED). This device also incorporate a temperature sensor (rw1820) which takes the environment temperature and sends it to the MQTT server.

## Installing the firmware
To install the firmware into the ESP32 NodeMCU-32S you should perform the following tasks:
- Download the Arduino software.
- Install the ESP32 board information into the Arduino ([link](https://www.instructables.com/Installing-the-ESP32-Board-in-Arduino-IDE-Windows-/)).
- Download the source code in this folder and open the file "Temperature_MQTT_esp32.ino".
- Install the required arduino libraries to compile the program.
-- Library "WiFi" is already included in the board information downloaded previously ([link](https://www.luisllamas.es/como-conectar-un-esp8266-a-una-red-wifi-modo-sta/)).
-- Library "PubSubClient" by Nick O'Leary ([link](https://www.luisllamas.es/enviar-y-recibir-mensajes-por-mqtt-con-arduino-y-la-libreria-pubsubclient/)).
-- Libraries "DallasTemperature" (created by Miles Burton) and "OneWire" (created by Paul Stoffregen) for getting data from rw1820 temperature sensor ([link](https://fluxworkshop.com/blogs/getting-started/lets-workshop-lc-technology-rw1820-temperature-sensor-module)).
- Select the board and the port for upload the firmware to the esp32 board.
-- In my case, board: "NodeMCU-32S" and port: USB0
- Click on Upload button in the ARDUINO app.
-- Reset NodeMCU board when connecting.


## Troubleshooting
- Linux error for dialout([link](https://docs.arduino.cc/software/ide-v1/tutorials/Linux)): 
```sudo usermod -a -G dialout <username>``` 
- Linux error for Python ([link1](https://forum.arduino.cc/t/esp32-ide-compiler-importerror-no-module-named-serial/968605)):
-- Error: ... import serial ImportError: No module named serial
```
sudo apt install python-is-python3
sudo apt install python-pip3
sudo pip install pyserial
```



