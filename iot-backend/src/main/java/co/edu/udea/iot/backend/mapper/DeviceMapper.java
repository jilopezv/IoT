package co.edu.udea.iot.backend.mapper;

import co.edu.udea.iot.backend.dto.DeviceDTO;
import co.edu.udea.iot.backend.model.Device;
import org.springframework.stereotype.Component;

@Component
public class DeviceMapper {

    public DeviceDTO toDto(Device device){
        DeviceDTO dto = new DeviceDTO();
        dto.setName(device.getName());
        dto.setStatus(device.getStatus().name());
        return dto;
    }


    public Device toEntity(DeviceDTO dto){
        Device entity = new Device();
        entity.setName(dto.getName());
        entity.setStatus(Device.Status.valueOf(dto.getStatus()));
        return entity;
    }
}
