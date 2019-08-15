package co.edu.udea.iot.backend.controller;

import co.edu.udea.iot.backend.model.Home;
import co.edu.udea.iot.backend.service.HomeService;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("api/homes")
public class HomeController {

    @Autowired
    private HomeService homeService;

    @ApiOperation(value = "View a list of available homes", response = List.class)
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Successfully retrieved list"),
            @ApiResponse(code = 401, message = "You are not authorized to view the resource"),
            @ApiResponse(code = 403, message = "Accessing the resource you were trying to reach is forbidden"),
            @ApiResponse(code = 404, message = "The resource you were trying to reach is not found")
    })
    @GetMapping()
    public List<Home> getAllDevices() {
        return homeService.findAllHomes();
    }
}
