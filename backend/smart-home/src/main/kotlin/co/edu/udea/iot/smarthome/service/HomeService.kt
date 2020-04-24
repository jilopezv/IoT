package co.edu.udea.iot.smarthome.service

import co.edu.udea.iot.smarthome.model.Home
import co.edu.udea.iot.smarthome.repository.HomeRepository
import mu.KotlinLogging
import org.springframework.stereotype.Service
import javax.transaction.Transactional

@Service
@Transactional
class HomeService(private val homeRepository: HomeRepository) {
    private val log = KotlinLogging.logger {}


    fun saveHome(home: Home): Home {
        log.info("saving home ${home.name}")
        return homeRepository.save(home)
    }


}
