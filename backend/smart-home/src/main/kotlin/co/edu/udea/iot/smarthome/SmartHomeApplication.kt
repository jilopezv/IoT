package co.edu.udea.iot.smarthome

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication

@SpringBootApplication
class SmartHomeApplication

fun main(args: Array<String>) {
	runApplication<SmartHomeApplication>(*args)
}
