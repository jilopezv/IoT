package co.edu.udea.iot.backend.service;

import co.edu.udea.iot.backend.model.Device;
import co.edu.udea.iot.backend.repository.DeviceRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DeviceService {

    private DeviceRepository deviceRepository;

    public DeviceService(DeviceRepository deviceRepository) {
        this.deviceRepository = deviceRepository;
    }

    public List<Device> findAllDevices() {
        return deviceRepository.findAll();
    }

    public void processMessage(String message) {
        //TODO parse the message and take actions
    }
}
