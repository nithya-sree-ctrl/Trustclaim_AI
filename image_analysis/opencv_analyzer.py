import cv2
import os


def analyze_damage(image_paths):

    results = []


    if not image_paths:
        return {
            "damage": "No image provided",
            "images_checked": 0
        }


    for image in image_paths:

        img = cv2.imread(image)


        if img is None:
            continue


        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )


        # detect edges/cracks
        edges = cv2.Canny(
            gray,
            100,
            200
        )


        damage_pixels = cv2.countNonZero(edges)

        total_pixels = edges.shape[0] * edges.shape[1]


        damage_ratio = (
            damage_pixels / total_pixels
        ) * 100



        if damage_ratio > 8:

            damage = "Major visible damage detected"

        elif damage_ratio > 3:

            damage = "Moderate damage detected"

        else:

            damage = "Minor damage detected"



        results.append({

            "image": os.path.basename(image),

            "damage_ratio":
            round(damage_ratio,2),

            "result": damage

        })



    return {

        "images_checked":len(results),

        "details":results,

        "status":
        "OpenCV image analysis completed"

    }