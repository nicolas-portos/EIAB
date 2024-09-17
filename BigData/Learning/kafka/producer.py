from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
    value_serializer=lambda m: dumps(m).encode('utf-8'),
    # bootstrap_servers=['10.133.29.238:9092']) # si abrimos el puerto en la maquina
    # ssh cesgaxuser@10.133.29.238 -L 9092:10.133.29.238:9092
    bootstrap_servers=['127.0.0.1:9092']) # Si redireccionamos con ssh -l

for i in range(10):
    # producer.send("iabd-topic", value={"nombre": "producer " + str(i)})
    producer.send("bigdata", value={"nombre": "producer " + str(i)})
# Como el envío es asíncrono, para que no se salga del programa antes de enviar el mensaje, esperamos 1 seg
time.sleep(1)
# producer.flush()