# Raspberry #

## Prerequisitos ##

### Instalación del broker ###

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

## Ejecución de la aplicación ##

#### Comando python ####

```bash
python3 main.py
```

#### Salida ####

![rasp](gateway_raspberry.jpg)

## Pruebas funcionales ##

Para probar la aplicación se puede hacer uso de los comandos de mosquitto o de algún otro cliente mqtt, ya sea local o 
remoto. La siguiente pantalla muestra una prueba que se llevó a cabo para verificar que la conexión entre los arduinos 
y la rPi se estaba dando.

![debug](debug_con_mosquitto.jpg)


## Ejecución de la aplicación en desarrollo ##
- Docker con rabbitMQ
- Docker con Mosquitto
---- docker-compose.yml

archivo -dev: valores de las variables para desarrollo


## Ejecución de la aplicación en producción ##
archivo -prod: valores de las variables para producción
instalar mosquitto en rasberry 
compilar y subir a la raspberry