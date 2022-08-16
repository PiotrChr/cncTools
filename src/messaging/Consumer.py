from confluent_kafka import Consumer as KafkaConsumer
from confluent_kafka import KafkaError, KafkaException
from config import config
import abc
import sys


class Consumer:
    def __init__(self, topics, config):
        self.consumer = KafkaConsumer(config)
        self.topics = topics
        self.running = True

    def subscribe(self):
        self.consumer.subscribe(self.topics)

    def close(self):
        self.consumer.close()

    def consume(self, commit=False):
        msg = self.consumer.poll(timeout=0.1)
        if msg is None:
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
                self.consumer.commit(asynchronous=True)
            return self.process(msg)

    @abc.abstractmethod
    def process(self, msg):
        pass

    def shutdown(self):
        self.running = False
