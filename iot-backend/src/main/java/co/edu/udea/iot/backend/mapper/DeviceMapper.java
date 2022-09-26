package co.edu.udea.iot.backend.mapper;

import co.edu.udea.iot.backend.dto.DeviceDTO;
import co.edu.udea.iot.backend.model.Device;
import org.mapstruct.Mapper;

@Mapper(componentModel = "spring")
public interface DeviceMapper {

    Device toEntity(DeviceDTO dto);
    DeviceDTO toDto(Device device);
}
