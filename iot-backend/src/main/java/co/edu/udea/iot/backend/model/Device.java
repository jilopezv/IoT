package co.edu.udea.iot.backend.model;


import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "devices")
public class Device {

    @Id
    private String name;
    private String status;
    private LocalDateTime lastUpdated;

    @Column(name = "fk_home")
    private String homeName;

    //relationships
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "fk_home", insertable = false, updatable = false)
    private Home home;


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Status getStatus() {
        return Status.valueOf(status);
    }

    public void setStatus(Status status) {
        this.status = status.name();
    }

    public LocalDateTime getLastUpdated() {
        return lastUpdated;
    }

    public void setLastUpdated(LocalDateTime lastUpdated) {
        this.lastUpdated = lastUpdated;
    }

    public String getHomeName() {
        return homeName;
    }

    public void setHomeName(Integer homeCode) {
        this.homeName = homeName;
    }

    public Home getHome() {
        return home;
    }

    public void setHome(Home home) {
        this.home = home;
    }

    public enum Status {
        OFFLINE, ON, OFF;
    }
}
