package co.edu.udea.iot.smarthome.model

import com.github.pozo.KotlinBuilder
import java.io.Serializable
import javax.persistence.*

@Entity
@Table(name = "users")
@KotlinBuilder
data class User(
        @Id @GeneratedValue
        var id: Long?,
        @Column(nullable = false)
        var email: String?,
        @Column(nullable = false)
        var firstName: String?,
        @Column(nullable = false)
        var lastName: String?,
        @Column(nullable = false)
        var nickName: String?,

        @OneToMany(mappedBy = "user")
        var homes: MutableList<Home>?,
        @OneToMany(mappedBy = "user")
        var accesses: MutableList<Access>?
)

@Entity
@Table(name = "homes")
@KotlinBuilder
data class Home(
        @Id
        var id: String,
        @Column(nullable = false)
        var name: String,
        @Column(name = "user_id", nullable = false)
        var userId: Long,

        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "user_id", insertable = false, updatable = false)
        var user: User?,
        @OneToMany(mappedBy = "home")
        var accesses: MutableList<Access>?,
        @OneToMany(mappedBy = "home")
        var rooms: MutableList<Room>?
)

@Entity
@Table(name = "rooms")
data class Room(
        @Id
        var id: String,
        @Column(nullable = false)
        var name: String,
        @Column(name = "home_id", nullable = false)
        var homeId: String,

        @ManyToOne(fetch = FetchType.LAZY)
        @JoinColumn(name = "home_id", insertable = false, updatable = false)
        var home: Home,
        @OneToMany(mappedBy = "room")
        var accesses: MutableList<Access>,
        @OneToMany(mappedBy = "room")
        var devices: MutableList<Device>
)

@Entity
@Table(name = "accesses")
@IdClass(AccessPK::class)
data class Access(
        @Id
        @Column(name = "home_id")
        var homeId: String,
        @Id
        @Column(name = "user_id")
        var userId: Long,
        @Id
        @Column(name = "room_id")
        var roomId: String,
        @Column(nullable = false)
        var level: Int,

        @ManyToOne
        @JoinColumn(name = "user_id", insertable = false, updatable = false)
        var user: User,
        @ManyToOne
        @JoinColumn(name = "home_id", insertable = false, updatable = false)
        var home: Home,
        @ManyToOne
        @JoinColumn(name = "room_id", insertable = false, updatable = false)
        var room: Room


)

@Entity
@Table(name = "devices")
data class Device(
        @Id
        var id: String,
        @Column(nullable = false)
        var state: String,
        @Column(nullable = false)
        var name: String,
        @Column(nullable = false)
        var accessLevel: Int,
        @Column(name = "room_id", nullable = false)
        var roomId: String,
        @Column(name = "type_id", nullable = false)
        var typeId: String,

        @ManyToOne
        @JoinColumn(name = "room_id", insertable = false, updatable = false)
        var room: Room,
        @ManyToOne
        @JoinColumn(name = "device_id", insertable = false, updatable = false)
        var deviceType: DeviceType
)

@Entity
@Table(name = "device_types")
data class DeviceType(
        @Id
        var id: String,
        @Column(nullable = false)
        var description: String
)

data class AccessPK(
        var homeId: String,
        var userId: Long,
        var roomId: String
) : Serializable





