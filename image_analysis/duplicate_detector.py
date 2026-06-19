import hashlib

def file_hash(path):

    with open(path, "rb") as f:
        return hashlib.md5(
            f.read()
        ).hexdigest()


def detect_duplicate(image_paths):

    hashes = []

    for img in image_paths:

        hashes.append(
            file_hash(img)
        )

    return len(hashes) != len(set(hashes))