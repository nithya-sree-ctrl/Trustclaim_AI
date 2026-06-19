import cv2


def check_image_quality(image_path):

    image = cv2.imread(image_path)

    if image is None:

        return {
            "valid": False,
            "reason": "Image not readable"
        }

    height, width = image.shape[:2]

    if width < 300 or height < 300:

        return {
            "valid": False,
            "reason": "Low resolution image"
        }

    return {
        "valid": True,
        "reason": "Good quality image"
    }