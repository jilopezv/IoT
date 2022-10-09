package co.edu.udea.iot.backend.broker.webclient;

import org.eclipse.paho.client.mqttv3.*;
import org.springframework.stereotype.Component;

import java.util.UUID;

@Component
public class WebPublisher {

    private final IMqttClient publisher;

    public WebPublisher() throws MqttException {
        String publisherId = UUID.randomUUID().toString();
        this.publisher = new MqttClient("ws://localhost:8000", publisherId);
        MqttConnectOptions options = new MqttConnectOptions();
        options.setAutomaticReconnect(true);
        options.setCleanSession(true);
        options.setConnectionTimeout(10);
        publisher.connect(options);
    }

    public void publish(String message) throws MqttException {
        if (!publisher.isConnected()) {
            //todo log message client not connected
            return;
        }
        MqttMessage msg = new MqttMessage(message.getBytes());
        msg.setQos(0);
        msg.setRetained(true);
        publisher.publish("web_inbound", msg);
    }
}
