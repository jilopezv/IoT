package co.edu.udea.iot.backend.config;

import org.springframework.amqp.core.*;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

//@Configuration
public class RabbitConfig
{
    public static final String QUEUE_HOME_OUT = "home_out";

    //@Bean
    Queue homeOutQueue() {
        return QueueBuilder.durable(QUEUE_HOME_OUT).build();
    }

}
