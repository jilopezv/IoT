package co.edu.udea.iot.smarthome.service

import co.edu.udea.iot.smarthome.comm.HomeSender
import co.edu.udea.iot.smarthome.dto.MessageDTO
import co.edu.udea.iot.smarthome.model.Home
import co.edu.udea.iot.smarthome.repository.HomeRepository
import co.edu.udea.iot.smarthome.repository.UserRepository
import co.edu.udea.iot.smarthome.service.exception.BusinessException
import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import mu.KotlinLogging
import org.springframework.stereotype.Service
import javax.transaction.Transactional

@Service
@Transactional
class HomeService(
    private val homeRepository: HomeRepository,
    private val userRepository: UserRepository,
    private val homeSender: HomeSender
) {
    private val log = KotlinLogging.logger {}

    //todo when a room is created the main user gets access with level 0

    fun saveHome(home: Home): Home {
        log.info("El id del usuario de la casa nueva es: ${home.userId}")
        val user = userRepository.findById(home.userId)
        if (!user.isPresent) {
            throw BusinessException("El usuario no se encuentra registrado")
        }
        log.info("saving home ${home.name}")
        return homeRepository.save(home)
    }

    fun sendMessageToDevice(messageDTO: MessageDTO) {
        val topic = "home_${messageDTO.homeId}_inbound"
        val mapper = jacksonObjectMapper()

        val jsonMessage = mapper.writeValueAsBytes(messageDTO)
        homeSender.send(topic, jsonMessage)
    }

}
