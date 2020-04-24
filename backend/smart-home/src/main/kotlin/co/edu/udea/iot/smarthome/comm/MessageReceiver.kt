package co.edu.udea.iot.smarthome.comm

import org.springframework.amqp.rabbit.annotation.RabbitHandler
import org.springframework.amqp.rabbit.annotation.RabbitListener
import org.springframework.amqp.rabbit.core.RabbitTemplate
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.scheduling.annotation.Scheduled
import org.springframework.stereotype.Component
import org.springframework.stereotype.Service


@RabbitListener(queues = ["home_outbound"])
@Component
class RabbitReceiver {

    @RabbitHandler
    fun receive(message: ByteArray) {
        println(" [x] Received '" + String(message) + "'")
    }
}



