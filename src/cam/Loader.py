import abc
import threading
import time
import cv2


class Loader:
    def __init__(self, refresh_rate, camera_id):
        self.processors = []
        self.actions = {}
        self.frame = None
        self.outputFrame = None
        self.refresh_rate = refresh_rate
        self.t = None
        self.is_running = True
        self.camera_id = camera_id

        print("Created cam loader with id:" + str(camera_id))

        super().__init__()

    def add_processor(self, processor):
        self.processors.append(processor)

    def add_action(self, processor, action):
        self.actions[processor] = action

    def read(self):
        while self.is_running:
            frame = self.get_frame()

            if frame is not None:
                for processor in self.processors:
                    process = processor.process(frame)
                    if process is None:
                        continue

                    frame = process
                    processor_name = processor.__class__.__name__
                    if processor_name in self.actions:
                        self.actions[processor_name](processor.yield_val)

                self.outputFrame = self.prepare_output_frame(frame)
                self.frame = frame
            else:
                print('no frame')
            time.sleep(self.refresh_rate)

        self.cleanup()

    def prepare_output_frame(self, frame):
        return frame

    def start(self):
        self.t = threading.Thread(
            target=self.start_read,
            daemon=False,
        )
        self.t.start()

    @abc.abstractmethod
    def get_frame(self):
        pass

    @abc.abstractmethod
    def start_read(self):
        pass

    def cleanup(self):
        pass
