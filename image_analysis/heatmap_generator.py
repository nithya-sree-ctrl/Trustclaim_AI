import cv2
import os


def create_heatmap(
    image_path,
    damage_regions=None
):

    image = cv2.imread(image_path)

    if image is None:
        return None

    if damage_regions is None:

        height, width = image.shape[:2]

        damage_regions = [
            (
                width // 4,
                height // 4,
                width // 3,
                height // 3
            )
        ]

    for x, y, w, h in damage_regions:

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 0, 255),
            3
        )

        cv2.putText(
            image,
            "Damage Area",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    output_folder = "frontend/static/heatmaps"

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    output_path = os.path.join(
        output_folder,
        os.path.basename(image_path)
    )

    cv2.imwrite(
        output_path,
        image
    )

    return output_path