import abc
import threading
import time
import cv2


class Loader:
    t: threading.Thread
    processors: list
    actions: dict
    frame = None
    outputFrame = None
    refresh_rate: int
    is_running: bool
    camera_id: int
    read_lock: threading.Lock

    def __init__(self, refresh_rate, camera_id):
        self.processors = []
        self.actions = {}
        self.frame = None
        self.outputFrame = None
        self.refresh_rate = refresh_rate
        self.t: threading.Thread
        self.is_running = False
        self.camera_id = camera_id
        self.read_lock = threading.Lock()

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

                self.read_lock.acquire()
                self.outputFrame = self.prepare_output_frame(frame)
                self.frame = frame
                self.read_lock.release()
            else:
                pass
                # print('no frame')
            time.sleep(self.refresh_rate)

        self.cleanup()

    def read_static(self):
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

            # self.read_lock.acquire()
            self.outputFrame = self.prepare_output_frame(frame)

            

    def prepare_output_frame(self, frame):
        return frame

    def start(self):
        if self.is_running:
            print("already started!!")
            return None

        self.is_running = True

        self.t = threading.Thread(
            target=self.start_read,
            daemon=False,
        )

        self.t.start()

        return self

    def start_static(self):
        self.start_read()

    def get_output_frame(self, static=False):
        if static:
            self.read_static()
            frame = self.outputFrame
        else:
            self.read_lock.acquire()
            frame = self.outputFrame
            self.read_lock.release()

        return frame

    @abc.abstractmethod
    def get_frame(self):
        pass

    def stop(self):
        self.is_running = False
        self.t.join()

    @abc.abstractmethod
    def start_read(self):
        pass

    def cleanup(self):
        pass
