## Lib for Kafka
from confluent_kafka import Producer
## Lib for timestamp
import time

## Def timestamp in ms
def current_milli_time():
    return round(time.time() * 1000)

##acked for callback method has two parameters – the first sends information about any error that occured whilst producing
# the message and the second information about the message produced.
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))
        
## Kafka Brokers
p = Producer({'bootstrap.servers': '129.213.117.48:9092'})

# loop to input message with ms current time
try:
    while True:
        ### 'TOPIC' , '{MESSAGE}'
        p.produce('input', '{0}'
                  .format(current_milli_time()), callback=acked)
        p.poll(0.5)

except KeyboardInterrupt:
    pass

p.flush(30)