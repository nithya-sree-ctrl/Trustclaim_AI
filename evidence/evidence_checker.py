def check_evidence(
    image_count,
    required_count
):

    if image_count >= required_count:

        return {
            "evidence_standard_met": True,
            "reason":
                f"{image_count} images provided. Requirement met."
        }

    return {
        "evidence_standard_met": False,
        "reason":
            f"Only {image_count} images provided. Minimum required is {required_count}."
    }