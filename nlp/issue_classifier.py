def classify_issue(
    claim_text
):

    text = claim_text.lower()

    if "scratch" in text:
        return "scratch"

    if "dent" in text:
        return "dent"

    if "crack" in text:
        return "crack"

    if "broken" in text:
        return "broken"

    if "water" in text:
        return "water_damage"

    return "unknown"