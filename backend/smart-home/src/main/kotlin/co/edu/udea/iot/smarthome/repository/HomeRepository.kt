package co.edu.udea.iot.smarthome.repository

import co.edu.udea.iot.smarthome.model.Home
import org.springframework.data.repository.CrudRepository

interface HomeRepository : CrudRepository<Home, String> {
}
