package co.edu.udea.iot.smarthome.service

import co.edu.udea.iot.smarthome.model.User
import co.edu.udea.iot.smarthome.repository.UserRepository
import mu.KotlinLogging
import org.springframework.stereotype.Service
import javax.transaction.Transactional

@Service
@Transactional
class UserService(private val userRepository: UserRepository) {
    private val log = KotlinLogging.logger {}


    fun getUserByEmail(email: String): User? {
        log.info("Looking for ${email}")
        return userRepository.findByEmail(email)
    }


}
