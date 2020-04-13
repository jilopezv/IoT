package co.edu.udea.iot.smarthome.controller

import co.edu.udea.iot.smarthome.repository.UserRepository
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/user")
class UserController(private val userRepository: UserRepository) {

    @GetMapping()
    fun findAll() = userRepository.findAll()

    @GetMapping("/{email}")
    fun findOne(@PathVariable email: String) =
            userRepository.findByEmail(email) ?: ResponseStatusException(HttpStatus.NOT_FOUND, "This user does not exist")

}
