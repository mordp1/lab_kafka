KFK_SRV = '129.213.117.48:9092'
from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import time
import datetime


##callback method has two parameters – the first sends information about any error that occured whilst producing
# the message and the second information about the message produced.
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        print("Message produced: {0}".format(msg.value()))


## Consumer Configuration connection Kafka Broker
settings = {
    'bootstrap.servers': '129.213.117.48:9092',
    'group.id': 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}
## Kafka Brokers Producer
p = Producer({'bootstrap.servers': '129.213.117.48:9092'})

c = Consumer(settings)
# Def Topic  where will consume
c.subscribe(['input'])

## Consume msg
try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print("Men="'{0}'.format(msg.value()))
            print (str.format(msg.value('utf-8')))
            str.format
#            p.produce('output', '{0}'
#                      .format(msg.value()), callback=acked)
#            p.poll(0.5)
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached {0}/{1}'
                  .format(msg.topic(), msg.partition()))
        else:
            print('Error occured: {0}'.format(msg.error().str()))


except KeyboardInterrupt:
    pass

finally:
    c.close()



