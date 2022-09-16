package co.edu.udea.iot.backend.exception;

public class DataDuplicatedException extends RuntimeException {
    public DataDuplicatedException(String message) {
        super(message);
    }
}
