import pandas as pd


def evaluate_evidence(claim_object, image_count):

    try:
        requirements = pd.read_csv(
            "dataset/evidence_requirements.csv"
        )

        row = requirements[
            requirements["claim_object"].str.lower()
            == claim_object.lower()
        ]

        if row.empty:
            return {
                "evidence_standard_met": False,
                "reason": "No evidence requirements found."
            }

        minimum_images = int(
            row.iloc[0]["minimum_images"]
        )

        if image_count >= minimum_images:
            return {
                "evidence_standard_met": True,
                "reason": (
                    f"{image_count} images provided. "
                    f"Minimum required is {minimum_images}."
                )
            }

        return {
            "evidence_standard_met": False,
            "reason": (
                f"Only {image_count} images provided. "
                f"Minimum required is {minimum_images}."
            )
        }

    except Exception as e:

        return {
            "evidence_standard_met": False,
            "reason": str(e)
        }