package co.edu.udea.iot.smarthome.dto

import com.github.pozo.KotlinBuilder

@KotlinBuilder
data class UserDTO(
        var id: Long,
        var email: String,
        var firstName: String,
        var lastName: String,
        var nickName: String
)

@KotlinBuilder
data class HomeDTO(
        var id: String,
        var name: String,
        var userId: Long
)
