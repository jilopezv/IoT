package co.edu.udea.iot.backend.repository;

import co.edu.udea.iot.backend.model.Device;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface DeviceRepository extends JpaRepository<Device, Integer> {

    Optional<Device> findByName(String name);

}
