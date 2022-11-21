from src.messaging.domains.main.message.Message import Message
import json


class StingDetectionNotification(Message):
    def __init__(self, labels, detected_label, confidence):
        super().__init__()
        self.labels = labels
        self.detected_label = detected_label
        self.confidence = confidence

    def to_json(self):
        return json.dumps(self.to_obj())

    def to_obj(self):
        return {
            'date': str(self.date),
            'labels': self.labels,
            'confidence': float(self.confidence),
            'detected_label': self.detected_label
        }