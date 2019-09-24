# Raspberry #

## Prerequisitos ##

### Instalacion del broker ###

```bash
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
```

### Instalación del paho ###

#### Python ####

```bash
sudo pip install paho-mqtt
```

#### Python 3 ####

```bash
sudo pip3 install paho-mqtt
```

Si los prerequisitos se cumplen puede ir directamente a la instalación de la aplicación.

## Ejecucución de la aplicación ##

#### Comando python ####

```bash
python3 main.py
```

#### Salida ####

![rasp](gateway_raspberry.jpg)

## Debug (opcional) ##

Para propositos de debug se puede hacer uso de los comandos de mosquitto o de algun otro cliente para debug ya sea local o remoto. La siguiente pantalla muestra un debug que se llevo a cabo para verificar que la conexión entre los arduinos y la rPi se estaba dando.

![debug](debug_con_mosquitto.jpg)
