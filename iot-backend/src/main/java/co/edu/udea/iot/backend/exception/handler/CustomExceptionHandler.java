package co.edu.udea.iot.backend.exception.handler;

import co.edu.udea.iot.backend.exception.DataDuplicatedException;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@RestControllerAdvice
public class CustomExceptionHandler extends ResponseEntityExceptionHandler {


    @ExceptionHandler(DataDuplicatedException.class)
    protected ResponseEntity handleDataDuplicatedException(DataDuplicatedException ex, WebRequest request) {
        System.out.println(request.getContextPath());
        return ResponseEntity.status(HttpStatus.CONFLICT).body(ex.getMessage());
    }
}
