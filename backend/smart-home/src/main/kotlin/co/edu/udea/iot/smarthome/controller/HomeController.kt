package co.edu.udea.iot.smarthome.controller

import co.edu.udea.iot.smarthome.dto.HomeDTO
import co.edu.udea.iot.smarthome.facade.HomeFacade
import io.swagger.v3.oas.annotations.Operation
import io.swagger.v3.oas.annotations.media.Content
import io.swagger.v3.oas.annotations.media.Schema
import io.swagger.v3.oas.annotations.responses.ApiResponse
import io.swagger.v3.oas.annotations.responses.ApiResponses
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/api/homes")
class HomeController(private val homeFacade: HomeFacade) {

    @PostMapping
    @Operation(summary = "Creates a new home record")
    @ApiResponses(value = [
        ApiResponse(responseCode = "200", description = "the home has been successfully created", content = [Content(schema = Schema(implementation = HomeDTO::class))]),
        ApiResponse(responseCode = "400", description = "Invalid request"),
        ApiResponse(responseCode = "500", description = "Internal error")
    ])
    fun createHome(@RequestBody homeDTO: HomeDTO) =
            homeFacade.saveHome(homeDTO)

}
