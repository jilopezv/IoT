package co.edu.udea.iot.smarthome.dto

import com.github.pozo.KotlinBuilder
import javax.validation.constraints.NotNull

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
        @NotNull(message = "El id del usuario es requerido")
        var userId: Long
)

@KotlinBuilder
data class MessageDTO(
        var homeId: String,
        var deviceType: String,
        var deviceId: String,
        var payload: String
)
