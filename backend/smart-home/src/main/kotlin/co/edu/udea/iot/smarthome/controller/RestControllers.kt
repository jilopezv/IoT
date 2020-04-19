package co.edu.udea.iot.smarthome.controller

import co.edu.udea.iot.smarthome.dto.UserDTO
import co.edu.udea.iot.smarthome.facade.UserFacade
import io.swagger.v3.oas.annotations.Operation
import io.swagger.v3.oas.annotations.media.Content
import io.swagger.v3.oas.annotations.media.Schema
import io.swagger.v3.oas.annotations.responses.ApiResponse
import io.swagger.v3.oas.annotations.responses.ApiResponses
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController
import org.springframework.web.server.ResponseStatusException

@RestController
@RequestMapping("/api/users")
class UserController(private val userFacade: UserFacade) {

    @GetMapping("/{email}")
    @Operation(summary = "Consulta la información de un usuario específico por email")
    @ApiResponses(value = [
        ApiResponse(responseCode = "200", description = "successful operation", content = [Content(schema = Schema(implementation = UserDTO::class))]),
        ApiResponse(responseCode = "400", description = "La petición es inválida"),
        ApiResponse(responseCode = "500", description = "Error interno al procesar la respuesta")
    ])
    fun findOne(@PathVariable email: String) =
            userFacade.getUserByEmail(email)
                    ?: ResponseStatusException(HttpStatus.NOT_FOUND, "This user does not exist")

}
