package co.edu.udea.iot.backend.broker;


import co.edu.udea.iot.backend.config.RabbitConfig;
import org.springframework.amqp.rabbit.annotation.RabbitHandler;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@RabbitListener(queues = RabbitConfig.QUEUE_HOME_OUT)
@Component
public class IotReceiver {

    @RabbitHandler
    public void receive(byte[] message) {
        System.out.println(" [x] Received '" + new String(message) + "'");
    }
}