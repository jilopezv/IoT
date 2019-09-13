package co.edu.udea.iot.backend.model;

public class Message {
    private String deviceName;
    private String payload;

    public Message(String deviceName, String payload) {
        this.deviceName = deviceName;
        this.payload = payload;
    }

    public String getDeviceName() {
        return deviceName;
    }

    public void setDeviceName(String deviceName) {
        this.deviceName = deviceName;
    }

    public String getPayload() {
        return payload;
    }

    public void setPayload(String payload) {
        this.payload = payload;
    }
}
