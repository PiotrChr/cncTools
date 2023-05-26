import abc
from datetime import datetime


class Message:
    def __init__(self):
        self.date = (datetime.now()).isoformat()

    @abc.abstractmethod
    def to_json(self):
        pass
