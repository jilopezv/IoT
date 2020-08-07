# Imagen base de rabbitmq 
FROM rabbitmq:latest

# Se habilita el plugin de gestión y mqtt
RUN rabbitmq-plugins enable --offline rabbitmq_management rabbitmq_mqtt rabbitmq_web_stomp

CMD ["rabbitmq-server"]