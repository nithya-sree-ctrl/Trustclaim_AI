def generate_explanation(
    evidence_met,
    duplicate,
    severity
):

    reasons = []

    if evidence_met:
        reasons.append(
            "Required image evidence supplied."
        )

    if duplicate:
        reasons.append(
            "Duplicate images detected."
        )

    reasons.append(
        f"Damage severity assessed as {severity}."
    )

    return reasons