def get_object_center(object_location):
    (top, right, bottom, left) = object_location

    x = right - int((right - left)/2)
    y = top - int((top - bottom)/2)

    return x, y


def get_center_offset(object_center, image_center):
    # print(face_location)
    x, y = object_center
    ic_x, ic_y = image_center

    return ic_x - x, ic_y - y


def get_frame_center(frame):
    (h, w) = frame.shape[:2]
    image_dim = (w, h)
    image_center = (int(w/2), int(h/2))

    return image_dim, image_center


def convert_and_trim_bb(image, rect):
    # extract the starting and ending (x, y)-coordinates of the
    # bounding box
    start_x = rect.left()
    start_y = rect.top()
    end_x = rect.right()
    end_y = rect.bottom()
    # ensure the bounding box coordinates fall within the spatial
    # dimensions of the image
    start_x = max(0, start_x)
    start_y = max(0, start_y)
    end_x = min(end_x, image.shape[1])
    end_y = min(end_y, image.shape[0])
    # compute the width and height of the bounding box
    w = end_x - start_x
    h = end_y - start_y
    # return our bounding box coordinates
    return start_x, start_y, w, h

def crop(image, rect):
