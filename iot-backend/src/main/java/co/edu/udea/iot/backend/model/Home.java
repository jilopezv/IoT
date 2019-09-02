package co.edu.udea.iot.backend.model;

import javax.persistence.*;
import java.util.Set;

@Entity
@Table(name = "homes")
public class Home {

    @Id
    private String name;
    private String status;

    //relationships
    @OneToMany(mappedBy = "home", fetch = FetchType.LAZY)
    private Set<Device> devices;


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public Set<Device> getDevices() {
        return devices;
    }

    public void setDevices(Set<Device> devices) {
        this.devices = devices;
    }

    public enum Status {
        ONLINE, OFFLINE;
    }

}
