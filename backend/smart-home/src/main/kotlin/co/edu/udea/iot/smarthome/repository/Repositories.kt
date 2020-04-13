package co.edu.udea.iot.smarthome.repository

import co.edu.udea.iot.smarthome.model.User
import org.springframework.data.repository.CrudRepository

interface UserRepository : CrudRepository<User, Long> {
    fun findByEmail(email: String): User?
}
