package co.edu.udea.iot.backend.service;

import co.edu.udea.iot.backend.broker.IotSender;
import co.edu.udea.iot.backend.model.Device;
import co.edu.udea.iot.backend.model.Home;
import co.edu.udea.iot.backend.model.Message;
import co.edu.udea.iot.backend.repository.DeviceRepository;
import co.edu.udea.iot.backend.repository.HomeRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@Service
public class HomeService {

    private HomeRepository homeRepository;

    private DeviceRepository deviceRepository;

    private IotSender iotSender;

    public HomeService(IotSender iotSender, HomeRepository homeRepository, DeviceRepository deviceRepository) {
        this.iotSender = iotSender;
        this.homeRepository = homeRepository;
        this.deviceRepository = deviceRepository;

        sendMessage("home_1", Arrays.asList(new Message("device_1", "HELLO WORLD")));
    }

    public List<Home> findAllHomes() {
        return homeRepository.findAll();
    }

    public void sendMessage(String homeName, List<Message> messages) {
        //TODO query homerepository to verify whether or not the home exists

        //TODO query devicerepository to verify devices existence

        StringBuilder sb = new StringBuilder();
        messages.forEach(message -> sb.append(message.getDeviceName()).append(",").append(message.getStatus()));
        iotSender.send(homeName + "_inbound", sb.toString().getBytes());
    }


    /**
     * @param message with the structure: home_name; {device_name, device_status}
     */
    public void processMessage(String message) {
        // splitting the received message
        String[] tokens = message.split(";");
        // getting home name
        String homeName = tokens[0];
        // searching for the home in the db
        Optional<Home> homeOptional = homeRepository.findByName(homeName);
        if (!homeOptional.isPresent()) {
            System.err.println("A MESSAGE FROM A UNKNOWN HOME HAS BEEN RECEIVED {" + homeName + "}");
            return;
        }
        Home home = homeOptional.get();
        // checking whether the home status is OFFLINE and updating it to ONLINE
        if (Home.Status.OFFLINE.equals(home.getStatus())) {
            home.setStatus(Home.Status.ONLINE);
            homeRepository.save(home);
        }
        // parsing every device notification
        for (int i = 1; i < tokens.length; i++) {
            String[] subtoken = tokens[i].split(",");
            String deviceName = subtoken[0];
            String deviceStatus = subtoken[1];
            Optional<Device> deviceOptional = deviceRepository.findByName(deviceName);
            if (!deviceOptional.isPresent()) {
                System.err.println("A MESSAGE FROM A UNKNOWN DEVICE HAS BEEN RECEIVED {" + deviceName + "}");
                return;
            }
            Device device = deviceOptional.get();
            Device.Status status;
            try {
                status = Device.Status.valueOf(deviceStatus);
            } catch (IllegalArgumentException iae) {
                iae.printStackTrace();
                return;
            }
            device.setStatus(status);
            device.setLastUpdated(LocalDateTime.now());
            deviceRepository.save(device);
        }
    }

    public List<Device> findAllDevices() {
        return deviceRepository.findAll();
    }
}
