package co.edu.udea.iot.backend.service;

import co.edu.udea.iot.backend.model.Home;
import co.edu.udea.iot.backend.repository.HomeRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class HomeService {

    private HomeRepository homeRepository;

    public HomeService(HomeRepository homeRepository) {
        this.homeRepository = homeRepository;
    }

    public List<Home> findAllHomes() {
        return homeRepository.findAll();
    }
}
