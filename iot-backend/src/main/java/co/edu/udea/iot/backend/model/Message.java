package co.edu.udea.iot.backend.model;

public class Message {
    private String deviceName;
    private String status;

    public Message(String deviceName, String status) {
        this.deviceName = deviceName;
        this.status = status;
    }

    public String getDeviceName() {
        return deviceName;
    }

    public void setDeviceName(String deviceName) {
        this.deviceName = deviceName;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
}
