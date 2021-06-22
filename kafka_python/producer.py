##Message produce in tipoic input ms current time
from kafka import KafkaProducer
## Lib for timestamp
import time
import datetime
## Lib OS
import os

#### Broker apache kafka, for produce and consume msg
#broker_kafka = '127.0.0.1:9092'
broker_kafka = os.environ.get('BROKER_KAFKA')
#### Conf Kafka Producer
producer = KafkaProducer(value_serializer=str.encode, bootstrap_servers=[broker_kafka])

## Def timestamp in ms
def current_milli_time():
    return str(round(time.time() * 1000))

### a single message is sent (or timeout), where 'output' is a topic name and 'value' is msg
def send_msg():
    future = producer.send('input', value=current_milli_time())
    result = future.get(timeout=60)
    print ("MSG TO INPUT:", current_milli_time(), "msg =", future)

# Block for 'synchronous' sends
try:
    while True:
        send_msg()
#        producer.send('input2', value=current_milli_time())
    # Successful result returns assigned partition and offset
#    print(record_metadata.topic)
#    print(record_metadata.partition)
#    print(record_metadata.offset)
#    print(record_metadata.value)
except KeyboardInterrupt:
        pass

