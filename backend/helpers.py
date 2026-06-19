import os
import uuid


def allowed_file(filename):

    allowed_extensions = {
        "jpg",
        "jpeg",
        "png"
    }

    return (
        "." in filename
        and
        filename.rsplit(
            ".",
            1
        )[1].lower()
        in allowed_extensions
    )


def generate_unique_filename(
    filename
):

    extension = filename.split(
        "."
    )[-1]

    return (
        str(uuid.uuid4())
        + "."
        + extension
    )


def ensure_folder_exists(
    folder_path
):

    os.makedirs(
        folder_path,
        exist_ok=True
    )