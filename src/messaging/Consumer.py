from confluent_kafka import Consumer as KafkaConsumer
from confluent_kafka import KafkaError, KafkaException, Message
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

    def consume_all(self, num_messages=1, commit=False):
        msgs: list = self.consumer.consume(num_messages=num_messages, timeout=0.1)

        messages = []

        for msg in msgs:
            if msg.error():
                self.handle_kafka_errors(msg)
            else:
                if commit:
                    self.consumer.commit(asynchronous=True)
                messages.append(self.process(msg))

        return messages

    @staticmethod
    def handle_kafka_errors(msg):
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # End of partition event
            sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                             (msg.topic(), msg.partition(), msg.offset()))
        elif msg.error():
            raise KafkaException(msg.error())

    def consume(self, commit=False):
        msg: Message = self.consumer.poll(timeout=0.1)
        if msg is None:
            return None

        if msg.error():
            self.handle_kafka_errors(msg)
        else:
            if commit:
                self.consumer.commit(asynchronous=True)
            return self.process(msg)

    @abc.abstractmethod
    def process(self, msg):
        pass

    def process_all(self, msgs):
        pass

    def shutdown(self):
        self.running = False
