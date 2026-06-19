import pandas as pd

def check_evidence(claim_object, image_count):

    requirements = pd.read_csv(
        "dataset/evidence_requirements.csv"
    )

    row = requirements[
        requirements["claim_object"] == claim_object
    ]

    if len(row) == 0:
        return False, "No requirement found"

    required_images = int(
        row.iloc[0]["minimum_images"]
    )

    if image_count >= required_images:
        return True, f"{image_count}/{required_images} images provided"

    return False, (
        f"Only {image_count}/{required_images} images provided"
    )