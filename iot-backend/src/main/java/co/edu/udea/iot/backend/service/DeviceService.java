package co.edu.udea.iot.backend.service;

import co.edu.udea.iot.backend.exception.DataDuplicatedException;
import co.edu.udea.iot.backend.model.Device;
import co.edu.udea.iot.backend.repository.DeviceRepository;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class DeviceService {

    private final DeviceRepository deviceRepository;

    public DeviceService(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    public Device saveDevice(Device device) {
        Optional<Device> deviceOptional = deviceRepository.findByName(device.getName());
        if (deviceOptional.isPresent()) {
            throw new DataDuplicatedException(String.format("There is already a device with name: %s", device.getName()));
        }
        return deviceRepository.save(device);
    }
}
