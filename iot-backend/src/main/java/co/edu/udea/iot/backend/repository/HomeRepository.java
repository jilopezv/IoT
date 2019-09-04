package co.edu.udea.iot.backend.repository;

import co.edu.udea.iot.backend.model.Home;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface HomeRepository extends JpaRepository<Home, Integer> {

    Optional<Home> findByName(String name);
}
