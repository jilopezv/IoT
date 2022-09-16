package co.edu.udea.iot.backend.controller;

import co.edu.udea.iot.backend.model.Device;
import co.edu.udea.iot.backend.service.DeviceService;
import co.edu.udea.iot.backend.service.HomeService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("api/devices")
public class DeviceController {

    private final HomeService homeService;

    private final DeviceService deviceService;

    public DeviceController(HomeService homeService, DeviceService deviceService) {
        this.homeService = homeService;
        this.deviceService = deviceService;
    }

    @Operation(description = "View a list of available devices")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Successfully retrieved list",
                    content = @Content(schema = @Schema(implementation = Device.class))),
            @ApiResponse(responseCode = "401", description = "You are not authorized to view the resource"),
            @ApiResponse(responseCode = "403", description = "Accessing the resource you were trying to reach is forbidden"),
            @ApiResponse(responseCode = "404", description = "The resource you were trying to reach is not found")
    })
    @GetMapping
    public List<Device> getAllDevices() {
        return homeService.findAllDevices();
    }

    @Operation(description = "Register a new Device")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "Device successfully registered",
                    content = @Content(schema = @Schema(implementation = Device.class))),
            @ApiResponse(responseCode = "401", description = "You are not authorized to view the resource"),
            @ApiResponse(responseCode = "403", description = "Accessing the resource you were trying to reach is forbidden"),
            @ApiResponse(responseCode = "404", description = "The resource you were trying to reach is not found")
    })
    @PostMapping
    public Device saveDevice(@RequestBody Device device) {
        return deviceService.saveDevice(device);
    }
}
