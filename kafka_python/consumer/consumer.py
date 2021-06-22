#### Libs for kafka
from kafka import KafkaConsumer
from kafka import KafkaProducer
#### Lib for time and rfc3339
from rfc3339 import rfc3339
import time
import datetime
## Lib OS
import os

#### Broker apache kafka, for produce and consume msg
#broker_kafka = '127.0.0.1:9092'
broker_kafka = os.environ.get('BROKER_KAFKA')
#### Conf Kafka Producer
producer = KafkaProducer(value_serializer=str.encode, bootstrap_servers=[broker_kafka])


####Kafka Consumer configs: intput is a topic name, group_id and kafka broker 
consumer = KafkaConsumer('input',
                         group_id='in_to_out',
                         bootstrap_servers=[broker_kafka])

### convert ms to datetime
def convert_dt(msg):
    dt = datetime.datetime.fromtimestamp(msg / 1000.0)
    #print("MS to Datetime:", dt)
    return dt

### a single message is sent (or timeout), where 'output' is a topic name and 'value' is msg
def send_msg(converted_to_str):
    future = producer.send('output', value=converted_to_str)
    result = future.get(timeout=60)


### Consume msg, print str message and def type to int
for message in consumer:
    print ("CONSUME TOPIC INPUT:", str(message.value, encoding='utf-8'))
    msg = int(str(message.value, encoding='utf-8'))
    convert_dt(msg)
    print ("MSG to Datetime:", convert_dt(msg))
    ## convert Datetime to RFC3339
    converted_to_str = rfc3339(convert_dt(msg), utc=True, use_system_timezone=False)
    send_msg(converted_to_str)
    print("MSG TO TOPIC OUTPUT:", converted_to_str)

# consume earliest available messages, don't commit offsets
KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=1000)