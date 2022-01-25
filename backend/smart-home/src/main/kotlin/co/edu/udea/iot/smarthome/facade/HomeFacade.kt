package co.edu.udea.iot.smarthome.facade

import co.edu.udea.iot.smarthome.dto.HomeDTO
import co.edu.udea.iot.smarthome.dto.MessageDTO
import co.edu.udea.iot.smarthome.dto.UserDTO
import co.edu.udea.iot.smarthome.mapper.HomeMapper
import co.edu.udea.iot.smarthome.mapper.UserMapper
import co.edu.udea.iot.smarthome.model.User
import co.edu.udea.iot.smarthome.service.HomeService
import co.edu.udea.iot.smarthome.service.UserService
import mu.KotlinLogging
import org.springframework.stereotype.Service
import javax.transaction.Transactional

@Service
@Transactional
class HomeFacade(private val homeMapper: HomeMapper, private val homeService: HomeService) {
    private val logger = KotlinLogging.logger {}


    fun saveHome(homeDTO: HomeDTO): HomeDTO? {
        logger.info("Saving for ${homeDTO.name}")
        return homeMapper.toDto(homeService.saveHome(homeMapper.toEntity(homeDTO)))
    }

    fun sendMessageToDevice(messageDTO: MessageDTO) {
        logger.info ("Sending message to ${messageDTO.deviceType}")
        homeService.sendMessageToDevice(messageDTO)
    }


}
