package co.edu.udea.iot.backend.dto;

import javax.validation.constraints.NotBlank;

public class DeviceDTO {

    @NotBlank(message = "Name is required")
    private String name;
    @NotBlank(message = "The status is required fafasfjkfakfjasfd")
    private String status;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
