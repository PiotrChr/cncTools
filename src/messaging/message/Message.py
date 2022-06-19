import abc


class Message:

    @abc.abstractmethod
    def to_json(self):
        pass