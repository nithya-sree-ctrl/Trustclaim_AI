import cv2


def preprocess_image(image_path):

    image = cv2.imread(image_path)

    if image is None:
        return None

    image = cv2.resize(
        image,
        (640, 640)
    )

    image = cv2.GaussianBlur(
        image,
        (3, 3),
        0
    )

    return image