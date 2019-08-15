package co.edu.udea.iot.backend.repository;

import co.edu.udea.iot.backend.model.Device;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DeviceRepository extends JpaRepository<Device, Integer> {

}
