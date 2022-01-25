package co.edu.udea.iot.smarthome.comm

import org.springframework.amqp.rabbit.core.RabbitTemplate
import org.springframework.scheduling.annotation.Scheduled
import org.springframework.stereotype.Service

@Service
class HomeSender (private val template: RabbitTemplate) {

    @Scheduled(fixedDelay = 1000, initialDelay = 500)
    fun send(topic: String, message: ByteArray) {
        template.convertAndSend("amq.topic", topic, message)
        println(" [x] Sent '$message'")
    }
}
