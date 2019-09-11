package co.edu.udea.iot.backend.broker;


import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

@Service
public class IotSender {

    @Autowired
    private RabbitTemplate template;


    @Scheduled(fixedDelay = 1000, initialDelay = 500)
    public void send(String target, byte[] message) {
        this.template.convertAndSend("amq.topic", target, message);
        System.out.println(" [x] Sent '" + message + "'");
    }
}
