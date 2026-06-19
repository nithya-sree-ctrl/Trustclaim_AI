import os

VALID_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png"
}


def validate_images(
    image_paths
):

    valid_images = []

    invalid_images = []

    for path in image_paths:

        ext = os.path.splitext(path)[1].lower()

        if ext in VALID_EXTENSIONS:

            valid_images.append(path)

        else:

            invalid_images.append(path)

    return {
        "valid": valid_images,
        "invalid": invalid_images,
        "valid_image":
            len(valid_images) > 0
    }