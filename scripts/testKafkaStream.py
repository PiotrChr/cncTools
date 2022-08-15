from confluent_kafka import Consumer as KafkaConsumer
from confluent_kafka import KafkaError, KafkaException
import sys
import cv2
import numpy as np
import atexit
import time
import uuid
import timeit

topic = ['StingFrames']


print('subscribing')
consumer = KafkaConsumer({
    "bootstrap.servers": "192.168.2.53:29092",
    "group.id": uuid.uuid4(),
    "enable.auto.commit": False
})
consumer.subscribe(topic)


time.sleep(2)
print('subscribed...')



def cleanup():
    cv2.destroyAllWindows()


def consume(commit=False):
    start_time = timeit.default_timer()
    msg = consumer.poll(timeout=0.5)
    print('polling time: ', timeit.default_timer() - start_time)

    if msg is None:
        print('got nothing')
        return None

    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
            raise KafkaException(msg.error())
    else:
        if commit:
            consumer.commit(asynchronous=True)
        return process(msg)


def process(msg):
    start_time = timeit.default_timer()
    # frame = np.frombuffer(msg.value(), dtype=np.uint8)
    # frame.shape = (225, 300, 3)

    frame = cv2.imdecode(np.fromstring(msg.value(), dtype=np.uint8), cv2.IMREAD_UNCHANGED)

    print('operating time: ', timeit.default_timer() - start_time)

    cv2.imshow('frame', frame)
    cv2.waitKey(10)


atexit.register(cleanup)

while True:
    consume()




