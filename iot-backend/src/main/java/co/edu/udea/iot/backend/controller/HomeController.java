package co.edu.udea.iot.backend.controller;

import co.edu.udea.iot.backend.model.Home;
import co.edu.udea.iot.backend.service.HomeService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("api/homes")
public class HomeController {

    @Autowired
    private HomeService homeService;

    @Operation(description = "View a list of available homes")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Successfully retrieved list"),
            @ApiResponse(responseCode = "401", description = "You are not authorized to view the resource"),
            @ApiResponse(responseCode = "403", description = "Accessing the resource you were trying to reach is forbidden"),
            @ApiResponse(responseCode = "404", description = "The resource you were trying to reach is not found")
    })
    @GetMapping()
    public List<Home> getAllDevices() {
        return homeService.findAllHomes();
    }

    @Operation(description = "Send a message to a specific device in a specific home")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Successfully retrieved list"),
            @ApiResponse(responseCode = "401", description = "You are not authorized to view the resource"),
            @ApiResponse(responseCode = "403", description = "Accessing the resource you were trying to reach is forbidden"),
            @ApiResponse(responseCode = "404", description = "The resource you were trying to reach is not found")
    })
    @PostMapping("/{homeName}/{deviceName}/{message}")
    public void sendMessage(@PathVariable String homeName, @PathVariable String deviceName, @PathVariable String message) {
        homeService.sendMessage(homeName, deviceName, message);
    }

}
