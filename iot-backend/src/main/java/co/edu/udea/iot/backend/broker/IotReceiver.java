package co.edu.udea.iot.backend.broker;


import co.edu.udea.iot.backend.config.RabbitConfig;
import co.edu.udea.iot.backend.service.HomeService;
import org.springframework.amqp.rabbit.annotation.RabbitHandler;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@RabbitListener(queues = RabbitConfig.QUEUE_HOME_OUT)
@Component
public class IotReceiver {

    @Autowired
    public HomeService homeService;

    @RabbitHandler
    public void receive(byte[] message) {
        System.out.println(" [x] Received '" + new String(message) + "'");
        homeService.processMessage(new String(message));
    }
}