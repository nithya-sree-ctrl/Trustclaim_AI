def predict_severity(
    issue_type
):

    issue_type = issue_type.lower()

    high = [
        "broken",
        "shattered",
        "major_crack"
    ]

    medium = [
        "dent",
        "crack",
        "water_damage"
    ]

    low = [
        "scratch",
        "minor_mark"
    ]

    if issue_type in high:
        return "high"

    if issue_type in medium:
        return "medium"

    if issue_type in low:
        return "low"

    return "unknown"