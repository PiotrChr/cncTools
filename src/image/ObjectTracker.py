import numpy as np
import dlib
import cv2
import src.image.utils as utils
import threading
import random


class ObjectTracker:
    def __init__(self, replace=None, daemon=False, scale_factor=1, on_recognition=None, on_track=None):
        self.CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
                        "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
                        "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
                        "sofa", "train", "tvmonitor"]
        self.prototxt = 'resources/object_tracker/model2/deploy.prototxt'
        self.model = 'resources/object_tracker/model2/mobilenet_iter_73000.caffemodel'

        self.net = cv2.dnn.readNetFromCaffe(self.prototxt, self.model)
        self.confidence = 0.5
        self.labels_to_find = ['person']
        self.image_dim = None
        self.image_center = None
        self.tracker = None
        self.label = None
        self.scale_factor = scale_factor
        self.replace = replace
        self.daemon = daemon
        self.object_center = None
        self.object_offset = None
        self.reset_tracker_limit = 50
        self.tracker_count = 0
        self.current_frame = None
        self.current_cropped_frame = None
        self.detection = None
        self.recognition_id = None
        self.on_recognition = on_recognition
        self.on_track = on_track
        self.w = None
        self.h = None

    def run_thread(self, frame):
        t = threading.Thread(
            target=self.track_and_detect,
            daemon=False,
            args=(frame,)
        )
        t.start()

    def track_and_detect(self, frame):
        self.current_cropped_frame = None

        if not self.image_center:
            self.image_dim, self.image_center = utils.get_frame_center(frame)
            self.w, self.h = self.image_dim

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        if self.tracker is None:
            blob = cv2.dnn.blobFromImage(rgb, 0.007843, (self.w, self.h), 127.5)
            # pass the blob through the network and obtain the detections
            # and predictions
            self.net.setInput(blob)

            detections = self.net.forward()

            if len(detections) > 0:
                # find the index of the detection with the largest
                # probability -- out of convenience we are only going
                # to track the first object we find with the largest
                # probability; future examples will demonstrate how to
                # detect and extract *specific* objects
                i = np.argmax(detections[0, 0, :, 2])
                # grab the probability associated with the object along
                # with its class label
                conf = detections[0, 0, i, 2]
                self.label = self.CLASSES[int(detections[0, 0, i, 1])]
                # print('label', self.label)
                if self.label in self.labels_to_find:
                    print('confidence', conf)

                if conf > self.confidence and self.label in self.labels_to_find:
                    print('match')
                    self.recognition_id = random.getrandbits(128)
                    # compute the (x, y)-coordinates of the bounding box
                    # for the object
                    box = detections[0, 0, i, 3:7] * np.array([self.w, self.h, self.w, self.h])
                    (startX, startY, endX, endY) = box.astype("int")

                    self.current_cropped_frame = frame[max(0, startY): min(self.h, endY), max(0, startX): min(self.w, endX)]

                    if self.on_recognition is not None:
                        self.on_recognition(self.current_cropped_frame, self.label, self.recognition_id)

                    # construct a dlib rectangle object from the bounding
                    # box coordinates and then start the dlib correlation
                    # tracker
                    self.tracker = dlib.correlation_tracker()
                    rect = dlib.rectangle(startX, startY, endX, endY)
                    self.tracker.start_track(rgb, rect)
                    if self.replace:
                        cv2.rectangle(frame, (startX, startY), (endX, endY),
                                      (0, 255, 0), 1)
                        cv2.putText(frame, self.label, (startX, startY - 15),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)
                else:
                    self.object_center = None
                    self.object_offset = None
            else:
                self.object_center = None
                self.object_offset = None
        else:
            self.tracker.update(rgb)
            pos = self.tracker.get_position()

            start_x = max(0, int(pos.left()))
            start_y = max(0, int(pos.top()))
            end_x = min(self.w, int(pos.right()))
            end_y = min(self.h, int(pos.bottom()))

            self.object_center = utils.get_object_center((start_y, end_x, end_y, start_x))
            self.object_offset = utils.get_center_offset(self.object_center, self.image_center)

            if self.replace:
                cv2.line(frame, self.object_center, self.image_center, (0, 255, 0), 2)
                # draw the bounding box from the correlation object tracker
                cv2.rectangle(frame, (start_x, start_y), (end_x, end_y),
                              (0, 255, 0), 1)
                cv2.putText(frame, self.label, (start_x, start_y - 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)

            current_cropped_frame = frame[start_y: end_y, start_x: end_x]

            if self.on_track is not None:
                self.on_track(current_cropped_frame, self.object_center, self.object_offset, self.image_dim)

            self.handle_tracker_reset()

        self.current_frame = frame

        # if self.current_cropped_frame is not None:
        #     return self.current_cropped_frame

        return frame

    def handle_tracker_reset(self):
        if self.tracker_count >= self.reset_tracker_limit:
            self.tracker_count = 0
            self.tracker = None

        self.tracker_count = self.tracker_count + 1
