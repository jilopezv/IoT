package co.edu.udea.iot.smarthome.mapper

import co.edu.udea.iot.smarthome.dto.HomeDTO
import co.edu.udea.iot.smarthome.dto.UserDTO
import co.edu.udea.iot.smarthome.model.Home
import co.edu.udea.iot.smarthome.model.User
import org.mapstruct.Mapper
import org.mapstruct.ReportingPolicy

interface EntityMapper<D, E> {
    fun toEntity(dto: D): E
    fun toDto(entity: E): D
    fun toEntity(dtoList: List<D>?): List<E>?
    fun toDto(entityList: List<E>?): List<D>?
    fun toEntity(dtoList: Set<D>?): Set<E>?
    fun toDto(entityList: Set<E>?): Set<D>?
}


@Mapper(componentModel = "spring", unmappedTargetPolicy = ReportingPolicy.IGNORE)
interface UserMapper : EntityMapper<UserDTO, User>

@Mapper(componentModel = "spring", unmappedTargetPolicy = ReportingPolicy.IGNORE)
interface HomeMapper : EntityMapper<HomeDTO, Home>
