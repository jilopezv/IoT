package co.edu.udea.iot.backend.broker;

import org.eclipse.paho.client.mqttv3.*;
import org.springframework.stereotype.Component;

import java.util.UUID;

@Component
public class HomeListener {

    public HomeListener() throws MqttException {
        String listenerId = UUID.randomUUID().toString();
        IMqttClient listener = new MqttClient("tcp://localhost:1883",listenerId);
        MqttConnectOptions options = new MqttConnectOptions();
        options.setAutomaticReconnect(true);
        options.setCleanSession(true);
        options.setConnectionTimeout(10);
        listener.connect(options);
        listener.subscribe("home_outbound", this::processMessage);
    }

    private void processMessage(String topic, MqttMessage message) {
        System.out.printf("%s -> %s", topic, message);
    }


}
