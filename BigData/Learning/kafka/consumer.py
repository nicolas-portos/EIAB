from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
    'iabd-topic',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='iabd-grupo-1',
    value_deserializer=lambda m: loads(m.decode('utf-8')),
    # bootstrap_servers=['10.133.29.238:9092']) # si abrimos el puerto en la maquina
    # ssh cesgaxuser@10.133.29.238 -L 9092:10.133.29.238:9092
    bootstrap_servers=['127.0.0.1:9092']) # Si redireccionamos con ssh -l

for m in consumer:
    print(m.value)