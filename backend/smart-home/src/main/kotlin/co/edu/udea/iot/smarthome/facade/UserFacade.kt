package co.edu.udea.iot.smarthome.facade

import co.edu.udea.iot.smarthome.dto.UserDTO
import co.edu.udea.iot.smarthome.mapper.UserMapper
import co.edu.udea.iot.smarthome.model.User
import co.edu.udea.iot.smarthome.service.UserService
import mu.KotlinLogging
import org.springframework.stereotype.Service
import javax.transaction.Transactional

@Service
@Transactional
class UserFacade(private val userMapper: UserMapper, private val userService: UserService) {
    private val log = KotlinLogging.logger {}


    fun getUserByEmail(email: String): UserDTO? {
        log.info("Looking for ${email}")
        val user: User = checkNotNull(userService.getUserByEmail(email))
        return userMapper.toDto(user)
    }


}
