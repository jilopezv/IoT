package co.edu.udea.iot.smarthome.model

import javax.persistence.Column
import javax.persistence.Entity
import javax.persistence.Id

@Entity
class User(
        @Id
        var id: String,
        @Column(nullable = false)
        var firstName: String,
        @Column(nullable = false)
        var lastName: String,
        @Column(nullable = false)
        var nickName: String,
        @Column(nullable = false)
        var email: String
)



